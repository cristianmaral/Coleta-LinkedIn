from urllib import quote_plus
import json
import requests

class LinkedIn:
    PROFILE = 'https://api.linkedin.com/v1/people'
    COMPANY = 'https://api.linkedin.com/v1/companies'

    def __init__(self, access_token):
        self.access_token = access_token

    #Metodo generico para realizar uma requisicao GET atraves de uma url e parametros extras
    def make_request(self, url, params=None):
        print url
        if (params == None):
            params = {}
        #Requisitando a resposta no formato json
        params.update({'format':'json'})
        #Anexando a access_token ao url de requisicao
        params.update({'oauth2_access_token': self.access_token})
        return requests.get(url, params).json()

    #Metodo para recuperar dados de um usuario especifico a partir de seu id
    def get_profile_id(self, id=None, fields=None):
        if id:
            url = '%s/id=%s' % (self.PROFILE, str(id))
        #Requisita os dados do dono da access_token caso o id seja None
        else:
            url = '%s/~' % (self.PROFILE)
        if fields:
            url = '%s:(%s)' % (url, ','.join(fields))
        return self.make_request(url)

    #Metodo para recuperar dados de um usuario especifico a partir de seu url
    def get_profile_url(self, url, fields=None):
        url = '%s/url=%s' % (self.PROFILE, quote_plus(url))
        if fields:
            url = '%s:(%s)' % (url, ','.join(fields))
        return self.make_request(url)

    #Metodo para conferir se e possivel compartilhar na pagina de uma empresa
    def check_company_share(self, id):
        url = '%s/%s/%s?' % (self.COMPANY, str(id), 'is-company-share-enabled')
        return self.make_request(url)

    #Metodo para recuperar dados das empresas relacionadas ao usuario correspondente a access_token
    def get_my_companies(self):
        return self.make_request(self.COMPANY, params={'is-company-admin':'true'})

    #Metodo para recuperar dados de uma empresa a partir de seu id
    def get_company_id(self, id, fields=None):
        url = '%s/%s' % (self.COMPANY, str(id))
        if fields:
            url = '%s:(%s)' % (url, ','.join(fields))
        return self.make_request(url)

    #Metodo para recuperar dados de uma empresa a partir de seu nome universal
    def get_company_universal_name(self, universal_name):
        url = '%s/universal-name=%s' % (self.COMPANY, universal_name)
        return self.make_request(url)

    #Metodo para recuperar dados das atualizacoes de uma empresa
    def get_company_updates(self, id, count):
        url = '%s/%s/updates' % (self.COMPANY, str(id))
        #Definindo a quantidade de atualizacoes da empresa que serao recuperadas
        params = {'count':count}
        return self.make_request(url, params=params)

    #Metodo para recuperar dados de uma atualizacao especifica de uma empresa
    def get_company_update_key(self, id, key):
        url = '%s/%s/updates/key=%s' % (self.COMPANY, str(id), key)
        return self.make_request(url)

    #Metodo para recuperar os dados de quem curtiu uma atualizacaoo especifica de uma empresa
    def get_company_update_likes(self, id, key):
        url = '%s/%s/updates/key=%s/likes' % (self.COMPANY, str(id), key)
        return self.make_request(url)
