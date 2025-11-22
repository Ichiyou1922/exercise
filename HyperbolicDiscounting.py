import numpy as np
import matplotlib.pyplot as plt

def exponential_discounting(value, rate, time):
    """
    指数割引（理性的・一貫した評価）
    V = Value * e^(-rate * time)
    """
    return value * np.exp(-rate * time)

def hyperbolic_discounting(value, k, time):
    """
    双曲割引（本能的・衝動的な評価）
    V = Value / (1 + k * time)
    """
    return value / (1 + k * time)

# 設定
time = np.linspace(0, 10, 100) # 0から10時点までの時間経過
future_reward = 100            # 将来得られるはずの成果（目標達成など）
discount_rate = 0.3            # 割引率
k_factor = 1.0                 # 双曲割引の衝動性パラメータ

# 価値の計算
rational_value = exponential_discounting(future_reward, discount_rate, time)
instinctive_value = hyperbolic_discounting(future_reward, k_factor, time)

# 可視化
plt.figure(figsize=(10, 6))
plt.plot(time, rational_value, label='Rational (Exponential) - Ideal Plan', linestyle='--')
plt.plot(time, instinctive_value, label='Instinctive (Hyperbolic) - Actual Feeling', linewidth=2.5, color='red')

# 交差ポイントの強調（「明日やる」が「今日やらない」に負ける瞬間）
plt.title("Why You Procrastinate: The War Between Logic and Instinct")
plt.xlabel("Time Delay (How far in the future?)")
plt.ylabel("Subjective Value (How much you care)")
plt.legend()
plt.grid(True)

# グラフに注釈
plt.text(0.5, 80, "Present Bias:\nImmediate rewards are\novervalued massively", color='red', fontsize=10)
plt.text(6, 40, "Future:\nRational planning prevails\n(You intend to be good)", color='blue', fontsize=10)

plt.show()
