import sys
from stats import average_by_city, read_valid, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    valid_records = read_valid(lines)
    
    total_valid = len(valid_records)
    total_lines = len(lines)
    empty_lines = sum(1 for line in lines if not line.strip())
    errors_count = total_lines - total_valid - empty_lines
    
    if total_valid > 0:
        best_city = warmest_city(valid_records)
        avg_temps = average_by_city(valid_records)
        print(total_valid)
        print(errors_count)
        print(f"{avg_temps[best_city]:.1f}")
    else:
        print(total_valid)
        print(errors_count)

if __name__ == "__main__":
    main()