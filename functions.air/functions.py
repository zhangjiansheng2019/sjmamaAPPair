# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

import time

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

#获取屏幕分辨率，查找手机麻麻app并点击
def touchAPP(leftcoords,rightcoords):
    xy=poco.get_screen_size()
    x=xy[0]
    y=xy[1]
    for i in range(3):
        if exists(Template(r"tpl1580875497337.png", record_pos=(0.196, 0.073), resolution=(1080, 1920))):

            touch(Template(r"tpl1580875511031.png", record_pos=(0.189, 0.064), resolution=(1080, 1920)))

            break
        else:
            swipe((x*rightcoords,y*0.5),(x*leftcoords,y*0.5))
touchAPP(0.1,0.9)        
sleep(10.0)
#登录
def login(phone,passwrod):
    if exists(Template(r"tpl1580875578342.png", record_pos=(-0.001, -0.277), resolution=(1080, 1920))):
        poco(name='com.jike.shoujimama:id/sys_message_close_view').click()
      
        poco(name='com.jike.shoujimama:id/tv_mine').click()
    else:
        poco(name='com.jike.shoujimama:id/tv_mine').click()

    poco(name='com.jike.shoujimama:id/tv_mine_login').click()
    poco(name='com.jike.shoujimama:id/phoneET').click()
    text(phone)
    poco(name='com.jike.shoujimama:id/et_setting_psw').click()
    text(passwrod)
    
    poco(name='com.jike.shoujimama:id/checkSDV').click()
    poco(name='com.jike.shoujimama:id/loginTV').click()
    poco(name='com.jike.shoujimama:id/tv_nearby').click()#返回主页
login('13422883445','123456')

#幸运大转盘
def lukewheel():
    poco(name='com.jike.shoujimama:id/tv_title').click()



