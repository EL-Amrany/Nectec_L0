# run.py
from flask import Flask
# if you keep routes in routes.py:
# from routes import bp as routes_bp

app = Flask(__name__)
# app.register_blueprint(routes_bp)

@app.route("/")
def home():
    return "OK from Flask on Vercel"

if __name__ == "__main__":
    # This should NOT execute on Vercel import
    app.run()

