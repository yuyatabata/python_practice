# 配列が空かどうか、if文でチェック
def check_items(items):
    if items:
        return items[0]
    else:
        return None

print(check_items([]))
print(check_items(['book']))

# not in の動作確認
items =['books','python']
print('book' not in items)

# 三項演算子
a = 1
result = "even" if a % 2 ==0 else 'odd'
print(result)
a = 6
result = 'even' if a % 2 ==0 else 'odd'
print(result)

# リスト内包表記と三項演算子
l = ['even' if i % 2 else i for i in range(10)]