# geometry/octahedron.py

import bpy
from .base_shape import PlatonShape

class Octahedron(PlatonShape):
    def __init__(self, name="Octahedron", location=(0, 0, 0)):
        super().__init__(name, location)
        self.build()

    def create_mesh(self):
        # Вершини октаедра
        vertices = [
            (0, 0, -1),    # 0 — нижній кінець
            (-1, 0, 0),    # 1
            (0, -1, 0),    # 2
            (1, 0, 0),     # 3
            (0, 1, 0),     # 4
            (0, 0, 1)      # 5 — верхній кінець
        ]

        # Грані — 8 трикутників
        faces = [
            (0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 4, 1),
            (5, 1, 2), (5, 2, 3), (5, 3, 4), (5, 4, 1)
        ]

        # Створення мешу
        mesh = bpy.data.meshes.new(f"{self.name}_Mesh")
        mesh.from_pydata(vertices, [], faces)
        mesh.update()

        # Додавання до сцени
        obj = bpy.data.objects.new(self.name, mesh)
        bpy.context.collection.objects.link(obj)

        self.obj = obj
