# tupleの操作について

def demonstrate_tuple_operations():
    print("=== tupleの操作について ===\n")
    
    # 基本的なtuple
    my_tuple = (1, 2, 3)
    print(f"元のtuple: {my_tuple}")
    
    # 1. addメソッドを試す（エラーが発生）
    print("\n1. addメソッドを試す:")
    try:
        my_tuple.add(4)
        print("addが成功しました（これは予期しない動作です）")
    except AttributeError as e:
        print(f"AttributeError: {e}")
    
    # 2. appendメソッドを試す（エラーが発生）
    print("\n2. appendメソッドを試す:")
    try:
        my_tuple.append(4)
        print("appendが成功しました（これは予期しない動作です）")
    except AttributeError as e:
        print(f"AttributeError: {e}")
    
    # 3. 正しい方法：新しいtupleを作成
    print("\n3. 正しい方法：新しいtupleを作成")
    new_tuple = my_tuple + (4,)
    print(f"元のtuple: {my_tuple}")
    print(f"新しいtuple: {new_tuple}")
    
    # 4. 複数の要素を追加
    print("\n4. 複数の要素を追加:")
    extended_tuple = my_tuple + (4, 5, 6)
    print(f"拡張されたtuple: {extended_tuple}")
    
    # 5. リストからtupleを作成
    print("\n5. リストからtupleを作成:")
    my_list = [1, 2, 3]
    tuple_from_list = tuple(my_list)
    print(f"リスト: {my_list}")
    print(f"tuple: {tuple_from_list}")
    
    # 6. 要素を変更しようとする（エラーが発生）
    print("\n6. 要素を変更しようとする:")
    try:
        my_tuple[0] = 10
        print("変更が成功しました（これは予期しない動作です）")
    except TypeError as e:
        print(f"TypeError: {e}")
    
    # 7. スライスで新しいtupleを作成
    print("\n7. スライスで新しいtupleを作成:")
    sliced_tuple = my_tuple[1:] + (4,)
    print(f"スライス結果: {sliced_tuple}")
    
    # 8. パフォーマンス比較
    print("\n8. パフォーマンス比較:")
    import time
    
    # tupleの連結
    start_time = time.time()
    result_tuple = ()
    for i in range(10000):
        result_tuple = result_tuple + (i,)
    tuple_time = time.time() - start_time
    print(f"tuple連結時間: {tuple_time:.4f}秒")
    
    # リストのappend
    start_time = time.time()
    result_list = []
    for i in range(10000):
        result_list.append(i)
    list_time = time.time() - start_time
    print(f"リストappend時間: {list_time:.4f}秒")
    
    print(f"tupleはリストの {tuple_time/list_time:.1f}倍 遅い")

if __name__ == "__main__":
    demonstrate_tuple_operations()
