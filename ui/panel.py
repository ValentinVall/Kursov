import bpy
from geometry import Tetrahedron, Cube, Octahedron, Dodecahedron, Icosahedron
from materials.material_utils import create_material, assign_material
from animation.animator import animate_rotation


class PlatonPanel(bpy.types.Panel):
    bl_label = "Platon Shapes"
    bl_idname = "PLATON_PT_shapes"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Platon'

    def draw(self, context):
        layout = self.layout

        # Панель для створення фігур
        layout.label(text="Create Platon Shapes:")

        row = layout.row()
        row.operator("mesh.create_tetrahedron", text="Tetrahedron")
        row.operator("mesh.create_cube", text="Cube")
        row.operator("mesh.create_octahedron", text="Octahedron")
        row.operator("mesh.create_dodecahedron", text="Dodecahedron")
        row.operator("mesh.create_icosahedron", text="Icosahedron")

        # Панель для анімацій
        layout.label(text="Animate Shapes:")

        row = layout.row()
        row.operator("object.animate_rotation", text="Animate Rotation")

        # Панель для матеріалів
        layout.label(text="Assign Material:")

        row = layout.row()
        row.operator("object.assign_material", text="Assign Material")

# Оператори для створення фігур
class CreateTetrahedronOperator(bpy.types.Operator):
    bl_idname = "mesh.create_tetrahedron"
    bl_label = "Create Tetrahedron"

    def execute(self, context):
        # Створюємо тетраедр
        shape = Tetrahedron()
        mat = create_material(name="TetrahedronMat", color=(1.0, 0.3, 0.3, 1.0))
        assign_material(shape.obj, mat)
        return {'FINISHED'}

class CreateCubeOperator(bpy.types.Operator):
    bl_idname = "mesh.create_cube"
    bl_label = "Create Cube"

    def execute(self, context):
        # Створюємо куб
        shape = Cube()
        mat = create_material(name="CubeMat", color=(0.2, 0.6, 1.0, 1.0))
        assign_material(shape.obj, mat)
        return {'FINISHED'}

class CreateOctahedronOperator(bpy.types.Operator):
    bl_idname = "mesh.create_octahedron"
    bl_label = "Create Octahedron"

    def execute(self, context):
        # Створюємо октаедр
        shape = Octahedron()
        mat = create_material(name="OctahedronMat", color=(0.3, 1.0, 0.6, 1.0))
        assign_material(shape.obj, mat)
        return {'FINISHED'}

class CreateDodecahedronOperator(bpy.types.Operator):
    bl_idname = "mesh.create_dodecahedron"
    bl_label = "Create Dodecahedron"

    def execute(self, context):
        # Створюємо додекаедр
        shape = Dodecahedron()
        mat = create_material(name="DodecahedronMat", color=(1.0, 0.85, 0.1, 1.0))
        assign_material(shape.obj, mat)
        return {'FINISHED'}

class CreateIcosahedronOperator(bpy.types.Operator):
    bl_idname = "mesh.create_icosahedron"
    bl_label = "Create Icosahedron"

    def execute(self, context):
        # Створюємо ікосаедр
        shape = Icosahedron()
        mat = create_material(name="IcosahedronMat", color=(0.1, 0.3, 1.0, 1.0))
        assign_material(shape.obj, mat)
        return {'FINISHED'}

# Оператор для анімації обертання
class AnimateRotationOperator(bpy.types.Operator):
    bl_idname = "object.animate_rotation"
    bl_label = "Animate Rotation"

    def execute(self, context):
        selected_obj = context.view_layer.objects.active
        if selected_obj:
            # Анімація обертання об'єкта
            animate_rotation(selected_obj, axis='Z', frames=100)
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "No object selected")
            return {'CANCELLED'}

# Оператор для призначення матеріалу
class AssignMaterialOperator(bpy.types.Operator):
    bl_idname = "object.assign_material"
    bl_label = "Assign Material"

    def execute(self, context):
        selected_obj = context.view_layer.objects.active
        if selected_obj:
            # Призначаємо матеріал
            mat = create_material(name="CustomMat", color=(0.7, 0.7, 0.2, 1.0))
            assign_material(selected_obj, mat)
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "No object selected")
            return {'CANCELLED'}

# Реєстрація панелі та операторів
def register():
    bpy.utils.register_class(PlatonPanel)
    bpy.utils.register_class(CreateTetrahedronOperator)
    bpy.utils.register_class(CreateCubeOperator)
    bpy.utils.register_class(CreateOctahedronOperator)
    bpy.utils.register_class(CreateDodecahedronOperator)
    bpy.utils.register_class(CreateIcosahedronOperator)
    bpy.utils.register_class(AnimateRotationOperator)
    bpy.utils.register_class(AssignMaterialOperator)

def unregister():
    bpy.utils.unregister_class(PlatonPanel)
    bpy.utils.unregister_class(CreateTetrahedronOperator)
    bpy.utils.unregister_class(CreateCubeOperator)
    bpy.utils.unregister_class(CreateOctahedronOperator)
    bpy.utils.unregister_class(CreateDodecahedronOperator)
    bpy.utils.unregister_class(CreateIcosahedronOperator)
    bpy.utils.unregister_class(AnimateRotationOperator)
    bpy.utils.unregister_class(AssignMaterialOperator)

if __name__ == "__main__":
    register()
