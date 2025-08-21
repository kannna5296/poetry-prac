# 四則演算関数
from docker_config_immutable.docker_config import DockerConfig, DockerConfigBuilder

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


    ###
    #ビルダーパターンで遊ぶ
    ###

    builder = DockerConfigBuilder()
    config : DockerConfig = builder.image("python:3.11-slim").port("8000:8000").env("APP_ENV", "production").volume("/data:/app/data").build()
    
    print("初期設定:")
    print(repr(config))
    
    # 変更を試みる（エラーが発生するはず）
    try:
        config.image = "python:3.11-slim!!!"
        print("変更が成功しました（これは予期しない動作です）")
    except AttributeError as e:
        print(f"変更が拒否されました: {e}")
    
    # 他のプロパティも変更できないことを確認
    try:
        config.ports = ["9000:9000"]
        print("portsの変更が成功しました（これは予期しない動作です）")
    except AttributeError as e:
        print(f"portsの変更が拒否されました: {e}")
    
    try:
        config.env_vars["NEW_VAR"] = "new_value"
        print("env_varsの変更が成功しました（これは予期しない動作です）")
    except (AttributeError, TypeError) as e:
        print(f"env_varsの変更が拒否されました: {e}")
    
    print("\n最終的な設定（変更されていないことを確認）:")
    print(repr(config))
    