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

    return increase_days, max_increment_day, max_increment_amount

def compute_decrease_days(data):
    decrease_days = []
    for index, day_data in enumerate(data[1:], start=1):
        net_profit = float(day_data['Net Profit'])
        previous_net_profit = float(data[index-1]['Net Profit'])
        difference = previous_net_profit - net_profit

        if difference > 0:
            decrease_days.append((index, difference))

    return decrease_days

def get_output_strings(data):
    increase_days, max_increment_day, max_increment_amount = compute_profit_difference(data)
    
    increase_days_output = ""
    if increase_days:
        increase_days_output = "[NET PROFIT SURPLUS] NET PROFIT IS HIGHER THAN ITS PREVIOUS DAY ONLY ON THE DAYS: " + ", ".join(map(str, increase_days))
    
    highest_increment_output = ""
    if max_increment_day is not None:
        highest_increment_output = f"[HIGHEST NET PROFIT SURPLUS] Day {max_increment_day}, Amount: USD{int(max_increment_amount)}"

    decrease_days = compute_decrease_days(data)
    decrease_days_output = ""
    for day, amount in decrease_days:
        decrease_days_output += f"[PROFIT DEFICIT] Day: {day}, Amount: USD{int(amount)}\n"

    return increase_days_output, highest_increment_output, decrease_days_output
