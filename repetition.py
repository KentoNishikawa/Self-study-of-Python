# for 変数 in シーケンス:
#     処理
#     で成立
lst = [1, 2, 3, 4, 5, 6]
for r in lst:
    print(r)

# 上記はlstの値を繰り返し表示
lst = [1, 2, 3, 4, 5, 6]
for r in lst:
    print(r*r)

# 整数のシーケンスを作成するために使用
for i in range(100, 130, 2):
    print(i)
# for i in range(開始値,終了値,ステップ値):

# 条件分岐と嚙合わせることも可能
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for result in num:
    if result % 2 == 0:
        print(result)

# 上記コードのwhile文
i = 1
num = 0
while num < 10:
    num += i
    if num % 2 == 0:
        print (num)

# helloを5かい繰り返す
#  range 関数は、与えられた範囲内の整数を返すイテレータを生成するのに使用
# for 〇 in range(△):で下記の処理を△回行う
for w in range(5):
    print (w)

# FizzBuzz問題
for nums in range(1, 30):
    if nums % 3 == 0 and nums % 5 == 0:
        print("FizzBuzz")
    elif nums % 3 == 0:
        print("Fizz")
    elif nums % 5 == 0:
        print ("Buzz")
    else:
        print (nums)
