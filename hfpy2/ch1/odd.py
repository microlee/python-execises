from datetime import datetime

odds = [x for x in range(1, 60, 2)]
right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print("Not an odd minute.")
