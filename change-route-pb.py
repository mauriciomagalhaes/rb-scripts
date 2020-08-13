
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import routeros_api
import json
from lib import *
import time

conn = routeros_api.RouterOsApiPool(
    '10.4.1.1', 
    username='admin', 
    password='passwd',
    plaintext_login=True
    )

api = conn.get_api()

lista = api.get_resource('/ip/route')

ident = (lista.get(comment='ZIMBRA')[0]['id'])
stats = (lista.get(comment='ZIMBRA')[0]['disabled'])

if stats == 'true':
    point = ['T3 Dedicado **','Vivo Adsl','Sair'] 
else:
    point = ['T3 Dedicado','Vivo Adsl <=','Sair'] 
    
while True:
        
    resposta = menu(point)
    
    if resposta == 1:
         lista.set(id=ident, disabled="true")
         point = ['T3 Dedicado *','Vivo Adsl','Sair']
    elif resposta == 2:
         lista.set(id=ident, disabled="false")
         point = ['T3 Dedicado','Vivo Adsl *','Sair'] 
    elif resposta == 3:
        print('Saindo do Sistema ...')
        time.sleep(3)
        break
    else:
        print('ERRO! Digite uma opção válida!')

