pacientes = [] # Lista para armazenar os dados dos pacientes
dentistas = [] # Lista para armazenar os dados dos dentistas
atendimentos = [] # Lista para armazenar os dados dos atendimentos
 
def validar_cpf(prompt): # Função para validar o CPF
    while True:
        cpf = input(prompt).strip().replace('.', '').replace('-', '') # Remove pontos e traços
        if len(cpf) == 11 and cpf.isdigit(): # Verifica se o CPF tem 11 dígitos numéricos
            return cpf # Retorna o CPF válido
        else:
            print("Erro: CPF inválido. Por favor, digite 11 dígitos numéricos.") 

def validar_string(prompt): # Função para validar entradas de texto
    while True:
        texto = input(prompt).strip() 
        if texto:
            return texto # Retorna o texto se não estiver vazio
        else: # Se estiver vazio, exibe uma mensagem de erro
            print("Erro: O campo não pode estar vazio.")

def validar_inteiro(prompt): # Função para validar entradas numéricas inteiras
    while True:
        valor = input(prompt).strip()  
        if valor.isdigit(): # Verifica se a entrada é composta apenas por dígitos
            return int(valor)  # Converte e retorna o valor como inteiro
        else: # Se não for um número inteiro, exibe uma mensagem de erro
            print("Erro: Entrada inválida. Por favor, digite um número inteiro.") 

def cadastrar_paciente(): # Função para cadastrar um novo paciente
    print("\n--- CADASTRAR PACIENTE ---")
    nome_paciente = validar_string("Digite o nome do paciente: ")
    idade_paciente = validar_inteiro("Digite a idade do paciente: ")
    cpf_paciente = validar_cpf("Digite o CPF do paciente: ")
    endereco_paciente = validar_string("Digite o endereço do paciente: ")
    problema_saude = validar_string("Descreva o problema de saúde bucal do paciente: ")
    telefone_paciente = validar_string("Digite o telefone do paciente: ")

    novo_paciente = { # Cria um dicionário com os dados do paciente
        "nome": nome_paciente,
        "idade": idade_paciente,
        "cpf": cpf_paciente,
        "endereco": endereco_paciente,
        "problema_saude": problema_saude,
        "telefone": telefone_paciente
    }
    pacientes.append(novo_paciente) # Adiciona o novo paciente à lista
    print(f"\nPaciente {nome_paciente} cadastrado com sucesso!") 

def cadastrar_dentista(): # Função para cadastrar um novo dentista
    print("\n--- CADASTRAR DENTISTA ---")
    nome_dentista = validar_string("Digite o nome do dentista: ")
    cro_dentista = validar_string("Digite o CRO do dentista: ")
    endereco_dentista = validar_string("Digite o endereço do consultório do dentista: ")
    telefone_dentista = validar_string("Digite o telefone do dentista: ")

    novo_dentista = { # Cria um dicionário com os dados do dentista
        "nome": nome_dentista,
        "cro": cro_dentista,
        "endereco": endereco_dentista,
        "telefone": telefone_dentista
    }
    dentistas.append(novo_dentista) # Adiciona o novo dentista à lista
    print(f"\nDentista {nome_dentista} cadastrado com sucesso!")

def ver_registros_pacientes(): # Função para ver os registros dos pacientes
    print("\n--- REGISTROS DE PACIENTES ---")
    if not pacientes: # Verifica se a lista de pacientes está vazia
        print("Nenhum paciente cadastrado.")
        return

    paciente_busca = input("Digite o nome do paciente para buscar (ou deixe vazio para ver todos): ").strip().lower()

    if paciente_busca: # Busca específica
        encontrados = [p for p in pacientes if paciente_busca in str(p['nome']).lower()] # Busca pacientes pelo nome
        if encontrados: # Se encontrou pacientes
            print("\nPacientes Encontrados:")
            for p in encontrados:  # Imprime os dados dos pacientes encontrados
                print(f"Nome: {p['nome']}, Idade: {p['idade']}, CPF: {p['cpf']}, Endereço: {p['endereco']}, Problema: {p['problema_saude']}, Telefone: {p['telefone']}")
        else:
            print(f"Nenhum paciente encontrado com o nome '{paciente_busca}'.") # Nenhum paciente encontrado
    else:
        print("\nTodos os Pacientes Cadastrados:") 
        for p in pacientes: # Imprime os dados de todos os pacientes
            print(f"Nome: {p['nome']}, Idade: {p['idade']}, CPF: {p['cpf']}, Endereço: {p['endereco']}, Problema: {p['problema_saude']}, Telefone: {p['telefone']}")

def ver_registros_dentistas(): # Função para ver os registros dos dentistas
    print("\n--- REGISTROS DE DENTISTAS ---")
    if not dentistas: # Verifica se a lista de dentistas está vazia
        print("Nenhum dentista cadastrado.")
        return

    dentista_busca = input("Digite o nome do dentista para buscar (ou deixe vazio para ver todos): ").strip().lower()

    if dentista_busca: # Busca específica
        encontrados = [d for d in dentistas if dentista_busca in str(d['nome']).lower()] # Busca dentistas pelo nome
        if encontrados: # Se encontrou dentistas
            print("\nDentistas Encontrados:")
            for d in encontrados: # Imprime os dados dos dentistas encontrados
                print(f"Nome: {d['nome']}, CRO: {d['cro']}, Endereço: {d['endereco']}, Telefone: {d['telefone']}") 
        else:
            print(f"Nenhum dentista encontrado com o nome '{dentista_busca}'.") # Nenhum dentista encontrado
    else:
        print("\nTodos os Dentistas Cadastrados:") 
        for d in dentistas: # Imprime os dados de todos os dentistas
            print(f"Nome: {d['nome']}, CRO: {d['cro']}, Endereço: {d['endereco']}, Telefone: {d['telefone']}")

def registrar_atendimento(): # Função para registrar um atendimento
    print("\n--- REGISTRAR ATENDIMENTO ---")
    data_atendimento = validar_string("Digite a data do atendimento (DD/MM/AAAA): ")
    nome_paciente = validar_string("Digite o nome do paciente: ")
    tratamento_realizado = validar_string("Descreva o tratamento realizado: ")
    relatorio = validar_string("Digite o relatório do atendimento: ")

    novo_atendimento = { # Cria um dicionário com os dados do atendimento
        "data": data_atendimento,
        "paciente": nome_paciente,
        "tratamento": tratamento_realizado,
        "relatorio": relatorio
    }
    atendimentos.append(novo_atendimento) # Adiciona o novo atendimento à lista
    print("\nRelatório de atendimento registrado com sucesso!")

def relatorio_atendimentos(): # Função para gerar o relatório de atendimentos
    print("\n--- RELATÓRIO DE ATENDIMENTOS ---")  
    if not atendimentos: # Verifica se a lista de atendimentos está vazia
        print("Nenhum atendimento registrado.")
        return

    print("\nTodos os Atendimentos Registrados:")
    for a in atendimentos: # Imprime os dados de todos os atendimentos
        print(f"Data: {a['data']}, Paciente: {a['paciente']}, Tratamento: {a['tratamento']}, Relatório: {a['relatorio']}")

def menu_principal(): # Função para exibir o menu principal
    print("BEM VINDO AO SISTEMA DA ONG TURMA DO BEM!")
    while True:  # Loop infinito para o menu principal
        print("\n================ MENU DE OPÇÕES ================")
        print("1 - ONG TURMA DO BEM")
        print("2 - DENTISTAS")
        print("3 - SAIR")

        escolha = validar_inteiro("Escolha uma opção: ")  

        if escolha == 1: # Chama o submenu da ONG
            submenu_opcao1()
        elif escolha == 2: # Chama o submenu dos dentistas
            submenu_opcao2()
        elif escolha == 3: # Sai do sistema
            print("SAINDO DO SISTEMA...")
            break 
        else: # Opção inválida
            print("Opção inválida! Tente novamente.")

def submenu_opcao1(): # Função para o submenu da ONG
    while True: # Loop infinito para o submenu da ONG
        print("\n================ MENU ONG TURMA DO BEM ================")
        print("1 - CADASTRAR PACIENTE")
        print("2 - CADASTRAR DENTISTA")
        print("3 - VER REGISTROS DE PACIENTES")
        print("4 - VER REGISTROS DE DENTISTAS")
        print("5 - VOLTAR AO MENU PRINCIPAL")

        escolha = validar_inteiro("Escolha uma opção: ")

        if escolha == 1: # Chama a função para cadastrar paciente
            cadastrar_paciente()
        elif escolha == 2: # Chama a função para cadastrar dentista
            cadastrar_dentista()
        elif escolha == 3: # Chama a função para ver registros de pacientes
            ver_registros_pacientes()
        elif escolha == 4: # Chama a função para ver registros de dentistas
            ver_registros_dentistas()
        elif escolha == 5: # Volta ao menu principal
            print("Voltando ao menu principal...")
            break
        else: # Opção inválida
            print("Opção inválida! Tente novamente.")

def submenu_opcao2(): # Função para o submenu dos dentistas
    while True:  # Loop infinito para o submenu dos dentistas
        print("\n================ MENU DENTISTAS ================")
        print("1 - REGISTRAR ATENDIMENTO")
        print("2 - RELATÓRIO DE ATENDIMENTOS")
        print("3 - VOLTAR AO MENU PRINCIPAL")

        escolha = validar_inteiro("Escolha uma opção: ")

        if escolha == 1: # Chama a função para registrar atendimento
            registrar_atendimento()
        elif escolha == 2:  # Chama a função para gerar relatório de atendimentos
            relatorio_atendimentos()
        elif escolha == 3: # Volta ao menu principal
            print("Voltando ao menu principal...")
            break
        else: # Opção inválida
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__": # Ponto de entrada do programa
    menu_principal()  # Chama a função do menu principal