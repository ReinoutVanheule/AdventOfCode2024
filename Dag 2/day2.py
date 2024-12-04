from aoc import read_input

# input
lines = read_input("inputdag2")

# part 1
reports = [list(map(int,report.split())) for report in lines]

def valid_report(report):
    diff = [report[i+1]-report[i] for i in range(len(report)-1)]
    return all(i in (1,2,3) for i in diff) or all(i in (-1,-2,-3) for i in diff)
    
print(sum(valid_report(report) for report in reports))

# part 2
def valid_report_2(report):    
    if valid_report(report):
        return True
    for i in range(len(report)):
        new_report = report.copy()
        del new_report[i]
        if valid_report(new_report):
            return True
    return False

print(sum(valid_report_2(report) for report in reports))
        
            
                