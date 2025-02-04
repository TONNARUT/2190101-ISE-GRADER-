sales_raw = input()

sales_individual = sales_raw.split()
sales_individual_int = [int(sales)for sales in sales_individual]

sales_total = sum(sales_individual_int)
print(sales_total)