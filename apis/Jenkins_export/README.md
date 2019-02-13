# Export repositórios jenkins

O mesmo foi desenvolvido em python 3.6+.

Libs utilizadas: `python-jenkins`, `xmltodict`.

**Observação:** Esse container basicamente realiza a leitura e exportação de repositórios de um jenkins.

# Como utilizar

```
  docker container run -ti -e "URL_JENKINS=URL_JENKINS" -e "USUARIO_JENKINS=USUARIO_JENKINS" -e "PASS_JENKINS=PASS_JENKINS" -e EXPORT_REPOSITORIOS=True -e "PROJETO=guide|RBC" cedrotechnologies/jenkins_api
```

Será realizando um saída padrão, com todos repositórios.
