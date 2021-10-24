import pygame
import time
from pygame.locals import *

class Bullet(object):#创建子弹类
    def __init__(self,x,y,screen):
        self.x=x+13
        self.y=y-20
        self.screen=screen
        self.image=pygame.image.load('./image/bullet.png')
        pass
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        pass
    def move(self):#子弹上升速度
        self.y-=1
        pass
    def judge(self):#判断子弹是否越界
        if self.y<=0:
            return True
        else :
            return False
        pass
    pass


class Heroplane(object):#初始化飞机函数
    def __init__(self,screen):#初始化函数
        self.x=150#飞机默认位置
        self.y=450
        self.screen=screen
        self.imagename='./image/hero1.png'
        self.image=pygame.image.load(self.imagename)
        self.bulletlist=[]#存放子弹的列表
        pass

    def moveleft(self):#左移动
        if self.x>0:
            self.x-=10
        pass
    def moveright(self):#右移动
        if self.x<300:
            self.x+=10
        pass
    def display(self):#显示图片&玩家的子弹
        self.screen.blit(self.image,(self.x,self.y))
        pass

        needDelitemlist=[]#遍历检测子弹数值是否到0 
        for item in self.bulletlist:
            if item.judge():
                needDelitemlist.append(item)#到0返回true 子弹对象添加到item
                pass
            pass
        for i in needDelitemlist:
            self.bulletlist.remove(i)
            pass
        for bullet in self.bulletlist:
            bullet.display()#显示子弹位制
            bullet.move()#修改位置移动

    def shootbullet(self):#发射子弹
        newbullet=Bullet(self.x,self.y,self.screen)#创建新的子弹对象
        self.bulletlist.append(newbullet)
        pass
    pass

def key_control(Heroobj):#键盘检测 Heroobj 检测的对象
    eventlist=pygame.event.get()#获取pygame按键插件赋值给eventlist
    for event in eventlist:
        if event.type==QUIT:#检测按键打印退出
            print('退出')
            exit()
            pass
        elif event.type==KEYDOWN:
            if event.key==K_a or event.key==K_LEFT:
                print('左')
                Heroobj.moveleft()
                pass
            elif event.key==K_d or event.key==K_RIGHT:
                print('右')
                Heroobj.moveright()
                pass    
            elif event.key==K_SPACE:
                print('发射')
                Heroobj.shootbullet()
                pass
    pass






def main():
    screen=pygame.display.set_mode((350,500))#创建背景框架范围,两层括号
    background=pygame.image.load("./image/bg.png")#bg图片地址

    hero=Heroplane(screen)#创建飞机对象
    # hero2=pygame.image.load('./image/hero2.png')

    pygame.display.set_caption("阶段总结-飞机游戏")#改标题

    pygame.mixer.init()#添加音乐
    pygame.mixer.music.load('./music/Slim Fey - 夏 日 時 光 ℃.mp3')
    pygame.mixer.music.set_volume(0.2)#音量
    pygame.mixer.music.play(-1)#给音乐循环（-1）

    


    while True:#检测玩家行动
        screen.blit(background,(0,0))#设定bg显示内容，居中
        # screen.blit(hero2,(0,0))
        hero.display()#显示玩家图片转到函数
            
        key_control(hero)#键盘检测函数
        
        pygame.display.update()#显示内容更新
        pass

if __name__=='__main__':
    main()