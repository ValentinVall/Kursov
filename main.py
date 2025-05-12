import sys
import os

# Додаємо шлях до кореневої директорії проекту
sys.path.append("C:/Users/Admin/PycharmProjects/Platocin")

import bpy
from geometry import Tetrahedron, Cube, Octahedron, Dodecahedron, Icosahedron
from materials.material_utils import create_material, assign_material
from ui import PlatonPanel
from exporter.export_utils import export_to_obj, export_to_gltf
from utils.scene_cleaner import clear_scene

# Очищення сцени
clear_scene()

# Створення фігур
def create_shapes():
    # Створення фігур Платонових тіл
    tetrahedron = Tetrahedron()

    cube = Cube()
    octahedron = Octahedron()
    dodecahedron = Dodecahedron()
    icosahedron = Icosahedron()

    # Створення матеріалів для кожної фігури
    tetrahedron_material = create_material(name="TetrahedronMat", color=(1.0, 0.3, 0.3, 1.0))
    cube_material = create_material(name="CubeMat", color=(0.2, 0.6, 1.0, 1.0))
    octahedron_material = create_material(name="OctahedronMat", color=(0.3, 1.0, 0.6, 1.0))
    dodecahedron_material = create_material(name="DodecahedronMat", color=(1.0, 0.85, 0.1, 1.0))
    icosahedron_material = create_material(name="IcosahedronMat", color=(0.1, 0.3, 1.0, 1.0))

    # Призначення матеріалів
    assign_material(tetrahedron.obj, tetrahedron_material)
    assign_material(cube.obj, cube_material)
    assign_material(octahedron.obj, octahedron_material)
    assign_material(dodecahedron.obj, dodecahedron_material)
    assign_material(icosahedron.obj, icosahedron_material)

    return [tetrahedron, cube, octahedron, dodecahedron, icosahedron]

# Анімація
def animate_shapes(shapes):
    for shape in shapes:
        shape.animate(axis='Z', frames=150)

# Експорт фігур у файли
def export_shapes(shapes):
    export_to_obj(shapes)
    export_to_gltf(shapes)

# Реєстрація панелі в Blender
def register_ui():
    bpy.utils.register_class(PlatonPanel)

# Реєстрація класів
def register():
    # Реєстрація панелі для Blender
    register_ui()

    # Створення фігур
    shapes = create_shapes()

    # Анімація фігур
    animate_shapes(shapes)

    # Експорт фігур
    export_shapes(shapes)

    print("Все готово! Фігури створені, анімовані та експортовані.")

# Відміна реєстрації
def unregister():
    bpy.utils.unregister_class(PlatonPanel)

if __name__ == "__main__":
    register()
