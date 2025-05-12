import sys
import os

# Додаємо шлях до кореневої директорії проекту
sys.path.append("C:/Users/Admin/PycharmProjects/Platocin")


import bpy
from geometry.tetrahedron import Tetrahedron
from geometry.cube import Cube
from geometry.octahedron import Octahedron
from geometry.dodecahedron import Dodecahedron
from geometry.icosahedron import Icosahedron
from animation.animator import animate_rotation
from materials.material_utils import create_material, apply_material

# Очищення сцени
def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

# Створення фігури за вибором
def create_shape(shape_name):
    if shape_name == 'Tetrahedron':
        shape = Tetrahedron()
    elif shape_name == 'Cube':
        shape = Cube()
    elif shape_name == 'Octahedron':
        shape = Octahedron()
    elif shape_name == 'Dodecahedron':
        shape = Dodecahedron()
    elif shape_name == 'Icosahedron':
        shape = Icosahedron()
    else:
        return None
    shape.create()

    # Робимо об'єкт активним і виділеним
    bpy.context.view_layer.objects.active = shape.obj
    shape.obj.select_set(True)

    return shape.obj


# Панель для взаємодії з користувачем
class PlatonicsPanel(bpy.types.Panel):
    bl_label = "Platonic Solids"
    bl_idname = "OBJECT_PT_platonic_solids"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Platonic Solids'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Кнопка очищення сцени
        layout.operator("object.clear_scene", text="Очистити сцену")

        # Вибір фігури
        layout.label(text="Виберіть Платонове тіло:")
        layout.prop(scene, "platonic_shape", text="")

        # Кнопка для створення фігури
        layout.operator("object.create_platonic", text="Створити фігуру")

        # Кнопка для анімації
        layout.operator("object.animate_rotation", text="Анімація обертання")

        layout.separator()

        # Вибір кольору
        layout.label(text="Матеріал:")
        layout.prop(scene, "platonic_color", text="Колір")
        layout.operator("object.apply_platonic_material", text="Застосувати колір")

# Оператор для очищення сцени
class ClearSceneOperator(bpy.types.Operator):
    bl_idname = "object.clear_scene"
    bl_label = "Очистити сцену"

    def execute(self, context):
        clear_scene()
        return {'FINISHED'}

# Оператор для створення фігури
class CreatePlatonicOperator(bpy.types.Operator):
    bl_idname = "object.create_platonic"
    bl_label = "Створити Платонове тіло"

    def execute(self, context):
        shape_name = context.scene.platonic_shape
        clear_scene()
        create_shape(shape_name)
        return {'FINISHED'}

# Оператор для анімації обертання
class AnimateRotationOperator(bpy.types.Operator):
    bl_idname = "object.animate_rotation"
    bl_label = "Анімація обертання"

    def execute(self, context):
        obj = context.active_object
        if obj:
            animate_rotation(obj, axis='Z', duration=100, rotation_speed=5)
            bpy.ops.screen.animation_play()
        else:
            self.report({'WARNING'}, "Немає активного об'єкта для анімації")
        return {'FINISHED'}

# Оператор для застосування матеріалу
class ApplyMaterialOperator(bpy.types.Operator):
    bl_idname = "object.apply_platonic_material"
    bl_label = "Застосувати матеріал"

    def execute(self, context):
        color = context.scene.platonic_color
        obj = context.active_object
        if obj is None:
            self.report({'WARNING'}, "Немає активного об'єкта для застосування матеріалу")
            return {'CANCELLED'}
        mat = create_material("PlatonicMaterial", (color[0], color[1], color[2], 1.0))
        apply_material(obj, mat)
        return {'FINISHED'}

# Реєстрація класів
classes = [
    PlatonicsPanel,
    ClearSceneOperator,
    CreatePlatonicOperator,
    AnimateRotationOperator,
    ApplyMaterialOperator
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.platonic_shape = bpy.props.EnumProperty(
        name="Platonic Solid",
        description="Виберіть фігуру для створення",
        items=[
            ('Tetrahedron', "Тетраедр", ""),
            ('Cube', "Куб", ""),
            ('Octahedron', "Октаедр", ""),
            ('Dodecahedron', "Додекаедр", ""),
            ('Icosahedron', "Ікосаедр", ""),
        ],
        default='Tetrahedron'
    )

    bpy.types.Scene.platonic_color = bpy.props.FloatVectorProperty(
        name="Колір",
        subtype='COLOR',
        min=0.0, max=1.0,
        default=(0.8, 0.2, 0.2),
        description="Колір матеріалу"
    )

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.platonic_shape
    del bpy.types.Scene.platonic_color

if __name__ == "__main__":
    register()
