FROM fedora
RUN yum install -y figlet
# Entrypoint gets startet with docker run ...
ENTRYPOINT ["figlet", "-f", "script"]
# This command is overwritten if string is passed like: 
# docker run figlet_font string
CMD ["I can be substituted"]