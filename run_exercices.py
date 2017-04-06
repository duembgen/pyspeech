#!/usr/bin/env python
import argparse
parser = argparse.ArgumentParser('Run exercice from "46 simple pyhton exercices"')
parser.add_argument('--number',type=int, help='number of exercice to run')

def spell_out_loud(filename, pause_words, pause_letters):
    import time
    import subprocess
    d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
         'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
         'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
         's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey',
         'x':'x-ray', 'y':'yankee', 'z':'zulu'}
    if filename[-3:]=="txt":
        f = open(filename, 'r')
        text = f.read()
    elif filename[-3:]=="png":
        import pytesseract
        from PIL import Image, ImageEnhance, ImageFilter
        im = Image.open(filename)
        im = im.convert('RGB')
        im = im.filter(ImageFilter.MedianFilter())
        enhancer = ImageEnhance.Contrast(im)
        im = enhancer.enhance(2)
        im = im.convert('1')
        im.save('result.jpg')

        text = pytesseract.image_to_string(Image.open('result.jpg'))
        print(text)

    for s in text:
        print(s.lower())
        if s == " ":
            time.sleep(pause_words)
        else:
            p1 = subprocess.Popen(["echo", d[s.lower()]], stdout=subprocess.PIPE)
            p2 = subprocess.Popen(["festival", "--tts"], stdin=p1.stdout, stdout=subprocess.PIPE)
            output,err = p2.communicate()

def run_exercice(number):
    if (number == 35):
        print('running exercice 35')
        #input_ = input('Please enter the filename of the text you would like to spell')
        #input_ = "test.txt"
        input_ = "love.png"
        input_ = "input.png"
        input_ = "test.png"
        spell_out_loud(input_, 0.01, 0.1)

    elif (number == 39):
        print('running exercice 39')
        import numpy as np
        n_low = 0
        n_high = 20
        max_trials = 10
        n = np.random.randint(n_low, n_high)

        guess = input('I am thinking of a number between {} and {}. Guess!'.format(n_low, n_high))
        counter = 0
        while counter < max_trials:
            if guess <= n:
                guess = input('Too low, try again')
            elif guess >= n:
                guess = input('Too high, try again')
            else:
                print('Well done, you got it right!')
                break
        again = input('Too bad, you used up all your trials. Play again?')
        if (again == ['y','Y',1,'yes']).any():
            run_exercice(39)
        else:
            return

if __name__=="__main__":
    args = parser.parse_args()
    #run_exercice(args.number)
    run_exercice(35)
