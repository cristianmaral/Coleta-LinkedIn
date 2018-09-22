from urllib import quote_plus
import json
import requests

class LinkedIn:
    PROFILE = 'https://api.linkedin.com/v1/people'
    COMPANY = 'https://api.linkedin.com/v1/companies'

    def __init__(self, access_token):
        self.access_token = access_token

    def make_request(self, url, params=None):
        if (params == None):
            params = {}
        params.update({'format':'json'})
        params.update({'oauth2_access_token': self.access_token})
        return requests.get(url, params).json()

    def get_profile_id(self, id=None):
        if id:
            url = '%s/id=%s' % (self.PROFILE, str(id))
        else:
            url = '%s/~' % (self.PROFILE)
        return self.make_request(url)

    def get_profile_url(self, url):
        url = '%s/url=%s' % (self.PROFILE, quote_plus(url))
        return self.make_request(url)

    def get_companies_ids(self, ids):
        identifiers = []
        identifiers += map(str, ids)
        url = '%s::(%s)' % (self.COMPANY, ','.join(identifiers))
        return self.make_request(url)

    def get_companies_universal_names(self, universal_names):
        identifiers = []
        identifiers += ['universal-name=%s' % un for un in universal_names]
        url = '%s::(%s)' % (self.COMPANY, ','.join(identifiers))
        return self.make_request(url)

    def get_company_updates(self, id, count):
        url = '%s/%s/updates' % (self.COMPANY, str(id))
        params = {'count':count}
        return self.make_request(url, params=params)
