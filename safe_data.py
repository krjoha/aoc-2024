from typing import List, Tuple
import csv

def is_report_safe(report: List[int]) -> bool:
    is_safe = False
    is_increasing = None

    for i, level in enumerate(report):
        if i >= len(report)-1:
            is_safe = True
            break

        diff = level - report[i+1]
        if diff == 0 or abs(diff) > 3:
            break
        if i == 0:
            is_increasing = diff > 0

        if is_increasing and diff < 0:
            break
        if not is_increasing and diff > 0:
            break

    return is_safe 

if __name__ == "__main__":
    num_safe_reports = 0

    with open("data/day2.csv") as f:
        file = csv.reader(f, delimiter=" ")
        for line in file:
            report = [int(level) for level in line]
            safe = is_report_safe(report)
            if safe:
                num_safe_reports += 1
            else:
                for i in range(0, len(report)):
                    safe = is_report_safe([level for j, level in enumerate(report) if j != i])
                    if safe:
                        num_safe_reports +=1
                        break
    
    print(num_safe_reports)
    
