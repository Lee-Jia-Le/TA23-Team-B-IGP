from pathlib import Path
import csv

def find_highest_overhead(csv_file_path):
    fp = Path(csv_file_path)
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        
        #create an empty list to store overhead Records 
        overheadRecords = []
        
        #append the first and second columns of the row as a list to the overheadRecords list
        for row in reader:
            overheadRecords.append([row[0], row[1]])

        for item in overheadRecords:
            value = item[1]
            item[1] = value.replace("$", "") #remove the dollar sign

        #create an empty list to store the functions  
        Expenses_list = []
        for item in overheadRecords:
            if item[1] not in Expenses_list:
                Expenses_list.append(float(item[1])) #convert the expenses to float 

        def find_highest_value(list):
            list.sort(reverse=True) 
            return list[0]     # Return the first element of the sorted list

        highestValue = find_highest_value(Expenses_list)
 # Initialize an empty list to store overhead records with the highest value
        highest_overheads = []
        for i in overheadRecords: 
            if float(i[1]) == highestValue:
                highest_overheads.append(i)
#Return the list of overhead records with the highest value
        return highest_overheads

# Call the function with your CSV file path
csv_file_path = "Overheads.csv"
result = find_highest_overhead(csv_file_path)

for i in result:
    print("HIGHEST OVERHEAD:", ' : '.join(i), "%")
