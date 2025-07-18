# 🧠 Desafio: Crie seu próprio CLI com argparse

![Python](https://img.shields.io/badge/Python-3.13%2B-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Este projeto é um **desafio educacional** para aprender a criar ferramentas de linha de comando (CLI) com Python e a biblioteca `argparse`.

## 🚀 Objetivo

Você vai implementar um CLI completo, com múltiplos subcomandos, argumentos requeridos e opcionais, validações, alias e muito mais. Tudo isso dentro de um projeto real de gerenciamento de tarefas.

---

## 📦 Como começar

Se não souber usar o git, faça o download direto, do contrário, faça o `git clone` (mostro logo abaixo).

### 0. Download direto para iniciantes (sem Git)

Se você tem alguma dificuldade em usar o Git, faça o download direto abaixo - se sabe usar o git pule para **1. Clone o repositório (com Git)**.

👉 [Clique aqui para baixar o `.zip`](https://github.com/luizomf/task_with_python_argparse/archive/refs/heads/start-argparse.zip)

Depois de extrair, siga normalmente os passos de ambiente e instalação descritos abaixo em **2. Crie e ative o ambiente virtual**.

### 1. Clone o repositório (com Git)

> Use o branch **start-argparse** para garantir que está no ponto certo do desafio (sem spoilers):

```bash
git clone https://github.com/luizomf/task_with_python_argparse.git
cd task_with_python_argparse
git checkout start-argparse
```

---

### 2. Crie e ative o ambiente virtual

**Com pip/venv:**

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.\.venv\Scripts\activate   # Windows
pip install -e .
```

**Com uv (recomendado):**

```bash
uv sync
```

---

### 3. Rode o projeto (modo básico)

Por enquanto, a única coisa que vai acontecer é limpar o terminal e imprimir:

```bash
task
# ou, se não ativou o ambiente:
uv run task
```

Saída esperada:

```
It works!
```

---

## 🛠️ O que você deve fazer

Implemente o CLI dentro de `src/task/cli.py`. Comece com o `build_parser()` e vá adicionando os subcomandos descritos durante o vídeo (ou definidos por você, se estiver estudando por conta própria).

---

## 📚 Dicas

Este projeto segue boas práticas modernas com:

- `pyproject.toml` completo com dependências, testes, lint, tipagem
- Código organizado em `src/`
- Suporte a instalação editável
- Comandos já registrados (`task = task.cli:run`)
- Pronto para uso com `uv`, `ruff`, `pyright`, `pytest`, etc.

---

## Regras do jogo

**Opcional**: todos os "helps" de todos os sub comandos podem ter cores (syntax highlight).

### 📌 Help principal (`task -h`)

Essas são as configurações que você deve usar no help principal do seu CLI. Ao digitar `task -h`, essas informações estarão visíveis para o usuário.

```
nome do comando = task

descrição =
    Task Manager helps you organize your tasks directly from the terminal.

    You can create, search, list, and delete tasks with ease - all from
    your CLI. No need for web apps, mouse clicks or distractions.
    Just productivity.

Epílogo =
    This will be shown below all arguments and can be used to add
    copyright or other complex examples.
```

### 📌 Subcomando `create`

Essas são as opções que o subcomando `create` deve conter. Ao digitar `task create -h`, o output precisa refletir essas informações:

```
nome do subcomando = create
aliases = new, add

descrição =
    Use this command to create a new task quickly and efficiently.

    Provide a title, optional tags, priority, and mark it as done if needed.
    Whether you're planning your day or dumping ideas into the terminal,
    this is your entry point.

epílogo =
    Examples:

      task create -t "Buy groceries"
      task create -t "Study argparse" --tag python --tag cli --priority high
      task create -t "Walk the dog" --done

    You can also combine options freely to match your workflow.
    Tags help with filtering later. Priorities can be: low, medium, high.

argumentos =
    -t, --task
        nome do valor = TASK
        requerido = Sim
        tipo = string
        help = Describes your task

    -d, --done, --no-done
        ação = BooleanOptionalAction (permite usar --option e --no-option)
        Padrão se não enviado = False
        help = Marks a task as complete

    --tag
        Ação = Salvar em uma lista cada argumento enviado
        Quantos valores são aceitos = Nenhum ou muitos (sem limite)
        Padrão = Uma lista vazia
        tipo = string
        Em qual chave do argparse salvar = tags
        help = Adds tags to your tasks for organization

    -p, --priority
        opções limitadas = low, medium, high
        padrão = medium
        help = Sets the priority for your task
```

---

### 📌 Subcomando `all` (`task all -h`)

Esse comando exibe todas as tarefas cadastradas no sistema.

```
nome do subcomando = all

descrição =
    Shows all tasks

epílogo = (não há)

argumentos = (nenhum)
```

---

### 📌 Subcomando `search` (`task search -h`)

Esse comando permite buscar tarefas com base em critérios específicos.

```
nome do subcomando = search

descrição =
    Search for tasks

epílogo = (não há)

argumentos =
    (TODOS OS ARGUMENTOS SÃO OPCIONAIS)

    -t, --task
        nome do valor = TASK
        padrão = None
        requerido = Não
        tipo = string
        help = Describes your task

    -d, --done, --no-done
        ação = BooleanOptionalAction (permite usar --option e --no-option)
        padrão = None
        requerido = Não
        help = Marks a task as complete

    --tag
        Ação = Salvar em uma lista cada argumento enviado
        Quantos valores são aceitos = Nenhum ou muitos (sem limite)
        padrão = None
        requerido = Não
        Em qual chave do argparse salvar = tags
        help = Adds tags to your tasks for organization

    -p, --priority
        opções limitadas = low, medium, high
        padrão = None
        requerido = Não
        help = Sets the priority for your task

    -l, --limit LIMIT
        help = Limits the number of tasks per search
        padrão = 10
        requerido = Não

```

---

### 📌 Subcomando `delete` (`task delete -h`)

Esse comando deleta uma tarefa específica com base no ID.

```
nome do subcomando = delete

descrição =
    Deletes one task by id

epílogo = (não há)

argumentos:

    -i, --task-id
        requerido = Sim
        help = Task ID
        tipo = Inteiro

    -f, --force, --no-force
        ação = BooleanOptionalAction (permite usar --option e --no-option)
        padrão = False
        requerido = Não
        help = Removes the confirmation when deleting tasks
```

---

### 📌 Subcomando `one` (`task one -h`)

Esse comando busca uma única tarefa com base no ID.

```
nome do subcomando = one

descrição =
    Finds one task by id

epílogo = (não há)

argumentos:

    -i, --task-id
        requerido = Sim
        help = Task ID
        tipo = Inteiro
```

---

## Testing commands (manual)

```bash
task create --task "Estudar Python moderno" --priority high --tag "estudo" --tag "python"
task create --task "Fazer compras no mercado" --no-done --priority low --tag "pessoal"
task create --task "Enviar relatório semanal" --done --priority medium --tag "trabalho" --tag "relatório"
task create --task "Limpar a casa" --priority medium --tag "pessoal"
task create --task "Atualizar repositório GitHub" --done --priority high --tag "dev" --tag "git"
task create --task "Assistir vídeo de tipagem em Python" --no-done --priority low --tag "estudo"
task create --task "Preparar apresentação" --priority high --tag "trabalho" --tag "slides"
task create --task "Organizar e-mails" --done --priority low --tag "trabalho"
task create --task "Estudar NamedTuple avançado" --no-done --priority medium --tag "estudo" --tag "tipagem"
task create --task "Configurar ambiente no VS Code" --priority medium --tag "dev" --tag "setup"
task create --task "Testar filtros do TinyDB" --priority high --tag "dev" --tag "teste"
task create --task "Refatorar código do CLI" --priority medium --tag "dev" --tag "argparse"
task create --task "Criar capa para vídeo" --done --priority low --tag "youtube" --tag "thumb"
task create --task "Estudar metaprogramação em Python" --priority high --tag "estudo" --tag "avançado"
task create --task "Pagar contas do mês" --no-done --priority medium --tag "pessoal" --tag "financeiro"
task create --task "Publicar vídeo no YouTube" --done --priority high --tag "youtube" --tag "trabalho"
task create --task "Criar função map_dict_to_task" --priority medium --tag "dev" --tag "tipagem"
task create --task "Limpar arquivos temporários" --priority low --tag "sistema"
task create --task "Testar tipagem com cast e TypedDict" --priority high --tag "estudo" --tag "tipagem"
task create --task "Responder comentários no canal" --no-done --priority low --tag "youtube" --tag "comunidade"
```

---

## 📜 Licença

Distribuído sob a licença MIT. Veja `LICENSE.txt` para mais informações.

---

## 👨‍🏫 Autor

Luiz Otávio Miranda
[YouTube](https://www.youtube.com/@OtavioMiranda) • [GitHub](https://github.com/luizomf)

---
