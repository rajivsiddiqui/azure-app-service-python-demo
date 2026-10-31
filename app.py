
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>DevOps Steps</title>
    </head>
    <body style="text-align:center; font-family:Arial;">
        <h1>Welcome to DevOps Steps!</h1>
        <h2>Azure App Service Demo4</h2>
        <p>My Python application is running on Azure.</p>
        <p>Deployment: Successful!</p>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}


@app.route("/config")
def config():
    environment = os.environ.get("APP_ENV", "Development")

    return {
        "environment": environment
    }


if __name__ == "__main__":
    app.run()

