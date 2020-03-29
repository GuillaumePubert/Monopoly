import random
from jeu import *
liste=[case_0,case_1,case_2,case_3,case_4,case_5,case_6,case_7,8,case_9,case_10,case_11,case_12,case_13,
                          case_14,case_15,case_16,case_17,case_18,case_19,case_20,case_21,case_22,case_23,case_24,
                          case_25,case_26,case_27,case_28,case_29,case_30,case_31,case_32]

cursor=0
cursorprec=0
for i in range(18):
    avancement=random.randint(2,12)
    cursor+=avancement
    print(avancement,cursor)
    while cursor > 20:
        cursorprec=cursor
        avancement=random.randint(2,12)
        cursor+=avancement
        if cursor<=32:
            print(avancement,cursor)
        if cursor>32:
            cursor=cursorprec-32+avancement
            print(avancement,cursor)
            break

