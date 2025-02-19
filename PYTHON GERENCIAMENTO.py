# Classe para representar um item do inventário
class Item:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"Item {self.id}: {self.name} (Quantity: {self.quantity})"

# Classe para gerenciar o inventário
class InventoryManager:
    def __init__(self):
        self.items = []  # Lista para armazenar os itens
        self.next_id = 1  # ID para o próximo item a ser adicionado

    def add_item(self, name, quantity):
        # Cria e adiciona um novo item ao inventário
        item = Item(self.next_id, name, quantity)
        self.items.append(item)
        self.next_id += 1
        print(f"Added: {item}")

    def remove_item(self, item_id):
        # Remove o item com o ID especificado
        self.items = [item for item in self.items if item.id != item_id]
        print(f"ID de item removido: {item_id}")

    def list_items(self):
        # Lista todos os itens no inventário
        if not self.items:
            print("Sem item no estoque.")
        else:
            for item in self.items:
                print(item)

# Função principal que oferece um menu interativo para o usuário
def main():
    manager = InventoryManager()
    while True:
        print("\nInventory Manager")
        print("1. Adicionar Item")
        print("2. Remover Item")
        print("3. Listagem de itens")
        print("4. Sair")
        choice = input("Selecione a opção: ")

        if choice == '1':
            # Adicionar um novo item
            name = input("O nome do item: ")
            quantity = int(input("Quantidade do item: "))
            manager.add_item(name, quantity)
        elif choice == '2':
            # Remover um item existente
            item_id = int(input("Qual ID do item para remover: "))
            manager.remove_item(item_id)
        elif choice == '3':
            # Listar todos os itens
            manager.list_items()
        elif choice == '4':
            break
        else:
            print("Opção invalida. Tente novamente.")

if __name__ == "__MENU__":
    main()