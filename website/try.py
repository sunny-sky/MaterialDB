from pymatgen.core.structure import Structure
from MaterialDB.settings import BASE_DIR

print(BASE_DIR)

# Student.objects.create(name='klc111', age=18)
# file_obj = "test.cif"
# print("../static/json/"+file_obj.split(".")[0]+".json")
# var = Structure.from_file("../static/cif/test.cif")
# print(var)
# var.to(filename="../static/json/test.json")

# BandStructureSymmLine.from_dict()
# p = plotter.BSPlotter("/static/json/jmol.json")
# p.show()

# # These three lines assimilate the data into ComputedEntries.
# drone = VaspToComputedEntryDrone()
# queen = BorgQueen(drone, "Li-O_runs", 2)
# entries = queen.get_data()
#
# # It's a good idea to perform a save_data, especially if you just assimilated
# # a large quantity of data which took some time. This allows you to reload
# # the data using a BorgQueen initialized with only the drone argument and
# # calling queen.load_data("Li-O_entries.json")
# queen.save_data("Li-O_entries.json")
#
# # These few lines generates the phase diagram using the ComputedEntries.
# pd = PhaseDiagram(entries)
# plotter = PDPlotter(pd)
# plotter.show()
