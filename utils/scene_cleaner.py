# utils/scene_cleaner.py

import bpy

def clear_scene():
    """
    Очищає всю поточну сцену в Blender: видаляє всі об'єкти, камери, лампи та інші елементи.
    """
    bpy.ops.object.select_all(action='SELECT')  # Вибираємо всі об'єкти на сцені
    bpy.ops.object.delete()  # Видаляємо вибрані об'єкти

    # Додатково можна додати очищення інших елементів сцени, таких як камери, світла
    for obj in bpy.data.objects:
        if obj.type in {'MESH', 'CAMERA', 'LIGHT'}:  # Перевірка на типи об'єктів
            bpy.data.objects.remove(obj, do_unlink=True)

    # Очищення матеріалів, текстур, шейдерів, якщо потрібно
    for material in bpy.data.materials:
        bpy.data.materials.remove(material)

    for texture in bpy.data.textures:
        bpy.data.textures.remove(texture)

    for image in bpy.data.images:
        bpy.data.images.remove(image)
