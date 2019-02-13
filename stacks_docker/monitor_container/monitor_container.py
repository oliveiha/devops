import docker
from slackclient import SlackClient
from time import sleep,strftime
from os import getenv

# Pre-requisitos
# - CHANNEL_SLACK=channel
# - TOKEN_SLACK=token <- https://api.slack.com/custom-integrations/legacy-tokens
# - TIMER=Xs
# - /var/run/docker.sock

# Globais
cliente = docker.DockerClient(base_url='unix://var/run/docker.sock')

lista_containers = cliente.containers.list(all)

# Receber a lista de containers, normalizar por exitcode sendo > 1 e capturando error
def containers_exited():
        lista = cliente.containers.list(all)
        hostname = getenv('HOSTNAME')
        # Separando containers por saída
        check_exitcode = [container for container in lista if container.attrs['State']['ExitCode'] > 1]
        list_container_exitcode = []
        dic_exitcode = {}
        # Get erro,exitcode nos containers
        for container in check_exitcode:
            container_exited = container.attrs['State']['ExitCode']
            container_error = container.attrs['State']['Error']
            container_name = container.attrs['Name']
            container_id = container.short_id
            dic_exitcode = {'ExitCode': container_exited, 'Error':container_error, 'Name':container_name, 'ID':container_id,'Host':hostname}
            list_container_exitcode.append(dic_exitcode)
        return list_container_exitcode

# slackclient check_conexão, recebe o token env_var
def conection_slack():
    token = getenv('TOKEN_SLACK')
    client_slack = SlackClient(token)
    return client_slack

# Recebe como parametro channel e mensagem que será enviada
def send_msg_slack(msg):
    data_agora = strftime("%d/%m/%Y - %H:%M:%S")

    client_slack = conection_slack()
    channel = getenv('CHANNEL_SLACK')

    try:
        print('Enviando notificação!')
        saida_envio_msg = client_slack.api_call("chat.postMessage", channel=channel, text=msg, username='Monitor container', icon_emoji=':robot_face:')
    except TypeError as saida_erro:
        print('Não foi possível realizar o envio da mesnagem!')
        print(f'Erro: {saida_erro}')
    else:
        print(f'Mensagem enviada com sucesso! {data_agora}')

def main():
    lista_exits = containers_exited()
    for container_exit in lista_exits:
        msg = "*-- Ocorre uma falha --*\n*Serviço:* `{}`\n*Host:* `{}`\n*Erro:* `{}`".format(container_exit["Name"],container_exit['Host'],container_exit["Error"])
        send_msg_slack(msg)

while True:
    main()
    sleep(int(getenv('TEMPO')))
