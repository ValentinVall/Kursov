import bpy

def create_material(name="Material", color=(1.0, 0.5, 0.5, 1.0), metallic=0.0, roughness=0.5):
    """
    Створює матеріал із заданим кольором, металічністю та шорсткістю.
    Повертає об'єкт матеріалу.
    """
    if name in bpy.data.materials:
        mat = bpy.data.materials[name]
    else:
        mat = bpy.data.materials.new(name=name)

    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    # Очистимо всі вузли, щоб уникнути конфліктів
    for node in nodes:
        nodes.remove(node)

    # Додаємо новий Principled BSDF
    output_node = nodes.new(type='ShaderNodeOutputMaterial')
    bsdf_node = nodes.new(type='ShaderNodeBsdfPrincipled')

    # Встановлюємо властивості
    bsdf_node.inputs['Base Color'].default_value = color
    bsdf_node.inputs['Metallic'].default_value = metallic
    bsdf_node.inputs['Roughness'].default_value = roughness

    # Зв'язуємо BSDF з виходом
    links.new(bsdf_node.outputs['BSDF'], output_node.inputs['Surface'])

    return mat


def assign_material(obj, material):
    """
    Призначає матеріал об'єкту.
    """
    if obj.data.materials:
        obj.data.materials[0] = material
    else:
        obj.data.materials.append(material)
