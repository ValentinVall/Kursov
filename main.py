import sys
import os

# Додаємо шлях до кореневої директорії проекту
sys.path.append("C:/Users/Admin/PycharmProjects/Platocin")

import bpy
from geometry.tetrahedron import Tetrahedron
from geometry.cube import Cube
from geometry.octahedron import Octahedron
from geometry.dodecahedron import Dodecahedron
from geometry.icosahedron import Icosahedron


def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def main():
    clear_scene()
    tetra = Tetrahedron(location=(0, 0, 0))
    print("Tetrahedron created successfully!")

    tetra = Cube(location=(3, 0, 0))
    print("Cube created successfully!")

    tetra = Octahedron(location=(-3, 0, 0))
    print("Octahedron created successfully!")

    tetra = Dodecahedron(location=(-6, 0, 0))
    print("Dodecahedron created successfully!")

    tetra = Icosahedron(location=(6, 0, 0))
    print("Icosahedron created successfully!")


if __name__ == "__main__":
    main()
