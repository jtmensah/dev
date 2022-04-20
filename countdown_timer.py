'''
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Timer completed!")

t = input("Enter the time in seconds: ")

countdown(int(t))



def main_timer(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t += 1

    print("Timer completed!")

main_timer(15)
'''

'''
current_time = dt.datetime.now().strftime("%X")
print("Start Time")
print(current_time)
current_seconds = int(dt.datetime.now().strftime("%S"))

while current_seconds > 1:
    current_seconds += 1
    time.sleep(1)
    print(current_seconds)
'''

import datetime as dt

def show_time():
    current_time = dt.datetime.now().strftime("%X")
    label = Label(root, text=current_time)
    label.pack()