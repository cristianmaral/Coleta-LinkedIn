from urllib import quote_plus
import json
import requests

class LinkedIn:
    PROFILE = 'https://api.linkedin.com/v1/people'
    COMPANY = 'https://api.linkedin.com/v1/companies'

    def __init__(self, access_token):
        self.access_token = access_token

    #Metodo generico para realizar uma requisicao GET atraves de uma url e parametros extras
    def realizar_requisicao(self, url, params=None):
        #Printando o url base de requisicao para facilitar os testes
        print url
        if (params == None):
            params = {}
        #Requisitando a resposta no formato json
        params.update({'format':'json'})
        #Anexando a access_token ao url de requisicao
        params.update({'oauth2_access_token': self.access_token})
        #Enviando a requisicao GET e retornando a resposta da Rest API
        return requests.get(url, params).json()

    ############################################ PROFILE API ############################################

    #Metodo para recuperar dados de um usuario especifico a partir de seu id
    def recuperar_usuario_id(self, id=None, campos=None):
        if id:
            url = '%s/id=%s' % (self.PROFILE, str(id))
        #Requisita os dados do dono da access_token caso o id seja None
        else:
            url = '%s/~' % (self.PROFILE)
        if campos:
            url = '%s:(%s)' % (url, ','.join(campos))
        return self.realizar_requisicao(url)

    #Metodo para recuperar dados de um usuario especifico a partir de seu url
    def recuperar_usuario_url(self, url, campos=None):
        url = '%s/url=%s' % (self.PROFILE, quote_plus(url))
        if campos:
            url = '%s:(%s)' % (url, ','.join(campos))
        return self.realizar_requisicao(url)

    ############################################ COMPANY API ############################################

    #Metodo para recuperar dados das empresas relacionadas ao usuario correspondente a access_token
    def recuperar_minhas_empresas(self):
        return self.realizar_requisicao(self.COMPANY, params={'is-company-admin':'true'})

    #Metodo para recuperar dados de uma empresa a partir de seu id
    def recuperar_empresa_id(self, id, campos=None):
        url = '%s/%s' % (self.COMPANY, str(id))
        if campos:
            url = '%s:(%s)' % (url, ','.join(campos))
        return self.realizar_requisicao(url)

    #Metodo para recuperar dados de uma empresa a partir de seu nome universal
    def recuperar_empresa_universal_name(self, universal_name):
        url = '%s/%s=%s' % (self.COMPANY, 'universal-name', universal_name)
        return self.realizar_requisicao(url)

    #Metodo para recuperar dados das atualizacoes de uma empresa
    def recuperar_updates_empresa(self, id, count):
        url = '%s/%s/updates' % (self.COMPANY, str(id))
        #Definindo a quantidade de atualizacoes da empresa que serao recuperadas
        params = {'count':count}
        return self.realizar_requisicao(url, params=params)

    #Metodo para recuperar dados de uma atualizacao especifica de uma empresa
    def recuperar_update_empresa(self, id, key):
        url = '%s/%s/%s/%s=%s' % (self.COMPANY, str(id), 'updates', 'key', key)
        return self.realizar_requisicao(url)

    #Metodo para recuperar dados referentes aos comentarios de uma atualizacao especifica de uma empresa
    def recuperar_comentarios_update(self, id, key):
        url = '%s/%s/%s/%s=%s/%s' % (self.COMPANY, str(id), 'updates', 'key', key, 'update-comments')
        return self.realizar_requisicao(url)

    #Metodo para recuperar os dados de quem curtiu uma atualizacao especifica de uma empresa
    def recuperar_likes_update(self, id, key):
        url = '%s/%s/%s/%s=%s/%s' % (self.COMPANY, str(id), 'updates', 'key', key, 'likes')
        return self.realizar_requisicao(url)

    #Metodo para recuperar a quantidade de seguidores de uma empresa
    def recuperar_seguidores_empresa(self, id):
        url = '%s/%s/%s' % (self.COMPANY, str(id), 'num-followers')
        return self.realizar_requisicao(url)

    #Metodo para recuperar as estatisticas de uma empresa
    def recuperar_estatisticas_empresa(self, id):
        url = '%s/%s/%s' % (self.COMPANY, str(id), 'company-statistics')
        return self.realizar_requisicao(url)

    #Metodo para conferir se e possivel compartilhar na pagina de uma empresa
    def checar_compartilhamento_empresa(self, id):
        url = '%s/%s/%s' % (self.COMPANY, str(id), 'is-company-share-enabled')
        return self.realizar_requisicao(url)

    #Metodo para conferir se o usuario correspondente a access_token e administrador de uma empresa
    def checar_adm_empresa(self, id):
        url = '%s/%s/%s/%s' % (self.COMPANY, str(id), 'relation-to-viewer', 'is-company-share-enabled')
        return self.realizar_requisicao(url)
