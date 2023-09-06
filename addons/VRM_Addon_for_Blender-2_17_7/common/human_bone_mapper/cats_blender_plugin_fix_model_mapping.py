from ..vrm1.human_bone import HumanBoneSpecification, HumanBoneSpecifications

mapping: dict[str, HumanBoneSpecification] = {
    "Hips": HumanBoneSpecifications.HIPS,
    "Spine": HumanBoneSpecifications.SPINE,
    "Chest": HumanBoneSpecifications.CHEST,
    "Neck": HumanBoneSpecifications.NECK,
    "Head": HumanBoneSpecifications.HEAD,
    "Eye_R": HumanBoneSpecifications.RIGHT_EYE,
    "Eye_L": HumanBoneSpecifications.LEFT_EYE,
    "Right shoulder": HumanBoneSpecifications.RIGHT_SHOULDER,
    "Right arm": HumanBoneSpecifications.RIGHT_UPPER_ARM,
    "Right elbow": HumanBoneSpecifications.RIGHT_LOWER_ARM,
    "Right wrist": HumanBoneSpecifications.RIGHT_HAND,
    "Left shoulder": HumanBoneSpecifications.LEFT_SHOULDER,
    "Left arm": HumanBoneSpecifications.LEFT_UPPER_ARM,
    "Left elbow": HumanBoneSpecifications.LEFT_LOWER_ARM,
    "Left wrist": HumanBoneSpecifications.LEFT_HAND,
    "Right leg": HumanBoneSpecifications.RIGHT_UPPER_LEG,
    "Right knee": HumanBoneSpecifications.RIGHT_LOWER_LEG,
    "Right ankle": HumanBoneSpecifications.RIGHT_FOOT,
    "Right toe": HumanBoneSpecifications.RIGHT_TOES,
    "Left leg": HumanBoneSpecifications.LEFT_UPPER_LEG,
    "Left knee": HumanBoneSpecifications.LEFT_LOWER_LEG,
    "Left ankle": HumanBoneSpecifications.LEFT_FOOT,
    "Left toe": HumanBoneSpecifications.LEFT_TOES,
    "Thumb0_R": HumanBoneSpecifications.RIGHT_THUMB_METACARPAL,
    "Thumb1_R": HumanBoneSpecifications.RIGHT_THUMB_PROXIMAL,
    "Thumb2_R": HumanBoneSpecifications.RIGHT_THUMB_DISTAL,
    "Thumb0_L": HumanBoneSpecifications.LEFT_THUMB_METACARPAL,
    "Thumb1_L": HumanBoneSpecifications.LEFT_THUMB_PROXIMAL,
    "Thumb2_L": HumanBoneSpecifications.LEFT_THUMB_DISTAL,
    "IndexFinger1_R": HumanBoneSpecifications.RIGHT_INDEX_PROXIMAL,
    "IndexFinger2_R": HumanBoneSpecifications.RIGHT_INDEX_INTERMEDIATE,
    "IndexFinger3_R": HumanBoneSpecifications.RIGHT_INDEX_DISTAL,
    "IndexFinger1_L": HumanBoneSpecifications.LEFT_INDEX_PROXIMAL,
    "IndexFinger2_L": HumanBoneSpecifications.LEFT_INDEX_INTERMEDIATE,
    "IndexFinger3_L": HumanBoneSpecifications.LEFT_INDEX_DISTAL,
    "MiddleFinger1_R": HumanBoneSpecifications.RIGHT_MIDDLE_PROXIMAL,
    "MiddleFinger2_R": HumanBoneSpecifications.RIGHT_MIDDLE_INTERMEDIATE,
    "MiddleFinger3_R": HumanBoneSpecifications.RIGHT_MIDDLE_DISTAL,
    "MiddleFinger1_L": HumanBoneSpecifications.LEFT_MIDDLE_PROXIMAL,
    "MiddleFinger2_L": HumanBoneSpecifications.LEFT_MIDDLE_INTERMEDIATE,
    "MiddleFinger3_L": HumanBoneSpecifications.LEFT_MIDDLE_DISTAL,
    "RingFinger1_R": HumanBoneSpecifications.RIGHT_RING_PROXIMAL,
    "RingFinger2_R": HumanBoneSpecifications.RIGHT_RING_INTERMEDIATE,
    "RingFinger3_R": HumanBoneSpecifications.RIGHT_RING_DISTAL,
    "RingFinger1_L": HumanBoneSpecifications.LEFT_RING_PROXIMAL,
    "RingFinger2_L": HumanBoneSpecifications.LEFT_RING_INTERMEDIATE,
    "RingFinger3_L": HumanBoneSpecifications.LEFT_RING_DISTAL,
    "LittleFinger1_R": HumanBoneSpecifications.RIGHT_LITTLE_PROXIMAL,
    "LittleFinger2_R": HumanBoneSpecifications.RIGHT_LITTLE_INTERMEDIATE,
    "LittleFinger3_R": HumanBoneSpecifications.RIGHT_LITTLE_DISTAL,
    "LittleFinger1_L": HumanBoneSpecifications.LEFT_LITTLE_PROXIMAL,
    "LittleFinger2_L": HumanBoneSpecifications.LEFT_LITTLE_INTERMEDIATE,
    "LittleFinger3_L": HumanBoneSpecifications.LEFT_LITTLE_DISTAL,
}

config = ("Cats Blender Plugin Fixed Model", mapping)