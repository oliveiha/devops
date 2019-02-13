import docker
from time import sleep,strftime
from os import getenv

cliente = docker.DockerClient(base_url='unix://var/run/docker.sock')

# Criar um lista com container todos containers
def lista_container():
    # Lista de todos containers
    lista_all_containers = cliente.containers.list(all)
    return lista_all_containers

# Separa os container com eventos com problema para remocao (exited, dead, removing, erro de execucao)
def check_remove_contianers():
    # Lista para armazenar todos id que serao removidos
    ls_containers_remove = []

    for container in lista_container():

        if container.status == 'exited' or container.stats == 'dead' or container.stats == 'removing':

            ls_containers_remove.append(container)

        elif container.attrs['State']['ExitCode'] > 0:
            container_exited = container.attrs['State']['ExitCode']
            container_erro = container.attrs['State']['Error']
            print(f'id contianer "{container.short_id}" exited "{container_exited}" com erro\n"{container_erro}"')
            ls_containers_remove.append(container)

    return ls_containers_remove

def deleta_container(lista):
    data_agora = strftime("%d/%m/%Y - %H:%M:%S")
    hostname = getenv('HOSTNAME')
    if len(lista) == 0:
        print(f'Sem containers para remocao {data_agora}')
    else:
        print('====='*5,'Executando','====='*5)
        for container in lista:
            print(f'Removendo os seguintes container "{container.short_id}" "{container.name}" do servidor "{hostname}" - {data_agora}')
            container.remove(force=True)
        print('====='*5,'Finalizando execucao','====='*5)

while True:
    deleta_container(check_remove_contianers())
    sleep(int(getenv('TEMPO')))
