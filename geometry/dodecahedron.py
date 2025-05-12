import bpy
import bmesh
from math import sqrt
from geometry.base_shape import PlatonShape


class Dodecahedron(PlatonShape):
    def __init__(self, name="Dodecahedron"):
        super().__init__(name)
        self.create_mesh()

    def create_mesh(self):
        phi = (1 + sqrt(5)) / 2  # Золоте співвідношення

        a, b = 1, 1 / phi

        verts = [
            (-a, -a, -a),
            (-a, -a, a),
            (-a, a, -a),
            (-a, a, a),
            (a, -a, -a),
            (a, -a, a),
            (a, a, -a),
            (a, a, a),
            (0, -b, -phi),
            (0, -b, phi),
            (0, b, -phi),
            (0, b, phi),
            (-b, -phi, 0),
            (-b, phi, 0),
            (b, -phi, 0),
            (b, phi, 0),
            (-phi, 0, -b),
            (phi, 0, -b),
            (-phi, 0, b),
            (phi, 0, b)
        ]

        faces = [
            (0, 8, 10, 2, 16),
            (0, 16, 18, 1, 12),
            (0, 12, 14, 4, 8),
            (8, 4, 17, 6, 10),
            (10, 6, 13, 3, 2),
            (2, 3, 19, 18, 16),
            (1, 18, 19, 7, 11),
            (1, 11, 9, 14, 12),
            (4, 14, 9, 5, 17),
            (6, 17, 5, 15, 13),
            (3, 13, 15, 7, 19),
            (7, 15, 5, 9, 11)
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
