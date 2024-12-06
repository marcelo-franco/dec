ARG ELASTIC_VERSION

#https://www.elastic.co/guide/en/beats/filebeat/current/running-on-docker.html
FROM docker.elastic.co/beats/filebeat:${ELASTIC_VERSION}
COPY config/filebeat.yml /usr/share/filebeat/filebeat.yml
USER root
RUN chown root:filebeat /usr/share/filebeat/filebeat.yml
RUN chmod 750 /usr/share/filebeat/filebeat.yml
RUN apt update -y
RUN apt install -y python3 
USER filebeat
COPY --from=dec_loggen:latest --chown=filebeat /usr/share/app/*.py /usr/share/app/
COPY --from=dec_loggen:latest --chown=filebeat /usr/share/app/config.json /usr/share/app
COPY --chown=filebeat:root --chmod=750 wrapper-script.sh /usr/share/filebeat/

