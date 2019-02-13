#!/usr/bin/env python
# coding: utf-8
import jenkins, os, time

# Conexão com jenkins
def conexao_jekins ():

    url = os.getenv('URL_JENKINS')
    username = os.getenv('USUARIO_JENKINS')
    password = os.getenv('PASS_JENKINS')

    if url == None or username == None or password == None:
        print('Para para utilizar esse container é necessário informa ("URL_JENKINS","USUARIO_JENKINS","PASS_JENKINS")')
    else:
        server = jenkins.Jenkins(url, username, password)
        return server

# Retorna a lista de todos jobs cadastrados
def get_all_jobs():
    server_jenkins = conexao_jekins()
    lista_bruta_jobs = server_jenkins.get_all_jobs()
    lista_jobs = [ x['name'] for x in lista_bruta_jobs ]
    return lista_jobs

# Realizar a execução do job
def build_jobs(job):
    server_jenkins = conexao_jekins()

    if server_jenkins.job_exists(job) == True:
        try:
            server_jenkins.build_job(job)
            print(f'Job "{job}" enviado para fila de execução!')
        except:
            print(f'Ocorreu um erro na execução do job "{job}", verifique!')
    else:
        print(f'Job "{job}" não existe.')

def main():

    server_jenkins = conexao_jekins()
    lista_jobs = get_all_jobs()

    for job in lista_jobs:
        build_jobs(job)
        time.sleep(5)
main()
