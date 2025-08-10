# Coffee Shops Tia Rosa - Sistema Básico
# Autor: Bárbara
# Sistema simples em Python com menu de opções
# Usando listas e dicionários para guardar dados

# Lista com produtos de exemplo
produtos = [
    {"nome": "Cappuccino", "preco": 12.50, "ingredientes": "Café, leite, açúcar"},
    {"nome": "Pão de Queijo", "preco": 5.00, "ingredientes": "Queijo, polvilho"},
    {"nome": "Bolo de Cenoura", "preco": 8.00, "ingredientes": "Cenoura, farinha, chocolate"}
]

# Lista com clientes de exemplo
clientes = [
    {"nome": "Maria Silva", "telefone": "61 99999-1111"},
    {"nome": "João Pereira", "telefone": "61 98888-2222"},
    {"nome": "Ana Souza", "telefone": "61 97777-3333"}
]

# Lista para pedidos
pedidos = []


# ----------- FUNÇÕES DE PRODUTOS -----------

def cadastrar_produto():
    print("\n--- Cadastro de Produto ---")
    nome = input("Nome do produto: ")
    preco = float(input("Preço (R$): "))
    ingredientes = input("Ingredientes: ")

    produto = {"nome": nome, "preco": preco, "ingredientes": ingredientes}
    produtos.append(produto)
    print(f"✅ Produto '{nome}' cadastrado com sucesso!")


def listar_produtos():
    print("\n--- Lista de Produtos ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for i, p in enumerate(produtos, start=1):
            print(f"{i}. {p['nome']} - R${p['preco']:.2f} | Ingredientes: {p['ingredientes']}")


# ----------- FUNÇÕES DE CLIENTES -----------

def cadastrar_cliente():
    print("\n--- Cadastro de Cliente ---")
    nome = input("Nome do cliente: ")
    telefone = input("Telefone: ")

    cliente = {"nome": nome, "telefone": telefone}
    clientes.append(cliente)
    print(f"✅ Cliente '{nome}' cadastrado com sucesso!")


def listar_clientes():
    print("\n--- Lista de Clientes ---")
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for i, c in enumerate(clientes, start=1):
            print(f"{i}. {c['nome']} - Tel: {c['telefone']}")


# ----------- FUNÇÕES DE PEDIDOS -----------

def registrar_pedido():
    print("\n--- Registrar Pedido ---")
    if not clientes:
        print("⚠ Nenhum cliente cadastrado! Cadastre antes de fazer um pedido.")
        return
    if not produtos:
        print("⚠ Nenhum produto cadastrado! Cadastre antes de fazer um pedido.")
        return

    listar_clientes()
    cliente_id = int(input("Escolha o número do cliente: ")) - 1
    cliente = clientes[cliente_id]

    listar_produtos()
    produto_id = int(input("Escolha o número do produto: ")) - 1
    produto = produtos[produto_id]

    pedido = {"cliente": cliente["nome"], "produto": produto["nome"], "valor": produto["preco"]}
    pedidos.append(pedido)
    print(f"✅ Pedido registrado: {cliente['nome']} pediu {produto['nome']}.")


def listar_pedidos():
    print("\n--- Lista de Pedidos ---")
    if not pedidos:
        print("Nenhum pedido registrado.")
    else:
        total = 0
        for i, p in enumerate(pedidos, start=1):
            print(f"{i}. Cliente: {p['cliente']} | Produto: {p['produto']} | Valor: R${p['valor']:.2f}")
            total += p['valor']
        print(f"💰 Total em vendas: R${total:.2f}")


# ----------- MENU PRINCIPAL -----------

def menu():
    while True:
        print("\n=== Coffee Shops Tia Rosa ===")
        print("1. Cadastrar Produto")
        print("2. Listar Produtos")
        print("3. Cadastrar Cliente")
        print("4. Listar Clientes")
        print("5. Registrar Pedido")
        print("6. Listar Pedidos")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            cadastrar_cliente()
        elif opcao == "4":
            listar_clientes()
        elif opcao == "5":
            registrar_pedido()
        elif opcao == "6":
            listar_pedidos()
        elif opcao == "7":
            print("Saindo do sistema... ☕")
            break
        else:
            print("Opção inválida! Tente novamente.")


# ----------- INÍCIO DO PROGRAMA -----------

menu()
