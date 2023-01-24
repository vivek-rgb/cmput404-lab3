#!/usr/bin/env python3
import os
import json
import cgi, cgitb
from urllib.parse import urlparse, parse_qs
import templates

# https://www.doppler.com/blog/environment-variables-in-python
env_vars = os.environ

# print("Content-Type: application/json")
# print()
# print(json.dumps(dict(env_vars)))



# Modify your CGI script to report the values of the query parameters in the HTML.
# form = cgi.FieldStorage()
# print("_"*80)
# print("Content-Type: application/json")
# print("<html><body>")
# for key in form.keys():
#     print("<p>{}: {}</p>".format(key, form[key].value))
# print("</body></html>")
# print("_"*80)

# print("Content-Type: text/html\n")
# print("<html><body>")
# print("<p>User's browser: {}</p>".format(os.environ['HTTP_USER_AGENT']))
# print("</body></html>")

cgitb.enable()

print("Content-type: text/html")
print()

form = cgi.FieldStorage()
print(templates.login_page())

