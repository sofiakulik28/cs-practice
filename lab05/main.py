
import logstats

path = input()

with open(path, encoding="utf-8") as file:
    counts = logstats.count_levels(file)

total = 0

for level in counts:
    total = total + counts[level]

with open(path, encoding="utf-8") as file:
    errors = logstats.top_errors(file, 5)

print(total)
print(counts["ERROR"])
print(counts["BROKEN"])

report = logstats.format_report(counts, errors)

with open("report.txt", "w", encoding="utf-8") as file:
    file.write(report)
