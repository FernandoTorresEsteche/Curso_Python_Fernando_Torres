from flask import Flask
from login import login_bp

app = Flask(__name__)
app.register_blueprint(login_bp)

if __name__ == '__main__':
    app.run(debug=True)
