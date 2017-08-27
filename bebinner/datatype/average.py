numbers = [10, 30, 33, 33, 23, 22, 44]


def calc_avg(values):
    """引数で渡されたリストの平均値を表示する."""
    # 戻り値は平均値（浮動小数点数型）
    s = 0
    for n in numbers:
        s += n
    average = s / len(numbers)
    return average


def main():
    """メインの処理."""
    res = calc_avg(numbers)
    print('{0:.3f}'.format(res))


if __name__ == '__main__':
    main()
