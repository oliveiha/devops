# Cedro monitoring

## Server requisites

- 200 hours of Monitoring
- 100GB
- 04 vCPU
- 16GB
---

# Stack monitoring Cedro

__Description:__ The monitoring stack work on `docker swarm mode`, this stack take many metrics about the swarm nodes and `docker` services, let's to know more about the components.


__Stack components__

- [Prometheus](https://prometheus.io/docs/prometheus/latest/getting_started/)
- [Alertmanager](https://prometheus.io/docs/alerting/alertmanager/)
- [Node-exporter](https://prometheus.io/docs/guides/node-exporter/)
- [Cadvisor](https://github.com/google/cadvisor)
- [Grafana](http://docs.grafana.org/guides/getting_started/)
- [Unsee](https://github.com/cloudflare/unsee)
- [Blackbox](https://github.com/prometheus/blackbox_exporter)


## Prometheus

Prometheus is a open-source system monitoring and alerting, this toolkit can be integrated with many others tools, this [link](https://prometheus.io/docs/instrumenting/exporters/) can show you some exemplos about it.

> The prometheus is the core monitoring, it's the most important component in the monitoring, be careful on with it.

## Alertmanager

Alertmanager can send alerts by diferentes conditions and channels ( email, slack, webhooks e etc ), the prometheus take the metrics and send to alertmanager to notify thoses teams.

## Node-exporter

Prometheus exporter or node-exporter take some  hardware and OS metrics exposed by `*NIX kernels`, written in Go with pluggable metric collectors.

## Advisor

cAdvisor (Container Advisor) provides container users an understanding of the resource usage and performance characteristics of their running containers. It is a running daemon that collects, aggregates, processes, and exports information about running containers. Specifically, for each container it keeps resource isolation parameters, historical resource usage, histograms of complete historical resource usage and network statistics. This data is exported by container and machine-wide.

## Grafana

Grafana is greate tool to make a dashboards, this tool used prometheus like data base, to take metrics e show a custom dashboard.

__Dashboards__

- 3662
- 6036
- 395
- 5174
- 1860
- 405
- 7587

## Unsee

It's just a interface with all alerts, available disposed in alertmanager.

## Blackbox-exporter
The blackbox exporter allows blackbox probing of endpoints over HTTP, HTTPS, DNS, TCP and ICMP.
---

# Deploy do monitoramento


1. Make a repository clone

```
  git clone https://<your user>@bitbucket.org/diogoamb/devops.git
```

2. Deploy the stack

```
  docker stack deploy -c docker-compose.yml <stack's name>
```
