```python
import csv
import os

def read_bom(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        bom = list(reader)
    return bom

def write_bom(file_path, bom):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Part Number', 'Description', 'Quantity', 'Supplier'])
        writer.writerows(bom)

def main():
    bom_files = ['Hardware/BOM/MainBoard_BOM.csv', 'Hardware/BOM/PowerSupply_BOM.csv']
    consolidated_bom = []

    for bom_file in bom_files:
        if os.path.exists(bom_file):
            consolidated_bom.extend(read_bom(bom_file))
        else:
            print(f'Warning: {bom_file} does not exist.')

    write_bom('Hardware/BOM/Consolidated_BOM.csv', consolidated_bom)

if __name__ == "__main__":
    main()
```
