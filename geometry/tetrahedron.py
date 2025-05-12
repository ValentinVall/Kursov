import bpy
import bmesh
from math import sqrt
from geometry.base_shape import PlatonShape


class Tetrahedron(PlatonShape):
    def __init__(self, name="Tetrahedron"):
        super().__init__(name)
        self.create_mesh()

    def create_mesh(self):
        # Координати вершин тетраедра (залишаємо як є)
        verts = [
            (1, 1, 1),
            (-1, -1, 1),
            (-1, 1, -1),
            (1, -1, -1)
        ]

        faces = [
            (0, 1, 2),
            (0, 3, 1),
            (0, 2, 3),
            (1, 3, 2)
        ]

        mesh = bpy.data.meshes.new(f"{self.name}_Mesh")
        obj = bpy.data.objects.new(self.name, mesh)
        bpy.context.collection.objects.link(obj)

        bm = bmesh.new()

        for v in verts:
            bm.verts.new(v)
        bm.verts.ensure_lookup_table()

        for f in faces:
            bm.faces.new([bm.verts[i] for i in f])

        bm.to_mesh(mesh)
        bm.free()

        self.obj = obj
