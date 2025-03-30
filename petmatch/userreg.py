#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql,os,re
from datetime import datetime
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
    <title>Shelter Registration</title>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
            crossorigin="anonymous"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css"
          integrity="sha512-5A8nwdMOWrSz20fDsjczgUidUBR8liPYU+WymTZP1lmY9G6Oc7HlZv156XqnsgNUzTyMefFTcsFH/tnJE/+xBg=="
          crossorigin="anonymous" referrerpolicy="no-referrer"/>
</head>
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
        height: 100%;
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
        padding: 2%;
        margin: auto;
        border-radius: 10px;
        background: rgba(255, 255, 255, 0.3);
    }
    form p {
        color:black;
    }
    label {
        color:black;
        font-family:Serif;
        font-size:20px;
        margin-right: 10px;
        display: inline-block;
        width: 150px;
    }
    .input-group {
        display: flex;
        align-items: center;
        margin-bottom: 15px;
    }
    .input-group input {
        width: 100%;
    }
</style>

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
<br>
<div class="form">
    <center><br>
        <form class="row g-3" method="post"enctype="multipart/form-data">
            <h2>User Registration</h2>
            <div class="input-group">
                <label>User Image:</label>
                <input type="file" class="form-control" name="img" required>
            </div>
            <div class="input-group">
                <label for="FName" class="form-label">First Name</label>
                <input type="text" class="form-control" id="FName" name="FName" required>
            </div>
            <div class="input-group">
                <label for="LName" class="form-label">Last Name</label>
                <input type="text" class="form-control" id="LName" name="LName" required>
            </div>
            <div class="input-group">
                <label for="Dob" class="form-label">Date of Birth:</label>
                <input type="date" class="form-control" id="Dob" name="Dob" required>
            </div>
            <div class="input-group">
                <label for="Email" class="form-label">Email</label>
                <input type="email" class="form-control" id="Email" name="email" required>
            </div>
            <div class="input-group">
                <label for="door" class="form-label">Door No</label>
                <input type="text" class="form-control" id="door" name="door" required>
            </div>
            <div class="input-group">
                <label for="Address1" class="form-label">Address 1</label>
                <input type="text" class="form-control" id="Address1" name="add1" required>
            </div>
            <div class="input-group">
                <label for="Address2" class="form-label">Address 2</label>
                <input type="text" class="form-control" id="Address2" name="add2" required>
            </div>
            <div class="input-group">
                <label for="City" class="form-label">City</label>
                <input type="text" class="form-control" id="City" name="city" required>
            </div>
            <div class="input-group">
                <label for="State" class="form-label">State</label>
                <input type="text" class="form-control" id="state" name="state" required>
            </div>
            <div class="input-group">
                <label for="country" class="form-label">Country</label>
                <input type="text" class="form-control" id="country" name="country" required>
            </div>
            <div class="input-group">
                <label for="username" class="form-label">Username</label>
                <input type="text" class="form-control" id="username" name="username" required>
            </div>
            <div class="input-group">
                <label for="password" class="form-label">Password</label>
                <input type="password" class="form-control" id="password" name="password" required>
            </div>
            <div class="col-12">
                <input type="submit" class="btn btn-primary" value="Register" name="register">
            </div>
            <p>Already have an account?<a href="./userlog.py">Login</a></p>
        </form>
    </center>
</div>
</body>
</html>
""")
submit = form.getvalue("register")
if submit != None:
    img2 = form['img']
    if img2.filename:
        pi2 = os.path.basename(img2.filename)
        open(f"proof/{pi2}", "wb").write(img2.file.read())
    fname=form.getvalue('FName')
    lname=form.getvalue('LName')
    DOB= form.getvalue('Dob')
    email=form.getvalue('email')
    door=form.getvalue('door')
    address1=form.getvalue('add1')
    address2=form.getvalue('add2')
    city=form.getvalue('city')
    state=form.getvalue('state')
    country=form.getvalue('country')
    username=form.getvalue('username')
    password=form.getvalue('password')
    q="""select(select count(*) from userreg where Email=%s) +(select count(*) from shelterreg where Email=%s) +(select count(*) from carereg where Email=%s) AS email_count"""
    cur.execute(q, (email, email, email))
    result = cur.fetchone()
    email_exists = result[0]
    dob = (datetime.now().replace(year=datetime.now().year - 18)).strftime('%Y-%m-%d')
    if email_exists > 0:
        print("""
                <script>
                    alert("This email is already registered in another account.");
                </script>
            """)
    elif DOB >dob:
        print("""
                            <script>
                                alert("your age should be greater than 18");
                            </script>
                     """)
    else:
            registration_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            query = f"""insert into userreg(image,Fname,Lname,DOB, Email, Door_no, Address1, Address2, city, state, country, username, password,registration_time) values('{pi2}','{fname}','{lname}','{DOB}', '{email}', '{door}', '{address1}', '{address2}', '{city}', '{state}', '{country}', '{username}', '{password}','{registration_time}')"""
            cur.execute(query)
            con.commit()
            print("""
                <script>
                alert("Registered successfully");
                </script>
                """)
