"""调试示例脚本。

用法：
  1. 在第 8、17 行左侧点一下，打上红点（断点）；
  2. 按 F5，选「Python: main.py」；
  3. 程序会停在断点处，左侧「变量」面板能看到 a、b、total、n 的实时值；
  4. 用 F10（单步跳过）/ F11（单步进入）/ F5（继续）走完。
"""


def add(a, b):
    total = a + b        # ← 在这里打断点
    return total


def main():
    numbers = [1, 2, 3, 4, 5]
    running = 0

    for n in numbers:    # ← 也可以在这里打断点，观察每轮循环
        running = add(running, n)
        print(f"{n} 累加后 = {running}")

    print("最终结果:", running)


if __name__ == "__main__":
    main()
