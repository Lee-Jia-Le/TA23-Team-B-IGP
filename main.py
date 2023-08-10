import Profit_and_loss
from Cash_on_hand import cash_on_hand, generate_summary_report as cash_generate_summary_report
from Overheads import find_highest_overhead as overhead_find_highest_overhead
# ^ Importing all the 3 python files and renaming functions here for more clarity

# Reading the CSV files and creating strings for profit and loss
file_path = "Profits_and_Loss.csv"
data = Profit_and_loss.read_csv_file(file_path)

increase_days_output, highest_increment_output, decrease_days_output = Profit_and_loss.get_output_strings(data)

# creating strings for cash on hand for better presentation
cash_on_hand_output = ""
cash_on_hand_summary = cash_generate_summary_report(cash_on_hand)
cash_on_hand_output += "[CASH ON HAND SEGMENT]\n"
cash_on_hand_output += "======================\n"
cash_on_hand_output += cash_on_hand_summary # binds figures all into one string (cash_on_hand_output) to minimise cluttering at end

# creating strings for overheads for better presentation
overheads_output = ""
overheads_result = overhead_find_highest_overhead("Overheads.csv")
overheads_output += "[OVERHEADS SEGMENT]\n"
overheads_output += "===================\n"
overheads_output += overheads_result # binds figures all into one string (overheads_output) to minimise cluttering at end

# Writing all of the strings to the summary_report.txt file for visual presentation
with open("summary_report.txt", 'w') as output_file:
    output_file.write(overheads_output + "\n")
    output_file.write(cash_on_hand_output + "\n")
    output_file.write("[PROFIT AND LOSS SEGMENT]\n")
    output_file.write("=========================\n")
    output_file.write(highest_increment_output + "\n")
    output_file.write(decrease_days_output)
