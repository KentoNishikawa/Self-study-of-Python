# if文の基本的な構文
a = 30
if a < 10:
    print (f"{a}は10より小さい")
elif a == 15 or a == 30:
    print (f"{a}は10より大きいが{a}というなんかいい数字")

# または(or)、且つ(and)
# pythonでは"else if"ではなく"elif"
elif a == 10:
    print (f"ジャスト{10}")
else:
    print (f"{a}は10より大きい")

# 演算も使用したif文
a = 0.5
b = 0.5
if a + b < a * b:
    print (f"({a}+{b}){a+b}は({a}×{b}){a*b}より小さい")
elif a / b == a * b:
    print (f"({a}÷{b}){a//b}は({a}×{b}){a*b}と値は同じ")
elif a + b == a * b:
    print (f"{a}と{b}は足しても掛けても同じ")
else:
    print (f"({a}+{b}){int(a+b)}は({a}×{b}){int(a*b)}より大きい")
# 掛け算で小数点以下を切り捨てて整数のみを表示する方法はint()関数を使用

# 三項演算子
a = 22
b = 200
c = f"{a}は{b}より大きい" if a > b else f"{a}は{b}より小さい"
print (c)

# 三項演算子にはelse ifは存在しない
d = f"({a}+{b}){a+b}は偶数です。" if (a + b) % 2 == 0 else f"({a}+{b}){a+b}奇数です。"
print (d)
