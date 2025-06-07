import argparse
from dataclasses import dataclass
from typing import Literal


def run() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "positional",  # Argumento posicional
        action="store",  # padrão
        metavar="Whatever",  # nome descritivo do valor do argumento
        help="Esse argumento é posicional",  # Ajuda
    )

    args = parser.parse_args()
    print(args)


@dataclass
class Todo:
    id: str
    task: str
    tags: list[str]
    created_at: str
    complete: bool = False
    priority: Literal["low", "medium", "high"] = "medium"


if __name__ == "__main__":
    run()
