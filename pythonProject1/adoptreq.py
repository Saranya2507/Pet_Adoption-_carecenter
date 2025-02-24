#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql,smtplib
from datetime import datetime
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="petmatch")
cur = con.cursor()
form = cgi.FieldStorage()
userid=form.getvalue('id')
shelterid = form.getvalue('id')
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shelter Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css"
        integrity="sha512-5A8nwdMOWrSz20fDsjczgUidUBR8liPYU+WymTZP1lmY9G6Oc7HlZv156XqnsgNUzTyMefFTcsFH/tnJE/+xBg=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />
        <style>
* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}
.sidebar {{
    width: 250px;
    height: 100vh;
    background-color: #333;
    position: fixed;
    top: 0;
    left: 0;
    padding-top: 20px;
}}

.sidebar ul {{
    list-style-type: none;
}}

.sidebar ul li {{
    padding: 15px;
    text-align: center;
}}

.sidebar ul li a{{
    color: white;
    text-decoration: none;
    display: block;
    font-size: 18px;
}}
.sidebar ul li a:hover {{
    background-color: #575757;
}}
.content {{
    margin-left: 250px;
    padding: 20px;
    font-family: Arial, sans-serif;
    align-item:center;
    justify-content:center;
}}
h1 {{
    font-size: 32px;
}}

p {{
    font-size: 18px;
}}
.content th{{
    background-color:pink;
}}
        </style>
</head>
<body>
 <div class="sidebar">
      <ul>
            <h2 style="color:white;">Shelter Dashboard</h2>
            <li><a href="profile.py?id={shelterid}"> Profile</a></li>
        <li class="dropdown-item">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Animal
          </a>
          <ul class="dropdown-menu dropdown-menu-dark">
            <li><a href="shelter.py?id={shelterid}">Add Animal</a></li>
            <li><a href="expet.py?id={shelterid}">Existing Pet</a></li>
          </ul>
        </li>
           <li class="dropdown-item">
          <a class="nav-link dropdown-toggle" href="" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Adopt Request
          </a>
          <ul class="dropdown-menu dropdown-menu-dark">
            <li><a href="adoptreq.py?id={shelterid}"> All Request</a></li>
            <li><a href="adoptaccept.py?id={shelterid}">Accepted</a></li>
            <li><a href="adoptrej.py?id={shelterid}">Rejected</a></li>
          </ul>
        </li>
             <li class="dropdown-item">
          <a class="nav-link dropdown-toggle" href="" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Questions & Replies
          </a>
        <ul class="dropdown-menu dropdown-menu-dark">
            <li><a href="questions.py?id={shelterid}">Questions Asked</a></li>
            <li><a href="replies.py?id={shelterid}">Replies</a></li>
        </ul>
        </li>
            <li><a href="home.py">Log Out</a></li>
      </ul>
</div>
    <div class="content">
        <h1 style="text-align:center;color:skyblue;">Adoption Request</h1>
                <table class="table table-bordered mt-4"border=1px;>
                    <tr>
                    <th>ID</th>
                    <th>Req.Date</th>
                    <th>Animal ID</th>
                    <th>Animal Name</th>
                    <th>Animal Image</th>
                    <th>User Name</b><br>
                    <th>User Image</th>
                    <th></th>
                    <th>More Detail</th>
""")
a=f"""select*from adopt where status='new'"""
cur.execute(a)
det=cur.fetchall()
j=1
for i in det:
    req_date= i[18].strftime('%d-%m-%Y')
    print(f"""
    <tr>
    <td>{j}</td>
   <td>{req_date}</td>
    <td>{i[2]}</td>
    <td>{i[3]}</td>
    <td><img src="{i[16]}" style="width:80px; height:80px;"></td>
    <td>{i[5]}</td>
    <td><img src="{i[4]}" style="width:80px; height:80px;"></td>""")
    j+=1
    print(f"""
    <td>
           <form method="post">
                <input type="hidden" name="action" value="accept">
                <input type="hidden" name="animal_id" value="{i[2]}">
                <input type="submit" class="btn btn-success" value="Accept">
            </form>
            <form method="post">
                <input type="hidden" name="action" value="reject">
                <input type="hidden" name="animal_id" value="{i[2]}">
                <input type="submit" class="btn btn-danger"value="Reject">
            </form>
    </td>
        </td>
        <td>
        <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal{i[0]}">
            Read More
        </button>
        </td>
    </td>
    </tr>
    <div class="modal fade" id="myModal{i[0]}" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLongTitle">Details for {i[1]} {i[2]}</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <h1>Animal Details</h1>
                        <b>Shelter ID:</b> {i[1]} <br>
                        <b>Animal ID:</b> {i[2]}<br>
                        <b>Animal Name:</b> {i[3]}<br>
                        <b>Animal Image:</b><br>
                        <img src="{i[16]}" style="width:100px; height:100px;"><br>
                        <h1>User Details</h1>
                        <img src="{i[4]}" style="width:100px; height:100px;"><br>
                        <b>Name:</b> {i[5]} <br>
                        <b>DOB:</b> {i[7]} <br>
                        <b>Email ID:</b> {i[8]} <br>
                        <b>Address:</b> {i[9]}, {i[10]}, {i[11]}, {i[12]}, {i[13]} <br>
                </div>
            </div>
        </div>
    </div>
    """)
action=form.getvalue('action')
ani_id=form.getvalue('animal_id')
if action and ani_id:
    current_time = datetime.now().strftime('%Y-%m-%d')
    if action == "accept":
        s=f"""select Fname,Email,Animal_name from adopt where Animal_id='{ani_id}'"""
        cur.execute(s)
        det = cur.fetchall()
        if det is not None:
            name = det[0]
            Email = det[0][1]
            ani_name=det[0][2]
            update = f"""update adopt set status='accepted',action_date='{current_time}' where Animal_id='%s'""" % (ani_id)
            cur.execute(update)
            con.commit()
            fromadd = "ssaranya0549@gmail.com"
            password1 = "htws rdcr qdtw hsfn"
            toadd = Email
            subject = """Adoption Request Accepting"""
            body = f""" Hi {name}!Your adoption request for the {ani_name} has been accepted,Thank You for adopting!!!"""
            msg = f"""Subject:{subject}\n\n{body}"""
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(fromadd, password1)
            server.sendmail(fromadd, toadd, msg)
            server.quit()
            print("""
                   <script>
                   alert("Mail send");
                   </script>
            """)
if action=="reject":
        u= f"""update adopt set status='rejected',action_date='{current_time}' where Animal_id='%s'""" % (ani_id)
        cur.execute(u)
        con.commit()
        print(f"""
            <script>
                alert("Rejected");
            </script>
        """)
print("""
                </table>
            </div>
        </div>
    </div>
</body>
</html>
""")