FROM python:3.11-slim

# 必要なパッケージのインストール
RUN apt-get update \
  && apt-get install -y --no-install-recommends curl git \
  && curl -sSL https://install.python-poetry.org | python3 - --version 1.6.1 \
  && ln -s /root/.local/bin/poetry /usr/local/bin/poetry \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリ
WORKDIR /workspace 