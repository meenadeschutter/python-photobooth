import os
from flask import Flask

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route("/")
def index():
    import cv2
    vid = cv2.VideoCapture(0)

    while True:
        ret, frame = vid.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()
    secret_key = app.config.get("SECRET_KEY")
    return f"{text}.\nThe configured secret key is {secret_key}."

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)