import csv

fp = Path.cwd()/"overheads-day-90.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    overheadRecords=[]

    for row in reader:
        overheadRecords.append([row[0], row[1]])

# print(overheadRecords)

for item in overheadRecords:
    value = item[1]
    item[1] = value.replace("$","")
# print(overheadRecords)

Expenses_list = []
for item in overheadRecords:
    if item[1] not in Expenses_list:
        Expenses_list.append(float(item[1]))

# print(Expenses_list)

def find_highest_value(list):
    list.sort(reverse=True)
    return(list[0])

highestValue = find_highest_value(Expenses_list)

print(f"Overheadrecords: {overheadRecords}")
print(f"Expense list: {Expenses_list}")
print(f"highest value: {highestValue}")

# loop thru the overheadRecords
#     loop thru the list of list
#         if it contains the highestValue, print that list
#         else: move on

for i in overheadRecords:
    if float(i[1]) == highestValue:
        print(i)
