def check_lines(lines):
    total_valid_records = []
    
    for line in lines:
        if not line.strip():
            continue
            
        lines_ = line.split(';')
        
        if len(lines_) != 3:
            continue 
            
        else:
            c, t, d = lines_
            c = c.strip()
            t = t.strip()
            d = d.strip()
            
            if not c or not d:
                continue

            try:
                temp_float = float(t)
            except ValueError:
                continue
                
            total_valid_records.append({'city': c, 'temp': temp_float, 'date': d})
            
    return total_valid_records

def get_averages(records):
    total = {}
    count = {}
    for r in records:
        c = r['city']
        t = r['temp']
        total[c] = total.get(c, 0) + t
        count[c] = count.get(c, 0) + 1
        
    averages = {}
    for c in total:
        averages[c] = round(total[c] / count[c], 1)
    return averages

def get_warmest_city(records):
    if not records:
        return ""
    averages = get_averages(records)
    best = max(averages.keys(), key=lambda x: (averages[x], [-ord(ch) for ch in x]))
    return best