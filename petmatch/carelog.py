#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="petmatch")
cur = con.cursor()
form = cgi.FieldStorage()
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Login</title>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
    crossorigin="anonymous"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css"
    integrity="sha512-5A8nwdMOWrSz20fDsjczgUidUBR8liPYU+WymTZP1lmY9G6Oc7HlZv156XqnsgNUzTyMefFTcsFH/tnJE/+xBg=="
    crossorigin="anonymous" referrerpolicy="no-referrer"/>
    <style>
        .head {
            text-align: center;
        }
        .head a {
            color:black;
            text-decoration:none;
            font-family:Serif;
            font-size:150%;
        }
        .form {
            background-image: url('./background.jpg');
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-size: cover;
            background-position: center;
            height: 100vh; 
            display: flex;
            align-items: center; 
            justify-content: center;
        }
        form {
            display: flex;
            flex-direction: column; 
            justify-content: center;
            align-items: center;
            width: 100%; 
            max-width: 500px;
            padding: 2%;
            margin: auto;  
            border-radius: 10px; 
            background: rgba(255, 255, 255, 0.3);
        }
        .form-row {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            margin-bottom: 10px;
        }
        .form-row label {
            flex: 1;
            margin-right: 10px;
            font-family: Serif;
            font-size: 20px;
            color: black;
        }
        .form-row input {
            flex: 2;
            width: 100%;
        }
        .btn {
            width: 100%;
        }
    </style>
</head>

<body>
    <div class="head d-flex align-items-center">
  <div class="logo1">
    <img src="./logo.jpg" style="width:60px; height:60px;">
  </div>
  <ul class="nav ms-auto">
    <li class="nav-item dropdown">
      <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">Login</a>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="userlog.py">User</a></li>
         <li><a class="dropdown-item" href="shelterlog.py">Shelter</a></li>
          <li><a class="dropdown-item" href="carelog.py">Care center</a></li>
          <a class="nav-link active" aria-current="page" href="adminlog.py">Admin</a>
        
      </ul>
    </li>
    <li class="nav-item dropdown">
      <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">Registration</a>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="userreg.py">User</a></li>
        <li><a class="dropdown-item" href="shelterreg.py">Shelter</a></li>
        <li><a class="dropdown-item" href="carereg.py">Care center</a></li>
      </ul>
    </li>
  </ul>
</div>
        <div class="form">
            <center>
                <form class="row g-3" method="post" enctype="multipart/form-data">
                    <h2>CareCenter Login</h2>
                    <div class="form-row">
                        <label for="name" class="form-label">Username</label>
                        <input type="text" class="form-control" id="name" name="uname">
                    </div>
                    <div class="form-row">
                        <label for="pass" class="form-label">Password</label>
                        <input type="password" class="form-control" id="pass" name="pass">
                    </div>
                    <div class="col-12">
                        <input type="submit" class="btn btn-primary" name="login" value="Log in">
                    </div>
                    <a href="./fpass.py">Forgot Password</a>
                    <p>Don't have an account?<a href="./carereg.py">Register</a></p>
                </form>
            </center>
        </div>
    </body>
</html>
""")
username = form.getvalue('uname')
password = form.getvalue('pass')
login = form.getvalue('login')
if login != None:
    q = f"""select id from carereg where careid='%s' and password='%s'""" % (username, password)
    cur.execute(q)
    res = cur.fetchone()
    if res:
        print(f"""
                    <script>
                        alert("Login successful!");
                        location.href = "caredb.py?id={res[0]}";
                    </script>
                    """)
