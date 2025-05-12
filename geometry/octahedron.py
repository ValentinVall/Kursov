import bpy
import bmesh
from geometry.base_shape import PlatonShape


class Octahedron(PlatonShape):
    def __init__(self, name="Octahedron"):
        super().__init__(name)
        self.create_mesh()

    def create_mesh(self):
        verts = [
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1)
        ]

        faces = [
            (0, 2, 4),
            (2, 1, 4),
            (1, 3, 4),
            (3, 0, 4),
            (0, 5, 2),
            (2, 5, 1),
            (1, 5, 3),
            (3, 5, 0)
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
