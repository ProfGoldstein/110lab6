
#!/usr/bin/python
# Ira Goldstein
# CSIS110 Lab 6

# Python program that displays the current time

# Import the date/time library
import datetime

# Get the current date and time object
now = datetime.datetime.now()

# Format to show 12-hour time, minutes, and AM/PM (e.g., "12:06 PM")
current_time = now.strftime("%I:%M %p")

# Print out the required starting HTML
print("Content-Type: text/html\n")

# Print out the minimal opening tags
print("<html><body>")

# Display the text
print("Hello World!  It is now  ")

# Display the time
print(current_time)


# Closing HTML tags
print("</body></html>")
