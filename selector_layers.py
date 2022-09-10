
import random, os

DIR_PATH = 'Users/alexovna.mac/Documents/lp26_main/les-2.w-2/maker_png/template721/'
NUM_LAYERS_LIST = []
NAME_LAYERS_LIST = []
FILE_PATH_layerOne = ''
FILE_PATH_layerTwo = ''


def generate_period():
    layer_one = random.randint(1, 3)
    layer_two = random.randint(1, 3)
    if layer_one != layer_two:
          NUM_LAYERS_LIST.append(layer_one)
          NUM_LAYERS_LIST.append(layer_two)
    else:
      generate_period()
    return NUM_LAYERS_LIST


def creatorNameLayer():
  generate_period()
  FILE_PATH_layerOne = os.path.join(DIR_PATH, f'{NUM_LAYERS_LIST[0]}' + '.png')
  FILE_PATH_layerTwo = os.path.join(DIR_PATH, f'{NUM_LAYERS_LIST[1]}' + '.png')
  NAME_LAYERS_LIST.insert(0, FILE_PATH_layerOne)
  NAME_LAYERS_LIST.insert(1, FILE_PATH_layerTwo)
  print(NAME_LAYERS_LIST)


if __name__ == '__main__':
    creatorNameLayer()


