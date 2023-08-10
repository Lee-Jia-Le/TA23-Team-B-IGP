import Overheads
import Cash_on_hand
import profit_loss

with open('summary_report.txt', 'w') as file:
    file.write(f"{print(Overheads.find_highest_overhead())} \n") # prints the Highest Overheads onto the .txt file using an f string
    file.write(f"{print(Cash_on_hand)} \n")
    file.write(f"{print(profit_loss.compute_decrease_days)} \n")
    file.write(f"{print(profit_loss.compute_profit_difference)}")