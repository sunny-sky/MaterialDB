from django.test import TestCase
import pymatgen as mg
from pymatgen.apps.borg.hive import VaspToComputedEntryDrone
from pymatgen.apps.borg.queen import BorgQueen
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDPlotter
from pymatgen import Lattice, Structure, Molecule

# Create your tests here.


class TestPymatgen(TestCase):
    def test_graph(self):
        # 从文件读结构
        print("1")
        structure = mg.Structure.from_file("jmol.cif")
        print(structure)
        if(structure):
            print("1")
        self.assertIs(structure, True)
