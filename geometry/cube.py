import bpy
import bmesh
from geometry.base_shape import PlatonShape


class Cube(PlatonShape):
    def __init__(self, name="Cube"):
        super().__init__(name)
        self.create_mesh()

    def create_mesh(self):
        verts = [
            (-1, -1, -1),
            (-1, -1,  1),
            (-1,  1, -1),
            (-1,  1,  1),
            (1, -1, -1),
            (1, -1,  1),
            (1,  1, -1),
            (1,  1,  1),
        ]

        faces = [
            (0, 1, 3, 2),
            (4, 6, 7, 5),
            (0, 4, 5, 1),
            (2, 3, 7, 6),
            (0, 2, 6, 4),
            (1, 5, 7, 3),
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
