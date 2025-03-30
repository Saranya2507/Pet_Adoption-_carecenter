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
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css">

    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
        }}
        /* Navbar */
        .navbar {{
            background-color: #343a40;
        }}
        .navbar-brand, .navbar-nav .nav-link {{
            color: white;
            font-size: 18px;
        }}
        .navbar-nav .nav-link:hover {{
            color: #f8f9fa;
        }}
        .dropdown-menu-dark {{
            background-color: #343a40;
        }}
        .dropdown-menu-dark .dropdown-item {{
            color: white;
        }}
        .dropdown-menu-dark .dropdown-item:hover {{
            background-color: #495057;
        }}
        /* Dashboard Cards */
        .dashboard-card {{
            padding: 20px;
            border-radius: 10px;
            background: white;
            box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.1);
            text-align: center;
        }}
        .dashboard-card h3 {{
            font-size: 22px;
            margin-bottom: 10px;
        }}
        .dashboard-card p {{
            font-size: 18px;
            font-weight: bold;
            color: #007bff;
        }}
    </style>
</head>

<body>

    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Shelter Dashboard</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="profile.py?id={shelterid}">Profile</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="animalDropdown" role="button" data-bs-toggle="dropdown">
                            Animal
                        </a>
                        <ul class="dropdown-menu dropdown-menu-dark">
                            <li><a class="dropdown-item" href="shelter.py?id={shelterid}">Add Animal</a></li>
                            <li><a class="dropdown-item" href="expet.py?id={shelterid}">Existing Pet</a></li>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="adoptDropdown" role="button" data-bs-toggle="dropdown">
                            Adopt Request
                        </a>
                        <ul class="dropdown-menu dropdown-menu-dark">
                            <li><a class="dropdown-item" href="adoptreq.py?id={shelterid}">All Requests</a></li>
                            <li><a class="dropdown-item" href="adoptaccept.py?id={shelterid}">Accepted</a></li>
                            <li><a class="dropdown-item" href="adoptrej.py?id={shelterid}">Rejected</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="questions.py?id={shelterid}">Questions Asked</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-danger" href="home.py">Log Out</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
  <div class="content">
           <div class="table-responsive mt-4">
    <table class="table table-bordered">
        <thead class="table-dark">
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