# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin?")) # Add the missing quotation mark and an extra equal sign.

''' if year < 1900: '''
if year <= 1900: # Add the missing colon.
    print("Woah, that's the past!") # Add the missing quotation marks.
'''elif year >= 1900 and year < 2020 : '''
elif year >= 1900 and year <= 2020: # Must add the word and to make the statement run.
    print("That's totally the present!")
'''else: '''
elif year >= 2020: # Add the statement to print the years that are in the future.
    print("Far out, that's the future!!")
