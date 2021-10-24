import pygame
from pygame.sprite import Group
from game_items import * 
class HUDPanel(object):#面板精灵的总控制类
    margin = 10
    white = (255,255,255)
    gray = (64,64,64)
    def __init__(self,display_group):

        #↓基本数据
        self.score = 0  #游戏得分，初始为0
        self.lives_count = 3  #初始生命值
        self.livel = 1  #默认游戏级别
        self.best_score = 0  #最好成绩 

        #状态图片精灵
        self.status_sprite = StatusButton(('pause.png','resume.png'),display_group)#设置暂停切换精灵
        self.status_sprite.rect.topleft = (self.margin,self.margin)

        #得分计数标签 
        self.score_label = Label('%d'%self.score,32,self.gray,display_group)
        self.score_label.rect.midleft = (self.status_sprite.rect.right + self.margin, self.status_sprite.rect.centery)


        #设置生命图片精灵
        self.lives_sprite = GameSprite('hero1.png',0,display_group)#设置命        
        self.lives_sprite.rect.bottom = SCREEN_RECT.bottom - self.margin#生命图片y

        #生命计数标签
        self.lives_label = Label('x %d'%self.lives_count,36,self.white,display_group)
        self.lives_label.rect.midright = (SCREEN_RECT.right - self.margin, self.lives_sprite.rect.centery)

        self.lives_sprite.rect.right = self.lives_label.rect.left - self.margin#生命图片x

        #炸弹图片精灵
        self.bomb_sprite = GameSprite('bullet.png',0,display_group)#设置炸弹
        self.bomb_sprite.rect.x = self.margin
        # self.bomb_sprite.rect.bottom = SCREEN_RECT.bottom - self.margin #取 窗口矩形底边数值减去 图片高+margin值 得到位置
        self.bomb_sprite.rect.centery = self.lives_sprite.rect.centery + 5 #把炸弹图片y轴中心对齐到生命图片的y轴中心

        #炸弹计数标签
        self.bomb_label = Label('x 3',36,self.white,display_group)
        self.bomb_label.rect.midleft = (self.bomb_sprite.rect.right + self.margin, self.bomb_sprite.rect.centery)

        #最好成绩
        self.best_label = Label('Best:%d'%self.best_score,36,self.white,display_group)
        self.best_label.rect.center = (SCREEN_RECT.centerx, SCREEN_RECT.centery -4*self.margin)#最好成绩对齐窗口居中

        #状态标签
        self.status_label = Label('Game Paused!',48,self.white,display_group)
        self.status_label.rect.midbottom = (self.best_label.rect.centerx, self.best_label.rect.y - 3*self.margin)

        #↓提示标签
        self.tip_label = Label('Press spacebar to continue',22,self.white,display_group)
        self.tip_label.rect.midtop = (self.best_label.rect.centerx, self.best_label.rect.y + 15*self.margin)


    def show_bomb(self,count):#修改炸弹数量
        self.bomb_label.set_text('x %d' %count)
        self.bomb_label.rect.midleft = (self.bomb_sprite.rect.right + self.margin, self.bomb_sprite.rect.centery)

    def show_lives(self,lives_count):#修改生命计数
        self.lives_label.set_text('x %d'%lives_count)#更新显示文本内容text
        self.lives_label.rect.midright = (SCREEN_RECT.right - self.margin, self.lives_sprite.rect.centery)#更新位置
        self.lives_sprite.rect.right = self.lives_label.rect.left - self.margin#更新生命图片x
