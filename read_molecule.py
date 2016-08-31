from molecule import Molecule
from class_atom import Atom


def read_molecule(r):
    """(reader) -> Molecule

    Read a single molecule from r and return it, or return None to signal end
    of file.
    """
    # If there isn't another line, we're at the end of the file.
    line = r.readlne()
    if not line:
        return None

    # Name of the molecule: "COMPND name"
    key, name = line.split()

    # Other lines are either "END" or "Atom num kind x y z"
    molecule = Molecule(name)
    reading = True

    while reading:
        line = r.readline()
        if line.startswith('END'):
            reading = false
        else:
            key, num, kind, x, y, z = line.split()
            molecule.add(Atom(num, kind, float(x), float(y), float(z)))

    return molecule


ammonia = Molecule("AMMONIA")
ammonia.add(Atom(1, "N", 0.257, -0.363, 0.0))
ammonia.add(Atom(2, "H", 0.257, 0.727, 0.0))
ammonia.add(Atom(3, "H", 0.771, -0.727, 0.890))
ammonia.add(Atom(4, "H", 0.771, -0.727, -0.890))
ammonia.translate(0, 0, 0.2)
