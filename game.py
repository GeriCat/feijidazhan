from typing import Sequence
import pygame
#引用外部文件
# 测试1
from game_hud import *
from game_items import *
from game_music import *
import random


class Game(object):
    def __init__(self):#游戏窗口 游戏状态 游戏精灵 音乐播放器 精灵组
        self.main_window = pygame.display.set_mode(SCREEN_RECT.size)#设置窗口大小，直接调用items文件内SCREEN_RECT变量(列表形式)
        self.is_game_over = False#定义游戏结束
        self.is_game_pause = False#游戏是否暂停
    

        self.all_group = pygame.sprite.Group()#界面上的精灵
        self.enemies_group = pygame.sprite.Group()#敌机精灵
        self.supplies_group = pygame.sprite.Group()#道具精灵

        Background(False,self.all_group)#调用精灵 
        Background(True,self.all_group)

        hero_sprite = GameSprite('hero1.png',0,self.all_group)#设置玩家
        hero_sprite.rect.center = SCREEN_RECT.center#设置玩家图片居中显示于窗口

        self.hud_panel = HUDPanel(self.all_group)

    def reset_game(self):#重置游戏状态
        self.is_game_over = False
        self.is_game_pause = False

    def start(self):#启动游戏
        clock = pygame.time.Clock()#调用clock时钟模块
        while True:

            if self.event_handler():#检测按键 返回true 触发退出事件
               return

            if self.is_game_over:
                 print('游戏结束，空格从新开始')
            elif self.is_game_pause:
                 print('游戏暂停，空格继续')
            else:
                print('游戏运行中')
                self.all_group.update()


            self.all_group.draw(self.main_window)

            pygame.display.update()#刷新界面
            clock.tick(60)#设置刷新率/帧率
            pass

    def event_handler(self):#处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#点击退出按钮
                return True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:#检测用户按下了esc
                return True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:#检测用户按下了空格
                if self.is_game_over:#如果游戏已经结束
                    self.reset_game()#重置游戏
                else:
                    self.is_game_pause = not self.is_game_pause#游戏没结束，切换暂停状态

            if not self.is_game_over and not self.is_game_pause:#检测是否暂停或死亡
                if event.type == pygame.KEYDOWN and event.key == pygame.K_b:#检测用户按下b
                    self.hud_panel.show_bomb(random.randint(0,100))
                    # self.hud_panel.lives_cunt = random.randint(0,10)
                    # self.hud_panel.show_lives()
                    self.hud_panel.show_lives(random.randint(0,10))
        return False

if __name__ == '__main__':
    pygame.init()#初始化游戏
    Game().start()#开始游戏
    pygame.quit()#退出游戏
    game = Game()#对象给到类
    
    