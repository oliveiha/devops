FROM grafana/grafana:5.2.1

RUN grafana-cli plugins install grafana-clock-panel
RUN grafana-cli plugins install grafana-piechart-panel
RUN grafana-cli plugins install savantly-heatmap-panel
RUN grafana-cli plugins install vonage-status-panel
RUN grafana-cli plugins install flant-statusmap-panel

COPY db /etc/grafana/provisioning/datasources/

COPY dashboards /etc/grafana/dashboards/

COPY conf/confs_grafana.yml /etc/grafana/provisioning/dashboards/
