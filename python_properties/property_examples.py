class ExampleClass:
    def __init__(self, value):
        self._value = value
        self._access_count = 0
    
    # 1. @property - 読み取り専用プロパティ
    @property
    def value(self):
        """読み取り専用プロパティ"""
        self._access_count += 1
        return self._value
    
    # 2. @setter - 書き込みプロパティ
    @value.setter
    def value(self, new_value):
        """書き込みプロパティ（バリデーション付き）"""
        if new_value < 0:
            raise ValueError("負の値は設定できません")
        self._value = new_value
    
    # 3. @deleter - 削除プロパティ
    @value.deleter #"del ナンちゃら"が使えるようになる
    def value(self):
        """削除プロパティ"""
        print("値を削除します")
        self._value = None
    
    # 読み取り専用プロパティ（setterなし）
    @property
    def access_count(self):
        """アクセス回数を返す（読み取り専用）"""
        return self._access_count
    
    # 計算プロパティ
    @property
    def doubled_value(self):
        """値を2倍にして返す（計算プロパティ）"""
        return self._value * 2
    
    # 条件付きプロパティ
    @property
    def is_positive(self):
        """値が正の数かどうかを返す"""
        return self._value > 0

# 使用例
def demonstrate_properties():
    print("=== プロパティデコレータの使用例 ===\n")
    
    obj = ExampleClass(10)
    
    # 1. 読み取り
    print(f"初期値: {obj.value}")
    print(f"2倍の値: {obj.doubled_value}")
    print(f"正の数か: {obj.is_positive}")
    print(f"アクセス回数: {obj.access_count}")
    
    # 2. 書き込み
    print(f"\n値を20に変更:")
    obj.value = 20
    print(f"新しい値: {obj.value}")
    print(f"2倍の値: {obj.doubled_value}")
    
    # 3. バリデーションエラー
    print(f"\n負の値を設定しようとすると:")
    try:
        obj.value = -5
    except ValueError as e:
        print(f"エラー: {e}")
    
    # 4. 削除
    print(f"\n値を削除:")
    del obj.value
    print(f"削除後の値: {obj.value}")
    
    # 5. 読み取り専用プロパティの変更を試みる
    print(f"\n読み取り専用プロパティを変更しようとすると:")
    try:
        obj.access_count = 100
    except AttributeError as e:
        print(f"エラー: {e}")

if __name__ == "__main__":
    demonstrate_properties()
