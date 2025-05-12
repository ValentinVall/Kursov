import bpy
import bmesh
from math import sqrt
from geometry.base_shape import PlatonShape


class Icosahedron(PlatonShape):
    def __init__(self, name="Icosahedron"):
        super().__init__(name)
        self.create_mesh()

    def create_mesh(self):
        phi = (1 + sqrt(5)) / 2  # Золоте співвідношення

        verts = [
            (-1,  phi,  0),
            ( 1,  phi,  0),
            (-1, -phi,  0),
            ( 1, -phi,  0),
            ( 0, -1,  phi),
            ( 0,  1,  phi),
            ( 0, -1, -phi),
            ( 0,  1, -phi),
            ( phi,  0, -1),
            ( phi,  0,  1),
            (-phi,  0, -1),
            (-phi,  0,  1)
        ]

        faces = [
            (0, 11, 5),
            (0, 5, 1),
            (0, 1, 7),
            (0, 7, 10),
            (0, 10, 11),
            (1, 5, 9),
            (5, 11, 4),
            (11, 10, 2),
            (10, 7, 6),
            (7, 1, 8),
            (3, 9, 4),
            (3, 4, 2),
            (3, 2, 6),
            (3, 6, 8),
            (3, 8, 9),
            (4, 9, 5),
            (2, 4, 11),
            (6, 2, 10),
            (8, 6, 7),
            (9, 8, 1)
        ]

        mesh = bpy.data.meshes.new(f"{self.name}_Mesh")
        obj = bpy.data.objects.new(self.name, mesh)
        bpy.context.collection.objects.link(obj)

        bm = bmesh.new()

        for v in verts:
            bm.verts.new(v)
        bm.verts.ensure_lookup_table()

        for f in faces:
            try:
                bm.faces.new([bm.verts[i] for i in f])
            except ValueError:
                # Уникаємо дублювання облич
                pass

        bm.to_mesh(mesh)
        bm.free()

        self.obj = obj
