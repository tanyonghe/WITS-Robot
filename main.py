import datetime as dt
from time import sleep

#from displayLED import *
import mediaAPI as mAPI
from scheduleAPI import *
import gui_activity as agui
    
    
def main():
	schedule = read_schedule('./data/schedule')
	
	hourly_alert = 1  # alerts once for a certain hour
	activity_alert = 1  # alerts once for a certain activity
    
	while True:
		current_time = dt.datetime.now().strftime("%H:%M")
		print_to_screen("Current Time: " + current_time)
        
		if timing_exists(current_time, schedule):
			"""
			If there is an activity, the robot will be blocked until the activity is finished.
			"""
			
			if activity_alert:
				activity_alert = 0
				print_timing_activity(current_time, schedule[current_time])
				#displayLED(0)
				mAPI.play_audio('./sounds/activity.wav')
				agui.initialize_gui(schedule[current_time])
				print_next_activity(current_time, schedule)				
                
		else:
			"""
			If there is no activity, the robot acts like a clock with hourly actions.
			"""
			
			activity_alert = 1
			
			if current_time[3:5] == '00':  # if it is a full hour timing
				if hourly_alert:
					hourly_alert = 0
					#displayLED(3)
					mAPI.play_audio('./sounds/hourly.wav')
			else:
				hourly_alert = 1
				#displayLED(2)
				
			sleep(1)
			clear_screen_text("Current Time: " + current_time)

        
if __name__ == "__main__":
	main()
