# Coleta-LinkedIn
Coleta de dados públicos da rede social LinkedIn

## Profile API

#### Campos específicos de um usuário
https://developer.linkedin.com/docs/fields/basic-profile

#### Campos padrões da resposta (parâmetro "fields" não especificado)
'headline', 'last-name', 'id' e 'first-name'

#### Recuperar dados do usuário que possui a access_token
.get_profile_id() -> url de requisição: "https://api.linkedin.com/v1/people/~"

#### Recuperar dados de um usuário a partir de seu identificador
.get_profile_id(id='user-id') -> url de requisição: "https://api.linkedin.com/v1/people/id=user-id"

#### Recuperar dados de um usuário a partir de seu url
.get_profile_url('user-url') -> url de requisição: "https://api.linkedin.com/v1/people/url=user-url"

#### Exemplo de uma requisição utilizando campos específicos
.get_profile_id(id='user-id', fields=['id', 'first-name', 'last-name']) -> url de requisição: "https://api.linkedin.com/v1/people/id=user-id:(id,first-name,last-name)"

## Company API

#### Campos específicos de uma empresa
https://developer.linkedin.com/docs/fields/company-profile

#### Campos padrões da resposta (parâmetro "fields" não especificado)
'id' e 'name'

#### Recuperar os dados das empresas em que o usuário que possui a access_token é administrador
.get_my_companies() -> url de requisição: "https://api.linkedin.com/v1/companies"

#### Recuperar dados de uma empresa a partir de seu identificador
.get_company_id('company-id') -> url de requisição: "https://api.linkedin.com/v1/companies/company-id"

#### Recuperar dados de uma empresa a partir de seu nome universal (não é possível definir os campos)
.get_company_universal_name('u-name') -> url de requisição: "https://api.linkedin.com/v1/companies/universal-name=u-name"

#### Recuperar N atualizações da página de uma empresa
.get_company_updates('company-id', N) -> url de requisição: "https://api.linkedin.com/v1/companies/2414183/updates?count=N"

#### Recuperar uma atualização específica de uma empresa
.get_company_update_key('company-id', 'update-key') -> url de requisição: "https://api.linkedin.com/v1/companies/company-id/updates/key=update-key"

#### Recuperar dados dos usuários/empresas que curtiram uma atualização específica de uma empresa
.get_company_update_likes('company-id', 'update-key') -> url de requisição: "https://api.linkedin.com/v1/companies/company-id/updates/key=update-key/likes"


