def parse_event(line):
    line = line.strip()
    if not line:
        raise ValueError("Пустая строка")
    parts = line.split(maxsplit=2)
    
    if len(parts) < 3:
        raise ValueError("Неверный формат строки")
    
    time_str = parts[0]
    level = parts[1].upper()
    message = parts[2]
    
    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}
    if level not in valid_levels:
        raise ValueError("Неизвестный уровень лога")
        
    return {
        "time": time_str,
        "level": level,
        "message": message
    }
def count_levels(lines):
    counts = {}
    for line in lines:
        if not line.strip():
            continue
            
        try:
            event = parse_event(line)
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
            
    return counts

def top_errors(lines, n):
    error_counts = {}

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)

            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1

        except ValueError:
            pass

    pairs = [[msg, count] for msg, count in error_counts.items()]

    pairs.sort(key=lambda x: (-x[1], x[0]))

    return pairs[:n]


def format_report(counts, errors):
    text = "Отчёт по журналу\n\n"
    
    for level in sorted(counts.keys()):
        text += f"{level}: {counts[level]}\n"
        
    text += "\nЧастые ошибки:\n"
    for msg, count in errors:
        text += f"- {msg} — {count}\n" 
        
    return text

