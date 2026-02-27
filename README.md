#Sistema de Gestão - ONG Turma do Bem 🦷

Este é um sistema de gerenciamento via linha de comando (CLI) desenvolvido em **Python**. O projeto foi criado para organizar o fluxo de trabalho da ONG **Turma do Bem**, permitindo o cadastro de pacientes, dentistas voluntários e o registro detalhado de atendimentos odontológicos.



## 📋 Funcionalidades

O sistema é dividido em módulos para facilitar a navegação:

### 1. Módulo Administrativo (ONG)
* **Cadastro de Pacientes:** Registro completo com validação de CPF, idade e descrição do problema de saúde bucal.
* **Cadastro de Dentistas:** Registro de profissionais voluntários, incluindo o número do CRO e dados de contato.
* **Consulta de Registros:** Sistema de busca por nome ou listagem geral de todos os cadastrados.

### 2. Módulo de Dentistas (Atendimento)
* **Registrar Atendimento:** O dentista pode relatar o tratamento feito em um paciente específico.
* **Relatório de Atendimentos:** Visualização de todo o histórico de procedimentos realizados.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Ter o **Python 3.x** instalado.

### Passo a Passo
1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    ```
2.  **Navegue até a pasta:**
    ```bash
    cd nome-do-repositorio
    ```
3.  **Execute o programa:**
    ```bash
    python seu_arquivo.py
    ```

---

## 🛠️ Tecnologias e Conceitos Utilizados

O código demonstra o uso de conceitos fundamentais de programação:
* **Dicionários e Listas:** Para armazenamento e organização dos dados em memória.
* **Tratamento de Erros/Validação:** Funções para garantir que o usuário não digite letras onde deveriam ser números ou deixe campos vazios.
* **Submenus e Loops:** Estrutura de repetição `while` para manter o sistema rodando até que o usuário decida sair.

---

## 📖 Estrutura do Menu Principal

| Opção | Descrição |
| :--- | :--- |
| **1 - ONG Turma do Bem** | Gerenciamento de cadastros de pacientes e dentistas. |
| **2 - Dentistas** | Registro e visualização de atendimentos clínicos. |
| **3 - Sair** | Encerra o programa com segurança. |

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *Issue* ou enviar um *Pull Request* com melhorias, como a implementação de salvamento em arquivos (JSON ou Banco de Dados).

---
**Desenvolvido para fins educacionais e de gestão social.** 🌟
