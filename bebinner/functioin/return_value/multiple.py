# 関数div_and_modを定義します
def div_and_mod(x, y):
    """xをyで割った、商の整数部分と余りを求める."""
    div = x//y
    mod = x%y
    return div, mod

div1, mod1 = div_and_mod(100, 23)
print(div1, mod1)

div2, mod2 = div_and_mod(235, 17)
print(div2, mod2)
