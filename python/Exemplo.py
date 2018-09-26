from LinkedIn import LinkedIn

access_token = 'insira a sua access_token aqui'
rest_api = LinkedIn(access_token)

print rest_api.recuperar_usuario_id(id='DxrBGvdo-X', campos=['id', 'first-name', 'last-name'])
print '\n'
print rest_api.recuperar_usuario_url('https://www.linkedin.com/in/cristian-amaral-silva-72a0b4116/')
print '\n'
print rest_api.checar_compartilhamento_empresa('2414183')
print '\n'
print rest_api.recuperar_minhas_empresas()
print '\n'
print rest_api.recuperar_empresa_id(2414183)
print '\n'
print rest_api.recuperar_empresa_universal_name('devtestco1')
print '\n'
print rest_api.recuperar_updates_empresa('2414183', 2)
print '\n'
print rest_api.recuperar_update_empresa('2414183','UPDATE-c2414183-6449959607602376704')
print '\n'
print rest_api.recuperar_comentarios_update('2414183', 'UPDATE-c2414183-6449959607602376704')
print '\n'
print rest_api.recuperar_likes_update('2414183', 'UPDATE-c2414183-6449959607602376704')
print '\n'
print rest_api.recuperar_seguidores_empresa('2414183')
