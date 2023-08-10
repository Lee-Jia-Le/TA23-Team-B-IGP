import profit_loss
from Cash_on_hand import cash_on_hand, generate_summary_report as cash_generate_summary_report
from Overheads import find_highest_overhead as overhead_find_highest_overhead

# Read the CSV files and generate output strings
file_path = "Profits_and_Loss.csv"
data = profit_loss.read_csv_file(file_path)

increase_days_output, highest_increment_output, decrease_days_output = profit_loss.get_output_strings(data)

# Cash on Hand
cash_on_hand_output = ""
cash_on_hand_summary = cash_generate_summary_report(cash_on_hand)
cash_on_hand_output += "[CASH ON HAND SUMMARY]\n"
cash_on_hand_output += cash_on_hand_summary

# Overheads
overheads_output = ""
overheads_result = overhead_find_highest_overhead("Overheads.csv")
overheads_output += "[OVERHEADS SUMMARY]\n"
overheads_output += overheads_result

# Write the output to output.txt
output_file_path = "output.txt"

with open(output_file_path, 'w') as output_file:
    output_file.write("Profit and Loss Summary:\n")
    output_file.write("Net Profit Increase Days:\n")
    output_file.write(increase_days_output + "\n")
    output_file.write("Highest Increment:\n")
    output_file.write(highest_increment_output + "\n")
    output_file.write("Profit Deficit Days:\n")
    output_file.write(decrease_days_output + "\n\n")

    output_file.write("Cash on Hand Summary:\n")
    output_file.write(cash_on_hand_output + "\n\n")

    output_file.write("Overheads Summary:\n")
    output_file.write(overheads_output + "\n")

print("Output has been written to", output_file_path)


