# === Stage 1: Каркас модуля ===
# Project: TeaCellar
from dataclasses import dataclass, field
from typing import List


@dataclass
class Tea:
    name: str
    kind: str
    harvest_year: int
    remaining_grams: float = 0.0


def make_demo_tea() -> List[Tea]:
    return [
        Tea("Гуань Инь", "Улун", 2023, 120.0),
        Tea("Дарджилинг", "Чёрный", 2022, 80.0),
        Tea("Матча", "Зелёный", 2024, 250.0),
        Tea("Пуэр", "Тёмный", 2021, 300.0),
    ]


def print_tea(tea: Tea) -> None:
    print(f"  {tea.name} ({tea.kind}, {tea.harvest_year}, {tea.remaining_grams} г)")


def main() -> None:
    print("TeaCellar: коллекция чая")
    print(f"Всего сортов: {len(make_demo_tea())}")
    for tea in make_demo_tea():
        print_tea(tea)


if __name__ == "__main__":
    main()
