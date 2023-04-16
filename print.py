# (1) : 直接表示
print ('Hello World!')

# (2) : 変数aに代入し、a(Hello World!)を表示
a = 'Hello World!'
print(a)

# (3) : b,c,dそれぞれに'Hello','World','!'を代入しb,c,dを表示
b = 'Hello'
c = 'World'
d = '!'

# (4) : .formatを使用し{}の中に順に入れていくやり方
print("{} {}{}".format(b,c,d))

# (5) : 先頭にfを着け{}にb,c,dを入れる(f文字列)
print(f"{b} {c}{d}")

# (6) : {}で囲んだ変数を更に{}で囲めば文字列として出力することができる
print(f"{b} {{b}} {c}{d}")

# (7) : (2)を応用し+を使うやり方
print(str(b) + " " + c +str(d))

# (8) : ""で囲めば変数としてではなく一つの文字として認識される為、代入はされない
print(str(b) + "b" + " " + c + "c" + str(d))
