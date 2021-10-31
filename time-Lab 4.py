currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait") # Add a parenthesis since it is missing

currentTimeInt = int(currentTimeStr) # Fix the name since it was a grammar mistake
waitTimeInt = int(waitTimeStr) # Fix the name since it was a grammar mistake

'''
Logic error: finalTime_Int shows the time in hours 0-23.
finalTime_Int = (currentTimeInt + waitTimeInt) % 24
'''

finalTime_Int = (currentTimeInt + waitTimeInt) # Missing the parenthesis
# Also to fix the name for line 7 since it was missing a underscore
print(finalTime_Int)
