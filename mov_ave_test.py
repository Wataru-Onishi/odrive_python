import time
import random

windows_size = 15
speed = [0] * windows_size

def mov_ave(new_val):
    speed.pop(0)
    speed.append(new_val)

    if not speed:  # 配列が空の場合
        return 0
    return sum(speed) / len(speed)  # 合計値を要素数で割って平均を求める


def output_random_values():
    while True:  # 無限ループでランダムな値を出力し続ける
        value = random.randint(0, 100)  # 0から100までのランダムな値を生成
        ave_val = mov_ave(value)
        print("ave_val:"+str(ave_val))
        time.sleep(1) # 1秒間待機


output_random_values()