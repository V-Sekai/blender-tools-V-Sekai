# MIT LICENSE
# Modified by iFire#6518 (Discord name)
# from https://blender.stackexchange.com/a/75049/33589

import bpy
import mathutils
from mathutils import Vector
from math import *


def CreateMesh(meshType):

    obj = bpy.context.active_object

    if obj == None:
        self.report({"ERROR"}, "No selection")
    elif obj.type != "ARMATURE":
        self.report({"ERROR"}, "Armature expected")
    else:
        processArmature(bpy.context, obj, meshType=meshType)


# Create the base object from the armature
def meshFromArmature(arm):
    name = arm.name + "_mesh"
    meshData = bpy.data.meshes.new(name + "Data")
    meshObj = bpy.data.objects.new(name, meshData)
    meshObj.matrix_world = arm.matrix_world.copy()
    return meshObj


# Create the bone geometry (vertices and faces)
def boneGeometry(l1, l2, x, z, baseSize, l1Size, l2Size, base, meshType):

    if meshType == "Tapered":
        print(meshType)
        x1 = x * baseSize * l1Size
        z1 = z * baseSize * l1Size

        x2 = x * baseSize * l2Size
        z2 = z * baseSize * l2Size
    elif meshType == "Box":
        print(meshType)
        lSize = (l1Size + l2Size) / 2
        x1 = x * baseSize * lSize
        z1 = z * baseSize * lSize

        x2 = x * baseSize * lSize
        z2 = z * baseSize * lSize

    else:  # default to Pyramid
        print(meshType)
        x1 = x * baseSize * l1Size
        z1 = z * baseSize * l1Size

        x2 = Vector((0, 0, 0))
        z2 = Vector((0, 0, 0))

    verts = [
        l1 - x1 + z1,
        l1 + x1 + z1,
        l1 - x1 - z1,
        l1 + x1 - z1,
        l2 - x2 + z2,
        l2 + x2 + z2,
        l2 - x2 - z2,
        l2 + x2 - z2,
    ]

    faces = [
        (base + 3, base + 1, base + 0, base + 2),
        (base + 6, base + 4, base + 5, base + 7),
        (base + 4, base + 0, base + 1, base + 5),
        (base + 7, base + 3, base + 2, base + 6),
        (base + 5, base + 1, base + 3, base + 7),
        (base + 6, base + 2, base + 0, base + 4),
    ]

    return verts, faces


# Process the armature, goes through its bones and creates the mesh
def processArmature(context, arm, genVertexGroups=True, meshType="Pyramid"):
    print("processing armature {0} {1}".format(arm.name, meshType))

    # Creates the mesh object
    meshObj = meshFromArmature(arm)
    context.collection.objects.link(meshObj)

    verts = []
    edges = []
    faces = []
    vertexGroups = {}

    bpy.ops.object.mode_set(mode="EDIT")

    try:
        # Goes through each bone
        for editBone in [b for b in arm.data.edit_bones if b.use_deform]:
            boneName = editBone.name
            # print( boneName )
            poseBone = arm.pose.bones[boneName]

            # Gets edit bone informations
            editBoneHead = editBone.head
            editBoneTail = editBone.tail
            editBoneVector = editBoneTail - editBoneHead
            editBoneSize = editBoneVector.dot(editBoneVector)
            editBoneRoll = editBone.roll
            editBoneX = editBone.x_axis
            editBoneZ = editBone.z_axis
            editBoneHeadRadius = editBone.head_radius
            editBoneTailRadius = editBone.tail_radius

            # Creates the mesh data for the bone
            baseIndex = len(verts)
            baseSize = sqrt(editBoneSize)
            newVerts, newFaces = boneGeometry(
                editBoneHead,
                editBoneTail,
                editBoneX,
                editBoneZ,
                baseSize,
                editBoneHeadRadius,
                editBoneTailRadius,
                baseIndex,
                meshType,
            )

            verts.extend(newVerts)
            faces.extend(newFaces)

            # Creates the weights for the vertex groups
            vertexGroups[boneName] = [(x, 1.0) for x in range(baseIndex, len(verts))]

        # Assigns the geometry to the mesh
        meshObj.data.from_pydata(verts, edges, faces)

    except:
        bpy.ops.object.mode_set(mode="OBJECT")
    else:
        bpy.ops.object.mode_set(mode="OBJECT")

    # Assigns the vertex groups
    if genVertexGroups:
        for name, vertexGroup in vertexGroups.items():
            groupObject = meshObj.vertex_groups.new(name=name)
            for (index, weight) in vertexGroup:
                groupObject.add([index], weight, "REPLACE")

    # Creates the armature modifier
    modifier = meshObj.modifiers.new("ArmatureMod", "ARMATURE")
    modifier.object = arm
    modifier.use_bone_envelopes = False
    modifier.use_vertex_groups = True

    meshObj.data.update()

    return meshObj


class MeshFromArmatureOperator(bpy.types.Operator):
    bl_idname = "wm.mesh_from_armature"
    bl_label = "MeshFromArmatureOperator"

    mesh_type: bpy.props.StringProperty(name="mesh_type")

    def execute(self, context):
        print("The mesh type is", self.mesh_type)
        CreateMesh(self, self.mesh_type)
        return {"FINISHED"}


if __name__ == "__main__":
    CreateMesh("Tapered")
