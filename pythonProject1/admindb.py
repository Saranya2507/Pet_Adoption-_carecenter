#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi,cgitb,pymysql
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="petmatch")
cur = con.cursor()
form = cgi.FieldStorage()
userid=form.getvalue('id')
shelterid=form.getvalue('id')
careid=form.getvalue('id')
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard</title>
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
</style>
</head>
<body>
<div class="sidebar">
    <ul>
            <h2 style="color:white;">Admin</h2>
            <li><a href="newuser.py"> Users</a></li>
      <li class="dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Shelter
          </a>
          <ul class="dropdown-menu dropdown-menu-dark">
            <li><a class="dropdown-item" href="shelternew.py">New Shelter</a></li>
            <li><a class="dropdown-item" href="shelterex.py">Existing Shelter</a></li>
            <li><a class="dropdown-item" href="shelterrej.py">Rejected Shelter</a></li>
          </ul>
      </li>
      <li class="dropdown">
        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Care Center
        </a>
          <ul class="dropdown-menu dropdown-menu-dark">
            <li><a class="dropdown-item" href="carenew.py">New CareCenter</a></li>
            <li><a class="dropdown-item" href="careex.py">Existing CareCenter</a></li>
            <li><a class="dropdown-item" href="carerej.py">Rejected CareCenter</a></li>
          </ul>
      </li>
      <li class="dropdown">
        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Adopt Detail
        </a>
          <ul class="dropdown-menu dropdown-menu-dark">
            <li><a class="dropdown-item" href="request.py">All Request</a></li>
            <li><a class="dropdown-item" href="accept.py">Accepted</a></li>
            <li><a class="dropdown-item" href="rejected.py">Rejected</a></li>
          </ul>
      </li>
            <li><a href="alltip.py">Tips</a></li>
            <li><a href="pet.py">Pets</a></li>
            <li><a href="home.py">Log Out</a></li>
    </ul>
</div>
    <div class="content">
    <center>
        <h1>Welcome to Dashboard</h1>
    </center>
    </div>
</body>
</html>
      """)