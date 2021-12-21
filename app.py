import os
from flask import Flask

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route("/")
def index():
    text = ''
    try:
        import cv2
        text = 'success' 
    except:
        text = 'fail'
        pass
    secret_key = app.config.get("SECRET_KEY")
    return f"{text}.\nThe configured secret key is {secret_key}."

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)