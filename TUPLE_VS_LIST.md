# Python tuple vs list 完全比較

## 概要

Pythonのtupleとlistは似たような使い方ができますが、重要な違いがあります：

- **tuple**: 不変（immutable）なシーケンス
- **list**: 可変（mutable）なシーケンス

## 1. 基本的な違い

### tuple（不変）
```python
my_tuple = (1, 2, 3)
# 以下はすべてエラー
my_tuple.add(4)        # AttributeError
my_tuple.append(4)     # AttributeError
my_tuple[0] = 10       # TypeError
```

### list（可変）
```python
my_list = [1, 2, 3]
# 以下はすべて成功
my_list.append(4)      # [1, 2, 3, 4]
my_list[0] = 10        # [10, 2, 3, 4]
my_list.extend([5, 6]) # [10, 2, 3, 4, 5, 6]
```

## 2. 要素の追加方法

### tupleの場合
```python
# 正しい方法：新しいtupleを作成
original = (1, 2, 3)
new_tuple = original + (4,)           # (1, 2, 3, 4)
extended = original + (4, 5, 6)       # (1, 2, 3, 4, 5, 6)

# 間違った方法（エラー）
original.add(4)        # AttributeError
original.append(4)     # AttributeError
```

### listの場合
```python
# 正しい方法
my_list = [1, 2, 3]
my_list.append(4)      # [1, 2, 3, 4]
my_list.extend([5, 6]) # [1, 2, 3, 4, 5, 6]
my_list += [7, 8]      # [1, 2, 3, 4, 5, 6, 7, 8]
```

## 3. パフォーマンス比較

### 要素追加のパフォーマンス
```python
import time

# tuple連結（遅い）
start = time.time()
result = ()
for i in range(10000):
    result = result + (i,)
tuple_time = time.time() - start

# list append（速い）
start = time.time()
result = []
for i in range(10000):
    result.append(i)
list_time = time.time() - start

print(f"tuple: {tuple_time:.4f}秒")
print(f"list:  {list_time:.4f}秒")
# 結果: tupleはlistの数百倍遅い
```

### 理由
- **tuple**: 毎回新しいオブジェクトを作成
- **list**: 既存のオブジェクトを拡張

## 4. 使用場面の使い分け

### tupleを使うべき場面

1. **辞書のキー**
```python
# tupleは辞書のキーに使える
coordinates = {(1, 2): "point A", (3, 4): "point B"}

# listは辞書のキーに使えない
# coordinates = {[1, 2]: "point A"}  # TypeError
```

2. **関数の戻り値**
```python
def get_coordinates():
    return (x, y)  # 複数の値を返す
```

3. **データの整合性を保ちたい場合**
```python
# 座標データ
point = (10, 20)
# 後から変更される心配がない
```

4. **メモリ効率**
```python
# tupleはlistよりメモリ効率が良い
import sys
print(sys.getsizeof((1, 2, 3)))  # 48 bytes
print(sys.getsizeof([1, 2, 3]))  # 80 bytes
```

### listを使うべき場面

1. **頻繁に要素を追加・削除する場合**
```python
items = []
for item in data:
    items.append(process(item))
```

2. **データの変更が必要な場合**
```python
scores = [85, 92, 78]
scores[1] = 95  # 変更可能
```

3. **スタックやキューとして使用**
```python
stack = []
stack.append(1)  # push
stack.pop()      # pop
```

## 5. 変換方法

### list → tuple
```python
my_list = [1, 2, 3]
my_tuple = tuple(my_list)  # (1, 2, 3)
```

### tuple → list
```python
my_tuple = (1, 2, 3)
my_list = list(my_tuple)   # [1, 2, 3]
```

## 6. 実用的なテクニック

### tupleの効率的な連結
```python
# 非効率
result = ()
for i in range(1000):
    result = result + (i,)

# 効率的
items = []
for i in range(1000):
    items.append(i)
result = tuple(items)
```

### 複数の値を一度に返す
```python
def get_person_info():
    return ("John", 30, "Engineer")

name, age, job = get_person_info()
```

## まとめ

| 特徴 | tuple | list |
|------|-------|------|
| 可変性 | 不変 | 可変 |
| パフォーマンス | 遅い（連結時） | 速い |
| メモリ使用量 | 少ない | 多い |
| 辞書のキー | 可能 | 不可能 |
| 要素追加 | 新しいオブジェクト作成 | 既存オブジェクト拡張 |

**選択の指針：**
- データが変更されない → **tuple**
- データが頻繁に変更される → **list**
- 辞書のキーとして使用 → **tuple**
- パフォーマンスが重要 → **list**
