# geometry/tetrahedron.py

import bpy
import bmesh
from .base_shape import PlatonShape

class Tetrahedron(PlatonShape):
    def __init__(self, name="Tetrahedron", location=(0, 0, 0)):
        super().__init__(name, location)
        self.build()  # одразу побудувати при створенні

    def create_mesh(self):
        # Вершини та грані тетраедра
        vertices = [
            (0.943, 0, -0.333),
            (-0.471, -0.816, -0.333),
            (-0.471, 0.816, -0.333),
            (0, 0, 1)
        ]

        faces = [
            (0, 1, 2),
            (0, 1, 3),
            (0, 2, 3),
            (1, 2, 3)
        ]

        # Створення мешу
        mesh = bpy.data.meshes.new(f"{self.name}_Mesh")
        mesh.from_pydata(vertices, [], faces)
        mesh.update()

        # Створення об'єкта та зв'язок зі сценою
        obj = bpy.data.objects.new(self.name, mesh)
        bpy.context.collection.objects.link(obj)

        self.obj = obj
