import bpy


def animate_rotation(obj, axis='Z', frames=120, degrees=360):
    """
    Додає обертання об'єкта навколо заданої осі.

    :param obj: Об'єкт Blender, який буде анімований
    :param axis: 'X', 'Y' або 'Z'
    :param frames: Кількість кадрів для повного оберту
    :param degrees: Кут обертання (за замовчуванням 360)
    """
    axis_index = {'X': 0, 'Y': 1, 'Z': 2}[axis.upper()]

    obj.rotation_euler = (0, 0, 0)
    obj.keyframe_insert(data_path="rotation_euler", frame=1)

    # Встановити кут обертання
    rot = list(obj.rotation_euler)
    rot[axis_index] += degrees * (3.14159265 / 180)  # Градуси → Радіани
    obj.rotation_euler = tuple(rot)
    obj.keyframe_insert(data_path="rotation_euler", frame=frames)

    # Задаємо інтерполяцію "лінійну", щоб було плавно
    action = obj.animation_data.action
    for fcurve in action.fcurves:
        for keyframe in fcurve.keyframe_points:
            keyframe.interpolation = 'LINEAR'
