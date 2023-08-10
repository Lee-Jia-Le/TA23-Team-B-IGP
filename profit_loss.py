import csv

def read_csv_file(file_path):
    """
    Read data from a CSV file and return it as a list of dictionaries.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        list: A list of dictionaries representing the CSV data.
    """
    data = []
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)
    return data

def compute_profit_difference(data):
    """
    Compute the days when the net profit increased and find the highest net profit increment.

    Parameters:
        data (list): A list of dictionaries representing the CSV data.

    Prints:
        str: Days when the net profit increased.
        str: Highest net profit increment and the corresponding day.
    """
    increase_days = [index for index, day_data in enumerate(data[1:], start=1) if float(day_data['Net Profit']) > float(data[index-1]['Net Profit'])]

    max_increment_day = None
    max_increment_amount = 0
    for index, day_data in enumerate(data[1:], start=1):
        net_profit = float(day_data['Net Profit'])
        difference = net_profit - float(data[index-1]['Net Profit'])
        if difference > max_increment_amount:
            max_increment_amount = difference
            max_increment_day = index

    print("[NET PROFIT SURPLUS] NET PROFIT IS HIGHER THAN ITS PREVIOUS DAY ONLY ON THE DAYS:",", ".join(map(str, increase_days)))
    if max_increment_day is not None:
        print(f"[HIGHEST NET PROFIT SURPLUS] Day {max_increment_day}, Amount: USD{int(max_increment_amount)}")

def compute_decrease_days(data):
    """
    Compute the days when the net profit decreased and the corresponding decrease amount.

    Parameters:
        data (list): A list of dictionaries representing the CSV data.

    Returns:
        list: A list of tuples containing the day and the decrease amount.
    """
    decrease_days = []
    for index, day_data in enumerate(data[1:], start=1):
        net_profit = float(day_data['Net Profit'])
        previous_net_profit = float(data[index-1]['Net Profit'])
        difference = previous_net_profit - net_profit

        if difference > 0:
            decrease_days.append((index, difference))

    return decrease_days

file_path = "Profits_and_Loss.csv"
data = read_csv_file(file_path)

compute_profit_difference(data)

decrease_days = compute_decrease_days(data)
for day, amount in decrease_days:
    print(f"[PROFIT DEFICIT] Day: {day}, Amount: USD{int(amount)}")
