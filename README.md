# Coleta-LinkedIn
Coleta de dados públicos da rede social LinkedIn

## Profile API

#### Recuperar dados do usuário que possui a access_token
.get_profile_id() -> url de requisição: "https://api.linkedin.com/v1/people/~"

#### Recuperar dados de um usuário a partir de seu identificador
.get_profile_id(id='user-id') -> url de requisição: "https://api.linkedin.com/v1/people/id=user-id"

#### Recuperar dados de um usuário a partir de seu url
.get_profile_url('user-url') -> url de requisição: "https://api.linkedin.com/v1/people/url=user-url"

#### Campos específicos de um usuário que podem ser utilizados para filtrar a resposta da requisição
https://developer.linkedin.com/docs/fields/basic-profile

#### Campos padrões da resposta (parâmetro "fields" não especificado)
'headline', 'last-name', 'id' e 'first-name'

#### Exemplo de uma requisição utilizando de campos específicos
.get_profile_id(id='user-id', fields=['id', 'first-name', 'last-name']) -> url de requisição: "https://api.linkedin.com/v1/people/id=user-id:(id,first-name,last-name)"





