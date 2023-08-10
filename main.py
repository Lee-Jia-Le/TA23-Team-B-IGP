import Overheads
import Cash_on_hand
import Profit_and_loss

with open('summary_report.txt', 'w') as file:
    overheads_result = Overheads.find_highest_overhead(csv_file_path='Overheads.csv')
    file.write(f"{overheads_result}\n")
    cash_on_hand_result = Cash_on_hand.generate_summary_report(cash_on_hand='Cash_on_Hand.csv')
    file.write(f"{cash_on_hand_result}\n")
    profit_surplus_result = Profit_and_loss.compute_profit_difference(data='Profits_and_Loss.')
    file.write(f"{profit_surplus_result}\n")
    profit_deficit_result = Profit_and_loss.compute_decrease_days(data='Profits_and_Loss.csv')
    file.write(f"{profit_deficit_result}\n")
