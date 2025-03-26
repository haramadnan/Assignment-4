import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)  # MM:SS format
        print(timer, end="\r")  # Overwrite previous output
        time.sleep(1)  # Delay
        seconds -= 1
    print("00:00 \n ⏳ Time's Up!")

total_seconds = int(input("Enter the time in seconds: "))
countdown_timer(total_seconds)