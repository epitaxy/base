def update_dict(input: dict, key: str, value, mode="append") -> dict:
    try:
        if mode in ["overwrite", "ovr", "w"]:
            raise Exception 
        input[key].append(value)
    except: # (KeyError, AttributeError, OverWrite):
        input.update({key: []})
        input[key].append(value)
    return input
