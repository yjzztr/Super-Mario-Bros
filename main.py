import pygame
import time

# 初始化 Pygame 库
pygame.init()

# 游戏界面的大小
width = 640
height = 480

# 创建游戏界面窗口
screen = pygame.display.set_mode((width, height))

# 设置游戏标题
pygame.display.set_caption("Super Mario")

# 加载玛丽的图片
mario = pygame.image.load("mario.png")

# 玛丽的初始位置
mario_x = 0
mario_y = 400

# 设置游戏帧率
fps = pygame.time.Clock()

# 游戏主循环
while True:
    # 处理游戏事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # 绘制游戏界面
    screen.fill((255, 255, 255)) # 清空屏幕
    screen.blit(mario, (mario_x, mario_y)) # 绘制玛丽

    # 更新游戏界面
    pygame.display.update()

    # 控制游戏帧率
    fps.tick(60)
