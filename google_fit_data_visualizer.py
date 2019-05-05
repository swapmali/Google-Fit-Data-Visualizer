import matplotlib.pyplot as plt
import pandas as pd
import os
import re
import math
import random
import numpy as np


def draw_graph(x_arr, y_arr, year_month, attribute):
    my_dpi = 96
    month_in_text = digit_month_text(int(year_month[5:]))
    index = np.arange(len(x_arr))
    # print(plt.style.available)    # from the available styles choose one
    plt.style.use('fivethirtyeight')
    plt.plot(x_arr, y_arr)

    plt.xticks(index, x_arr, fontsize=6)
    plt.yticks(fontsize=6)

    plt.xlabel(month_in_text, fontsize=8)
    plt.ylabel(attribute, fontsize=8)
    plt.title('Analysis of {} burnt in {} {}'
              .format(attribute, month_in_text, year_month[:4]),
              fontsize=15)
    plt.savefig('output_files\{}_{}_{}.png'
                .format(year_month[:4], month_in_text, random.randint(1, 100)), dpi=my_dpi)
    plt.show()


def read_csv(month):
    data = pd.read_csv('input_files\Daily Summaries.csv')
    pattern = '2019-' + month + '-.{2}'
    # print(pattern[:-5])
    attribute_counter(data, pattern, 'Calories (kcal)')
    attribute_counter(data, pattern, 'Step count')


def attribute_counter(data, pattern, attribute):
    counter_arr = []
    date_arr = []
    cnt_matches = 0
    for index, row in data.iterrows():
        test_string = row['Date']
        #print(test_string)
        if re.match(pattern, test_string):
            date_arr.append(test_string[-2:])
            counter_arr.append(math.ceil(row[attribute]))
            cnt_matches += 1
    draw_graph(date_arr, counter_arr, pattern[:-5], attribute)
    # print(date_arr)
    # print(counter_arr)
    # print(cnt_matches)


def digit_month_text(digit):
    month_arr = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]
    return month_arr[digit - 1]


def find_all_csv():
    return os.listdir('F:\Code Expert\Python for Spreadsheets\Google fit\input_files')


if __name__ == '__main__':
    month = input('\nEnter Month (in 2 digits): ')
    read_csv(month)
