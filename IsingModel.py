#!/bin/python3
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class IsingModelLogic:
    def should_flip(self, dE, T):
        if dE < 0:
            return True
        else:
            return random.random() < math.exp(-dE/T)
    
class IsingSimulation:
    def __init__(self, N, T):
        self.N = N 
        self.T = T
        # スピン情報が-1か1のどちらかで，座標はN*Nの格子点の内どこか
        self.grid = np.random.choice([-1, 1], size=(N, N))
        self.logic = IsingModelLogic()
        
    def calculate_dE(self, x, y):
        # 現在のスピン
        s = self.grid[x, y]
        u_y = y + 1
        r_x = x + 1
        d_y = y - 1
        l_x = x - 1
        # 周期的境界条件
        if x == self.N-1:
            r_x = 0
        elif x == 0:
            l_x = self.N - 1

        if y == self.N-1:
            u_y = 0
        elif y == 0:
            d_y = self.N - 1
        
        # 隣接するスピンの座標
        s_u = self.grid[x, u_y]
        s_r = self.grid[r_x, y]
        s_d = self.grid[x, d_y]
        s_l = self.grid[l_x, y]
        neighbor_sum = s_u + s_r + s_d + s_l
        
        # エネルギー変化
        dE = 2 * s * neighbor_sum
        return dE

    def step(self):
        # ランダムに一点選ぶ
        x = np.random.randint(0, self.N)
        y = np.random.randint(0, self.N)

        # エネルギー変化を計算
        dE = self.calculate_dE(x, y)

        # 判定ロジックへ
        if self.logic.should_flip(dE, self.T):
            self.grid[x, y] *= -1

# 設定：サイズと温度
N = 50
# 臨界温度 Tc ≈ 2.269 (オンサーガーの解)
# これより高いと「無秩序」、低いと「秩序(磁石)」になる
T_high = 10.0  # 高温
T_low = 1.0    # 低温
T_critical = 2.3 # 臨界点付近

# シミュレーション作成
sim = IsingSimulation(N, T=T_critical) # お好みの温度で

# アニメーションの準備
fig = plt.figure()
im = plt.imshow(sim.grid, cmap='gray', vmin=-1, vmax=1, interpolation='nearest')
plt.title(f"Ising Model T={sim.T}")

def update(frame):
    # 1フレームにつき N*N 回ステップを進める（モンテカルロ・ステップ）
    # こうしないと描画が遅すぎて変化が見えない
    for _ in range(N * N):
        sim.step()
    
    im.set_array(sim.grid)
    return [im]

ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)
plt.show()
