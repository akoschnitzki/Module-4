str_time = input("What time is it now?")
str_wait_time = input("What is the number of nours to wait?")
time = int(str_time)
wait_time = int(str_wait_time) # Fix the name since it is a grammar mistake

time_when_alarm_go_off = (time + wait_time) # Add parenthesis around them.
print(time_when_alarm_go_off)
