from pathlib import Path
import csv

def find_highest_overhead(csv_file_path):
    fp = Path(csv_file_path)
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        overheadRecords = []

        for row in reader:
            overheadRecords.append([row[0], row[1]])

        for item in overheadRecords:
            value = item[1]
            item[1] = value.replace("$", "")

        Expenses_list = []
        for item in overheadRecords:
            if item[1] not in Expenses_list:
                Expenses_list.append(float(item[1]))

        def find_highest_value(list):
            list.sort(reverse=True)
            return list[0]

        highestValue = find_highest_value(Expenses_list)

        highest_overheads = []
        for i in overheadRecords:
            if float(i[1]) == highestValue:
                highest_overheads.append(i)

        return highest_overheads

# Call the function with your CSV file path
csv_file_path = "Overheads.csv"
result = find_highest_overhead(csv_file_path)

for i in result:
    print("HIGHEST OVERHEAD:", ' : '.join(i), "%")
