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
        self.saldo=[]
    
    ##Senha vai ficar salva
    #input('Digite a senha para realizar login ') 

    print('-=-' *10)
    print('Bem vindo ao seu aplicativo de banco'.upper())
    print('Por padrão como sua conta foi criada agora, voce tem um bonus' 
          'de deposito de R$100, aproveite para movimentar sua conta')
    print('-=-' *10)
    
    ##Escolha das opções de serviço no app do banco
    print('Qual das opções voce deseja escolher ')

    ##FUNÇÃO PARA DEPOSITO
    def depositar(self):
        valor=int(input('Qual quantia deseja depositar ?'))
        self.saldo.append(valor)
        print('Historico de deposito')
        print('-=-' *14)
        for n in self.saldo:
            print(n)
            print('-=-'*14)
    
    ##FUNÇÃO PARA SALDO ATUAL    
    def saldo_atual(self):
        print(self.saldo)
        tot=sum(self.saldo)
        for t in self.saldo:
            print('Deposito')
            print(t)
            print('=-='*8)
        print(f'Saldo atual na conta é de  R${tot}')
    
    ##FUNÇÃO PARA TRANSFERENCIA
    def transferencia(self):
        transferir=int(input('Selecione um valor para transferir '))
        print(self.saldo)
        tot=sum(self.saldo)
        if self.saldo>tot:
            print(f'Transferencia aprovada de R${transferir}')
            self.saldo=self.saldo-tot
        else:
            print('Valor para trasnferencia insuficiente')
        
    ##FUNÇÃO PARA SAQUE
    def saque(self):
        saque=int(input('Qual quantia deseja sacar ?'))
        total=sum(self.saldo)
        if saque > total:
            print(f'Voce não pode sacar, pois não existe R${total} na sua conta')
        else:
            valor_atual=total-saque
            print(valor_atual)
            
            
        
        
    
p1=Banco('Addam','2569','123456')
print(p1._nome_titular)
p1.depositar()
p1.saldo_atual()
p1.depositar()
p1.saldo_atual()
