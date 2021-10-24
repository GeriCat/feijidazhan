import pygame


SCREEN_RECT = pygame.Rect(0,0,480,700)#游戏窗口


class GameSprite(pygame.sprite.Sprite):
    res_path = './image/'#简化路径
    def __init__(self,image_name,speed,*group):#初始化精灵对象
        super(GameSprite,self).__init__(*group)#调用父类方法，把精灵放到精灵组里调用（强制性的必须的）
        self.image = pygame.image.load(self.res_path + image_name)#创建图片
        self.rect = self.image.get_rect()#获取矩形
        self.speed = speed#定义速度

    def update(self,*args):
        self.rect.y += self.speed

class Background(GameSprite):#继承上面的精灵类
    def __init__(self,is_alt,*group):
        super(Background,self).__init__('bg.png',1,*group)#设置背景
        if is_alt:#检测is_alt如果为true，y值减去高则为外部背景图片
            self.rect.y = - self.rect.h

    def update(self,*arge):
        super(Background,self).update(*arge)#如果图片滚出窗口外，则返回原位
        if self.rect.y > self.rect.h:
            self.rect.y = - self.rect.y

class StatusButton(GameSprite):
    def __init__(self,image_names,*groups):# image_name接收一个元组，元组0的下标必须是暂停图片，1是播放
        super(StatusButton,self).__init__(image_names[0],0,*groups)
        self.images = [ pygame.image.load(self.res_path+name) for name in image_names ]#获取图片地址，遍历 添加 到image_names列表中

    def switch_status(self,is_pause):
        self.image = self.images[ 1 if is_pause else 0 ]#根据是否暂停，切换使用的图片

class Label(pygame.sprite.Sprite):#定义按键精灵类

    font_path = './font/CORNET.TTF'

    def __init__(self,text,size,color,*gruops):#text文本 size大小 color颜色 
        super(Label,self).__init__(*gruops)

        self.font = pygame.font.Font(self.font_path,size)#创建字体对象

        self.color = color
        #精灵必备属性↓ 生成文本 矩形框大小
        self.image = self.font.render(text,True,self.color)#render渲染，文本 是否抗锯齿 颜色

        self.rect = self.image.get_rect()

    def set_text(self,text):#更新显示文本内容text
        self.image = self.font.render(text,True,self.color)
        self.rect = self.image.get_rect()