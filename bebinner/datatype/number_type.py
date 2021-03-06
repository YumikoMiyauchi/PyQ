scores = {
    '国語': 99,
    '算数': 71,
    '英語': 80
}


def main():
    total = 0
    for score in scores.values():
        total += score
        

    print('3教科の合計点は{:d}点'.format(total))
    print('3教科の平均点は{:f}点'.format(total/3))


if __name__ == '__main__':
    main
    
    
    
    
    x = 11
y = 2.5555555
z = 1000000
print('{0:d}, {0:5d}, {0:05d}, {1:f}, {1:.2f}, {2:,d}'.format(x, y, z))
# 11,    11, 00011, 2.555556, 2.56, 1,000,000

{0:d}は1番目のxを表示。
{0:5d}は1番目のxを5桁の領域に右づめで表示。余った桁は空白で埋める。
{0:05d}は1番目のxを5桁の領域に右づめで表示。余った桁は0で埋める。
{1:f}は2番目の値yを浮動小数点数型で表示。
{1:.2f}は2番目の値yを小数点三位で丸めて表示。
{2:,d}は3番目の値zをカンマ（,)で3桁区切りし、表示。{:,.2f}とかくと浮動小数点数をカンマ（,)で3桁区切りし、小数点第2位まで表示。
