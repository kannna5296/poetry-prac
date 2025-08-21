# 四則演算関数
from docker_config import DockerConfig, DockerConfigBuilder

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError('0で割ることはできません')
    return a / b

if __name__ == "__main__":
    print("Hello World!")

    builder = DockerConfigBuilder()
    config : DockerConfig = builder.image("python:3.11-slim").port("8000:8000").env("APP_ENV", "production").volume("/data:/app/data").build()
    print(repr(config))
    