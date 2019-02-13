# Start all jobs jenkins

O mesmo foi desenvolvido em python 3.6+.

Libs utilizadas: `python-jenkins`.

**Observação:** Esse container basicamente realiza a leitura e exportação de repositórios de um jenkins.

# Como utilizar

```
  docker container run -ti -e "URL_JENKINS=URL_JENKINS" -e "USUARIO_JENKINS=USUARIO_JENKINS" -e "PASS_JENKINS=PASS_JENKINS" cedrotechnologies/jenkins_startall_jobs
```

Será realizar a execução de todos jobs, com intervalor de 10 segundo
