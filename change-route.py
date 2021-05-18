
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import routeros_api
import json
from lib import *

conn = routeros_api.RouterOsApiPool(
    '10.4.1.1', 
    username='', 
    password='',
    plaintext_login=True
    )

api = conn.get_api()

lista = api.get_resource('/ip/route')

ident = (lista.get(comment='ZIMBRA')[0]['id'])
stats = (lista.get(comment='ZIMBRA')[0]['disabled'])

while True:
    resposta = menu(['T3 Dedicado','Vivo Adsl','Sair'])
    if resposta == 1:
         lista.set(id=ident, disabled="true")
    elif resposta == 2:
         lista.set(id=ident, disabled="false")
    elif resposta == 3:
        print('Saindo do Sistema')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')

