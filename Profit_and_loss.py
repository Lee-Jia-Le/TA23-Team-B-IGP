import csv

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)
    return data

def compute_profit_difference(data):
    increase_days = [index for index, day_data in enumerate(data[1:], start=1) if float(day_data['Net Profit']) > float(data[index-1]['Net Profit'])]

    max_increment_day = None
    max_increment_amount = 0
    for index, day_data in enumerate(data[1:], start=1):
        net_profit = float(day_data['Net Profit'])
        difference = net_profit - float(data[index-1]['Net Profit'])
        if difference > max_increment_amount:
            max_increment_amount = difference
            max_increment_day = index

    print("[Days OF NET PROFIT SURPLUS]", ", ".join(map(str, increase_days)))
    if max_increment_day is not None:
        print(f"[HIGHEST NET PROFIT SURPLUS] Day {max_increment_day}, Amount: USD{int(max_increment_amount)}")

def compute_decrease_days(data):
    decrease_days = []
    for index, day_data in enumerate(data[1:], start=1):
        net_profit = float(day_data['Net Profit'])
        previous_net_profit = float(data[index-1]['Net Profit'])
        difference = previous_net_profit - net_profit

        if difference > 0:
            decrease_days.append((index, difference))

    return decrease_days

if __name__ == "__main__":
    file_path = "Profits_and_Loss.csv"
    data = read_csv_file(file_path)

    print("Scenario 1:") ###remove as needed
    compute_profit_difference(data)

    print("\nScenario 2:") ###remove as needed
    decrease_days = compute_decrease_days(data)
    for day, amount in decrease_days:
        print(f"[PROFIT DEFICIT] Day: {day}, Amount: USD{int(amount)}")