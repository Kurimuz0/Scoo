from flask import *
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("MOE.html")

@app.route("/search", methods = ["POST"])
def search():
    connec = sqlite3.connect("School.db")
    data = request.form
    schoolname = data["SchoolName"]
    department = data["Department"]
    cursor = connec.execute("SELECT School.Name, Staff.Name, Staff.Department, Staff.Contact, School.Address FROM Staff, School WHERE Staff.Department = ? AND School.Name LIKE" + "?", (department,"%"+schoolname+"%"))
    lst_school = []
    lst_staff = []
    lst_department = []
    lst_contact = []
    lst_address = []
    for row in cursor:
        lst_school.append(row[0])
        lst_staff.append(row[1])
        lst_department.append(row[2])
        lst_contact.append(row[3])
        lst_address.append(row[4])
    
    return render_template("search.html", school = lst_school, staff = lst_staff, department = lst_department,
                           contact = lst_contact, address = lst_address)



if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)
