#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql,smtplib
from datetime import datetime
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="petmatch")
cur = con.cursor()
form = cgi.FieldStorage()
userid=form.getvalue('id')
shelterid=form.getvalue('id')
careid = form.getvalue('id')
w = """select*from shelterreg where status='accept'"""
cur.execute(w)
shelternew = cur.fetchall()
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
 <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css"
        integrity="sha512-5A8nwdMOWrSz20fDsjczgUidUBR8liPYU+WymTZP1lmY9G6Oc7HlZv156XqnsgNUzTyMefFTcsFH/tnJE/+xBg=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />
    <style>
        body {{
            font-family: Arial, sans-serif;
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
            padding: 0;
        }}
        .sidebar ul li {{
            padding: 15px;
            text-align: center;
        }}
        .sidebar ul li a {{
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
        }}
        @media (max-width: 768px) {{
            .sidebar {{
                width: 100%;
                height: auto;
                position: relative;
            }}
            .content {{
                margin-left: 0;
            }}
        }}
        .dropdown-menu {{
    background-color: #333 !important;
}}

.dropdown-item {{
    color: white !important;
}}

.dropdown-item:hover {{
    background-color: #575757 !important;
}}

    </style>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark d-lg-none">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">Admin</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item"><a class="nav-link" href="newuser.py">Users</a></li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="shelterDropdown" role="button" data-bs-toggle="dropdown">Shelter</a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="shelternew.py">New Shelter</a></li>
                        <li><a class="dropdown-item" href="shelterex.py">Existing Shelter</a></li>
                        <li><a class="dropdown-item" href="shelterrej.py">Rejected Shelter</a></li>
                    </ul>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="careDropdown" role="button" data-bs-toggle="dropdown">Care Center</a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="carenew.py">New CareCenter</a></li>
                        <li><a class="dropdown-item" href="careex.py">Existing CareCenter</a></li>
                        <li><a class="dropdown-item" href="carerej.py">Rejected CareCenter</a></li>
                    </ul>
                </li>
                 <li class="nav-item"><a class="nav-link" href="request.py">Adopt detail</a></li>
                
             <li class="dropdown">
        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Tips
        </a>
          <ul class="dropdown-menu dropdown-menu-dark">
            <li><a class="dropdown-item" href="alltip.py">Tips</a></li>
            <li><a class="dropdown-item" href="extips.py">Existing Tips</a></li>
          </ul>
      </li>
                <li class="nav-item"><a class="nav-link" href="pet.py">Pets</a></li>
                <li class="nav-item"><a class="nav-link" href="home.py">Log Out</a></li>
            </ul>
        </div>
    </div>
</nav>

<div class="sidebar d-none d-lg-block">
  
        <h2 style="color:white;">Admin</h2>
       <ul class="navbar-nav">
                <li class="nav-item"><a class="nav-link" href="newuser.py">Users</a></li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="shelterDropdown" role="button" data-bs-toggle="dropdown">Shelter</a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="shelternew.py">New Shelter</a></li>
                        <li><a class="dropdown-item" href="shelterex.py">Existing Shelter</a></li>
                        <li><a class="dropdown-item" href="shelterrej.py">Rejected Shelter</a></li>
                    </ul>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="careDropdown" role="button" data-bs-toggle="dropdown">Care Center</a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="carenew.py">New CareCenter</a></li>
                        <li><a class="dropdown-item" href="careex.py">Existing CareCenter</a></li>
                        <li><a class="dropdown-item" href="carerej.py">Rejected CareCenter</a></li>
                    </ul>
                </li>
              <li><a  href="request.py">Adopt detail</a></li>
             <li class="dropdown">
        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Tips
        </a>
          <ul class="dropdown-menu dropdown-menu-dark">
            <li><a class="dropdown-item" href="alltip.py">Tips</a></li>
            <li><a class="dropdown-item" href="extips.py">Existing Tips</a></li>
          </ul>
      </li>
                <li class="nav-item"><a class="nav-link" href="pet.py">Pets</a></li>
                <li class="nav-item"><a class="nav-link" href="home.py">Log Out</a></li>
            </ul>
</div>
  <div class="content">
        <h1 style="text-align:center;color:skyblue;">Existing Shelter</h1>
           <div class="table-responsive">
        <table class="table table-bordered">
                    <tr>
                    <th>ID</th>
                    <th>Reg.Date</th>
                    <th style="width:10%;">Image</th>
                    <th>Name</th>
                    <th>Register No</th>
                    <th>Phone Number</th>
                    <th>Alternate Number</th>
""")
j=1
for i in shelternew:
    action_date = i[20].strftime('%d-%m-%Y')
    reg_date = i[19].strftime('%d-%m-%Y')
    print(f"""
    <tr>
    <td>{j}</td>
    <td>{reg_date}</td>
    <td ><img src="{i[1]}" style="width:80%;height:80%;"></td>
    <td>{i[2]}</td>
    <td>{i[4]}</td>
    <td>{i[5]}</td>
    <td>{i[6]}</td>
    <td>
            <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal{i[0]}">
                Read More
            </button>
        </td>
    </tr>""")
    j+=1
    print(f"""
    <div class="modal fade" id="myModal{i[0]}" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLongTitle">Details for {i[2]}</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <center><img src="{i[1]}" style="width:50%;height:50%;"><br></center>
                    <b>Name:</b> {i[2]} <br>
                    <b>Register No:</b> {i[4]}<br>
                    <b>Phone Number:</b>{i[5]}<br>
                    <b>Alternate Number:</b>{i[6]}</br>
                    <b>Email ID:</b>{i[7]}</br>
                    <b>Address:</b>{i[8]},<br> {i[9]},<br> {i[10]}, <br>{i[11]},<br>{i[12]},<br>{i[13]}<br>
                    <b>Username:</b>{i[17]}<br>
                    <b>Password:</b>{i[18]}<br>
                    <b>Registered Date:</b>{reg_date}<br>
                    <b>Accepted Date:</b>{action_date}<br>
                   <form method="post" action="">
                        <div class="input-group">
                            <label><b>Password:</b></label>
                            <input type="text" class="form-control" name="pass" value="{i[18]}">
                            <input type="hidden" name="shelterid" value="{i[0]}">
                        </div>
                        <div class="col-12">
                            <input type="submit" class="btn btn-primary" name="upd" value="Update">
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
    """)
print("""
                </table>
            </div>
        </div>
    </div>
</body>
</html>
""")
submit=form.getvalue('upd')
if submit:
    Password=form.getvalue('pass')
    shelterid=form.getvalue('shelterid')
    update=f"""update shelterreg set password='%s' where id='%s'"""%(Password,shelterid)
    cur.execute(update)
    con.commit()
    s=f"""select Name,Email from shelterreg where id='%s'""" % (shelterid)
    cur.execute(s)
    det = cur.fetchone()
    if det is not None:
        name = det[0]
        Email = det[1]
        fromadd = "ssaranya0549@gmail.com"
        password1 = "htws rdcr qdtw hsfn"
        toadd = Email
        subject = """Regarding Password Updated"""
        body = f"""Your password has been updated and Your new password is :{Password}"""
        msg = f"""Subject:{subject}\n\n{body}"""
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(fromadd, password1)
        server.sendmail(fromadd, toadd, msg)
        server.quit()
        print(f"""
                <script>
                alert("Mail send");
                location.href="shelterex.py";
                </script>
                """)

