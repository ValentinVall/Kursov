# geometry/dodecahedron.py

import bpy
from .base_shape import PlatonShape

class Dodecahedron(PlatonShape):
    def __init__(self, name="Dodecahedron", location=(0, 0, 0)):
        super().__init__(name, location)
        self.build()

    def create_mesh(self):
        # Вершини додекаедра
        vertices = [
            (1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1), (1, 1, -1), (1, -1, -1),
            (-1, -1, -1), (-1, 1, -1), (0, 1.618, 0.618), (0, -1.618, 0.618),
            (0, -1.618, -0.618), (0, 1.618, -0.618), (0.618, 0, 1.618), (-0.618, 0, 1.618),
            (-0.618, 0, -1.618), (0.618, 0, -1.618), (1.618, 0.618, 0), (-1.618, 0.618, 0),
            (-1.618, -0.618, 0), (1.618, -0.618, 0)
        ]

        # Грані додекаедра (п'ятикутники)
        faces = [
            (8, 11, 4, 16, 0), (8, 11, 7, 17, 3), (9, 10, 5, 19, 1), (9, 10, 6, 18, 2),
            (12, 13, 3, 8, 0), (12, 13, 2, 9, 1), (15, 14, 7, 11, 4), (15, 14, 6, 10, 5),
            (16, 19, 1, 12, 0), (16, 19, 5, 15, 4), (17, 18, 2, 13, 3), (17, 18, 6, 14, 7)
        ]

        # Створення мешу
        mesh = bpy.data.meshes.new(f"{self.name}_Mesh")
        mesh.from_pydata(vertices, [], faces)
        mesh.update()

        # Додавання об'єкта на сцену
        obj = bpy.data.objects.new(self.name, mesh)
        bpy.context.collection.objects.link(obj)

        self.obj = obj
