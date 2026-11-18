# === Stage 6: Связи между сущностями ===
# Project: TeaCellar
from typing import List, Dict, Any, Optional


class Tea:
    def __init__(self, name: str, tea_type: str, harvest_year: int, remaining_grams: float):
        self.name = name
        self.tea_type = tea_type
        self.harvest_year = harvest_year
        self.remaining_grams = remaining_grams

    def __repr__(self):
        return f"Tea(name={self.name!r}, tea_type={self.tea_type!r}, harvest_year={self.harvest_year}, remaining_grams={self.remaining_grams})"


class Brewing:
    def __init__(self, tea_id: int, tea: Tea, water_temperature_c: float, steeping_time_seconds: int):
        self.tea_id = tea_id
        self.tea = tea
        self.water_temperature_c = water_temperature_c
        self.steeping_time_seconds = steeping_time_seconds

    def __repr__(self):
        return f"Brewing(tea_id={self.tea_id}, tea={self.tea!r}, water_temperature_c={self.water_temperature_c}, steeping_time_seconds={self.steeping_time_seconds})"


class TeaCellar:
    def __init__(self):
        self.teas: Dict[int, Tea] = {}
        self.brewings: Dict[int, Brewing] = {}

    def add_tea(self, tea: Tea) -> int:
        tea_id = len(self.teas) + 1
        self.teas[tea_id] = tea
        return tea_id

    def add_brewing(self, brewing: Brewing) -> None:
        self.brewings[brewing.tea_id] = brewing

    def get_brewings_for_tea(self, tea_id: int) -> List[Brewing]:
        return [brewing for brewing in self.brewings.values() if brewing.tea_id == tea_id]

    def check_integrity(self, tea_id: int) -> bool:
        if tea_id not in self.teas:
            return False
        brewings = self.get_brewings_for_tea(tea_id)
        for brewing in brewings:
            if brewing.water_temperature_c < 0 or brewing.water_temperature_c > 100:
                return False
            if brewing.steeping_time_seconds <= 0:
                return False
        return True


if __name__ == "__main__":
    cellar = TeaCellar()
    green = Tea("Longjing", "green", 2023, 150.0)
    black = Tea("Assam", "black", 2022, 100.0)
    cellar.add_tea(green)
    cellar.add_tea(black)
    print("Заваривания для чая 'Longjing':")
    print(cellar.get_brewings_for_tea(green.tea_id))
    print("Целостность для чая 'Longjing':")
    print(cellar.check_integrity(green.tea_id))
