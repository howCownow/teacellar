# === Stage 8: Сортировка записей ===
# Project: TeaCellar
def sort_by_name(records, reverse=False):
    """Сортировка записей «чай» по названию (возрастание/убывание)."""
    return sorted(records, key=lambda rec: rec["name"], reverse=reverse)


def sort_by_creation_date(records, reverse=False):
    """Сортировка записей «чай» по дате создания (возрастание/убывание)."""
    return sorted(records, key=lambda rec: rec["created_at"], reverse=reverse)


def sort_by_name_then_created(records, reverse=False):
    """Сортировка «чай» по названию, а затем по дате создания."""
    return sorted(
        records,
        key=lambda rec: (rec["name"], rec["created_at"]),
        reverse=reverse,
    )


def sort_by_created_then_name(records, reverse=False):
    """Сортировка «чай» по дате создания, а затем по названию."""
    return sorted(
        records,
        key=lambda rec: (rec["created_at"], rec["name"]),
        reverse=reverse,
    )


def sort_by_name_case_insensitive(records, reverse=False):
    """Сортировка «чай» по названию без учёта регистра."""
    return sorted(
        records,
        key=lambda rec: rec["name"].lower(),
        reverse=reverse,
    )


def sort_by_name_length(records, reverse=False):
    """Сортировка «чай» по длине названия (возрастание/убывание)."""
    return sorted(
        records,
        key=lambda rec: len(rec["name"]),
        reverse=reverse,
    )


def sort_by_name_length_then_name(records, reverse=False):
    """Сортировка «чай» по длине названия, а затем по названию."""
    return sorted(
        records,
        key=lambda rec: (len(rec["name"]), rec["name"]),
        reverse=reverse,
    )
