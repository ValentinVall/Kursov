# geometry/icosahedron.py

import bpy
from .base_shape import PlatonShape

class Icosahedron(PlatonShape):
    def __init__(self, name="Icosahedron", location=(0, 0, 0)):
        super().__init__(name, location)
        self.build()

    def create_mesh(self):
        # Вершини икосаедра
        vertices = [
            (0, 1, 1.618), (0, -1, 1.618), (0, 1, -1.618), (0, -1, -1.618),
            (1.618, 0, 1), (1.618, 0, -1), (-1.618, 0, 1), (-1.618, 0, -1),
            (1, 1.618, 0), (-1, 1.618, 0), (1, -1.618, 0), (-1, -1.618, 0)
        ]
        faces = [
            (0, 1, 4), (0, 1, 6), (2, 3, 5), (2, 3, 7),
            (4, 5, 8), (4, 5, 10), (6, 7, 9), (6, 7, 11),
            (8, 9, 0), (8, 9, 2), (10, 11, 1), (10, 11, 3),
            (0, 4, 8), (1, 4, 10), (1, 6, 11), (0, 6, 9),
            (2, 5, 8), (3, 5, 10), (3, 7, 11), (2, 7, 9)
        ]

        # Створення мешу
        mesh = bpy.data.meshes.new(f"{self.name}_Mesh")
        mesh.from_pydata(vertices, [], faces)
        mesh.update()

        # Додавання об'єкта на сцену
        obj = bpy.data.objects.new(self.name, mesh)
        bpy.context.collection.objects.link(obj)

        self.obj = obj
