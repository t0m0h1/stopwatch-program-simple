import time
#time module 

#timer bits

start_time = time.time()
last_time = start_time
lap_num = 1

x = input("welcome to the stopwatch, press enter to count laps.")

print(x + "use conrtol+C to stop")

try:
    while True:
        input()
        laptime=round((time.time() - last_time), 2)
        total_time=round((time.time() - start_time), 2)

        print("Lap number "+str(lap_num))
        print("Total time: "+ str(total_time))
        print("Lap time: "+str(laptime))

        print("*"*20)


        last_time = time.time()
        lap_num = lap_num + 1

except KeyboardInterrupt:
    print("   cool story,  cya soon!   ")




#the number of key presses (Enter) determines the number of laps, 
#this program will calculate the intervals


