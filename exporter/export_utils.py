import bpy

# Експортуємо 3D-моделі у формат .obj
def export_to_obj(shapes):
    for shape in shapes:
        file_path = f"{shape.name}.obj"  # Шлях для збереження файлу .obj
        bpy.ops.export_scene.obj(filepath=file_path)
        print(f"Експортовано {shape.name} у {file_path}")

# Експортуємо 3D-моделі у формат .gltf
def export_to_gltf(shapes):
    for shape in shapes:
        file_path = f"{shape.name}.gltf"  # Шлях для збереження файлу .gltf
        bpy.ops.export_scene.gltf(filepath=file_path)
        print(f"Експортовано {shape.name} у {file_path}")
