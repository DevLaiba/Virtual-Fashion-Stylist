import cv2
import os

MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")

AGE_MODEL = cv2.dnn.readNetFromCaffe(
    os.path.join(MODEL_DIR, "age_deploy.prototxt"),
    os.path.join(MODEL_DIR, "age_net.caffemodel")
)

GENDER_MODEL = cv2.dnn.readNetFromCaffe(
    os.path.join(MODEL_DIR, "gender_deploy.prototxt"),
    os.path.join(MODEL_DIR, "gender_net.caffemodel")
)

AGE_LIST = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
GENDER_LIST = ['Male', 'Female']

def detect_age_gender(image_path):
    # Bypass model for now due to caffemodel errors
    return "(3-5)", "male"
# def detect_age_gender(image_path):
#     image = cv2.imread(image_path)
#     blob = cv2.dnn.blobFromImage(image, 1.0, (227, 227),
#                                  (78.426337, 87.768914, 114.895847), swapRB=False)

#     GENDER_MODEL.setInput(blob)
#     gender_preds = GENDER_MODEL.forward()
#     gender = GENDER_LIST[gender_preds[0].argmax()]

#     AGE_MODEL.setInput(blob)
#     age_preds = AGE_MODEL.forward()
#     age = AGE_LIST[age_preds[0].argmax()]

#     return age, gender

def estimate_measurements(image_path):
    image = cv2.imread(image_path)
    height_px = image.shape[0]
    width_px = image.shape[1]

    base_height_cm = 100
    scale = base_height_cm / height_px

    shoulder_width = int(width_px * 0.35)
    hip_width = int(width_px * 0.5)

    return {
        "height_cm": base_height_cm,
        "shoulder_width_cm": round(shoulder_width * scale),
        "hips_cm": round(hip_width * scale),
        "chest_cm": round(shoulder_width * scale * 1.1),
        "waist_cm": round(((shoulder_width + hip_width) / 2) * scale * 0.9),
        "inseam_cm": round(base_height_cm * 0.45)
    }
