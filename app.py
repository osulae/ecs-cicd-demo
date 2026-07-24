from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Amazon ECS CI/CD Pipeline Successful!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
