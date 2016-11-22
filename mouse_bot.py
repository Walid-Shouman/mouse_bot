import time             # have a timed loop
import pyautogui        # deal with the mouse
import argparse         # parse the arguments
import pyautogui.tweens # else we aren't able to use tweens

def main():

    req_time_in_min=.2

    parser = argparse.ArgumentParser(prog='mouse_bot')
    parser.add_argument('--time', dest='req_time_in_min', type=float)
    args = parser.parse_args()

    print args
    if args.req_time_in_min:
        req_time_in_min = args.req_time_in_min
    print req_time_in_min

    currentMouseX, currentMouseY = pyautogui.position()

    initial_message(currentMouseX, currentMouseY)
    # manual action_loop
    # action_loop(currentMouseX, currentMouseY, req_time_in_min)

    # automatic action_loop
    action_loop_auto(req_time_in_min=req_time_in_min, stop=.155555)

    final_message()

def initial_message(cmx, cmy):
    print "Mouse started at ({cmx}, {cmy}).".format(cmx=cmx, cmy=cmy)

def final_message():
    print "Done with execution!"

# Deprecated function
def action_loop(cmx, cmy, req_time_in_min=.2, deltax=5, deltay=40, stop=5, update_from_gui=True):
    # req_time_in_min of 2 gives a loop of 2 minutes
    timeout = time.time() + 60*req_time_in_min

    while True:
        if time.time() > timeout:
            break

        if update_from_gui:
            currentMouseX, currentMouseY = pyautogui.position()
            cmx, cmy = [currentMouseX, currentMouseY]

        for i in range(stop):
            if update_from_gui:
                currentMouseX, currentMouseY = pyautogui.position()
            pyautogui.moveTo(cmx + i*deltax, cmy + i*deltay)

        for i in range(stop):
            if update_from_gui:
                currentMouseX, currentMouseY = pyautogui.position()
            pyautogui.moveTo(cmx - i*deltax, cmy - i*deltay)

def action_loop_auto(destx=200, desty=200, stop=2, req_time_in_min=5):
    timeout = time.time() + 60*req_time_in_min

    tween=tween_strategy('linear')

    cmx, cmy = pyautogui.position()

    while True:
        if time.time() > timeout:
            break

        pyautogui.moveTo(cmx+destx, cmy+desty, stop, tween)
        pyautogui.moveTo(cmx, cmy, stop, tween)

def tween_strategy(strategy):
    if strategy == 'linear':
        return pyautogui.tweens.linear
    elif strategy == 'easeInQuad':
        return pyautogui.tweens.easeInQuad
    elif strategy == 'easeInOutQuad':
        return pyautogui.tweens.easeInOutQuad
    elif strategy == 'easeInOutSine':
        return pyautogui.tweens.easeInSine
    else:
        print 'Error: Invalid option to tween_strategy, fallback to linear'
        return pyautogui.tweens.linear


if __name__ == '__main__':
    main()
