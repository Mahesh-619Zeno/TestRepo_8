import csv
import os
from typing import List, Dict


def ensure_sales_file(file_path: str) -> None:
    """Ensure the sales file exists; if not, create a sample file."""
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8", newline="") as f:
            f.write("product,amount\nSample,10.5\n")


def read_sales(file_path: str) -> List[Dict[str, float]]:
    """Read sales records from a CSV file."""
    ensure_sales_file(file_path)

    sales = []
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row["amount"] = float(row["amount"])
            sales.append(row)

    return sales


def summarize_sales(sales: List[Dict[str, float]]) -> Dict[str, float]:
    """Return total and per-product sales."""
    by_product = {}
    for s in sales:
        by_product.setdefault(s["product"], 0)
        by_product[s["product"]] += s["amount"]

    total = sum(by_product.values())
    return {"total": total, "by_product": by_product}


def print_report(summary: Dict[str, float]) -> None:
    """Print sales summary to console."""
    print(f"Total Sales: ${summary['total']:.2f}")
    for product, amount in summary["by_product"].items():
        print(f"{product}: ${amount:.2f}")


def write_report(summary: Dict[str, float], output_path: str = "report.txt") -> None:
    """Write sales report to a text file."""
    with open(output_path, "w", encoding="utf-8") as f:
        for product, amount in summary["by_product"].items():
            f.write(f"{product}: {amount:.2f}\n")
        f.write(f"Total Sales: {summary['total']:.2f}\n")


def generate_report(file_path: str, delete_source=False) -> None:
    """Read sales, generate a report, write to file, optionally delete CSV."""
    sales = read_sales(file_path)
    summary = summarize_sales(sales)

    print_report(summary)
    write_report(summary)

    if delete_source and os.path.exists(file_path):
        os.remove(file_path)


if __name__ == "__main__":
    generate_report("sales.csv", delete_source=False)
    input("Press Enter to exit...")
