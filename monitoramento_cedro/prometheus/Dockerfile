FROM prom/prometheus:v2.3.2
MAINTAINER DevOps cedro team

ENTRYPOINT [ "/bin/prometheus" ]
CMD [ "--config.file=/etc/prometheus/prometheus.yml", "--storage.tsdb.path=/prometheus","--web.console.libraries=/usr/share/prometheus/console_libraries", "--web.console.templates=/usr/share/prometheus/consoles","--web.enable-lifecycle", "--storage.tsdb.retention=30d", "--storage.tsdb.no-lockfile" ]
