#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql,os
from datetime import datetime
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="petmatch")
cur = con.cursor()
form = cgi.FieldStorage()
print(f"""
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
        crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<style>
    .head {{
        text-align: center;
    }}
    .head a {{
        color: black;
        text-decoration: none;
        font-family: Serif;
        font-size: 150%;
    }}
    .form {{
        background-image: url('./background.jpg');
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-size: cover;
        background-position: center;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }}
    form {{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 100%;
        max-width: 900px;
        padding: 2%;
        margin: auto;
        border-radius: 10px;
        background: rgba(255, 255, 255, 0.3);
    }}
    form p {{
        color: black;
    }}
    .form-row {{
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        margin-bottom: 10px;
    }}
    .form-row label {{
        flex: 1;
        margin-right: 10px;
        font-family: Serif;
        font-size: 20px;
        color: black;
    }}
    .form-row input {{
        flex: 2;
        width: 100%;
    }}
    .btn {{
        width: 100%;
    }}
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
            <center><br>
                <form method="post" enctype="multipart/form-data">
                    <h1>Care Center Registration</h1>
                    <hr>
                    <h3>Basic Information</h3>

                    <div class="form-row">
                        <input type="file" class="form-control" id="imge" name="img" placeholder="Care Center Image">
                    </div>
                    <div class="form-row">
                        <input type="text" class="form-control" id="name" name="name" placeholder="Care Center Name">
                    </div>
                    <div class="form-row">
                        <input type="text" class="form-control" id="regno" name="regno" placeholder="Certificate Reg.No">
                    </div>
                    <div class="form-row">
                        <input type="text" class="form-control" id="hour" name="hour" placeholder="Operating Hours">
                    </div>
                    <div class="form-row">
                        <input type="text" class="form-control" id="day" name="day" placeholder="Operating Days">
                    </div>
                    <hr>

                    <h3>Contact Information</h3>
                    <div class="form-row">
                        <input type="tel" class="form-control" id="phno" name="phno" placeholder="Phone Number">
                    </div>
                    <div class="form-row">
                        <input type="tel" class="form-control" id="altphno" name="altphno" placeholder="Alternate PhoneNumber">
                    </div>
                    <div class="form-row">
                        <input type="email" class="form-control" id="email" name="email"placeholder="Email">
                    </div>
                    <div class="form-row">

                        <input type="text" class="form-control" id="link" name="link" placeholder="Website Link">
                    </div>
                    <hr>

                    <h3>Care Center Location</h3>
                    <div class="form-row">
                        <input type="text" class="form-control" id="inputdoor" name="door" placeholder="Door no">
                    </div>
                    <div class="form-row">
                        <input type="text" class="form-control" id="inputAddress1" name="add1" placeholder="Address1">
                    </div>
                    <div class="form-row">
                        <input type="text" class="form-control" id="inputAddress2" name="add2" placeholder="Address2">
                    </div>
                    <div class="form-row">
                        <input type="text" class="form-control" id="City" name="city" placeholder="City">
                    </div>
                    <div class="form-row">
                        <input type="text" class="form-control" id="State" name="state" placeholder="State">
                    </div>
                    <div class="form-row">
                        <input type="number" class="form-control" id="code" name="code" placeholder="Code">
                    </div>

                    <hr>
                    <h3>Veterinarian Information</h3>
                    <div class="form-row">
                        <input type="text" class="form-control" id="vname" name="vname" placeholder="Veterinarian Nmae">
                    </div>
                    <div class="form-row">
                        <input type="date" class="form-control" id="dob" name="dob" placeholder="Date of Birth">
                    </div>
                    <div class="form-row">
                        <input type="text" class="form-control" id="qual" name="qual" placeholder="Qualification">
                    </div>
                    <div class="form-row">
                        <input type="text" class="form-control" id="spec" name="spec" placeholder="Specialization">
                    </div>
                    <div class="form-row">
                        <input type="text" class="form-control" id="expr" name="expr" placeholder="Experience">
                    </div>

                    <div class="col-4">
                        <input type="submit" class="btn btn-primary" value="Sign Up" name="reg">
                    </div>
                    <p>Already have an account? <a href="./carelog.py">Login</a></p>
                </form>
            </center>
        </div>
    </body>
</html>
""")
if len(form) != 0:
    submit = form.getvalue("reg")
    if submit!= None:
        Cname=form.getvalue('name')
        Regno=form.getvalue('regno')
        Hours=form.getvalue('hour')
        Days=form.getvalue('day')
        Phno=form.getvalue('phno')
        Altphno=form.getvalue('altphno')
        Email=form.getvalue('email')
        Weblink=form.getvalue('link')
        Doorno=form.getvalue('door')
        Address1=form.getvalue('add1')
        Address2=form.getvalue('add2')
        City=form.getvalue('city')
        State=form.getvalue('state')
        Code=form.getvalue('code')
        VName=form.getvalue('vname')
        DOB = form.getvalue('dob')
        Qualification=form.getvalue('qual')
        Specialize=form.getvalue('spec')
        Experience=form.getvalue('expr')
        img=form['img']
        j=f"""select count(*) from carereg where Phno = '{Phno}' or Altphno = '{Altphno}'"""
        cur.execute(j)
        phone = cur.fetchone()
        phno=phone[0]
        dob_limit = (datetime.now().replace(year=datetime.now().year - 18)).strftime('%Y-%m-%d')
        if DOB>dob_limit:
            print("""
                <script>
                    alert("Your age should be greater than 18.");
                    window.location.href = "carereg.py";
                </script>
            """)
            exit()

        q = """select(select count(*) from userreg where Email=%s) +(select count(*) from shelterreg where Email=%s) + (select count(*) from carereg where Email=%s) AS email_count"""
        cur.execute(q, (Email, Email, Email))
        result = cur.fetchone()
        email_exists = result[0]
        if email_exists > 0:
            print("""
                                   <script>
                                       alert("This email is already registered in another account.");
                                   </script>
                               """)
        if phno>0:
            print("""
                <script>
                    alert("Phone number already exists. Please use a different phone number.");
                    location.href="carereg.py";
                </script>
            """)
        reg_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if img.filename and reg_time:
            pi = os.path.basename(img.filename)
            open(f"proof/{pi}", "wb").write(img.file.read())
        s=f"""insert into carereg (Image, Cname, DOB, Regno, Hours, Days, Phno, Altphno, Email, Link, Door_no, Address1, Address2, City, State, Code, Vname, Qualification, Specialize, Experience, status,registration_time) values ('{pi}', '{Cname}', '{DOB}', '{Regno}', '{Hours}', '{Days}', '{Phno}', '{Altphno}', '{Email}', '{Weblink}', '{Doorno}', '{Address1}', '{Address2}', '{City}', '{State}', '{Code}', '{VName}', '{Qualification}', '{Specialize}', '{Experience}', 'new','{reg_time}')"""
        cur.execute(s)
        con.commit()
        print("""
            <script>
                alert("Registered successfully");
               location.href="home.py";
            </script>
        """)
