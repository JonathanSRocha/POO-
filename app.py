class ContaBancaria:
    def __init__(self, nome, saldo=0):
        self.nome = nome
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor} realizado. Novo saldo: R${self.saldo}')
        else:
            print('Valor de depósito inválido.')

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado. Novo saldo: R${self.saldo}')
        else:
            print('Saque não permitido. Saldo insuficiente.')

    def consultar_saldo(self):
        print(f'Saldo atual de {self.nome}: R${self.saldo}')

# Criando uma conta bancária
minha_conta = ContaBancaria("João", 1000)

# Simulando transações com condicionais
while True:
    print("\nEscolha uma ação:")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Sair")
    
    escolha = input("Digite o número da ação desejada: ")

    if escolha == "1":
        minha_conta.consultar_saldo()
    elif escolha == "2":
        valor = float(input("Digite o valor do depósito: R$"))
        minha_conta.depositar(valor)
    elif escolha == "3":
        valor = float(input("Digite o valor do saque: R$"))
        minha_conta.sacar(valor)
    elif escolha == "4":
        print("Saindo do programa.")
        break
    else:
        print("Escolha inválida. Tente novamente.")

