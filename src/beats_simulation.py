import numpy as np
import matplotlib.pyplot as plt



def simulate_beat_frequency(f1=440, f2=444, A1=1.0, A2=1.0, t_start=0, t_end=1, num_points=5000, show_plot=True):
    """
    任务1: 拍频现象的数值模拟
    参数说明:
        f1, f2: 两个波的频率(Hz)
        A1, A2: 两个波的振幅
        t_start, t_end: 时间范围(s)
        num_points: 采样点数
    """
    # 生成时间范围
    t = np.linspace(t_start, t_end, num_points)

    # 生成两个正弦波
    wave1 = A1 * np.sin(2 * np.pi * f1 * t)
    wave2 = A2 * np.sin(2 * np.pi * f2 * t)

    # 叠加两个波
    superposed_wave = wave1 + wave2

    # 计算拍频
    beat_frequency = abs(f2 - f1)

    # 绘制图像
    if show_plot:
        plt.figure(figsize=(12, 6))

        # 绘制第一个波
        plt.subplot(3, 1, 1)
        plt.plot(t, wave1, color='blue')
        plt.title(f'Wave 1: Frequency = {f1} Hz, Amplitude = {A1}')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')

        # 绘制第二个波
        plt.subplot(3, 1, 2)
        plt.plot(t, wave2, color='red')
        plt.title(f'Wave 2: Frequency = {f2} Hz, Amplitude = {A2}')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')

        # 绘制叠加波
        plt.subplot(3, 1, 3)
        plt.plot(t, superposed_wave, color='green')
        plt.title(f'Superposed Wave (Beat Frequency = {beat_frequency} Hz)')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')

        plt.tight_layout()
        plt.show()

    return t, superposed_wave, beat_frequency


def parameter_sensitivity_analysis():
    """
    任务2: 参数敏感性分析
    需要完成:
    1. 分析不同频率差对拍频的影响
    2. 分析不同振幅比例对拍频的影响
    """
    # 频率差分析
    plt.figure(1, figsize=(12, 8))
    delta_fs = [1, 2, 5, 10]
    for i, df in enumerate(delta_fs):
        f2 = 440 + df
        t, wave, beat_freq = simulate_beat_frequency(f1=440, f2=f2, t_end=2, show_plot=False)
        plt.subplot(len(delta_fs), 1, i + 1)
        plt.plot(t, wave)
        plt.title(f'Frequency Difference = {df} Hz, Beat Frequency = {beat_freq} Hz')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
    plt.tight_layout()

    # 振幅比例分析
    plt.figure(2, figsize=(12, 8))
    A_params = [(0.5, 1), (1, 1), (2, 1), (5, 1)]
    for i, (A1, A2) in enumerate(A_params):
        t, wave, beat_freq = simulate_beat_frequency(f1=440, f2=444, A1=A1, A2=A2, show_plot=False)
        plt.subplot(len(A_params), 1, i + 1)
        plt.plot(t, wave)
        plt.title(f'Amplitude Ratio A1/A2 = {A1 / A2:.2f}, Beat Frequency = {beat_freq} Hz')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # 示例调用
    print("=== 任务1: 基本拍频模拟 ===")
    t, wave, beat_freq = simulate_beat_frequency()
    print(f"计算得到的拍频为: {beat_freq} Hz")

    print("\n=== 任务2: 参数敏感性分析 ===")
    parameter_sensitivity_analysis()
