# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   移动类道具
# ------------------------(max to 80 columns)-----------------------------------


import sys
sys.path.append('..')
# 引用自定义的类及功能包
from pkg_KOG.class_equipment import Equipment


class EQMove(Equipment):

    # 添加独有加成

    def show_me_unique(self):
        print('-----独有加成-----')
        print('                无')
        print('-----------------')
        return


if __name__ == '__main__':
    eq = EQMove()
    eq.show_me()
    eq.show_me_unique()
