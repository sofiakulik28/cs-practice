import logstats

path = input().strip()

with open(path, encoding="utf-8") as log:
    counts = logstats.count_levels(log)

total = 0

for level in counts:
    total = total + counts[level]

with open(path, encoding="utf-8") as log:
    errors = logstats.top_errors(log, 5)

print(total)
print(counts["ERROR"])
print(counts["BROKEN"])

report = logstats.format_report(counts, errors)

with open("report.txt", "w", encoding="utf-8") as file:
    file.write(report)
