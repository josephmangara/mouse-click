from pynput.mouse import Button, Controller

mouse = Controller()

# read pointer position 
print('the current pointer position is {}'.format(mouse.position))

mouse.position = (10, 20)
print('Now we have moved it to {0}'.format(
    mouse.position))

mouse.press(Button.left)
mouse.release(Button.left)

# monitoring mouse position 
def on_click(x,y, button, pressed, injected):
    print('{} at {}; it was {}'.format(
        'pressed' if pressed else 'released',
        (x,y, 'faked' if injected else "not faked")
    ))
    if not pressed:
        return False