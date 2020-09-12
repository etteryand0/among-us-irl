greetings = '''Hello there!
    You can handle databse of tasks by this script
    Choose option you wanna use:
        1) Regenerate tasks database \x1b[31m(Warning! Your changes wont last!)\x1b[0m
        2) Append new task to tasks database
        3) Delete task from tasks database \x1b[31m(Warngin! You can`t recover deleted tasks!)\x1b[0m
        4) Spectate tasks database
        5) Redact task
'''

print(greetings)
# grab choice
method = input(str('Your choice: '))

# check if method is in range of valid methods
if valid := method not in map(str, 
                              range(1,5 + 1)):
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
    Database().append()
elif method == 3:
    # delete task
    Database().pop()
elif method == 4:
    # spectate tasks
    Database().spectate()
else:
    # redact task
    Database().redact()
