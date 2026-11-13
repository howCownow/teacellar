# === Stage 5: Удаление и восстановление ===
# Project: TeaCellar
from datetime import datetime


class Tea:
    def __init__(self, name, tea_type, harvest_year, grams):
        self.name = name
        self.tea_type = tea_type
        self.harvest_year = harvest_year
        self.grams = grams


class TeaCellar:
    def __init__(self):
        self._teas = []
        self._trash = []
        self._counter = 0

    def add_tea(self, name, tea_type, harvest_year, grams):
        tea = Tea(name, tea_type, harvest_year, grams)
        self._teas.append(tea)
        return tea

    def find_tea(self, name):
        for tea in self._teas:
            if tea.name == name:
                return tea
        return None

    def remove_tea(self, name):
        tea = self.find_tea(name)
        if not tea:
            return False
        index = self._teas.index(tea)
        self._teas.pop(index)
        self._trash.append((tea, datetime.now()))
        self._counter += 1
        return True

    def restore_tea(self, name):
        tea = self.find_trash_tea(name)
        if not tea:
            return False
        self._teas.append(tea)
        self._trash = [item for item in self._trash if item[0].name != name]
        return True

    def find_trash_tea(self, name):
        for tea, _ in self._trash:
            if tea.name == name:
                return tea
        return None

    def list_trash(self):
        return [tea for tea, _ in self._trash]
