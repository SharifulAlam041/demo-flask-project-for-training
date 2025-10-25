import socket
import consul
from config import Config

def register_service():
    c = consul.Consul(host=Config.CONSUL_HOST, port=Config.CONSUL_PORT)
    service_id = f"{Config.SERVICE_NAME}-{socket.gethostname()}"
    check = consul.Check.http(
        url=f"http://{socket.gethostname()}:{Config.SERVICE_PORT}/health",
        interval="10s",
        timeout="5s",
        deregister="30s"
    )
    c.agent.service.register(
        name=Config.SERVICE_NAME,
        service_id=service_id,
        address=socket.gethostname(),
        port=Config.SERVICE_PORT,
        check=check
    )
    print(f"✅ Registered {Config.SERVICE_NAME} to Consul")
