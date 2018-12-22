import pickle


def timing_exists(timing, schedule):
    return timing in schedule
    
    
def update_schedule_file(file_name, schedule):
    with open(file_name, 'wb') as fp:
        pickle.dump(schedule, fp)
        fp.close()

    
def remove_from_schedule(timing, schedule, file_name):
    # add in regex to check timing
    if not timing_exists(timing, schedule):
        print("Error: No activity exists at that timing.")
    else:
        activity = schedule[timing]
        schedule.pop(timing)
        update_schedule_file(file_name, schedule)
        print(f"{activity} at {timing} successfully removed.")
    return
    
    
def add_to_schedule(timing, activity, schedule, file_name):
    # add in regex to check timing
    if timing_exists(timing, schedule):
        print("Error: An activity already exists at that timing.")
    else:
        schedule[timing] = activity
        update_schedule_file(file_name, schedule)
        print(f"{activity} at {timing} successfully added.")
    return


def read_schedule(file_name):
    try:
        with open(file_name, 'rb') as fp:
            schedule = pickle.load(fp)
            return schedule
    except:
        schedule = dict()
        update_schedule_file(file_name, schedule)
    
    
def test_case_1():
    test_schedule = read_schedule('test_schedule')
    
    # Expected to pass
    add_to_schedule("10:30:00", "Game 1", test_schedule, 'test_schedule')
    print(test_schedule)
    add_to_schedule("14:15:00", "Game 2", test_schedule, 'test_schedule')
    print(test_schedule)
    add_to_schedule("16:45:00", "Game 3", test_schedule, 'test_schedule')
    print(test_schedule)
    add_to_schedule("21:00:00", "Game 4", test_schedule, 'test_schedule')
    print(test_schedule)
    remove_from_schedule("16:45:00", test_schedule, 'test_schedule')
    print(test_schedule)
    
    # Expected to fail as timing already exists in schedule
    add_to_schedule("21:00:00", "Game 5", test_schedule, 'test_schedule')
    print(test_schedule)
    
    # Expected to fail as timing/activity does not exist
    remove_from_schedule("10:00:00", test_schedule, 'test_schedule')
    print(test_schedule)   
    
    return
    

# Uncomment to run test cases
# test_case_1()