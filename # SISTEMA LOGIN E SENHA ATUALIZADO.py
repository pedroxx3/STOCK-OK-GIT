# SISTEMA LOGIN E SENHA
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# Classe para gerenciar os usuários
class UserManager:
    def __init__(self):
        self.users = {}
        self.add_user('admin', 'admin')  # Adiciona um usuário padrão

    def add_user(self, username, password):
        self.users[username] = User(username, password)

    def authenticate(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            return True
        return False

# Classe para representar um item do inventário
class Item:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"Produto {self.id}: {self.name} (Quantidade: {self.quantity})"

# Classe para gerenciar o inventário
class InventoryManager:
    def __init__(self):
        self.items = []
        self.next_id = 1

    def add_item(self, name, quantity):
        item = Item(self.next_id, name, quantity)
        self.items.append(item)
        self.next_id += 1
        print(f"Adicionado: {item}")

    def remove_item(self, item_id):
        self.items = [item for item in self.items if item.id != item_id]
        print(f"Produto removido ID: {item_id}")

    def list_items(self):
        if not self.items:
            print("Sem produtos no estoque.")
        else:
            for item in self.items:
                print(item)

# Função principal que oferece um menu interativo para o usuário
def main():
    user_manager = UserManager()
    inventory_manager = InventoryManager()

    print("Bem vindo ao StockOK")

    # Autenticação do usuário
    while True:
        username = input("Usuario: ")
        password = input("Senha: ")
        if user_manager.authenticate(username, password):
            print("Logado!")
            break
        else:
            print("Usuario inválido ou senha. Tente novamente.")

    # Menu interativo para gerenciamento de estoque
    while True:
        print("\nInventário")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Lista de Produtos")
        print("4. Sair")
        choice = input("Selecione uma opção: ")

        if choice == '1':
            name = input("Nome do Produto: ")
            quantity = int(input("Quantidade do Produto: "))
            inventory_manager.add_item(name, quantity)
        elif choice == '2':
            item_id = int(input("Digite o ID do produto a ser removido: "))
            inventory_manager.remove_item(item_id)
        elif choice == '3':
            inventory_manager.list_items()
        elif choice == '4':
            break
        else:
            print("Opção Inválida. Tente novamente.")

if __name__ == "__main__":
    main()