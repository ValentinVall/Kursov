import bpy
import os

def export_active_object_to_obj(filepath=None):
    obj = bpy.context.active_object
    if not obj:
        print("Немає активного об'єкта для експорту.")
        return

    if not filepath:
        desktop = os.path.expanduser("~/Desktop")
        filepath = os.path.join(desktop, f"{obj.name}.obj")

    bpy.ops.export_scene.obj(
        filepath=filepath,
        use_selection=True,
        use_materials=True
    )
    print(f"Об'єкт експортовано у .obj: {filepath}")


def export_active_object_to_gltf(filepath=None):
    obj = bpy.context.active_object
    if not obj:
        print("Немає активного об'єкта для експорту.")
        return

    if not filepath:
        desktop = os.path.expanduser("~/Desktop")
        filepath = os.path.join(desktop, f"{obj.name}.glb")

    bpy.ops.export_scene.gltf(
        filepath=filepath,
        export_selected=True,
        export_format='GLB',
        export_apply=True
    )
    print(f"Об'єкт експортовано у .glb: {filepath}")
