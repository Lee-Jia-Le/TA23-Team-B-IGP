from pathlib import Path
import csv

fp = Path.cwd()/"overheads-day-90.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    overheadRecords=[]

    for row in reader:
        overheadRecords.append([row[0], row[1]])

# print(overheadRecords)
# replace $ symbol 
for item in result:
    value = item[1]
    item[1] = value.replace("$","")
# print(overheadRecords)
# create a list to store the expenses 
Expenses_list = []
for item in result:
    if item[1] not in Expenses_list:
        Expenses_list.append(float(item[1])) #convert to float 

# print(Expenses_list)

# create a function to find the highest value 
def find_highest_value(list):
    list.sort(reverse=True) # use list.sort to sort the values from ascending order 
    return(list[0])

#find the highest value expense
highestValue = find_highest_value(Expenses_list)

print(f"Overheadrecords: {overheadRecords}")
print(f"Expense list: {Expenses_list}")
print(f"highest value: {highestValue}")

# loop thru the overheadRecords
#     loop thru the list of list
#         if it contains the highestValue, print that list
#         else: move on
#Loop through overheadRecords to find and print the records with the highest expense value
for i in result:
    if float(i[1]) == highestValue:
        print(i)
