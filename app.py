import os

from dotenv import load_dotenv
from flask import Flask, redirect, url_for

from controllers.auth_controller import auth
from controllers.posts_controller import posts
from extensions import bcrypt

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "cambia-esta-clave")
bcrypt.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(posts)


@app.route("/")
def index():
    return redirect(url_for("posts.foro"))


if __name__ == "__main__":
    app.run(debug=True)
