# === Stage 10: Поиск по нескольким словам ===
# Project: TeaCellar
from typing import Iterable, TypeVar

T = TypeVar("T")


def _split_terms(query: str) -> Iterable[str]:
    cleaned = query.replace("-", "- ").strip()
    return (token for token in cleaned.split() if token)


def contains(term: str, haystack: str) -> bool:
    return term in haystack.lower()


def search(
    items: Iterable[T],
    query: str,
    *,
    contains=contains,
) -> list[T]:
    terms = list(_split_terms(query))
    if not terms:
        return list(items)

    positive, negative = [], []
    for term in terms:
        if term.startswith("-"):
            negative.append(term[1:].strip())
        else:
            positive.append(term)

    if negative:
        def excludes(item: T) -> bool:
            return all(not contains(term, str(item)) for term in negative)

        items = (item for item in items if excludes(item))

    if positive:
        def includes(item: T) -> bool:
            return any(contains(term, str(item)) for term in positive)

        items = (item for item in items if includes(item))

    return list(items)
