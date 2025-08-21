# Python プロパティデコレータ完全ガイド

## 概要

Pythonのプロパティデコレータは、クラスの属性アクセスを制御するための強力な機能です。主に3つのデコレータがあります：

1. `@property` - 読み取り専用プロパティ
2. `@setter` - 書き込みプロパティ  
3. `@deleter` - 削除プロパティ

## 1. @property（読み取り専用）

```python
@property
def attribute_name(self):
    return self._private_attribute
```

**特徴：**
- メソッドを属性のようにアクセス可能
- 読み取り専用（setterがない場合）
- 計算プロパティとして使用可能
- バリデーションやログ記録が可能

**使用例：**
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def area(self):
        """面積を計算して返す"""
        return 3.14159 * self._radius ** 2

circle = Circle(5)
print(circle.area)  # 78.53975
```

## 2. @setter（書き込み）

```python
@attribute_name.setter
def attribute_name(self, value):
    # バリデーションや処理
    self._private_attribute = value
```

**特徴：**
- 属性への代入を制御
- バリデーションが可能
- 型変換や前処理が可能
- 副作用（ログ記録など）が可能

**使用例：**
```python
class Temperature:
    def __init__(self):
        self._celsius = 0
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("絶対零度以下は設定できません")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

temp = Temperature()
temp.celsius = 25  # OK
print(temp.fahrenheit)  # 77.0
```

## 3. @deleter（削除）

```python
@attribute_name.deleter
def attribute_name(self):
    # 削除時の処理
    pass
```

**特徴：**
- `del`文での削除を制御
- クリーンアップ処理が可能
- 削除を禁止することも可能

**使用例：**
```python
class Database:
    def __init__(self):
        self._connection = None
    
    @property
    def connection(self):
        return self._connection
    
    @connection.deleter
    def connection(self):
        if self._connection:
            self._connection.close()
            print("データベース接続を閉じました")
        self._connection = None

db = Database()
# ... 接続処理 ...
del db.connection  # 接続を閉じる
```

## 実用的なパターン

### 1. 読み取り専用プロパティ
```python
@property
def id(self):
    return self._id  # setterなし = 読み取り専用
```

### 2. バリデーション付きプロパティ
```python
@property
def age(self):
    return self._age

@age.setter
def age(self, value):
    if not isinstance(value, int):
        raise TypeError("年齢は整数で指定してください")
    if value < 0 or value > 150:
        raise ValueError("年齢は0-150の範囲で指定してください")
    self._age = value
```

### 3. 計算プロパティ
```python
@property
def full_name(self):
    return f"{self._first_name} {self._last_name}"

@property
def is_adult(self):
    return self._age >= 18
```

### 4. 遅延評価（Lazy Loading）
```python
@property
def expensive_data(self):
    if not hasattr(self, '_expensive_data'):
        self._expensive_data = self._load_expensive_data()
    return self._expensive_data
```

## 注意事項

1. **パフォーマンス**: プロパティはメソッド呼び出しなので、頻繁にアクセスする場合は注意
2. **命名規則**: プロパティ名とプライベート属性名は明確に区別する
3. **一貫性**: 同じ属性に対して`@property`、`@setter`、`@deleter`を定義する場合は同じ名前を使用
4. **ドキュメント**: プロパティの動作を明確にドキュメント化する

## 実際の使用場面

- **データベースORM**: フィールドアクセスの制御
- **設定管理**: 設定値のバリデーション
- **API ラッパー**: 外部APIとの連携
- **キャッシュ**: 計算結果のキャッシュ
- **ログ記録**: アクセスログの記録
