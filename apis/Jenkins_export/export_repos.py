import jenkins, os, xmltodict, re

# capturar lista de repositorios
def conexao_jekins ():

    url = os.getenv('URL_JENKINS')
    username = os.getenv('USUARIO_JENKINS')
    password = os.getenv('PASS_JENKINS')
    export_repos = os.getenv('EXPORT_REPOSITORIOS')

    if url == None or username == None or password == None and export_repos == True:
        print('Para para utilizar esse container é necessário informa ("URL_JENKINS","USUARIO_JENKINS","PASS_JENKINS")e o "EXPORT_REPOSITORIOS=True"')
    else:
        # Para tratar certificado https invalido
        #os.environ.setdefault("PYTHONHTTPSVERIFY", "0")
        server = jenkins.Jenkins(url, username, password)
        return server

# Captura nomes de todos jobs
def get_all_jobs():
    cliente = conexao_jekins()
    lista_jobs_fullname = []
    all_jobs_brutos = cliente.get_all_jobs()
    for job in all_jobs_brutos:
        job['fullname']
        lista_jobs_fullname.append(job['fullname'])
    return lista_jobs_fullname

# Captura o nome dos repositorios e extrai apenas o nome do repositorio
def get_repo(job):
    cliente = conexao_jekins()
    projeto = os.getenv('PROJETO')

    # Get dados do job e colocar no formato dicionario
    job_dict = xmltodict.parse(cliente.get_job_config(job))

    # Extraindo url do repositorio
    job_dict_repo = job_dict['project']['scm']['userRemoteConfigs']['hudson.plugins.git.UserRemoteConfig']['url']

    if projeto.upper() == "GUIDE":
        # Modelo Guide
        extract_url_1 = re.sub(r'^.*guideinvestimentos\/', "", job_dict_repo)
        extract_url_2 = re.sub(r'.git', "", extract_url_1)
    elif projeto.upper() == "RBC":
        # Modelo RB
        extract_url_1 = re.sub(r'^.*release\/', "", job_dict_repo)
        extract_url_2 = re.sub(r'\/dev.*', "", extract_url_1)
    else:
        print('Projeto não encontrado!')
        break
    return extract_url_2

# Crianando um arquivo com a lista de todos repositorios
def list_repos(lista):

    print('Iniciando procedimento\n')
    for job in lista:
        try:
            job_repo = get_repo(job)
            print(job_repo)
        except:
            continue
    print('\nProcedimento concluído!')


list_repos(get_all_jobs())
