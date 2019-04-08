FROM 172.17.1.119:5555/litemind/acai_service:0.1

RUN rm -rf  /etc/localtime && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

COPY . /core/

WORKDIR /core

CMD "sh" "-c" "echo nameserver 8.8.8.8 > /etc/resolv.conf"
RUN ["pip", "install", "-r", "requirements.txt"]
#RUN echo `ls /core`

ENTRYPOINT  ["python", "-m", "litemind.apis.server", "-c", "/config_advanced_search.json"]