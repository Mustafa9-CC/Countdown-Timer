import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)       # convert seconds → minutes, seconds
        hrs, mins = divmod(mins, 60)     # convert minutes → hours, minutes
        timer = f"{hrs:02}:{mins:02}:{secs:02}"  # format as HH:MM:SS
        print(f"Countdown: {timer}", end="\r")   # overwrite same line
        time.sleep(1)
        t -= 1

    print("\nCountdown Complete! 🎉")

if __name__ == "__main__":
    user_time = int(input("Enter time in seconds: "))
    countdown(user_time)
