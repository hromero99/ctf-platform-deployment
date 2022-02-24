FROM kalilinux/kali-rolling:latest

RUN apt-get update && apt-get install -y kali-desktop-xfce tightvncserver dbus dbus-x11 novnc net-tools wireshark

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
