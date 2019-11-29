# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   移动类道具
# ------------------------(max to 80 columns)-----------------------------------

import random
import sys
sys.path.append('..')
# ----------------------------
# 引用自定义的类及功能包
from pkg_KOG.class_equipment import Equipment
import pkg_KOG.global_var as GLV


class EQMove(Equipment):

    # 添加独有加成

    def __init__(self):
        '''按规则随机生成攻击类道具 '''
        # 随机挑选一个道具名称
        self.name = self.__set_name()

        # 随机生成各类加成值
        for i in range(GLV.MAX_FORGE_TIMES):
            n = random.randint(0, 10)
            self.__forge_eq(n)

        return

    def show_me_unique(self):
        print('-----独有加成-----')
        print('                无')
        print('-----------------')
        return

    def __set_name(self):

        all_eq_name = (
            '神速之靴',
            '影忍之足',
            '抵抗之靴',
            '冷静之靴',
            '秘法之靴',
            '急速战靴',
            '疾步之靴'
        )

        return random.choice(all_eq_name)

    def __forge_eq(self, skill_num):
        ''' 锻造道具 '''
        if skill_num == 0:  # +物理攻击
            pass
        elif skill_num == 1:  # +物理防御
            self.add_physical_defense += 0.05 * GLV.MAX_DEFENSE
        elif skill_num == 2:  # +法术防御
            self.add_mana_defense += 0.05 * GLV.MAX_DEFENSE
        elif skill_num == 3:  # +回蓝
            self.restore_mana_power += random.uniform(0.01, 0.1)
            if self.restore_mana_power >= 0.1:
                self.restore_mana_power = 0.1
        elif skill_num == 4:  # +移动速度
            self.add_move_speed += 0.05 * GLV.MAX_MOVE_SPEED
        elif skill_num == 5:  # +最大生命
            pass
        elif skill_num == 6:  # +最大法力
            pass
        elif skill_num == 7:  # +暴击率
            pass
        elif skill_num == 8:  # +物理吸血
            pass
        elif skill_num == 9:  # +法术攻击
            pass
        elif skill_num == 10:  # +回血
            pass
        else:
            pass

        return


if __name__ == '__main__':
    eq = EQMove()
    eq.show_me()
    eq.show_me_unique()
