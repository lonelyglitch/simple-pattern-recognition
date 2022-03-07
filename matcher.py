from re import template
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from random import randint
import colorama
from os import listdir, startfile
from os.path import dirname, isfile

colorama.init(autoreset=True)

def check_file(filename):
   
    try :
        open(filename, 'r')
        print(colorama.Fore.GREEN + "File loaded successfully!")
        return True
    except:
        return False

def import_image():
    
    print(colorama.Fore.BLUE + "In which file would you like to search for image paterns?", end="\t")

    srcfile = input()
    while (check_file(srcfile) is False):
        print(colorama.Fore.RED + "FILE DOES NOT EXIST!", end="\n")
        print(colorama.Fore.BLUE + "In which file would you like to search for image paterns?", end="\t")
    
        srcfile = input()

    return srcfile

def input_num():

    print(colorama.Fore.BLUE + "Specify the threshold (0 to 1).\nConsider using 0.98 as it is the optimal ratio.", end="\t")
    inp = input()

    try: 
        num = float(inp)
        if (num <= 1 and num > 0):

            return num

        else: 

            print(colorama.Fore.YELLOW + "Threshold should be between 0 and 1.", end="\n")

            input_num()

    except:

        print("Incorrect input! only numbers from 0 to 1 supported.")
        
        input_num()


def listkeys():

    list = [f for f in listdir(pattern_dir) if ".png" in f and isfile(pattern_dir + "\\" + f)]
    file_list = [f.replace('.png', '') for f in list]

    return file_list

def init_process():

    threshold = input_num()

    for key in listkeys():
        
        searcher(key, threshold)
    
    cv.imwrite('result.png',img_rgb)
    startfile("result.png")

    print(colorama.Fore.MAGENTA + "A total of " + str(global_cntr) + " matches were found.", end="\n")
    print(colorama.Fore.CYAN + "Program Finished Successfully!", end="\n")

def searcher(key, threshold):

    template = cv.imread(pattern_dir + "\\" + key + ".png",0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    loc = np.where( res >= threshold)
    color = [randint(50, 100), randint(50, 100), randint(50, 100)]
    cntr = 0
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (color[0], color[1], color[2]), 1)
        cntr = cntr + 1

    global global_cntr
    global_cntr = global_cntr + cntr

    print(colorama.Fore.GREEN +  key + " = " + str(cntr), end="\n")

pattern_dir = dirname(__file__) + "//patterns"
global_cntr = 0
img_rgb = cv.imread(import_image())
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
init_process()