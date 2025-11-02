#!/usr/bin/python
# Ira Goldstein
# CSIS110 Lab 6

# Python program that displays information about the server
# and about the browser

# Import the OS library
import os

# Print out the required starting HTML
print("Content-Type: text/html\n")
print("<html><body>")

# Header/Banner
print("<h1>Environment Variables</h1>")

# Loop over and print all of the environment data available
for key, value in os.environ.items():
    print("<p>", key, ":  ", value, "</p>")

# Closing HTML tags
print("</body></html>")
