def update_dict(input: dict, key: str, value) -> dict:
    try:
        input[key].append(value)
    except (KeyError, AttributeError):
        input.update({key: []})
        input[key].append(value)
    return input
