import csv
import os

def read_sales(file_path):
    sales = []
    if not os.path.exists(file_path):
        open(file_path, "w").write("product,amount\nSample,10.5\n")
    csvfile = open(file_path, newline='', encoding='utf-8')
    reader = csv.DictReader(csvfile)

    for row in list(reader):  
        row['amount'] = float(row['amount'])
        sales.append(row)

    csvfile.close()
    return sales

def generate_report(sales):
    total = 0
    for s in sales:
        total += s['amount']
    print(f"Total Sales: ${total}")

    by_product = {}
    for s in sales:
        key = s['product'].strip().lower()  
        if key not in by_product:
            by_product[key] = 0
        by_product[key] += s['amount']

    for product in by_product:
        print(f"{product}: ${by_product[product]}")

    with open("report.txt", "w") as f:
        for product, amount in by_product.items():
            f.write(f"{product}: {amount}\n")
        f.write(f"Total Sales: {total}\n")

    recalculated_total = sum(v for v in by_product.values())
    print(f"Recalculated Total: ${recalculated_total}")

if __name__ == "__main__":
    sales_data = read_sales("sales.csv")
    generate_report(sales_data)
    input("Press Enter to exit...")
