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
    
    for line in lines:
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




# def parse_event(line):
#     parts = line.strip().split(None, 2)

#     if len(parts) != 3:
#         raise ValueError

#     time = parts[0]
#     level = parts[1]
#     message = parts[2]

#     if level != "DEBUG" and level != "INFO" and level != "WARNING" and level != "ERROR":
#         raise ValueError

#     event = {
#         "time": time,
#         "level": level,
#         "message": message
#     }

#     return event



# def count_levels(lines):
#     counts = {}

#     for line in lines:
#         if line.strip() == "":
#             continue

#         try:
#             event = parse_event(line)
#             level = event["level"]

#             if level in counts:
#                 counts[level] = counts[level] + 1
#             else:
#                 counts[level] = 1

#         except ValueError:
#             if "BROKEN" in counts:
#                 counts["BROKEN"] = counts["BROKEN"] + 1
#             else:
#                 counts["BROKEN"] = 1

#     return counts



# def top_errors(lines, n):
#     errors = {}

#     for line in lines:
#         if line.strip() == "":
#             continue

#         try:
#             event = parse_event(line)

#             if event["level"] == "ERROR":
#                 message = event["message"]

#                 if message in errors:
#                     errors[message] = errors[message] + 1
#                 else:
#                     errors[message] = 1

#         except ValueError:
#             pass

#     result = []

#     for message in errors:
#         result.append([message, errors[message]])

#     for i in range(len(result)):
#         for j in range(i + 1, len(result)):
#             if result[i][1] < result[j][1]:
#                 result[i], result[j] = result[j], result[i]

#             elif result[i][1] == result[j][1]:
#                 if result[i][0] > result[j][0]:
#                     result[i], result[j] = result[j], result[i]

#     return result[:n]


# def format_report(counts, errors):
#     report = "Отчёт по журналу\n\n"

#     levels = sorted(counts)

#     for level in levels:
#         report = report + level + ": " + str(counts[level]) + "\n"

#     report = report + "\nЧастые ошибки:\n"

#     for error in errors:
#         report = report + "- " + error[0] + " — " + str(error[1]) + "\n"

#     return report
