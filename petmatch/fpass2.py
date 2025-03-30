#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql,smtplib
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
            width: 150%; 
            padding:2%;
            margin: auto;  
            border-radius: 10px; 
            background: rgba(255, 255, 255, 0.3);
        }
         form p{
          color:black;
         }
          label {
            color:black;
            font-family:Serif;
            font-size:20px;
          }
          .form-control{
            width:150%;
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
          <div class="form">
            <center>
              <form class="row g-3"method="post">
                <h2>Retrieve Password</h2>
                <div class="col-md-4">
                  <label for="email" class="form-label">Email</label>
                  <input type="email" class="form-control" id="email" name="email">
                </div>
                <div class="col-12">
                  <input type="submit" class="btn btn-primary"name="submit"value="Submit">
                </div>
              </form>
            </center>
          </div><br>
</body>    
""")
Email=form.getvalue('email')
submit=form.getvalue('submit')
if submit!=None:
    q=f"""select password,username from carereg where Email='%s'"""%(Email)
    cur.execute(q)
    password= cur.fetchall()
    if password!=():
        username2=password[0][1]
        password2=password[0][0]
        fromadd="ssaranya0549@gmail.com"
        password1="htws rdcr qdtw hsfn"
        toadd=Email
        subject=" Your Password"
        body=f"Your Userid is{username2}\nPassword is{password2}"
        msg=f"""Subject:{subject}\n\n{body}"""
        server=smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(fromadd,password1)
        server.sendmail(fromadd,toadd,msg)
        server.quit()
        print("""
        <script>
        alert("Mail send");
        </script>
        """)
    else:
        print("""
                <script>
                alert("Mail ID Not in Database Please Register");
                </script>
        """)