import csv
import json
from io import StringIO



def csv_to_records(text: str) -> list[dict]:
    file = StringIO(text)
    reader = csv.DictReader(file, skipinitialspace=True)

    records = []

    for row in reader:
        new_row = {}

        for key, value in row.items():
            key = key.strip()

            if value is not None:
                value = value.strip()

            new_row[key] = value

        records.append(new_row)

    return records



def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_key = None

    for line in lines:
        line = line.split("#")[0].strip()

        if line == "":
            continue

        if line.startswith("-"):
            if current_key is not None:
                value = line[1:].strip()

                if isinstance(result[current_key], list):
                    result[current_key].append(convert_value(value))

            continue

        if ":" in line:
            key, value = line.split(":", 1)

            key = key.strip()
            value = value.strip()

            current_key = key

            if value == "":
                result[key] = []
            else:
                result[key] = convert_value(value)

    return result



def convert_value(value):
    value = value.strip()

    if value == "true" or value == "yes":
        return True

    if value == "false" or value == "no":
        return False

    try:
        return int(value)
    except ValueError:
        pass

    try:
        return float(value.replace(",", "."))
    except ValueError:
        return value



def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    result = []

    for row in rows:
        new_row = {}

        if key in row and row[key] in extra:
            new_row.update(extra[row[key]])

        new_row.update(row)

        result.append(new_row)

    return result


def records_to_json(records: list[dict]) -> str:
    result = json.dumps(
        records,
        ensure_ascii=False,
        indent=2,
        sort_keys=True
    )

    return result
