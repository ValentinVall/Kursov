import bpy

def clear_scene():
    """Видаляє всі об'єкти зі сцени"""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    # Очищення матеріалів
    for material in bpy.data.materials:
        bpy.data.materials.remove(material)

    # Очищення мешів
    for mesh in bpy.data.meshes:
        bpy.data.meshes.remove(mesh)

    # Очищення світла
    for light in bpy.data.lights:
        bpy.data.lights.remove(light)

    # Очищення камер
    for cam in bpy.data.cameras:
        bpy.data.cameras.remove(cam)

def setup_basic_scene():
    """Додає базову камеру та джерело світла"""
    # Камера
    cam_data = bpy.data.cameras.new("Camera")
    cam_obj = bpy.data.objects.new("Camera", cam_data)
    bpy.context.collection.objects.link(cam_obj)
    cam_obj.location = (5, -5, 5)
    cam_obj.rotation_euler = (1.1, 0, 0.9)
    bpy.context.scene.camera = cam_obj

    # Світло
    light_data = bpy.data.lights.new(name="Main_Light", type='POINT')
    light = bpy.data.objects.new(name="Main_Light", object_data=light_data)
    bpy.context.collection.objects.link(light)
    light.location = (4, 4, 4)
