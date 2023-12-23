```python
import os

class FootprintGenerator:
    def __init__(self, name):
        self.name = name
        self.file_content = []

    def add_header(self):
        self.file_content.append('(module {} (layer F.Cu)'.format(self.name))
        self.file_content.append('(fp_text reference REF** (at 0 0.5) (layer F.SilkS))')
        self.file_content.append('(fp_text value {} (at 0 -0.5) (layer F.Fab))'.format(self.name))

    def add_pin(self, number, x, y):
        self.file_content.append('(pad {} smd rect (at {} {}) (size 1.5 1.5) (layers F.Cu F.Paste F.Mask))'.format(number, x, y))

    def add_footer(self):
        self.file_content.append(')')

    def generate(self):
        self.add_header()
        self.add_pin(1, -1.5, 0)
        self.add_pin(2, 1.5, 0)
        self.add_footer()

        return '\n'.join(self.file_content)

if __name__ == "__main__":
    generator = FootprintGenerator('Custom_Footprint')
    footprint = generator.generate()

    with open(os.path.join('Tools', 'KiCAD_Extensions', 'custom_footprint_generator.py'), 'w') as f:
        f.write(footprint)
```
