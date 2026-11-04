# === Stage 2: Проверка полей ===
# Project: TeaCellar
def normalize_chai_name(name: str) -> str:
    return (name.strip().title() + " ").rstrip()


def normalize_chai_type(chai_type: str) -> str:
    return chai_type.strip().lower()


def normalize_chai_year(chai_year: str) -> int:
    year = chai_year.strip()
    if not year.isdigit():
        raise ValueError("Год сбора должен быть числом, например, 2023.")
    year_int = int(year)
    if year_int < 1000 or year_int > 9999:
        raise ValueError("Год сбора должен быть четырехзначным числом.")
    return year_int


def normalize_chai_amount(chai_amount: str) -> float:
    amount = chai_amount.strip()
    try:
        amount_float = float(amount)
    except ValueError:
        raise ValueError("Остаток граммов должен быть числом.")
    if amount_float < 0:
        raise ValueError("Остаток граммов не может быть отрицательным.")
    return amount_float


def validate_chai_name(name: str) -> str:
    if not name or not name.strip():
        raise ValueError("Название не может быть пустым.")
    normalized_name = normalize_chai_name(name)
    if len(normalized_name) > 100:
        raise ValueError("Название слишком длинное (максимум 100 символов).")
    return normalized_name


def validate_chai_type(chai_type: str) -> str:
    if not chai_type or not chai_type.strip():
        raise ValueError("Тип не может быть пустым.")
    normalized_type = normalize_chai_type(chai_type)
    if len(normalized_type) > 50:
        raise ValueError("Тип слишком длинный (максимум 50 символов).")
    return normalized_type


def validate_chai_year(chai_year: str) -> int:
    year = normalize_chai_year(chai_year)
    return year


def validate_chai_amount(chai_amount: str) -> float:
    amount = normalize_chai_amount(chai_amount)
    return amount


def validate_chai(name: str, chai_type: str, chai_year: str, chai_amount: str):
    normalized_name = validate_chai_name(name)
    normalized_type = validate_chai_type(chai_type)
    normalized_year = validate_chai_year(chai_year)
    normalized_amount = validate_chai_amount(chai_amount)
    return normalized_name, normalized_type, normalized_year, normalized_amount
