# -*- coding: utf-8 -*-
# @Time    : 2018/12/13
# @Author  : Yifei Duan
# @Summary :

import csv
from datetime import datetime
from matplotlib import pyplot as plt

# filename = 'sitka_weather_07-2014.csv'
filename = 'sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 输出行头
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # 从文件获取获取最高温度
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        highs.append(int(row[1]))
        lows.append(int(row[2]))

    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # 图形格式
    plt.title('Daily high and low temperatures, 2014', fontsize=24)
    plt.xlabel("", fontsize=14)
    fig.autofmt_xdate()
    plt.ylabel("Temperatures(F)", fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=14)

    plt.show()
