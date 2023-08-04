from pathlib import Path
import csv

fp = Path.cwd()/"Profits_and_Loss.csv" 
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)