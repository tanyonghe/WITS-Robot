import datetime as dt
from time import sleep

import serial

import gui_activity as agui
import mediaAPI as mAPI
from scheduleAPI import *


arduinoSerialData = serial.Serial('/dev/ttyACM0', 9600)
sleep(2)
#arduinoSerialData = ""


def initialize_demo_schedule():
	demo_schedule = read_schedule('./data/demo_schedule')
    
	add_to_schedule("09:05", "Stretching Exercises", demo_schedule, './data/demo_schedule')
	add_to_schedule("09:35", "Play Power Shake Game", demo_schedule, './data/demo_schedule')
	add_to_schedule("16:45", "Strength Training", demo_schedule, './data/demo_schedule')
	add_to_schedule("21:00", "Time to bathe!", demo_schedule, './data/demo_schedule') 
    
	return demo_schedule
    
    
def main():
	schedule = initialize_demo_schedule()

	hourly_alert = 1  # alerts once for a certain hour
	activity_alert = 1  # alerts once for a certain activity
	
	seconds = 0
    
	while True:
		if seconds < 10:
			current_time = '09:0' + str(seconds)
		else:
			current_time = '09:' + str(seconds)
		seconds = (seconds + 1) % 60
        
		print_to_screen("Current Time: " + current_time)
        
		if timing_exists(current_time, schedule):
			"""
			If there is an activity, the robot will be blocked until the activity is finished.
			"""
			
			if activity_alert:
				activity_alert = 0
				print_timing_activity(current_time, schedule[current_time])
				arduinoSerialData.write(b'1')
				mAPI.play_audio('./sounds/activity.wav')
				agui.initialize_gui(arduinoSerialData, schedule[current_time])
				print_next_activity(current_time, schedule)
                
		else:
			"""
			If there is no activity, the robot acts like a clock with hourly actions.
			"""
			
			activity_alert = 1
			
			if current_time[3:5] == '00':  # if it is a full hour timing
				if hourly_alert:
					hourly_alert = 0
					arduinoSerialData.write(b'1')
					mAPI.play_audio('./sounds/hourly.wav')
			else:
				hourly_alert = 1
				
			sleep(1)
			clear_screen_text("Current Time: " + current_time)

        
if __name__ == "__main__":
	main()
