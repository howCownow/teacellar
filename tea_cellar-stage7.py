# === Stage 7: Генерация идентификаторов ===
# Project: TeaCellar
import string
import secrets


PROJECT_PREFIX = "tea"


def _generate_suffix(length: int = 8) -> str:
    """Генерирует случайную строку из букв и цифр заданной длины."""
    alphabet = string.ascii_lowercase + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def generate_unique_id(existing_ids: set[str],
                         prefix: str = PROJECT_PREFIX,
                         length: int = 8,
                         attempts: int = 100) -> str:
    """
    Генерирует уникальный идентификатор с префиксом проекта,
    не совпадающий ни с одним из id в existing_ids.
    """
    for _ in range(attempts):
        candidate = f"{prefix}-{_generate_suffix(length)}"
        if candidate not in existing_ids:
            return candidate
    raise ValueError("Не удалось сгенерировать уникальный идентификатор")


def assign_unique_ids(objects, existing_ids: set[str] | None = None,
                      prefix: str = PROJECT_PREFIX,
                      length: int = 8) -> dict:
    """
    Назначает уникальный идентификатор каждому объекту из коллекции.
    Возвращает словарь вида {id: объект}.
    """
    ids: set[str] = set(existing_ids) if existing_ids is not None else set()
    result: dict = {}
    for obj in objects:
        new_id = generate_unique_id(ids, prefix, length)
        ids.add(new_id)
        result[new_id] = obj
    return result
