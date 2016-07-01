"""
=====================
Transformation Editor
=====================

The transformation editor can be used to manipulate transformations.
"""
from pytransform.transform_manager import TransformManager
from pytransform.editor import TransformationEditor
from pytransform.transformations import transform_from
from pytransform.rotations import matrix_from_euler_xyz


tm = TransformManager()

tm.add_transform(
    "tree", "world",
    transform_from(
        matrix_from_euler_xyz([0, 0.5, 0]),
        [0, 0, 0.5]
    )
)
tm.add_transform(
    "car", "world",
    transform_from(
        matrix_from_euler_xyz([0.5, 0, 0]),
        [0.5, 0, 0]
    )
)

te = TransformationEditor(tm, "world")
te.show()
print("tree to world:")
print(te.transform_manager.get_transform("tree", "world"))
