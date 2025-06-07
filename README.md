# Task Manager CLI

![Python](https://img.shields.io/badge/Python-3.13%2B-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Um gerenciador de tarefas de linha de comando (CLI) simples e poderoso, construído com Python.

## Sobre o Projeto

Este projeto foi desenvolvido como um case de estudo para um **vídeo educacional no YouTube** com o objetivo de ensinar, na prática, como utilizar a biblioteca `argparse` do Python para construir interfaces de linha de comando robustas e profissionais.

A ideia é demonstrar como estruturar comandos, sub-comandos, argumentos e validações em uma aplicação real, indo além do tradicional "hello world".

**Assista ao vídeo no canal:** [VÍDEO AINDA NÃO GRAVADO]

---

## Funcionalidades

- **Crie** tarefas com título, tags e prioridade.
- **Liste** todas as tarefas pendentes.
- **Pesquise** por tarefas com base em múltiplos critérios.
- **Delete** tarefas de forma segura.
- Interface elegante e colorida, graças à biblioteca `rich`.

---

## Instalação e Setup

Para rodar este projeto localmente, escolha **um** dos caminhos abaixo.

---

### Caminho 1: Com `uv` (Recomendado)

Se você já usa `uv`, o processo é extremamente simples.

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/luizomf/task_with_python_argparse.git task_with_argparse
    cd task_with_argparse
    ```

2.  **Sincronize o ambiente:**
    Este único comando irá criar o ambiente virtual, se necessário, e instalar todas as dependências e o projeto em modo editável.

    ```bash
    uv sync
    ```

3.  **Ative o ambiente (Opcional, mas recomendado):**
    Para usar o comando `task` diretamente.
    ```bash
    source .venv/bin/activate
    ```
    _Se não ativar, você ainda pode rodar os comandos via `uv run task ...`._

---

### Caminho 2: Com `pip` e `venv` (Tradicional)

Se você prefere o método tradicional.

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/luizomf/task_with_python_argparse.git task_with_argparse
    cd task_with_argparse
    ```

2.  **Crie e ative o ambiente virtual:**

    ```bash
    python -m venv .venv
    # No Linux/macOS
    source .venv/bin/activate
    # No Windows
    .\.venv\Scripts\activate
    ```

3.  **Instale o projeto e suas dependências:**
    ```bash
    pip install -e .
    ```

---

_Se tiver dúvidas sobre ambientes Python, confira esta série de vídeos:_

- _Parte 1: [Ambiente Python Moderno - Tradicional](https://youtu.be/QTw5eB6GTM8)_
- _Parte 2: [Ambiente Python Moderno - Pyenv e Pyenv-win](https://youtu.be/X38M7C_A2XU)_
- _Parte 3: [Ambiente Python Moderno - UV Astral](https://youtu.be/HuAc85cLRx0)_

## Como Usar

Após a instalação, você pode usar o comando `task` diretamente no seu terminal (com o ambiente virtual ativo).

### Comando Principal

Para ver a lista de todos os comandos disponíveis, use `-h` ou `--help`.

```bash
task -h
```

```
Usage: task [-h] {create,new,add,all,search,delete,one} ...

Task Manager helps you organize your tasks directly from the terminal.

You can create, search, list, and delete tasks with ease - all from
your CLI. No need for web apps, mouse clicks or distractions.
Just productivity.

Positional Arguments:
  {create,new,add,all,search,delete,one}
    create (new, add)   Create a new task with optional metadata
    all                 Shows all tasks
    search              Searches for tasks
    delete              Deletes one task by id
    one                 Finds one task by id

Options:
  -h, --help            show this help message and exit
```

_(As seções de ajuda para cada sub-comando foram omitidas por brevidade, mas podem ser consultadas com `task <comando> -h`)_

---

## Commands Cheat Sheet

#### Criando Tarefas

```bash
# Com opções longas
task create --task "Estudar Python moderno" --priority high --tag "estudo" --tag "python"

# Com opções curtas e múltiplos valores para uma tag
task create -t "Fazer café" -p low --tag "lazer" "alimentação" "cafeína"
```

#### Buscando Tarefas

```bash
# Busca combinando múltiplos critérios (lógica E/AND)
task search -p low --tag "lazer"

# Busca por texto no título (case-insensitive, usa regex)
task search -t "python"

# Busca usando uma expressão regular mais complexa
task search -t '(p.{4}n)' # Encontra 'python'

# Para listar todas as tarefas com limite padrão, use "search" sem argumentos
task search

# Para aumentar o limite de resultados
task search -l 100
```

#### Outros Comandos

```bash
# Listar todas as tarefas (semelhante a 'search' sem filtros)
task all

# Encontrar uma tarefa pelo seu ID
task one -i 1

# Deletar por ID (será pedida uma confirmação)
task delete -i 1

# Deletar por ID (sem confirmação)
task delete -i 2 -f
```

---

## Desenvolvimento

Este projeto utiliza `ruff` para linting e formatação, e `pyright` para checagem de tipos. As dependências de desenvolvimento são instaladas junto com o projeto ao seguir os passos de instalação.

- **Checar e corrigir o código com Ruff:**

  ```bash
  ruff check . --fix
  # ou com uv
  uvx ruff check . --fix
  ```

- **Formatar o código com Ruff:**

  ```bash
  ruff format .
  # ou com uv
  uvx ruff format .
  ```

- **Rodar a checagem de tipos com Pyright:**
  ```bash
  pyright .
  # ou com uv
  uvx pyright .
  ```

---

## Licença

Distribuído sob a licença MIT. Veja `LICENSE.txt` para mais informações.

---

## Contato

Luiz Otávio Miranda - [YouTube](https://www.youtube.com/c/Ot%C3%A1vioMiranda) - [GitHub](https://github.com/luizomf)
