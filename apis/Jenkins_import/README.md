# Import jobs jenkins

O mesmo foi desenvolvido em python 3.6+.

Libs utilizadas: `python-jenkins`, `xmltodict`.

**Observação:** Esse container basicamente realiza a leitura e exportação de repositórios de um jenkins.

# Como utilizar

```
  docker container run -ti --mount type=bind,src=/var/cedro/Jenkins_api/teste.txt,dst=/usr/src/app/file.txt -e "URL_JENKINS=URL_JENKINS" -e "USUARIO_JENKINS=USUARIO_JENKINS" -e "PASS_JENKINS=PASS_JENKINS" -e "JOB_PADRAO=JOB_PADRAO" cedrotechnologies/jenkins_import_job:v0.1
```

Será realizando um saída padrão, com todos repositórios.
