# Python tuple vs list 比較

このフォルダには、Pythonのtupleとlistの違い、特に不変性とパフォーマンスに関するファイルが含まれています。

## ファイル一覧

- `tuple_operations.py` - tupleの操作とlistとの比較デモンストレーション
- `TUPLE_VS_LIST.md` - tupleとlistの詳細な比較と使い分けガイド

## 実行方法

```bash
cd tuple_list_comparison
python tuple_operations.py
```

## 学習内容

- tupleの不変性（immutable）
- listの可変性（mutable）
- 要素追加のパフォーマンス比較
- 使用場面の使い分け
- 辞書のキーとしての使用
- メモリ効率の違い

## 重要な発見

- tupleに`add()`メソッドは存在しない
- tuple連結はlistのappendより数百倍遅い
- tupleは辞書のキーとして使用可能
- tupleはメモリ効率が良い
