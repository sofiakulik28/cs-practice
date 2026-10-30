def parse_record(line: str) -> dict:
    parts = line.split(';')
    if len(parts) != 3:
        raise ValueError("...")
    
    city, temp_str, date = parts
    city = city.strip()
    temp_str = temp_str.strip()
    date = date.strip()

    if not city or not date:
        raise ValueError("...")

    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError("not float")

    return {'city': city, 'temperature': temp, 'date': date}

def read_valid(lines: list[str]) -> list[dict]:
    valid_records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            continue 
    return valid_records

def average_by_city(records: list[dict]) -> dict:
    totals = {}
    counts = {}
    for r in records:
        city = r['city']
        temp = r['temperature']
        totals[city] = totals.get(city, 0) + temp
        counts[city] = counts.get(city, 0) + 1
        
    return {city: round(totals[city] / counts[city], 1) for city in totals}

def warmest_city(records: list[dict]) -> str:
    if not records:
        return ""
    averages = average_by_city(records)
    return max(averages.keys(), key=lambda c: (averages[c], [-ord(char) for char in c]))