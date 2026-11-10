# === Stage 3: Хранилище в памяти ===
# Project: TeaCellar
import threading


class TeaStore:
    """Память для сущностей чая с добавлением, получением и списком."""

    def __init__(self):
        self._tea = {}
        self._lock = threading.Lock()

    def add(self, tea):
        """Добавить чай по его идентификатору.

        Возвращает True, если чай был добавлен, и False,
        если чай с таким идентификатором уже существует.
        """
        with self._lock:
            return self._tea.setdefault(tea.id, tea) is None

    def get(self, tea_id):
        """Вернуть чай по идентификатору или None, если его нет."""
        with self._lock:
            return self._tea.get(tea_id)

    def all(self):
        """Вернуть список всех чаев в порядке добавления."""
        with self._lock:
            return list(self._tea.values())

    def __len__(self):
        with self._lock:
            return len(self._tea)


class Tea:
    """Сущность чая: название, тип, год сбора, остаток граммов."""

    def __init__(self, id, name, tea_type, harvest_year, remaining_grams=0):
        self.id = id
        self.name = name
        self.tea_type = tea_type
        self.harvest_year = harvest_year
        self.remaining_grams = remaining_grams

    def brew(self, water_milliliters, temperature_celsius, minutes):
        """Записать рецепт заваривания для этого чая."""
        return BrewRecipe(self, water_milliliters, temperature_celsius, minutes)

    def __repr__(self):
        return (f"Tea(id={self.id!r}, name={self.name!r}, "
                f"tea_type={self.tea_type!r}, harvest_year={self.harvest_year!r}, "
                f"remaining_grams={self.remaining_grams!r})")


class BrewRecipe:
    """Рецепт заваривания: объём воды, температура, время."""

    def __init__(self, tea, water_milliliters, temperature_celsius, minutes):
        self.tea = tea
        self.water_milliliters = water_milliliters
        self.temperature_celsius = temperature_celsius
        self.minutes = minutes

    def description(self):
        return (f"{self.tea.name}: {self.water_milliliters} мл при "
                f"{self.temperature_celsius}°C, {self.minutes} минут")

    def __repr__(self):
        return (f"BrewRecipe(tea={self.tea.id!r}, "
                f"water_milliliters={self.water_milliliters!r}, "
                f"temperature_celsius={self.temperature_celsius!r}, "
                f"minutes={self.minutes!r})")


if __name__ == "__main__":
    store = TeaStore()
    tea1 = Tea(1, "Гуньцзинь", "Улун", 2023, 100)
