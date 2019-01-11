#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FuncFormatter
import seaborn as sns; sns.set()
# import seaborn as sns; sns.set_style('whitegrid')


def getFiles(path):
    files = os.listdir(path)
    # print(files)

    return files


def formatnum(x, pos):
    return '$%.1f$x$10^{4}$' % (x/10000)


def formatdate(num):
    return files[num][4:6] + '-' + files[num][6:8]


nums = []
files = getFiles('./data')
# for file in files:
#     date = file.split('.')[0]
#     df = pd.read_csv('./data/%s.csv' % date)
#     num = len(df)
#     nums.append(num)

nums = [
        144120,
        56276,
        45419,
        51750,
        25165,
        67593,
        43888,
        30343,
        39254,
        281853,
        133671,
        24692,
        19134,
        23385,
        17023,
        21531,
        17291,
        14899,
        15253,
        14085,
        13531,
        28641,
        33120,
        31018,
        39864,
        46823,
        55213,
        70323,
        63904,
        87530,
        41783,
        46540,
        75592,
        68907,
        70321,
        57338,
        56827,
        55229,
        19493,
        15817,
        16425,
        43330,
        55752,
        60859,
        45071,
        45761,
        67471,
        68585,
        65248,
        73998,
        75841,
        47258,
        51323,
        86716,
        77394,
        73765,
        77072,
        65321,
        34891,
        33236,
        47554,
        47260,
        34382
]

ax = plt.axes()
ax.bar(files, nums)
# x 轴
ax.set_xlim([-1, 63])
xmajorLocator   = MultipleLocator(20)
xmajorFormatter = FormatStrFormatter('%.0f')
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)
ax.set_xticks([0, 20, 40, 60])
ax.set_xticklabels([formatdate(0), formatdate(20), formatdate(40), formatdate(60)])
# y 轴
formatter = FuncFormatter(formatnum)
ax.yaxis.set_major_formatter(formatter)

plt.show()