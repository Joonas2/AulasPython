"""Tratamento de erros e exceções"""

#try tente fazer a operação
    #operação
#except: se der erro, irá executar o codigo aqui dentro
# else: irá executar se não houver erro
#finally: ira aconter indepentende se destiver certo ou errado

try:
    a = int(input('Digite um numero: '))
    b = int(input(('Digite um numero: ')))
    r = a/b

except(ValueError, TypeError):
    print('Tivemos uma problema com os tipos de dados')
except KeyboardInterrupt:
    print('O Usuario não informou os tipos de dados')

else:
    print(r)
finally: #ira acontecer sempre, pode ser utilizado para finalizar um arquivo, fechar o BD, algo assim
    print('volte sempre')