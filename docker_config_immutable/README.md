# DockerConfig 不変性（Immutability）

このフォルダには、DockerConfigクラスを不変（immutable）にする実装に関するファイルが含まれています。

## ファイル一覧

- `docker_config.py` - 不変なDockerConfigクラスの実装
- `IMMUTABLE_CONFIG.md` - 不変性の実装方法とメリットの説明

## 実行方法

```bash
cd docker_config_immutable
# main.pyからimportして使用
```

## 学習内容

- 不変オブジェクトの設計
- プロパティデコレータを使用したアクセス制御
- プライベート属性の使用
- 不変なデータ構造（tuple、MappingProxyType）
- ビルダーパターンとの組み合わせ

## 実装のポイント

- `@property`で読み取り専用アクセス
- `@setter`で変更を拒否
- 内部属性は`_`で始まるプライベート属性
- `tuple`と`MappingProxyType`で不変性を確保
- エラーメッセージの統一

## メリット

- 設定の安全性確保
- 予測可能な動作
- スレッドセーフ
- デバッグのしやすさ
