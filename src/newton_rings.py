import numpy as np
import matplotlib.pyplot as plt

def setup_parameters():
    """
    设置模拟牛顿环所需的参数

    返回:
    tuple: 包含激光波长(lambda_light,单位m)、透镜曲率半径(R_lens,单位m)的元组
    """
    # 氦氖激光波长 (m)
    lambda_light = 632.8e-9
    # 透镜曲率半径 (m)
    R_lens = 0.1
    return lambda_light, R_lens


def generate_grid():
    """
    生成模拟所需的网格坐标

    返回:
    tuple: 包含网格坐标X、Y以及径向距离r的元组
    """
    # 设置空间范围（5mm x 5mm区域）
    x = np.linspace(-0.005, 0.005, 1000)
    y = np.linspace(-0.005, 0.005, 1000)

    # 生成网格坐标
    X, Y = np.meshgrid(x, y)

    # 计算径向距离
    r = np.sqrt(X ** 2 + Y ** 2)

    return X, Y, r


def calculate_intensity(r, lambda_light, R_lens):
    """
    计算干涉强度分布

    参数:
    r (np.ndarray): 径向距离数组
    lambda_light (float): 激光波长(m)
    R_lens (float): 透镜曲率半径(m)

    返回:
    np.ndarray: 干涉强度分布数组
    """
    # 计算相位差项
    phase_term = (np.pi * r ** 2) / (lambda_light * R_lens)

    # 根据干涉公式计算强度
    intensity = np.sin(phase_term) ** 2  # 使用正弦平方体现半波损失

    return intensity


def plot_newton_rings(intensity):
    """
    绘制牛顿环干涉条纹图像

    参数:
    intensity (np.ndarray): 干涉强度分布数组
    """
    plt.figure(figsize=(8, 8))

    # 显示干涉图样（使用灰度色图）
    plt.imshow(intensity,
               cmap='gray',
               extent=[-0.005, 0.005, -0.005, 0.005],vmin=0, vmax=1,
               origin='lower')
    #设置颜色条
    plt.colorbar(label='Intensity')

    # 美化显示设置
    plt.title("Newton's Rings Interference Pattern", fontsize=14)
    #设置x轴标签
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.axis('off')  # 关闭坐标轴

    plt.show()


if __name__ == "__main__":
    # 1. 设置参数
    lambda_light, R_lens = setup_parameters()

    # 2. 生成网格坐标
    X, Y, r = generate_grid()

    # 3. 计算干涉强度分布
    intensity = calculate_intensity(r, lambda_light, R_lens)

    # 4. 绘制牛顿环
    plot_newton_rings(intensity)
