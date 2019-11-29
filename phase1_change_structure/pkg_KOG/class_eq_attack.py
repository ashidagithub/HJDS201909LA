# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11.23
# Description:
#   攻击类道具
# ------------------------(max to 80 columns)-----------------------------------

import sys
sys.path.append('..')
# 引用自定义的类及功能包
from pkg_KOG.class_equipment import Equipment
#from class_equipment import Equipment


class EQAttack(Equipment):
    # 添加独有加成
    critical_strike = 0.0
    physical_suck = 0.0

    def show_me_unique(self):
        print('-----独有加成-----')
        print('       +暴击率:%0.2f' % (self.critical_strike))
        print('     +物理吸血:%0.2f' % (self.physical_suck))
        print('-----------------')
        return


if __name__ == '__main__':
    eq = EQAttack()
    eq.show_me()
    eq.show_me_unique()
