import os
import cv2
from flask import Flask, Response, render_template, url_for

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

camera = cv2.VideoCapture(0)

def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/")
def index():
    text = ""
    try:
        return render_template('index.html')
    except:
        text="fail"
    
    secret_key = app.config.get("SECRET_KEY")
    return f"{text}.\nThe configured secret key is {secret_key}."

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)