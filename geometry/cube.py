# geometry/cube.py

import bpy
import bmesh
from .base_shape import PlatonShape

class Cube(PlatonShape):
    def __init__(self, name="Cube", location=(0, 0, 0)):
        super().__init__(name, location)
        self.build()

    def create_mesh(self):
        # Вершини куба
        vertices = [
            (1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1),
            (1, 1, -1), (1, -1, -1), (-1, -1, -1), (-1, 1, -1)
        ]

        # Грані (квадрати з 4 вершин)
        faces = [
            (0, 1, 2, 3),  # верх
            (0, 1, 5, 4),  # перед
            (1, 2, 6, 5),  # низ
            (2, 3, 7, 6),  # зад
            (3, 0, 4, 7),  # ліво
            (4, 5, 6, 7)   # право
        ]

        # Створення мешу
        mesh = bpy.data.meshes.new(f"{self.name}_Mesh")
        mesh.from_pydata(vertices, [], faces)
        mesh.update()

        # Додаємо об'єкт на сцену
        obj = bpy.data.objects.new(self.name, mesh)
        bpy.context.collection.objects.link(obj)

        self.obj = obj
