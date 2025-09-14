import keyboard as key


def test(event):
    print(event.scan_code)
key.on_press(test)

key.wait('esc')