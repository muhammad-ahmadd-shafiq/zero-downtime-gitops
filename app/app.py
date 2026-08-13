from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = "v3.0.0"

@app.route("/")
def home():
    return jsonify({
        "application":"Zero Downtime Gitops Pipeline v3",
        "version": APP_VERSION,
        "message": "Application is running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }),200

@app.route("/version")
def version():
    return jsonify({
        "version": APP_VERSION
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)