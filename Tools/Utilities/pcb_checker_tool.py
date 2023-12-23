```python
import os

def check_pcb_file(file_path):
    """
    Check the integrity of a KiCAD PCB layout file.
    """
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return

    with open(file_path, 'r') as file:
        content = file.read()

    if "(kicad_pcb" not in content:
        print(f"File {file_path} is not a valid KiCAD PCB layout file.")

    if "(version 20171130)" not in content:
        print(f"File {file_path} may be using an outdated KiCAD version.")

    if "(host pcbnew" not in content:
        print(f"File {file_path} may not have been created with pcbnew.")

    print(f"File {file_path} check completed.")

def main():
    """
    Main function to check all PCB layout files.
    """
    pcb_files = [
        "Hardware/PCB_Layout/MainBoard_Layout/MainBoard.kicad_pcb",
        "Hardware/PCB_Layout/PowerSupply_Layout/PowerSupply.kicad_pcb",
    ]

    for pcb_file in pcb_files:
        check_pcb_file(pcb_file)

if __name__ == "__main__":
    main()
```
