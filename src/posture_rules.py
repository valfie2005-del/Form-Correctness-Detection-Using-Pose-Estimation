from angle_utils import calculate_angle
def check_bicep_curl(shoulder, elbow, wrist):
    angle = calculate_angle(shoulder, elbow, wrist)
    if angle < 40:
        return "Over-flexed arm", False
    elif angle > 160:
        return "Incomplete curl", False
    else:
        return "Correct bicep curl", True
def check_wrist_alignment(shoulder, wrist):
    if abs(wrist[1] - shoulder[1]) < 0.1:
        return "Good wrist alignment", True
    else:
        return "Wrist not aligned with shoulder", False
def check_shoulder_stability(left_shoulder, right_shoulder):
    if abs(left_shoulder[1] - right_shoulder[1]) < 0.05:
        return "Stable posture", True
    else:
        return "Leaning posture detected", False
