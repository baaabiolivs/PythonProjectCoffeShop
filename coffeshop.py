# Coffee Shops Tia Rosa - Sistema Simples
# Autor: Bárbara
# Sistema simples em Python com menu de opções
# Usando listas e dicionários para guardar dados
# Observação: foquei em lógica/estruturas, por isso usei interface em linha de comando.
produtos = []      # {"nome": "Cappuccino", "preco": 12.5, "ingredientes": ["café", "leite", "açúcar"]}
clientes = []      # {"nome": "Ana", "telefone": "61..."}
pedidos = []       # {"cliente": "Ana", "itens": [{"produto": "Cappuccino", "qtd": 2}], "total": 25.0}

# Lista com produtos
produtos = [
    {"nome": "Cappuccino", "preco": 12.50, "ingredientes": "Café, leite vaporizado, açúcar, canela"},
    {"nome": "Pão de Queijo", "preco": 5.00, "ingredientes": "Queijo, polvilho"},
    {"nome": "Bolo de Cenoura", "preco": 8.00, "ingredientes": "Cenoura, farinha, açúcar, chocolate"}
]

# Lista com clientes
clientes = [
    {"nome": "Pedro Guilherme", "telefone": "61 99273-1111"},
    {"nome": "Nícolas Santos", "telefone": "61 99664-6765"},
    {"nome": "Ana Souza", "telefone": "61 98408-9000"}
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
    """
    Registra um pedido com múltiplos itens.
    Enquanto não digitar 0, dá pra ir adicionando produtos.
    """
    print("\n--- Registrar Pedido ---")

    # checagens básicas
    if not clientes:
        print("⚠ Nenhum cliente cadastrado! Cadastre antes de fazer um pedido.")
        return
    if not produtos:
        print("⚠ Nenhum produto cadastrado! Cadastre antes de fazer um pedido.")
        return

    # escolher cliente
    listar_clientes()
    try:
        cliente_id = int(input("Escolha o número do cliente: ").strip()) - 1
        cliente = clientes[cliente_id]
    except (ValueError, IndexError):
        print("Cliente inválido.")
        return

    itens = []
    total = 0.0

    # loop para adicionar vários itens
    while True:
        print("\n--- Produtos ---")
        for i, p in enumerate(produtos, start=1):
            print(f"{i}. {p['nome']} - R$ {p['preco']:.2f}")

        escolha = input("Produto (número) — 0 para finalizar: ").strip()
        try:
            idx = int(escolha)
        except ValueError:
            print("Digite um número válido.")
            continue

        if idx == 0:
            break
        if not (1 <= idx <= len(produtos)):
            print("Produto inválido.")
            continue

        try:
            qtd = int(input("Quantidade: ").strip())
            if qtd <= 0:
                print("Quantidade deve ser positiva.")
                continue
        except ValueError:
            print("Quantidade inválida.")
            continue

        prod = produtos[idx - 1]
        itens.append({"produto": prod["nome"], "qtd": qtd, "preco": prod["preco"]})
        total += prod["preco"] * qtd
        print(f"✔ Adicionado: {qtd}x {prod['nome']}")

    if not itens:
        print("Pedido vazio, operação cancelada.")
        return

    pedidos.append({"cliente": cliente['nome'], "itens": itens, "total": total})
    print(f"✅ Pedido registrado para {cliente['nome']}! Total: R$ {total:.2f}")



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
