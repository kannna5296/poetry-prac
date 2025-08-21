class DockerConfig:
    def __init__(self, image, ports=None, env_vars=None, volumes=None):
        self.image = image
        self.ports = ports or []
        self.env_vars = env_vars or {}
        self.volumes = volumes or []

    def __repr__(self):
        return (f"DockerConfig(image={self.image}, "
                f"ports={self.ports}, "
                f"env_vars={self.env_vars}, "
                f"volumes={self.volumes})")

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
            image=self.image,
            ports=list(self._ports),
            env_vars=dict(self._env_vars),
            volumes=list(self._volumes)
        )
