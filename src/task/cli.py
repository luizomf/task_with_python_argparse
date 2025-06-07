import os


def clear() -> None:
    os.system("cls" if os.name == "nt" else "clear")  # noqa: S605
    return


def run() -> None:
    clear()
    print("It works!")


if __name__ == "__main__":
    clear()
    run()
