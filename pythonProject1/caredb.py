#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe

print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="petmatch")
cur = con.cursor()
form = cgi.FieldStorage()
careid = form.getvalue('id')
q = f"""select Animal_id from addanimal"""
cur.execute(q)
animal = cur.fetchone()
if animal:
      ani_id= animal[0]
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
            <h2 style="color:white;">Care Center Dashboard</h2>
            <li><a href="careprofile.py?id={careid}">Profile</a></li>
            <li><a href="adopters.py?id={careid}&ani_id={ani_id}">Adopters</a></li>
             <li class="dropdown">
          <a class="nav-link dropdown-toggle" href="" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Tips for a pet
          </a>
          <ul class="dropdown-menu dropdown-menu-dark">
          <li><a class="dropdown-item" href="cctips.py?id={careid}">Give Your Tip</a></li>
            <li><a class="dropdown-item" href="extip.py?id={careid}">Existing Tip</a></li>
          </ul>
      </li>
            <li><a href="suggestions.py?id={careid}"">Suggestions</a></li>
            <li><a href="home.py">Log Out</a></li>
        </ul>
</div>
""")
q=f"""select Cname from carereg where id='%s'"""%(careid)
cur.execute(q)
name=cur.fetchone()
print(f"""
    <div class="content">
    <center>
        <h1>Welcome {name[0]}</h1>
    </center>  
    </div>
</body>
</html>
      """)