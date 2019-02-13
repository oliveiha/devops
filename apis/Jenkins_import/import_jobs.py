import jenkins, xmltodict,re,os

def recebe_arquivo ():
    with open('/usr/src/app/file.txt','r') as arq_repos:
        lista_repos = [ x.replace('-','_').lower().replace('\n','') for x in arq_repos if len(x) > 1 ]
    return lista_repos

# Conexao com jenkins
def connection_jenkins ():
    url = os.getenv('URL_JENKINS')
    username = os.getenv('USUARIO_JENKINS')
    password = os.getenv('PASS_JENKINS')
    if url == None or username == None or password == None:
        print('Para para utilizar esse container e necessario informa ("URL_JENKINS","USUARIO_JENKINS","PASS_JENKINS")')
    else:
        server = jenkins.Jenkins(url, username, password)
        return server

# Job modelo
def job_modelo(conexao):
    #conexao_jenkins = connection_jenkins()
    conexao_jenkins = conexao

    with open('/usr/src/app/modelo_job.txt','r') as file_job:
        modelo_job = file_job.read()

    nome_job_padrao = 'TEMPLATE_PADRAO-QA'

    if conexao_jenkins.job_exists(nome_job_padrao) != True:

        # convertendo xml em dics
        job_dic = xmltodict.parse(modelo_job)

        # Convertendo de dicionario to xml
        job_alterado = xmltodict.unparse(job_dic)

        #job_modelo = conexao_jenkins.get_job_config('TEMPLATE_PADRAO-QA')
        conexao_jenkins.create_job(nome_job_padrao,job_alterado)

        return "Job padrao foi criado com sucesso!"

# Cria jobs
def job_create(job_modelo,job_novo):
    conexao_jenkins = connection_jenkins()

    job_novo_normalizado = job_novo.replace(' ','_').replace('-','_').lower() + '-QA'

    # Removendo palabras vazias com com meno de tres caracteres
    if conexao_jenkins.job_exists(job_novo_normalizado) != True:
        try:
            conexao_jenkins.copy_job(job_modelo,job_novo_normalizado)
            print(f'O job {job_novo_normalizado} foi criado com sucesso!')
        except jenkins.JenkinsException as err:
            print(f'Job modelo nao encontrado - "error {err}"')
        except:
            print(f'Esse job ja existe "{job_novo_normalizado}"')
    else:
        print(f'Job {job_novo_normalizado} ja existe!')


# Arquivo do job
def job_change(job_nome):

    # Normalizando nome job
    job_novo_normalizado = job_nome.replace(' ','_').replace('-','_').lower() + '-QA'

    nome_repo = job_nome.replace(' ','_').replace('-','_').lower()

    # conexão com jenkins
    conexao_jenkins = connection_jenkins()

    if conexao_jenkins.job_exists(job_novo_normalizado) == True:
        # Instanciando job infos
        job_base = conexao_jenkins.get_job_config(job_novo_normalizado)

        # Convertendo de xml to dicionario
        job_dict = xmltodict.parse(job_base)

        # Alterando url do repositorio
        job_dict_alterado = job_dict['project']['scm']['userRemoteConfigs']['hudson.plugins.git.UserRemoteConfig']['url'] = f'git@bitbucket.org:guideinvestimentos/{nome_repo}.git'

        # Convertendo de dicionario to xml
        job_alterado = xmltodict.unparse(job_dict)

        try:
            # Update do job
            job_update = conexao_jenkins.reconfig_job(job_novo_normalizado, job_alterado)
            print('Job alterado com sucesso!')
        except:
            print('Ocorreu um erro ao alterar o job!')

        return job_update
    else:
        print('Esse job nao existe!')
        print(job_novo_normalizado)

# Cria view baseado no nome da api
def view_create(view_nome,regex):

    cliente = connection_jenkins()

    view_name_padronizado = view_nome.capitalize().replace(' ','_')

    # Capturando dados do modelos de view
    with open('/usr/src/app/modelo_view.txt','r') as file_view:
        modelo_view = file_view.read()

    if cliente.view_exists(view_nome) != True:
        # Convertendo de xml to dicionario
        view_dict = xmltodict.parse(modelo_view)

        # Alterando dados nome e regex
        view_nova = view_dict['hudson.model.ListView']['name'] = f'{view_name_padronizado}'
        view_regex = view_dict['hudson.model.ListView']['includeRegex'] = f'{regex}'

        # Convertendo de dicionario to xml
        view_xml = xmltodict.unparse(view_dict)
        cliente.create_view(view_nome,view_xml)
        #return view_xml
        print(f'View "{view_name_padronizado}" criada com sucesso!')
    else:
        print(f'View "{view_nome}" já existe!')

# Criando vários jobs basendos no template padrao de QA
def main():
    cliente = connection_jenkins()

    job_padro = os.getenv('JOB_PADRAO')

    if cliente.job_exists(job_padro) == True:

        lista_view = [{"view_name":'Cadastro','regex':'^register.*'},{"view_name":'Home Broker','regex':'^hb.*'},{"view_name":'Org unit','regex':'^register.*'},
{"view_name":'Sinacor','regex':'^sinacor.*'},{"view_name":'Cockpits','regex':'^cockpit.*'},{"view_name":'Caixa online','regex':'^online_balance.*'},
{"view_name":'Funds','regex':'^fund.*'},{"view_name":'Jobs','regex':'^job.*'}]

        lista_repos = recebe_arquivo()
        # Criando jobs em massa
        for job in lista_repos:
            job_create(job_padro,job)
            job_change(job)

        for dados_view in lista_view:
            view_create(dados_view['view_name'],dados_view['regex'])
    else:
        print(f'Job padrão não existe "{job_padro}"')

main()
