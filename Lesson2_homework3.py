# Deposit and withdraw money through ATM

def ATM(balance):
    input_type = input('Please select your transaction \n 1. Balance\n 2. Withdraw\n 3. Deposit\n 4. Exit  \n')
    while input_type != '4':
        if input_type == '1':
            print('Your balance is', balance)
        elif input_type == '2':
            withdraw_temp = int(input('Please select withdraw amount: '))
            if balance < withdraw_temp:
                print('Your balance is not enough')
            else:
                balance += - withdraw_temp
                print('Your balance is ', balance)
        elif input_type == '3':
            deposit_temp = int(input('Please select deposit amount: '))
            balance += deposit_temp
            print('Your balance is ', balance)
        input_type = input('Please select your transaction \n 1. Balance\n 2. Withdraw\n 3. Deposit\n 4. Exit  \n')

org_balance = 1000
ATM(org_balance)