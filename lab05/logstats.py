
def parse_event(line):
    parts = line.strip().split(None, 2)

    if len(parts) != 3:
        raise ValueError

    time = parts[0]
    level = parts[1]
    message = parts[2]

    if level != "DEBUG" and level != "INFO" and level != "WARNING" and level != "ERROR":
        raise ValueError

    event = {
        "time": time,
        "level": level,
        "message": message
    }

    return event



def count_levels(lines):
    counts = {}

    for line in lines:
        if line.strip() == "":
            continue

        try:
            event = parse_event(line)
            level = event["level"]

            if level in counts:
                counts[level] = counts[level] + 1
            else:
                counts[level] = 1

        except ValueError:
            if "BROKEN" in counts:
                counts["BROKEN"] = counts["BROKEN"] + 1
            else:
                counts["BROKEN"] = 1

    return counts



def top_errors(lines, n):
    errors = {}

    for line in lines:
        if line.strip() == "":
            continue

        try:
            event = parse_event(line)

            if event["level"] == "ERROR":
                message = event["message"]

                if message in errors:
                    errors[message] = errors[message] + 1
                else:
                    errors[message] = 1

        except ValueError:
            pass

    result = []

    for message in errors:
        result.append([message, errors[message]])

    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i][1] < result[j][1]:
                result[i], result[j] = result[j], result[i]

            elif result[i][1] == result[j][1]:
                if result[i][0] > result[j][0]:
                    result[i], result[j] = result[j], result[i]

    return result[:n]


def format_report(counts, errors):
    report = "Отчёт по журналу\n\n"

    levels = sorted(counts)

    for level in levels:
        report = report + level + ": " + str(counts[level]) + "\n"

    report = report + "\nЧастые ошибки:\n"

    for error in errors:
        report = report + "- " + error[0] + " — " + str(error[1]) + "\n"

    return report
