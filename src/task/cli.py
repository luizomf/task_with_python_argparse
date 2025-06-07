from task.settings import clear


def build_parser() -> None:
    print("It works!")


def run() -> None:
    clear()  # limpa o terminal
    build_parser()


if __name__ == "__main__":
    # entry point ao usar o módulo diretamente
    run()
