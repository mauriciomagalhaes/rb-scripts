
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import routeros_api
import json

conn = routeros_api.RouterOsApiPool(
    'IP', 
    username='admin', 
    password='',
    plaintext_login=True
    )
api = conn.get_api()

lista = api.get_resource('/ip/route')

ident = (lista.get(comment='ZIMBRA')[0]['id'])
stats = (lista.get(comment='ZIMBRA')[0]['disabled'])

if stats == 'true':
    print('Rota T3')
else:
    print('Rota VIVO')

print('Habilitar Rota digite 1 VIVO e 0 T3' )
escolha = input()

if escolha == '1':
    lista.set(id=ident, disabled="false")
else:
    lista.set(id=ident, disabled="true")
