# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11.23

# Description:
#   使用英雄的类
# ------------------------(max to 80 columns)-----------------------------------

from pkg_KOG.class_hero import Hero

cjsh = Hero('苍狼末裔', '成吉思汗', '射手ARCHER')
#cjsh.show_me()
print(cjsh.name)
print(cjsh.position)
print(cjsh.ab_difficulty)

#cjsh.name = '张三'
cjsh.ab_difficulty = 999
print(cjsh.ab_difficulty)
