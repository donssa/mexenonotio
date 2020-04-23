#código do git:

from notion.client import NotionClient
from notion.block import PageBlock
from notion.block import TodoBlock

import pandas as pd

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
token="8c367e647c7f3db99590cf5c6a12eaf148c13c825c88134327355f1f1838f54c7d7e5e9636a7b65bf6b91b09fc1e6958fde77bed6a0bb2cb721eb61e0c5984fe4d82e92fa48ef4ae0a706976755e"
#variável client é o "cliente" aberto no login do navegador. qual a segurança disso? posso tentar testar
client = NotionClient(token_v2=token)

#O DONSA
DONSA = client.get_block("29af322f-3eb3-40a7-89be-2dd7afd78408")
#Todas as páginas do DONSA
HOMEPAGE = client.get_block("29cd1701-b3f6-495e-b94e-535a2c03be37")
#sandbox pro python
sandbox = client.get_block("ab9ebc44-60fb-4dd6-8bb0-f4ca08d9730e")
Calendário = client.get_block("125a4883-97b2-4181-a46c-e0e42f40cd91")

coluna = client.get_collection("058cd2b2-735c-45a6-bc75-6be2b59caaa1")

filter_params = [{"TIPO": "DataCamp"}]

#print(client.get_block("125a4883-97b2-4181-a46c-e0e42f40cd91"))

#print(sandbox.children[1])

#sandbox.children.add_new(PageBlock, title='foi meu copaero')

#sandbox.children[0].add_new(PageBlock, title='foi meu copaero')


#for child in HOMEPAGE.children:
#    print(child)

#input("ENTER EXIT")
