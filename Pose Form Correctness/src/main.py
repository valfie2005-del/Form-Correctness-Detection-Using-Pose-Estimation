import cv2
from pose_detection import detect_pose, mp_pose, mp_drawing
from angle_utils import calculate_angle
from posture_rules import (
    check_bicep_curl,
    check_wrist_alignment,
    check_shoulder_stability
)
from feedback import get_feedback_visuals
input_video = "../data/sample_video.mp4"
output_video = "../output/output_video.mp4"
cap = cv2.VideoCapture(input_video)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(
    output_video,
    fourcc,
    int(cap.get(cv2.CAP_PROP_FPS)),
    (int(cap.get(3)), int(cap.get(4)))
)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = detect_pose(image_rgb)
    feedbacks = []
    if results.pose_landmarks:
        lm = results.pose_landmarks.landmark
        shoulder = [
            lm[mp_pose.PoseLandmark.RIGHT_SHOULDER].x,
            lm[mp_pose.PoseLandmark.RIGHT_SHOULDER].y
        ]
        elbow = [
            lm[mp_pose.PoseLandmark.RIGHT_ELBOW].x,
            lm[mp_pose.PoseLandmark.RIGHT_ELBOW].y
        ]
        wrist = [
            lm[mp_pose.PoseLandmark.RIGHT_WRIST].x,
            lm[mp_pose.PoseLandmark.RIGHT_WRIST].y
        ]

        left_shoulder = [
            lm[mp_pose.PoseLandmark.LEFT_SHOULDER].x,
            lm[mp_pose.PoseLandmark.LEFT_SHOULDER].y
        ]
        right_shoulder = shoulder
        angle = calculate_angle(shoulder, elbow, wrist)
        feedbacks.append(check_bicep_curl(shoulder, elbow, wrist))
        feedbacks.append(check_wrist_alignment(shoulder, wrist))
        feedbacks.append(check_shoulder_stability(left_shoulder, right_shoulder))
        mp_drawing.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS
        )
        elbow_point = (
            int(elbow[0] * frame.shape[1]),
            int(elbow[1] * frame.shape[0])
        )

        cv2.putText(
            frame,
            f"Angle: {int(angle)}",
            elbow_point,
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )

    else:
        feedbacks.append(("No person detected", False))
    y = 40
    for msg, status in feedbacks:
        color = get_feedback_visuals(status)
        cv2.putText(
            frame,
            msg,
            (30, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            color,
            2
        )
        y += 35

    out.write(frame)
    cv2.imshow("Exercise Form Check", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()

