import os

def count_by_extension(paths):
    result = {}


    for path in paths:
        filename = path.replace("\\", "/").split("/")[-1]

        extension = os.path.splitext(filename)[1]
        extension = extension.lower().replace(".", "")

        if extension in result:
            result[extension] += 1
        else:
            result[extension] = 1

    return result


def deepest_path(paths):
    if len(paths) == 0:
        return ""

    deepest = ""
    max_depth = -1

    for path in paths:
        parts = path.replace("\\", "/").split("/")

        depth = 0

        for part in parts:
            if part != "":
                depth += 1

        if depth > max_depth:
            max_depth = depth
            deepest = path

        elif depth == max_depth:
            if path < deepest:
                deepest = path

    return deepest


def human_size(n_bytes):
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]

    size = float(n_bytes)
    unit_index = 0

    while size >= 1024 and unit_index < 4:
        size = size / 1024
        unit_index += 1

    if unit_index == 0:
        return str(int(size)) + " Б"

    return str(round(size, 1)) + " " + units[unit_index]