##Conta  Numero conta, Titular
##Extrato
##Deposito
##Saque
##Saldo Disponivel
##Transferencia
##Recarga
##Emprestimo

class Banco: ##Atributos privados nome,agencia e numero
    def __init__(self,nome_titular, agencia,numero_conta):
        self._nome_titular=nome_titular
        self._agencia=agencia
        self._numero_conta=numero_conta
        self.extrato=[]
        self.total=float
      
    ##DEPOSITOS E INSERÇÃO DE DEPOSITO MAX   
    def deposito(self):
        valor=float(input('Digite um valor para deposito '))
        self.extrato.append(valor)
        self.total=sum(self.extrato)
        
            
    ##FUNÇÃO PARA SALDO TOTAL   
    def total_conta(self):
        print(f'Seu saldo atual é de  R${self.total}')
        print('-=-' *10)
    
    ##FUNÇÃO PARA SAQUE 
    def saque(self):
        valor=float(input('Digite o valor que deseja sacar '))
        if valor > self.total:
            print('O valor que deseja sacar excede seu limite bancario ')
            print('-=-' *10)
        else:
            self.total-=valor
            print(f'Valor de R${valor} sacado com sucesso ')
            print('-=-' *10)
    
    ##FUNÇÃO DE RECARGA
    def recarga(self):
        print('Digite o numero do celular, operadora e valor do credito')
        numero=input('numero: ')
        print('-=-' *10)
        operadora=input('operadora: ')
        print('-=-' *10)
        credito=float(input('credito: '))
        if credito > self.total:
            print('Valor acima do saldo: ')
        else:
            self.total-=credito
            print(f'Celular carregado com valor de R${credito} de credito com sucesso ') 
            print('-=-' *10)
            
    ##HISTORICO DE DEPOSITOS
    def historico(self):
        print('historico de depositos'.upper())
        for n in self.extrato:
            print('-=-' *10)
            print(f'Valor depositado de {n}')
            print('-=-' *10)  
            
p1=Banco('Addam','21564',1525)
p1.deposito()
p1.deposito()
p1.total_conta()
p1.saque()
p1.total_conta()
p1.recarga()
p1.total_conta()
p1.historico()



