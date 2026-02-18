# sistema bancario e transação
class Auth:
    def __init__(self):
        self.database = {}
    def register(self, username,password):
        if username in self.database:
            return False, "Usuário já existente!"
        self.database[username] = {"password":password,"saldo atual":0, "saldo pendente": 0}
        return True, "Usuário cadastrado, seu saldo atual é 0, até o momento você tem 0 reais para receber"

    def login(self, username, password):
        if username not in self.database:
            return False, "Usuário não encontrado!"
        else:
            if password != self.database[username]["password"]:
                return False, "Acesso negado!"
            return True, "Acesso concedido!"
    def transfer(self,active_user,active_password, received, password,quantia):
        self_active_saldo = self.database[active_user]["saldo atual"]
        self_active_saldo_pendente = self.database[active_user]["saldo pendente"]
        received_saldo = self.database[received]["saldo atual"]
        received_saldo_pendente = self.database[received]["saldo pendente"]
auth = Auth()
print(auth.register("matheus", "senha")[1])
print(auth.transfer("matheus","senha", 5))