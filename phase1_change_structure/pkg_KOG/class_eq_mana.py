# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   法术类道具
# ------------------------(max to 80 columns)-----------------------------------


import sys
sys.path.append('..')
# 引用自定义的类及功能包
from pkg_KOG.class_equipment import Equipment

class EQMana(Equipment):

    # 添加独有加成
    add_mana_attack = 0.0

    def show_me_unique(self):
        print('-----独有加成-----')
        print('      法术攻击+%2d' % (self.add_mana_attack))
        print('-----------------')
        return


if __name__ == '__main__':
    eq = EQMana()
    eq.show_me()
    eq.show_me_unique()
