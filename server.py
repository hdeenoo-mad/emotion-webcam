from flask import Flask, request, jsonify, send_from_directory
import cv2
import numpy as np
from deepface import DeepFace
import base64

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

def to_serializable(obj):
    """Convertit numpy types -> python natifs pour JSON"""
    if isinstance(obj, (np.float32, np.float64)):
        return float(obj)
    if isinstance(obj, (np.int32, np.int64)):
        return int(obj)
    return str(obj)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json["image"]

    # Décoder base64 -> image OpenCV
    img_data = base64.b64decode(data.split(",")[1])
    np_arr = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    try:
        result = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)
        if isinstance(result, list):
            result = result[0]

        # Nettoyer les valeurs numpy
        clean_result = {k: to_serializable(v) if not isinstance(v, dict) else {kk: to_serializable(vv) for kk, vv in v.items()} for k, v in result.items()}

        return jsonify(clean_result)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
