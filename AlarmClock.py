import time
import datetime
import winsound

def myAlarm():
    try:
        set_alarm = list(map(int,input("Enter alarm time in hr min sec(hh:mm:ss)\n").split(':')))
        if len(set_alarm) == 3:
            alarm_time_sec = set_alarm[0]*60*60+set_alarm[1]*60+set_alarm[2]
            total_Sec = datetime.datetime.now().time().hour*3600 + \
                        datetime.datetime.now().time().minute*60 +\
                        datetime.datetime.now().time().second - \
                        alarm_time_sec
            if total_Sec < 0:
                total_Sec *= -1
            time.sleep(total_Sec)
            frequency = 2500
            duration = 3000
            winsound.Beep(frequency,duration)
            #winsound.PlaySound('Downloads\parasytewav.wav',winsound.SND_ASYNC)
        else:
            print("Incorrect time format (hh:mm:ss)")
            myAlarm()
    except Exception as e:
        print("Incorrect values for time given",e)
        myAlarm()
myAlarm()
