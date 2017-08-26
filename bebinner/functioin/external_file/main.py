def check_even_odd(num):
    if num % 2 == 0:
        print(num, 'is even number!')
    else:
        print(num, 'is odd number!')


def main():
    
    # 実行
    check_even_odd(14)
    check_even_odd(25)
    check_even_odd(33)


    解説

わざわざ、 if __name__ == '__main__': の下に main() のみ記述し、関数 main を定義して処理を記述しています。
このような書き方を良くします。

def 関数():
    処理

def main():
    処理

if __name__ == '__main__':
    main()

後ほどテストの解説で触れますが、 if __name__ == '__main__': の下に色々な処理を書くとテストが書きにくいです。
そこで、 if __name__ == '__main__': の下には関数 main の実行だけ書きます。
