# DockerConfig の不変性（Immutability）

## 概要

`DockerConfig`クラスは、一度作成されたら後から変更できない不変（immutable）なオブジェクトとして設計されています。

## 実装方法

### 1. プライベート属性
- すべての設定値は`_`で始まるプライベート属性として保存
- 直接アクセスを防ぐ

### 2. プロパティデコレータ
- `@property`を使用して読み取り専用アクセスを提供
- `@setter`で変更を試みた場合に`AttributeError`を発生

### 3. 不変なデータ構造
- `ports`と`volumes`: `tuple`を使用（不変なリスト）
- `env_vars`: `MappingProxyType`を使用（読み取り専用の辞書ビュー）

## 使用例

```python
# 正しい使用方法
builder = DockerConfigBuilder()
config = builder.image("python:3.11-slim").port("8000:8000").build()

# 読み取りは可能
print(config.image)  # "python:3.11-slim"
print(config.ports)  # ('8000:8000',)

# 変更は不可能（エラーが発生）
try:
    config.image = "python:3.12-slim"
except AttributeError as e:
    print(e)  # "DockerConfigは不変です。設定を変更することはできません。"
```

## メリット

1. **安全性**: 設定が意図せず変更されることを防ぐ
2. **予測可能性**: オブジェクトの状態が常に一定
3. **スレッドセーフ**: 複数のスレッドから同時アクセスしても安全
4. **デバッグのしやすさ**: 問題の原因を特定しやすい

## 注意事項

- 一度作成した設定を変更したい場合は、新しい`DockerConfig`オブジェクトを作成する必要があります
- ビルダーパターンを使用して、必要な設定をすべて指定してから`build()`を呼び出してください
