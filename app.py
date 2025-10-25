from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from flasgger import Swagger
from routes.demo_routes import demo
from config import Config
from consul_client import register_service
from opentelemetry import trace
from opentelemetry.exporter.zipkin.json import ZipkinExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from asgiref.wsgi import WsgiToAsgi

# === Flask App Setup ===
app = Flask(__name__)
app.config.from_object(Config)

# === Swagger ===
app.config['SWAGGER'] = {
    'title': 'Flask Demo Service',
    'uiversion': 3
}
Swagger(app)

# === Prometheus Metrics ===
metrics = PrometheusMetrics(app)
metrics.info("app_info", "Flask Demo Service", version="1.0.0")

# === Tracing ===
# trace.set_tracer_provider(TracerProvider())
# zipkin_exporter = ZipkinExporter(endpoint=Config.ZIPKIN_ENDPOINT)
# trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(zipkin_exporter))
# tracer = trace.get_tracer(__name__)

# === Health Check ===
@app.route('/health')
def health():
    return jsonify({"status": "UP"}), 200

# === Register Routes ===
app.register_blueprint(demo)

# === Register to Consul on startup ===
with app.app_context():
    register_service()

asgi_app = WsgiToAsgi(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=Config.SERVICE_PORT, debug=True)
