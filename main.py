# dirs key: head-1 rot-2 txt-3
# variable layers: in 1/2/3 in one color - (#000000)
# 0-0: for all img in one color - (#ffffff)
import random
import os


combinatedLayers_list = []

DIR_PATH = 'Users/alexovna.mac/Documents/lp26_main/les-2.w-2/maker_png/template721/'


def generate_period():
    start = random.randint(1, 3)
    end = random.randint(1, 3)
    if start == end:
        generate_period()
    return start, end


def createNameLayer():
    generate_period()
    # layer_name = str(random.randint(a=start, b=end)) + '.png'
    file_path = os.path.join(DIR_PATH, str(random.randint(a=start, b=end)) + '.png')
    print(file_path)
    return file_path


def createListSelectedNameLayers():
    createNameLayer()
    combinatedLayers_list.append(file_path)
    return combinatedLayers_list
    print(combinatedLayers_list)


def choiseLayer():
    # генератор диапазона числового значения для выбора рандомного слоя // слои поименованы так: число.png
    generate_period()
    # записывает имена выбранных слоев в список // combinatedLayers_list
    createListSelectedNameLayers()
    while len(combinatedLayers_list) < 1:
        choiseLayer()


createNameLayer()
# choiseLayer()
# joinerLayers()
# saveResultToArchive()
