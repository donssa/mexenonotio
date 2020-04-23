#código do git:

from notion.client import NotionClient

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
token="8c367e647c7f3db99590cf5c6a12eaf148c13c825c88134327355f1f1838f54c7d7e5e9636a7b65bf6b91b09fc1e6958fde77bed6a0bb2cb721eb61e0c5984fe4d82e92fa48ef4ae0a706976755e"
#variável client é o "cliente" aberto no login do navegador. qual a segurança disso? posso tentar testar
client = NotionClient(token_v2=token)

#Todas as páginas do DONSA
HOMEPAGE = client.get_block("29cd1701-b3f6-495e-b94e-535a2c03be37")
Calendário = client.get_block("125a4883-97b2-4181-a46c-e0e42f40cd91")

kidshome=HOMEPAGE.children
print(Calendário)
titulo=HOMEPAGE.title
pais=HOMEPAGE.parent

for child in HOMEPAGE.children:
    print(child)

print("Parent of {} is {}".format(HOMEPAGE.id, HOMEPAGE.parent.id))

#print("PARENTS:",pais,'\n')
#print("O tipo de estrutura do título é:",type(titulo),'\n')
#print("The child titles are:",'\n',kidshome,'\n')
#print("O tipo de estrutura dos blocos é:",type(kidshome),'\n')

# Note: You can use Markdown! We convert on-the-fly to Notion's internal formatted text data structure.



#input("ENTER EXIT")
