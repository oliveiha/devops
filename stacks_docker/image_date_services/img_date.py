import docker
from time import sleep,strftime
from os import getenv

cliente = docker.from_env()
ls_images = cliente.images.list()

def data_image():
    data_agora = strftime("%d/%m/%Y - %H:%M:%S")
    hostname = getenv('HOSTNAME')
    print('\n','====='*5,'Iniciando Execução','====='*5)
    for img in ls_images:
        img_create = img.attrs['Created']
        img_name = img.attrs['RepoTags']
        if len(img_name) > 0:
            img_name_ok = img_name[0]
            print(f'A image "{img_name_ok}" foi criada na data de "{img_create}" está no servidor "{hostname}".')
    print('====='*5,f'Finalizando Execução - {data_agora}','====='*5)

while True:
    data_image()
    sleep(int(getenv('TEMPO')))
