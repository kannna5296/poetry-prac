from types import MappingProxyType

class DockerConfig:
    def __init__(self, image, ports=None, env_vars=None, volumes=None):
        self._image = image
        self._ports = tuple(ports or [])  # タプルにして不変にする
        self._env_vars = dict(env_vars or {})  # コピーを作成
        self._volumes = tuple(volumes or [])  # タプルにして不変にする

    error_message = "DockerConfigは不変です。設定を変更することはできません。"

    @property
    def image(self):
        return self._image
    
    @image.setter
    def image(self, value):
        raise AttributeError(self.error_message)

    @property
    def ports(self):
        return self._ports
    
    @ports.setter
    def ports(self, value):
        raise AttributeError("DockerConfigは不変です。設定を変更することはできません。")

    @property
    def env_vars(self):
        return MappingProxyType(self._env_vars)  # 読み取り専用の辞書ビューを返す
    
    @env_vars.setter
    def env_vars(self, value):
        raise AttributeError("DockerConfigは不変です。設定を変更することはできません。")

    @property
    def volumes(self):
        return self._volumes
    
    @volumes.setter
    def volumes(self, value):
        raise AttributeError("DockerConfigは不変です。設定を変更することはできません。")

    def __repr__(self):
        return (f"DockerConfig(image={self._image}, "
                f"ports={self._ports}, "
                f"env_vars={self._env_vars}, "
                f"volumes={self._volumes})")

# お試しビルダーパターン(デザインパターン)
# 
class DockerConfigBuilder:
    def __init__(self):
        self._image = None
        self._ports = []
        self._env_vars = {}
        self._volumes = []

    def image(self, image: str):
        self._image = image
        return self# メソッドチェーン可能

    def port(self, port: str):
        self._ports.append(port)
        return self  

    def env(self, key: str, value: str):
        self._env_vars[key] = value
        return self

    def volume(self, volume: str):
        self._volumes.append(volume)
        return self

    def build(self):
        # DockerConfigは不変にしておく（安全）
        return DockerConfig(
            image=self._image,
            ports=list(self._ports),
            env_vars=dict(self._env_vars),
            volumes=list(self._volumes)
        )
