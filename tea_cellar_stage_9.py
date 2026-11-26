# === Stage 9: Текстовый поиск ===
# Project: TeaCellar
def highlight_search(text, pattern, case_insensitive=True):
    if not pattern:
        return text
    if case_insensitive:
        pattern = pattern.lower()
        text = text.lower()
    flags = 0
    escaped = re.escape(pattern)
    if case_insensitive:
        regex = re.compile('(?i)' + escaped)
    else:
        regex = re.compile(escaped)
    result = []
    index = 0
    for match in regex.finditer(text):
        start, end = match.span()
        result.append(text[index:start])
        result.append('\033[1m' + text[start:end] + '\033[0m')
        index = end
    result.append(text[index:])
    return ''.join(result)


def search_tea(tea_list, query, case_insensitive=True):
    if not query:
        return list(tea_list)
    pattern = query.strip()
    if not pattern:
        return list(tea_list)
    matches = []
    for tea in tea_list:
        name = tea.get('name', '')
        tea_type = tea.get('tea_type', '')
        combined = name + ' ' + tea_type
        if pattern.lower() in combined.lower():
            matches.append(tea)
    return matches


def format_search_result(tea):
    name = tea.get('name', '')
    tea_type = tea.get('tea_type', '')
    harvest_year = tea.get('harvest_year', '')
    remaining = tea.get('remaining_grams', '')
    line = 'Название: ' + name + ' | Тип: ' + tea_type + ' | Год сбора: ' + harvest_year + ' | Остаток: ' + remaining + ' г'
    highlighted = highlight_search(line, tea.get('name', ''))
    return highlighted
