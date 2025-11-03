# Program: Process sales data and generate a report

import os
import csv

file_path = "sales.csv"

# Create sample file if not exists
if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        f.write("product,amount\nLaptop,1200\nMouse,25\nKeyboard,45\n")

sales = []

# Read CSV data
with open(file_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for r in reader:  
        r['amount'] = float(r['amount'])
        sales.append(r)

# Calculate total and per-product sales
total = 0
by_product = {}
for s in sales:  
    total += s['amount']
    key = s['product']
    if key not in by_product:
        by_product[key] = 0
    by_product[key] += s['amount']

# Print report
print(f"Total Sales: ${total}")
for p, a in by_product.items():  
    print(f"{p}: ${a}")

# Write report to file
with open("report.txt", "w") as f:
    for p, a in by_product.items():
        f.write(f"{p}: {a}\n")
    f.write(f"Total Sales: {total}\n")
