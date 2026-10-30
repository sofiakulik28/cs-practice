import sys
from stats import check_lines, get_averages, get_warmest_city

lines = sys.stdin.read().splitlines()

try:
    valid_records = check_lines(lines)
except ValueError:
    print('Bad Data') 
else:
    total_valid = len(valid_records)
    total_lines = len(lines)
    empty_lines = sum(1 for line in lines if not line.strip())
    
    errors_count = total_lines - total_valid - empty_lines
    
    if total_valid > 0:
        best_city = get_warmest_city(valid_records)
        avg_temps = get_averages(valid_records)
        
        print(total_valid)
        print(errors_count)
        print(f"{avg_temps[best_city]:.1f}") 
    else:
        print(total_valid)
        print(errors_count)