ARG ELK_VERSION

#https://www.elastic.co/guide/en/beats/filebeat/current/running-on-docker.html
FROM docker.elastic.co/beats/filebeat:${ELK_VERSION}
COPY config/filebeat.yml /usr/share/filebeat/filebeat.yml
USER root
RUN chown root:filebeat /usr/share/filebeat/filebeat.yml
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm
RUN yum update -y
RUN yum install -y python36u python36u-libs python36u-devel python36u-pip
USER filebeat
COPY --from=dec_loggen:latest --chown=filebeat /usr/share/app/*.py /usr/share/app/
COPY --from=dec_loggen:latest --chown=filebeat /usr/share/app/config.json /usr/share/app
COPY wrapper-script.sh /usr/share/filebeat/

