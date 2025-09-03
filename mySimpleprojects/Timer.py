import  time

print("⏳Welcome to the pomodoro timer!")
timeInMinute= int(input("Enter time in minutes: \n"))

timeInsecs = timeInMinute * 60
while(timeInsecs>0) :
    mins = timeInsecs // 60
    secs = timeInsecs % 60

    clock = f"{mins : 02d} : {secs: 02d}"

    print(f"\r time remaining:{clock} " , end = "")
    time.sleep(1)
    timeInsecs-=1

print("Time's up ! take a break.")
