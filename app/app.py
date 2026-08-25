from flask import Flask, jsonify, Response, request
from prometheus_client import Counter, generate_latest
app = Flask(__name__)

APP_VERSION = "v99-test"

REQUEST_COUNT = Counter(
    "http_request_total",
    "Total HTTP Requests"
)

@app.route("/")
def home():
    REQUEST_COUNT.inc()

    return jsonify({
        "application":"Zero Downtime Gitops Pipeline v3",
        "version": APP_VERSION,
        "message": "Application is running"
    })

@app.route("/health")
def health():
    REQUEST_COUNT.inc()

    return jsonify({
        "status": "healthy"
    }),200

@app.route("/version")
def version():
    REQUEST_COUNT.inc()

    return jsonify({
        "version": APP_VERSION
    })

@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype="text/plain"
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)