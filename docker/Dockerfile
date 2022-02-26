FROM kalilinux/kali-rolling:latest

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -yq kali-desktop-xfce tightvncserver dbus dbus-x11 novnc net-tools wireshark-gtk git python2 python2-dev git build-essential python3-virtualenv
RUN git clone "https://github.com/volatilityfoundation/volatility.git" /opt/volatility && virtualenv -p python2 /opt/volatility/venv 
RUN /opt/volatility/venv/bin/pip install distorm3==3.4.4 yara-python pycrypto pillow openpyxl ujson
RUN alias volatility ='/opt/volatility/venv/bin/python /opt/volatility/vol.py'

ENV USER root
ENV VNCEXPOSE 1
ENV VNCPORT 5900
ENV VNCPWD changeme
ENV VNCDISPLAY 1920x1080
ENV VNCDEPTH 16
ENV NOVNCPORT 8080


COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]
