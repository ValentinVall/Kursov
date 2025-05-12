# geometry/base_shape.py

import bpy
from abc import ABC, abstractmethod


class PlatonShape(ABC):
    def __init__(self, name: str, location=(0, 0, 0)):
        self.name = name
        self.location = location
        self.obj = None  # Об'єкт Blender, який буде створено

    @abstractmethod
    def create_mesh(self):
        """Абстрактний метод для створення геометрії"""
        pass

    def place_object(self):
        """Додає об'єкт на сцену"""
        if self.obj:
            self.obj.location = self.location
            self.obj.name = self.name
        else:
            raise ValueError("Object has not been created yet!")

    def delete_if_exists(self):
        """Видаляє об'єкт із тією ж назвою, якщо вже існує в сцені"""
        old_obj = bpy.data.objects.get(self.name)
        if old_obj:
            bpy.data.objects.remove(old_obj, do_unlink=True)

    def build(self):
        """Шаблонний метод, який керує створенням"""
        self.delete_if_exists()
        self.create_mesh()
        self.place_object()
