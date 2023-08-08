import csv
from pathlib import Path

#Set up the file path and open the CSV file for reading
def process_csv_file(file_path, skip_condition=None):
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header

    # create an empty list to store the overhead records 
        overheadRecords = []

        for row in reader:
            if skip_condition and skip_condition(row):
                continue  # Skip this row and move to the next iteration

            overheadRecords.append([row[0], row[1]])  # Process the row if not skipped

    return overheadRecords

if __name__ == "__main__":
    csv_file_path = Path.cwd() / "overheads-day-90.csv"

    def custom_skip_condition(row):
        # Define your custom condition here
        # For example: return row[0] == "skip_this_row"
        return False

    result = process_csv_file(csv_file_path, skip_condition=custom_skip_condition)
    # Now 'result' contains only the processed rows according to the condition

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

print(f"Overheadrecords: {result}")
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
