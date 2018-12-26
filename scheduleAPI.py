import pickle


def print_timing_activity(timing, activity):
	timing_activity_text = "It is now " + timing + ". Activity: " + activity
	print(timing_activity_text)

	
def print_timing(timing):
	timing_text = "It is now " + timing + "."
	print(timing_text)


def is_valid_time(timing):
	if len(timing) == 5:
		HH = timing[0:2]
		MM = timing [3:5]
		if HH.isdigit() and MM.isdigit():
			HH = int(HH)
			MM = int(MM)
		else:
			print("Error: HH and MM values should be numerical.")
			return False
		
		if HH < 24 or MM < 60:
			return True
		else:
			print("Error: HH should be below 24 and MM should be below 60.")
			return False
	else:
		print("Error: Timing should be in HH:MM format.")
		
	return False
	

def timing_exists(timing, schedule):
	return timing in schedule
    
    
def update_schedule_file(file_path, schedule):
	with open(file_path, 'wb') as fp:
		pickle.dump(schedule, fp)
		fp.close()

    
def remove_from_schedule(timing, schedule, file_path):
	if not is_valid_time(timing):
		print(activity, "at", timing, "is NOT successfully added.")
		return
		
	if not timing_exists(timing, schedule):
		print("Error: No activity exists at that timing.")
	else:
		activity = schedule[timing]
		schedule.pop(timing)
		update_schedule_file(file_path, schedule)
		print(activity, "at", timing, "successfully removed.")
		
	return
    
    
def add_to_schedule(timing, activity, schedule, file_path):
	if not is_valid_time(timing):
		print(activity, "at", timing, "is NOT successfully added.")
		return
	
	if timing_exists(timing, schedule):
		print("Error: An activity already exists at that timing.")
	else:
		schedule[timing] = activity
		update_schedule_file(file_path, schedule)
		print(activity, "at", timing, "successfully added.")
		
	return


def read_schedule(file_path):
	try:
		with open(file_path, 'rb') as fp:
			schedule = pickle.load(fp)
			return schedule
	except:
		schedule = dict()
		update_schedule_file(file_path, schedule)
    
    
def test_case_1():
	test_schedule = read_schedule('./data/test_schedule')
    
    # Expected to pass
	add_to_schedule("10:30", "Game 1", test_schedule, './data/test_schedule')
	print(test_schedule)
	add_to_schedule("14:15", "Game 2", test_schedule, './data/test_schedule')
	print(test_schedule)
	add_to_schedule("16:45", "Game 3", test_schedule, './data/test_schedule')
	print(test_schedule)
	add_to_schedule("21:00", "Game 4", test_schedule, './data/test_schedule')
	print(test_schedule)
	remove_from_schedule("16:45", test_schedule, './data/test_schedule')
	print(test_schedule)
    
    # Expected to fail as timing already exists in schedule
	add_to_schedule("21:00", "Game 5", test_schedule, './data/test_schedule')
	print(test_schedule)
    
    # Expected to fail as timing/activity does not exist
	remove_from_schedule("10:00", test_schedule, './data/test_schedule')
	print(test_schedule)   
    
	return
    

# Uncomment to run test cases
# test_case_1()