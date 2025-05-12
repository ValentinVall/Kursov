import bpy
import math


def animate_rotation(obj, axis='Z', duration=100, rotation_speed=1):
    """
    Функція для анімації обертання об'єкта навколо заданої осі.

    :param obj: Об'єкт, який потрібно анімувати.
    :param axis: Ось обертання ('X', 'Y', 'Z').
    :param duration: Тривалість анімації (кількість кадрів).
    :param rotation_speed: Швидкість обертання (кількість градусів за кадр).
    """

    # Перевіряємо, чи є об'єкт в сцені
    if obj not in bpy.context.view_layer.objects:
        print(f"Об'єкт {obj.name} не знайдений в сцені.")
        return

    # Видаляємо існуючі анімації
    obj.animation_data_clear()

    # Встановлюємо кадр 0
    bpy.context.scene.frame_set(0)

    # Створюємо анімацію для обертання об'єкта
    if axis == 'X':
        obj.rotation_mode = 'XYZ'
        obj.keyframe_insert(data_path="rotation_euler", index=0, frame=0)
        obj.rotation_euler[0] += math.radians(rotation_speed)
        obj.keyframe_insert(data_path="rotation_euler", index=0, frame=duration)
    elif axis == 'Y':
        obj.rotation_mode = 'XYZ'
        obj.keyframe_insert(data_path="rotation_euler", index=1, frame=0)
        obj.rotation_euler[1] += math.radians(rotation_speed)
        obj.keyframe_insert(data_path="rotation_euler", index=1, frame=duration)
    elif axis == 'Z':
        obj.rotation_mode = 'XYZ'
        obj.keyframe_insert(data_path="rotation_euler", index=2, frame=0)
        obj.rotation_euler[2] += math.radians(rotation_speed)
        obj.keyframe_insert(data_path="rotation_euler", index=2, frame=duration)

    # Встановлюємо тип інтерполяції для плавності
    for fcurve in obj.animation_data.action.fcurves:
        for keyframe in fcurve.keyframe_points:
            keyframe.interpolation = 'LINEAR'

    # Відтворення анімації
    bpy.context.scene.frame_set(0)

    print(f"Анімація обертання для {obj.name} навколо осі {axis} завершена.")
