import logging
import os
import pickle
import sys


path = './logs'
name = '/scheduleAPI.log'
access_rights = 0o755

try:  
    os.mkdir(path, access_rights)
except OSError:  
    pass
else:  
    logging.info("Successfully created the directory %s" % path)

logging.basicConfig(filename=path+name, filemode='w', format='%(asctime)s %(message)s', level=logging.INFO)


def print_next_activity(current_timing, schedule):
	timings = [key for (key, value) in sorted(schedule.items())]
	activities = [value for (key, value) in sorted(schedule.items())]
	timing_index = timings.index(current_timing)
	if timing_index + 1 >= len(activities):
		timing_index = 0
	else:
		timing_index += 1
	next_activity_text = "\nNext Activity: " + activities[timing_index] + " at " + timings[timing_index] + "\n"
	print_to_screen(next_activity_text)


def print_to_screen(text):
	sys.stdout.write(text)
	sys.stdout.flush()

	
def clear_screen_text(text):
	text_length = len(text)
	text_buffer = ' ' * text_length
	sys.stdout.write('\r')
	sys.stdout.write(text_buffer)
	sys.stdout.write('\r')
	sys.stdout.flush()


def print_timing_activity(timing, activity):
	timing_activity_text = "\nIt is now " + timing + ". Activity: " + activity + "\n"
	print_to_screen(timing_activity_text)

	
def print_timing(timing):
	timing_text = "Current Time: " + timing
	print_to_screen(timing_text)


def is_valid_time(timing):
	if len(timing) == 5:
		HH = timing[0:2]
		MM = timing [3:5]
		if HH.isdigit() and MM.isdigit():
			HH = int(HH)
			MM = int(MM)
		else:
			logging.info("HH and MM values should be numerical.")
			return False
		
		if HH < 24 or MM < 60:
			return True
		else:
			logging.info("HH should be below 24 and MM should be below 60.")
			return False
	else:
		logging.info("Timing should be in HH:MM format.")
		
	return False
	

def timing_exists(timing, schedule):
	return timing in schedule
    
    
def update_schedule_file(file_path, schedule):
	with open(file_path, 'wb') as fp:
		pickle.dump(schedule, fp)
		fp.close()

    
def remove_from_schedule(timing, schedule, file_path):
	if not is_valid_time(timing):
		logging.info(activity + " at " + timing + " is NOT successfully added.")
		return
		
	if not timing_exists(timing, schedule):
		logging.info("No activity exists at that timing.")
	else:
		activity = schedule[timing]
		schedule.pop(timing)
		update_schedule_file(file_path, schedule)
		logging.info(activity + " at " + timing + " successfully removed.")
		
	return
    
    
def add_to_schedule(timing, activity, schedule, file_path):
	if not is_valid_time(timing):
		logging.info(activity + " at " + timing + " is NOT successfully added.")
		return
	
	if timing_exists(timing, schedule):
		logging.info("An activity already exists at that timing.")
	else:
		schedule[timing] = activity
		update_schedule_file(file_path, schedule)
		logging.info(activity + " at " + timing + " successfully added.")
		
	return


def read_schedule(file_path):
	try:
		with open(file_path, 'rb') as fp:
			schedule = pickle.load(fp)
			return schedule
	except:
		schedule = dict()
		update_schedule_file(file_path, schedule)
		return schedule
    
    
def test_case_1():
	test_schedule = read_schedule('./data/test_schedule')
    
    # Expected to pass
	add_to_schedule("10:30", "Game 1", test_schedule, './data/test_schedule')
	logging.debug(test_schedule)
	add_to_schedule("14:15", "Game 2", test_schedule, './data/test_schedule')
	logging.debug(test_schedule)
	add_to_schedule("16:45", "Game 3", test_schedule, './data/test_schedule')
	logging.debug(test_schedule)
	add_to_schedule("21:00", "Game 4", test_schedule, './data/test_schedule')
	logging.debug(test_schedule)
	remove_from_schedule("16:45", test_schedule, './data/test_schedule')
	logging.debug(test_schedule)
    
    # Expected to fail as timing already exists in schedule
	add_to_schedule("21:00", "Game 5", test_schedule, './data/test_schedule')
	logging.debug(test_schedule)
    
    # Expected to fail as timing/activity does not exist
	remove_from_schedule("10:00", test_schedule, './data/test_schedule')
	logging.debug(test_schedule)   
    
	return
    

# Uncomment to run test cases
# test_case_1()