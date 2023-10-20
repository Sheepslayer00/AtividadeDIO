menu="""
###########Seja Bem Vindo##########
  Qual operação deseja realizar ?
  [s]Saque
  [d]Deposito
  [e]Extrato
  [q]Sair do menu
###################################
"""
saldo=1500
vezes_de_saque=0
extrato=""
LIMITE_DE_SAQUE=500
LIMITE_DE_VEZES_DE_SAQUE=3

while True:
    opçao=input(menu)
    if opçao=="d":
        valor=float(input("qual o valor que deseja depositar?\n"))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito de R$ {valor:.2f}\n"
        else :
            print("valor invalido!")
    
    if opçao == "e":
        if extrato != "":
            print(f"Segue Extrato:\n{extrato}Saldo final R$ {saldo:.2f}")
        else: 
            print("nao foram realizadas movimentaçoes")
    if opçao== "q":
        print("obrigado pela preferencia ")
        break
        
    if opçao == "s":
        if vezes_de_saque < LIMITE_DE_VEZES_DE_SAQUE:
            valor=float(input("qual o valor que voce deseja sacar ?\n"))
            if valor <= LIMITE_DE_SAQUE:
                 if valor <= saldo:
                    saldo -= valor
                    extrato += f"Saque de R$ {valor:.2f}\n"
                    vezes_de_saque +=1
                 else:
                     print('saldo insuficiente:')
                     
            else :
                print('Valor do saque execido')
        else :
            print('limite de saque ultrapassado')
        

