# === Stage 4: Редактирование записей ===
# Project: TeaCellar
def edit_tea(tea_collection, tea_id, changes):
    """Редактирование сущности «чай» по идентификатору.

    changes — словарь {поле: новое_значение}. Разрешённые поля:
    name, type, harvest_year, remaining_grams.
    """
    allowed_fields = {"name", "type", "harvest_year", "remaining_grams"}
    invalid_fields = set(changes) - allowed_fields
    if invalid_fields:
        raise ValueError("Запрещённые поля для редактирования: " + ", ".join(sorted(invalid_fields)))
    if not changes:
        raise ValueError("Необходимо передать хотя бы одно допустимое поле для изменения")

    for tea in tea_collection:
        if tea.get("id") == tea_id:
            for field in allowed_fields:
                if field in changes:
                    if field == "harvest_year":
                        new_value = changes[field]
                        if not isinstance(new_value, int) or new_value < 1000 or new_value > 9999:
                            raise ValueError("Год сбора должен быть целым числом в диапазоне 1000–9999")
                        tea[field] = new_value
                    elif field == "remaining_grams":
                        new_value = changes[field]
                        if not isinstance(new_value, (int, float)) or new_value < 0:
                            raise ValueError("Остаток граммов должен быть неотрицательным числом")
                        tea[field] = new_value
                    else:
                        tea[field] = changes[field]
            return True
    return False


def validate_change_value(field, value):
    """Проверка допустимости значения для конкретного поля редактирования."""
    if field == "harvest_year":
        if not isinstance(value, int) or isinstance(value, bool):
            return False
        if value < 1000 or value > 9999:
            return False
        return True
    if field == "remaining_grams":
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            return False
        if value < 0:
            return False
        return True
    if field in ("name", "type"):
        return isinstance(value, str) and len(value.strip()) > 0
    return False
