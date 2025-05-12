import bpy


class PlatonShape:
    def __init__(self, name="PlatonShape"):
        self.name = name
        self.obj = None  # Змінна для зберігання об'єкта Blender

    def create_mesh(self):
        """Метод для створення 3D-моделі (місце для переозначення в дочірніх класах)."""
        raise NotImplementedError("Цей метод має бути реалізований у дочірніх класах.")

    def set_material(self, material):
        """Призначення матеріалу об'єкту."""
        if self.obj:
            if material:
                self.obj.data.materials.append(material)
            else:
                print(f"Матеріал не знайдений для {self.name}")
        else:
            print(f"{self.name} ще не створено")

    def animate(self, axis='Z', frames=100, rotation_angle=360):
        """Анімація обертання об'єкта по заданій осі."""
        if not self.obj:
            print(f"{self.name} ще не створено.")
            return

        if axis not in ['X', 'Y', 'Z']:
            print(f"Невірна вісь: {axis}. Має бути X, Y, або Z.")
            return

        # Анімація обертання
        self.obj.rotation_mode = 'XYZ'
        self.obj.rotation_euler = (0, 0, 0)
        self.obj.keyframe_insert(data_path="rotation_euler", frame=0)

        rotation = {
            'X': (rotation_angle, 0, 0),
            'Y': (0, rotation_angle, 0),
            'Z': (0, 0, rotation_angle)
        }

        self.obj.rotation_euler = rotation[axis]
        self.obj.keyframe_insert(data_path="rotation_euler", frame=frames)

    def move(self, location=(0, 0, 0)):
        """Переміщення об'єкта в задану точку."""
        if self.obj:
            self.obj.location = location
        else:
            print(f"{self.name} ще не створено")

    def scale(self, scale=(1, 1, 1)):
        """Масштабування об'єкта."""
        if self.obj:
            self.obj.scale = scale
        else:
            print(f"{self.name} ще не створено")
