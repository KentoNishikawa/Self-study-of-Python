# (1)「Hello, World!」を出力するプログラムを書いてください。
a = "Hello, World!"
print (a)
# (2)変数xの値が10で、変数yの値が5の場合、「x + y = 15」という文字列を出力するプログラムを書いてください。
x = 10
y = 5
print ("x + y = ",x+y)
# (3)文字列「abcdefg」の各文字を一行ずつ出力するプログラムを書いてください。
a="abcdefg"
for b in a:
    print (b)
# (4)リストcolorsに"red"、"green"、"blue"が格納されている場合、「red, green, blue」という文字列を出力するプログラムを書いてください。
colors = ["red","green","blue"]
separetor = ","
print (separetor.join(colors))
# joinメソッドは、文字列やリストなどのシーケンス型オブジェクトの要素を指定した区切り文字で連結するために使用
# (5)文字列"hello world"を逆順にして出力するプログラムを書いてください。
a ="hello world"
print (a[::-1])
# (6)文字列"abcde"をリストに変換して、そのリストの各要素を一行ずつ出力するプログラムを書いてください。
s = "abcde"
lst = list(s)
for r in lst:
    print (r)
# (3)をリストに入れただけ
# 任意の単語や文章を入力として受け取り、その入力をアルファベット順に並び替えた結果を出力するプログラムを書いてください。
s = input("Enter a word or sentence: ")
s_sorted = ''.join(sorted(s))
print(s_sorted)
# 任意の文字列を入力として受け取り、その文字列に含まれる英数字の個数を出力するプログラムを書いてください。
s = input("Enter a string: ")
count = 0
for c in s:
    if c.isalnum():
        count += 1
print("The number of alphanumeric characters is:", count)
