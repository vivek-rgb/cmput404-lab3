import templates
import os
import secret
import cgi, cgitb

form = cgi.FieldStorage()
cgitb.enable()

print("Content-type: text/html")
# print()
# print(templates.secret_page(form.getvalue("username"), form.getvalue("password")))


cookies = cookies = os.environ.get("HTTP_COOKIE")
cookies = dict(c.split("=") for c in cookies.split(";"))
if secret.username == form.getvalue("username") and secret.password == form.getvalue("password"):
    # set a cookie
    print("Set-Cookie: logged_in=true")

    
    if "logged_in" in cookies and cookies["logged_in"] == "true":
        print(templates.secret_page(form.getvalue("username"), form.getvalue("password")))

elif "logged_in" in cookies and cookies["logged_in"] == "true":
        print(templates.secret_page(form.getvalue("username"), form.getvalue("password")))