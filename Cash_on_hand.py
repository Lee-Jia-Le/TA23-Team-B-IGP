def find_surplus_deficit_days(cash_on_hand):
    """
    Finds the surplus and deficit days in Cash-on-Hand.

    Input:
        cash_on_hand (list): List of cash on hand amounts over days.

    Returns:
        A tuple containing two lists - surplus_days and deficit_days.
    """
    surplus_days = []
    deficit_days = []

    # Loop through the cash_on_hand list and identify surplus and deficit days
    for day in range(1, len(cash_on_hand)):
        if cash_on_hand[day] > cash_on_hand[day - 1]:
            surplus_days.append(day)
        elif cash_on_hand[day] < cash_on_hand[day - 1]:
            deficit_days.append(day)

    return surplus_days, deficit_days

def find_highest_increment(cash_on_hand):
    """
    Finds the day and amount of the highest increment in Cash-on-Hand.

    Input:
        cash_on_hand (list): List of cash on hand amounts over days.

    Returns:
        A tuple containing the day and amount of the highest increment.
    """
    highest_increment = 0
    day_of_highest_increment = 0

    # Loop through the cash_on_hand list and calculate the highest increment
    for day in range(1, len(cash_on_hand)):
        current_increment = cash_on_hand[day] - cash_on_hand[day - 1]
        if current_increment > highest_increment:
            highest_increment = current_increment
            day_of_highest_increment = day

    return day_of_highest_increment, highest_increment

def generate_summary_report(cash_on_hand):
    """
    Generate the summary report and print it in the console.

    Input:
        cash_on_hand (list): List of cash on hand amounts over days.
    """
    surplus_days, deficit_days = find_surplus_deficit_days(cash_on_hand)

    if surplus_days:
        print("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        day_of_highest_increment, highest_increment = find_highest_increment(cash_on_hand)
        print(f"[HIGHEST CASH SURPLUS] DAY: {day_of_highest_increment + 1}, AMOUNT: USD{highest_increment}")
    else:
        print("[CASH DEFICIT] DAY: , AMOUNT: USD0")

    # Loop through deficit_days and print information about each deficit day
    for day in deficit_days:
        if day > 1:
            deficit_amount = cash_on_hand[day - 1] - cash_on_hand[day]
            print(f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD{deficit_amount}")

# Read data from cash_on_hand.csv file
cash_on_hand = []
with open("cash_on_hand.csv", "r") as csv_file:
    next(csv_file)  # Skip the header line
    for line in csv_file:
        day, cash = line.strip().split(',')
        cash_on_hand.append(int(cash))

# Generate the summary report and print it to the console
generate_summary_report(cash_on_hand)
