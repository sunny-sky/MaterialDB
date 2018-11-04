import pymatgen as mg
import json
from pybtex.database import parse_file
structure = mg.Structure.from_file("../static/cif/jmol.cif")
structure.to(filename="../static/json/jmol.json")
# print(structure)
with open("../static/json/jmol.json", 'r') as load_f:
    load_dict = json.load(load_f)
    print(load_dict['sites'])
