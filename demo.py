import datetime
from time import sleep

# from displayLED import *
from mediaAPI import *
from scheduleAPI import *


def initialize_demo_schedule():
	demo_schedule = read_schedule('./data/demo_schedule')
    
	add_to_schedule("09:50", "Game 1", demo_schedule, './data/demo_schedule')
	add_to_schedule("14:15", "Game 2", demo_schedule, './data/demo_schedule')
	add_to_schedule("16:45", "Game 3", demo_schedule, './data/demo_schedule')
	add_to_schedule("21:00", "Game 4", demo_schedule, './data/demo_schedule') 
    
	return demo_schedule
    
    
def main():
	schedule = initialize_demo_schedule()
	
	hourly_alert = 1  # alerts once for a certain hour
	activity_alert = 1  # alerts once for a certain activity
	
	timing_list = ['09:50', '09:55', '10:00']
	timing_size = len(timing_list)
	time_index = 0
    
	while True:
		sleep(10)
		current_time = timing_list[time_index]
		time_index = (time_index + 1) % timing_size
        
		if timing_exists(current_time, schedule):
			"""
			If there is an activity, the robot will be blocked until the activity is finished.
			"""
			
			if activity_alert:
				activity_alert = 0
				print_timing_activity(current_time, schedule[current_time])
				#displayLED(0)
				play_audio('./sounds/activity.wav')
				# TODO: Insert while loop for game here.
				# TODO: Add in noise and action if activity is not completed.
                
		else:
			"""
			If there is no activity, the robot acts like a clock with hourly updates.
			"""
			
			activity_alert = 1
			
			if current_time[3:5] == '00':  # if it is a full hour timing
				if hourly_alert:
					hourly_alert = 0
					#displayLED(3)
					# TODO: Add in noise and action.
					print_timing(current_time)
					play_audio('./sounds/hourly.wav')
			else:
				hourly_alert = 1
				#displayLED(2)
				play_audio('./sounds/angry.wav')

        
if __name__ == "__main__":
	main()
	