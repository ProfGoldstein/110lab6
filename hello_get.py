#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')
quant = form.getvalue('quant')
unit_cost = form.getvalue('unit_cost')
total = int(quant) * float(unit_cost)

print ("Content-Type: text/html\n")
print ("<html>")
print ("<head><title>Welcome!</title></head>")
print ("<body>")
print ("<h1>We Welcome You To CSIS110</h1>")
print ("<h2>Hello ", first_name,  last_name,  "</h2>")
print ("<h2>Total:", quant, " @ ", unit_cost, " = ", total, "</h2>")
print ('</body>')
print ('</html>')
