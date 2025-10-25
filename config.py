from decouple import config

class Config:
    SERVICE_NAME = config("SERVICE_NAME", default="flask-demo")
    SERVICE_PORT = config("SERVICE_PORT", default=8889, cast=int)
    CONSUL_HOST = config("CONSUL_HOST", default="localhost")
    CONSUL_PORT = config("CONSUL_PORT", default=8500, cast=int)
    #ZIPKIN_ENDPOINT = config("ZIPKIN_ENDPOINT", default="http://localhost:9411/api/v2/spans")
