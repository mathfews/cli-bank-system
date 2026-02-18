import os
from auth import Auth
auth = Auth()
def clean_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def bank_ui(active_user):
    info = auth.show_info(active_user)
    bank_ui = f"""╔════════════════╗
║  🏦 BANKSTACK  ║
╚════════════════╝
👤 Username :  {active_user}
💰 Current balance:  ${info["current balance"]:.2f}
📥 Pending Incoming: ${info["pending incoming"]:.2f}
---------------------------
1) Deposit ➕💵
2) Withdraw ➖💸
3) Transfer 🔄💰
4) Exit 🚪"""
    print(bank_ui)
def user_auth(type):
        while True:
            clean_terminal()
            username = input("Enter your username(Digit 0 to return): ")
            if username == "0":
                 clean_terminal()
                 break
            password = input("Enter your password: ")
            result = getattr(auth, type)(username,password)
            if type == "register" and result[0] == True:
                 print(f"{result[1]} | Press enter return")
                 input("")
                 break
            if result[0]:
                print(f"{result[1]} | Press enter in your account")
                input("")
                return username
            print(f"{result[1]} | Press enter to try again")
            input("")
while True:
    while True:
                while True:
                    try:
                        amount = float(input("> Deposit amount: "))
                        if auth.deposit(username, amount):
                            print(f"Transferência feita com sucesso!")
                            input("")
                            break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                        input("")
        elif user_input == "withdraw" or user_input == "2":
            print(auth.withdraw(username)[1])
            input("")
        elif user_input == "transfer" or user_input == "3":
            recipient = input("> Enter recipient username: ")
            amount = float(input("> Enter amount to transfer: "))
            while True:
                confirm = input(f"Confirm transfer of ${amount} to {recipient} (y/n) ") 
                if confirm == "y":
                    break
            result = auth.transfer(username,user_info["db_password"], recipient, amount)
            print(f"* {result[1]}")
            input("")
        elif user_input == "exit" or user_input == "4":
            input("Press enter to exit")
            clean_terminal()
            break