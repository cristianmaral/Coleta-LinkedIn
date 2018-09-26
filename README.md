# Coleta-LinkedIn
Devido a uma falta de materiais e bibliotecas disponíveis que facilitam a interação entre o desenvolvedor e a API oficial do **LinkedIn** (https://developer.linkedin.com/docs/rest-api), este projeto está sendo desenvolvido com o intuito de proporcionar um acesso rápido e intuitivo às funcionalidades disponibilizadas pela mesma que possuem algum tipo de relação com coleta de dados públicos.

Vale ressaltar que a coleta de dados públicos referentes à rede social LinkedIn é bastante restrita, visto que a maioria das requisições fornecidas por sua API oficial necessitam do identificador único de um usuário ou empresa e a prática de uma coleta por meios automatizados de **"raspagem"** é estritamente proibida e pode acarretar em medidas judiciais.

Dito isso, ao utilizar esta biblioteca, tenha em mente que a **Rest API** foi disponibilizada com o intuito de proporcionar a possibilidade da criação de aplicativos/plugins para a sua plataforma e não de fornecer uma forma de coleta de dados eficiente.

## Requisitos de utilização
Para que os métodos que serão explicados ao longo deste documento possam ser utilizados corretamente, é necessário uma **access_token**, que é uma chave de acesso única que pode ser obtida através deste tutorial oficial: https://developer.linkedin.com/docs/oauth2.

#### ATENÇÃO
**Este processo é bastante burocrático e requer um certo tempo para ser concluído.**

## Observações importantes
  * Todas as requisições à API oficial que são realizadas por esta biblioteca utiliza como um parâmetro adicional o formato em que os resultados devem ser obtidos. Em prol de uma maior legibilidade das informações, **json** foi o formato escolhido.
  * Nenhum método de requisição **POST** foi implementado devido ao objetivo do projeto, que é voltado apenas para a coleta de dados e não para o compartilhamento automatizado de informações/comentários.

## Profile API
Mais informações em https://developer.linkedin.com/docs/guide/v2/people/profile-api

### Campos específicos de um usuário
https://developer.linkedin.com/docs/fields/basic-profile

### Campos padrões da resposta (parâmetro "campos" não especificado)
'headline', 'last-name', 'id' e 'first-name'

### Recuperar dados do usuário que possui a access_token
.recuperar_usuario_id() -> url de requisição: "https://api.linkedin.com/v1/people/~"

### Recuperar dados de um usuário a partir de seu identificador
.recuperar_usuario_id(id='user-id') -> url de requisição: "https://api.linkedin.com/v1/people/id=user-id"

### Recuperar dados de um usuário a partir de seu url
.recuperar_usuario_url('user-url') -> url de requisição: "https://api.linkedin.com/v1/people/url=user-url"

### Exemplo de uma requisição utilizando campos específicos
.recuperar_usuario_id(id='user-id', campos=['id', 'first-name', 'last-name']) -> url de requisição: "https://api.linkedin.com/v1/people/id=user-id:(id,first-name,last-name)"

## Company API
Mais informações em https://developer.linkedin.com/docs/company-pages

### Campos específicos de uma empresa
https://developer.linkedin.com/docs/fields/company-profile

### Campos padrões da resposta (parâmetro "campos" não especificado)
'id' e 'name'

### Recuperar os dados das empresas em que o usuário que possui a access_token é administrador
.recuperar_minhas_empresas() -> url de requisição: "https://api.linkedin.com/v1/companies"

### Recuperar dados de uma empresa a partir de seu identificador
.recuperar_empresa_id('company-id') -> url de requisição: "https://api.linkedin.com/v1/companies/company-id"

### Recuperar dados de uma empresa a partir de seu nome universal (não é possível definir os campos)
.recuperar_empresa_universal_name('u-name') -> url de requisição: "https://api.linkedin.com/v1/companies/universal-name=u-name"

### Recuperar N atualizações da página de uma empresa
.recuperar_updates_empresa('company-id', N) -> url de requisição: "https://api.linkedin.com/v1/companies/company-id/updates?count=N"

### Recuperar uma atualização específica de uma empresa
.recuperar_update_empresa('company-id', 'update-key') -> url de requisição: "https://api.linkedin.com/v1/companies/company-id/updates/key=update-key"

### Recuperar dados referentes aos comentários de uma atualização específica de uma empresa
.recuperar_comentarios_update('company-id', 'update-key') -> url de requisição: "https://api.linkedin.com/v1/companies/company-id/updates/key=update-key/update-comments"

### Recuperar dados dos usuários/empresas que curtiram uma atualização específica de uma empresa
.recuperar_likes_update('company-id', 'update-key') -> url de requisição: "https://api.linkedin.com/v1/companies/company-id/updates/key=update-key/likes"

### Recuperar a quantidade de seguidores de uma empresa
.recuperar_seguidores_empresa('company-id') -> url de requisição: "https://api.linkedin.com/v1/companies/company-id/num-followers"

### Recuperar as estatísticas de uma empresa
O retorno desta requisição é composto por alguns campos específicos, sendo necessário a utilização dos seguintes links para suas devidas interpretações:

Company Size -> https://developer.linkedin.com/docs/reference/company-size-codes

Region -> https://developer.linkedin.com/docs/reference/geography-codes

Job Function -> https://developer.linkedin.com/docs/reference/job-function-codes

Employee Seniority -> https://developer.linkedin.com/docs/reference/seniority-codes


.recuperar_estatisticas_empresa('company-id') -> url de requisição: "https://api.linkedin.com/v1/companies/company-id/company-statistics"

#### ATENÇÃO
Esta requisição está retornando uma mensagem de erro interno da Rest API, pode ser um problema momentâneo ou esta possibilidade de recuperação está sendo desabilitada pelos desenvolvedores do LinkedIn.

### Conferir se é possível compartilhar informações na página de uma empresa (true ou false)
.checar_compartilhamento_empresa('company-id') -> url de requisição: "https://api.linkedin.com/v1/companies/company-id/is-company-share-enabled"

### Conferir se o usuário que possui a access_token é administrador de uma empresa (true ou false)
.checar_adm_empresa('company_id') -> url de requisição: "https://api.linkedin.com/v1/companies/company-id/relation-to-viewer/is-company-share-enabled"

## Dados disponibilizados pelo LinkedIn de uma empresa própria para testes de desenvolvedores
Company Name: DevTestCo

Company URL: https://www.linkedin.com/company/devtestco

Company ID: 2414183 
