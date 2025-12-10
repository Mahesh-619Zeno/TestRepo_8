import csv
import os
from pathlib import Path


def ensure_sample_file(file_path: Path):
    """Create a sample CSV if none exists."""
    if not file_path.exists():
        file_path.write_text("product,amount\nSample,10.5\n", encoding="utf-8")


def read_sales(file_path: str):
    """Read sales data from a CSV file and return a list of dicts."""
    file_path = Path(file_path)
    ensure_sample_file(file_path)

    sales = []
    with file_path.open(newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                row["amount"] = float(row["amount"])
            except ValueError:
                # Skip malformed rows instead of crashing
                continue
            sales.append(row)

    return sales


def generate_report(sales, report_file="report.txt"):
    """Generate a text report summarizing total and product sales."""
    total_sales = sum(s["amount"] for s in sales)

    # Aggregate by product
    by_product = {}
    for s in sales:
        by_product[s["product"]] = by_product.get(s["product"], 0) + s["amount"]

    # Print to console
    print(f"Total Sales: ${total_sales:.2f}")
    for product, amount in by_product.items():
        print(f"{product}: ${amount:.2f}")

    # Save report
    with open(report_file, "w", encoding="utf-8") as f:
        for product, amount in by_product.items():
            f.write(f"{product}: {amount}\n")
        f.write(f"Total Sales: {total_sales}\n")

    # Optional: controlled deletion
    # if os.path.exists("sales.csv"):
    #     os.remove("sales.csv")


def main():
    sales_data = read_sales("sales.csv")
    generate_report(sales_data)
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
