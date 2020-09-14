greetings = '''Hello there!
    You can handle databse of tasks by this script
    Choose option you wanna use:
        1) Regenerate tasks table \x1b[31m(Warning! Your changes wont last!)\x1b[0m
        2) Append new task to tasks table
        3) Delete task from tasks table \x1b[31m(Warnging! You can`t recover deleted tasks!)\x1b[0m
        4) Inspect tasks table
        5) Redact tasks table
        6) Clear game sessions table \x1b[31m(Warning! You can`t recover deleted sessions!)\x1b[0m
        7) Redact default game rules table
'''

print(greetings)
# grab choice
method = input(str('Your choice: '))

# check if method is in range of valid methods
if valid := method not in map(str, 
                              range(1,7 + 1)):
    # method is not in range of possible methods. Abort
    import sys
    sys.exit('\x1b[31mFatal error! Invalid method! \x1b[0m')
else:
    # method is valid. Let`s prepare it for if else logics
    method = int(method)

    # and import tasks.Database() 
    from tasks import Database

if method == 1:
    # regenerate database
    Database().regenerate()
elif method == 2:
    # add new task
    Database().append_task()
elif method == 3:
    # delete task
    Database().pop_task()
elif method == 4:
    # spectate tasks
    Database().spectate_tasks()
elif method == 5:
    # redact tasks
    Database().redact()
elif method == 6:
    # clear game sessions
    Database().clear_sessions()
elif method == 7:
    # redact default game rules
    Database().redact_rules()
