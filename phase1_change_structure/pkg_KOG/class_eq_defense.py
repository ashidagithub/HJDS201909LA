# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   防御类道具
# ------------------------(max to 80 columns)-----------------------------------


import sys
sys.path.append('..')
# 引用自定义的类及功能包
from pkg_KOG.class_equipment import Equipment


class EQDefense(Equipment):

    # 添加独有加成
    restore_life_force = 0.0

    def show_me_unique(self):
        print('-----独有加成-----')
        print('       +回血:%0.2f' % (self.restore_life_force))
        print('-----------------')
        return


if __name__ == '__main__':
    eq = EQDefense()
    eq.show_me()
    eq.show_me_unique()
