#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-13 14:27
# @Author  : zhangzhen
# @Site    : 
# @File    : production_app.py
# @Software: PyCharm
import argparse
import logging
import json
from flask import Flask, request, jsonify, render_template, current_app, Response
from gevent.pywsgi import WSGIServer

from logists.csv_utils import columns_mapper_entity

logger = logging.getLogger(__name__)


def create_argument_parser():
    """Parse all the command line arguments for the server script."""

    parser = argparse.ArgumentParser(description='starts server to serve an agent')
    parser.add_argument('-p', '--port', type=int, default=1234, help="port to run the server at")
    parser.add_argument('--auth_token', type=str,
                        help="Enable token based authentication. Requests need to provide the token to be accepted.")
    parser.add_argument('-o', '--log_file', type=str, dest="logfile", default="csv2graph.log",
                        help="store log file in specified file")
    add_logging_option_arguments(parser)

    return parser


def add_logging_option_arguments(parser):
    """Add options to an argument parser to configure app.logger levels."""

    # arguments for app.logger configuration
    parser.add_argument(
        '--debug',
        help="Print lots of debugging statements. "
             "Sets app.logger level to DEBUG",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
        default=logging.INFO,
    )
    parser.add_argument(
        '-v', '--verbose',
        help="Be verbose. Sets logger level to INFO",
        action="store_const",
        dest="loglevel",
        const=logging.INFO,
    )


def configure_colored_logging(loglevel):
    import coloredlogs
    field_styles = coloredlogs.DEFAULT_FIELD_STYLES.copy()
    field_styles['asctime'] = {}
    level_styles = coloredlogs.DEFAULT_LEVEL_STYLES.copy()
    level_styles['debug'] = {}
    coloredlogs.install(
        level=loglevel,
        use_chroot=False,
        fmt='%(asctime)s %(levelname)-8s %(name)s  - %(message)s',
        level_styles=level_styles,
        field_styles=field_styles)


def configure_file_logging(loglevel, logfile):
    if logfile:
        formatter = logging.Formatter("[%(asctime)s-%(filename)s-line:%(lineno)d-%(levelname)s] %(message)s")
        fh = logging.FileHandler(logfile, encoding="utf-8")
        fh.setLevel(loglevel)

        ch = logging.StreamHandler()
        ch.setLevel(loglevel)

        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logging.getLogger('').addHandler(fh)
        logging.getLogger("").addHandler(ch)
    logging.captureWarnings(True)


def create_app(parse_args):
    """Class representing a HTTP server."""
    loglevel = parse_args.loglevel if hasattr(parse_args, "loglevel") else "INFO"
    logfile = parse_args.logfile if hasattr(parse_args, "logfile") else "logs/csv2graph.log"
    configure_file_logging(loglevel, logfile)

    app = Flask(__name__)
    app.config['ALLOWED_EXTENSIONS'] = set('txt')

    @app.route("/")
    def index():
        text = {"code": 200, "text": "hi, default request"}
        return Response(json.dumps(text), mimetype='application/json')

    @app.route("/litemind/csv2graph", methods=['POST'])
    def columns2entities():
        filename = request.json.get("filename")
        data = request.json.get("data", [])
        logging.info("filename {}, data {}".format(filename, data))
        # 校验参数的正确性
        if filename and isinstance(data, list) and len(data) > 0 and isinstance(data[0], list):
            # 执行csv2graph解析
            rsJson = columns_mapper_entity(filename, data)
            rsText = json.dumps(rsJson)
        else:
            rsText = json.dumps({'code': '201', 'msg': '接口参数异常'})

        logging.info("csv2graph: {}".format(rsText))
        return Response(rsText, mimetype='application/json')

    return app


if __name__ == '__main__':

    arg_parser = create_argument_parser()
    cmdline_args = arg_parser.parse_args()

    # Setting up the color scheme of logger
    configure_colored_logging(cmdline_args.loglevel)

    # Setting up the application framework
    app = create_app(cmdline_args)
    logger.warning("Started http server on port %s" % cmdline_args.port)
    # Running the server at 'this' address with the
    # app.debug = True
    http_server = WSGIServer(('0.0.0.0', cmdline_args.port), app)
    logger.warning("Up and running")
    try:
        http_server.serve_forever()
    except Exception as exc:
        logger.exception(exc)
