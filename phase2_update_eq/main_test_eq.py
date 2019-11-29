# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11.23

# Description:
#   使用道具的类
# ------------------------(max to 80 columns)-----------------------------------


'''
import sys
sys.path.append('..')
'''

from pkg_KOG.class_equipment import Equipment
from pkg_KOG.class_eq_attack import EQAttack
from pkg_KOG.class_eq_defense import EQDefense
from pkg_KOG.class_eq_mana import EQMana
from pkg_KOG.class_eq_move import EQMove

'''
eq1 = Equipment()
eq1.show_me()
'''

eq2 = EQAttack()
eq2.show_me()
eq2.show_me_unique()

eq3 = EQDefense()
eq3.show_me()
eq3.show_me_unique()

eq4 = EQMana()
eq4.show_me()
eq4.show_me_unique()

eq5 = EQMove()
eq5.show_me()
eq5.show_me_unique()
