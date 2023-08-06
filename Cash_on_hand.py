def find_surplus_deficit_days(cash_on_hand):
    """Finds the surplus and deficit days in Cash-on-Hand."""
    surplus_days = []
    deficit_days = []

    # Loop through the cash_on_hand list and check for surplus and deficit days
    for day in range(1, len(cash_on_hand)):
        if cash_on_hand[day] > cash_on_hand[day - 1]:
            surplus_days.append(day)
        elif cash_on_hand[day] < cash_on_hand[day - 1]:
            deficit_days.append(day)

    return surplus_days, deficit_days

def find_highest_increment(cash_on_hand):
    """Finds the day and amount of the highest increment in Cash-on-Hand."""
    highest_increment = 0
    day_of_highest_increment = 0

    # Loop through the cash_on_hand list and find the highest increment
    for day in range(1, len(cash_on_hand)):
        current_increment = cash_on_hand[day] - cash_on_hand[day - 1]
        if current_increment > highest_increment:
            highest_increment = current_increment
            day_of_highest_increment = day

    return day_of_highest_increment, highest_increment

def generate_summary_report(cash_on_hand):
    """Generate the summary report and save it in a text file."""
    with open("summary_report.txt", "w") as file:
        surplus_days, deficit_days = find_surplus_deficit_days(cash_on_hand)

        # Check for surplus days and write corresponding information to the file
        if surplus_days:
            file.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
            day_of_highest_increment, highest_increment = find_highest_increment(cash_on_hand)
            file.write(f"[HIGHEST CASH SURPLUS] DAY: {day_of_highest_increment + 1}, AMOUNT: USD {highest_increment}\n")
        else:
            # If no surplus days, write the deficit information to the file
            file.write("[CASH DEFICIT] DAY: , AMOUNT: USD 0\n")

        # Write information for each deficit day to the file
        for day in deficit_days:
            deficit_amount = cash_on_hand[day - 1] - cash_on_hand[day]  # Correct the deficit_amount calculation
            file.write(f"[CASH DEFICIT] DAY: {day + 1}, AMOUNT: USD {deficit_amount}\n")

if __name__ == "__main__":
    # Cash on hand scenarios 
    # cash_on_hand_scenario1 = [3487400, 3329490, 2643180, 2365949, 2821462, 1112311, 1179895, 75233, 164433, 2700980]
    # cash_on_hand_scenario2 = [3487400, 3329490, 2643180, 2365949, 2821462, 1112311, 1179895, 75233, 164433, 2700980]
    
    cash_on_hand_scenario1 = [3487400, 3329490, 2643180, 2365949, 2821462, 1112311, 1179895, 75233, 164433, 2700980, 2687691, 2010130, 1938975, 4068431, 2762974, 1617661, 2944445, 3651099, 1500097, 1554861]
    cash_on_hand_scenario2 = [3487400, 3329490, 2643180, 2365949, 2821462, 1112311, 1179895, 75233, 164433, 2700980, 2687691, 2010130, 1938975, 4068431, 2762974, 1617661, 2944445, 3651099, 1500097, 1554861]

    # Generate and save the summary report for each scenario
    generate_summary_report(cash_on_hand_scenario1)
    generate_summary_report(cash_on_hand_scenario2)