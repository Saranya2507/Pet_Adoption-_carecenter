#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql,os
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="petmatch")
cur = con.cursor()
form = cgi.FieldStorage()
shelterid=form.getvalue('id')
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
        *{{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}
.sidebar{{
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
        </style>
</head>
<body>
    <div class="sidebar">
      <ul>
            <h2 style="color:white;">Shelter Dashboard</h2>
            <li><a href="profile.py"> Profile</a></li>
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
            <li><a href="questions.py?id={shelterid}">Questions Asked</a></li>
            <li><a href="home.py">Log Out</a></li>
      </ul>
</div>
    <div class="content">
        """)
shelterid=form.getvalue('id')
s=f"""select*from shelterreg where id='%s'"""%(shelterid)
cur.execute(s)
v=cur.fetchall()
print(f"""
       <div class="form">
        <center>
        <form class="row g-3" method="post" enctype="multipart/form-data">
            <h3>Basic Information</h3>
            <div class="col-md-6">
                <label for="img" class="form-label">Shelter Image</label>
                <input type="file" class="form-control" id="img" name="img"><br>
                <img src="proof/{v[0][1]}" style="width: 100px; height: auto; margin-top: 10px;">
            </div>
            <div class="col-md-6">
                <label for="name" class="form-label">Name</label>
                <input type="text" class="form-control" id="name" name="name" value={v[0][2]}>
            </div>
            <div class="input-group">
                <label>Date Of Birth:</label>
                <input type="date" class="form-control" name="dob"value="{v[0][3]}">
            </div>
            <div class="col-md-6">
                <label for="regno" class="form-label">Register Number</label>
                <input type="text" class="form-control" id="regno" name="regno" placeholder="Certificate Reg.No" value={v[0][4]}>
            </div>
            <hr>
            <h3>Contact Information</h3>
            <div class="col-md-6">
                <label for="phno" class="form-label">Phone Number</label>
                <input type="tel" class="form-control" id="phno" name="phno" value={v[0][5]}>
            </div>
            <div class="col-6">
                <label for="altphno" class="form-label">Alternate Contact Number</label>
                <input type="tel" class="form-control" id="altphno" name="altphno" placeholder="Optional" value={v[0][6]}>
            </div>
            <div class="col-12">
                <label for="email" class="form-label">Email</label>
                <input type="email" class="form-control" id="email" name="email" value={v[0][7]}>
            </div>
            <hr>
            <h3>Shelter Location</h3>
            <div class="col-md-12">
                <label for="door" class="form-label">Door No </label>
                <input type="text" class="form-control" id="door" name="door" value={v[0][8]}>
            </div>
            <div class="col-md-12">
                <label for="inputAddress1" class="form-label">Address 1</label>
                <input type="text" class="form-control" id="inputAddress1" name="add1" value={v[0][9]}>
            </div>
            <div class="col-md-12">
                <label for="inputAddress2" class="form-label">Address 2</label>
                <input type="text" class="form-control" id="inputAddress2" name="add2" value={v[0][10]}>
            </div>
            <div class="col-md-4">
                <label for="City" class="form-label">City</label>
                <input type="text" class="form-control" id="City" name="city" value={v[0][11]}>
            </div>
            <div class="col-md-4">
                <label for="State" class="form-label">State</label>
                <input type="text" class="form-control" id="State" name="state" value={v[0][12]}>
            </div>
            <div class="col-md-4">
                <label for="code" class="form-label">Pincode</label>
                <input type="number" class="form-control" id="code" name="code" value={v[0][13]}>
            </div>
            <hr>
            <h3>Legal and Documentation Requirements</h3>
            <div class="col-md-6">
                <label for="license" class="form-label">License or Certification Documents</label>
                <input type="file" class="form-control" id="license" name="license"><br>
                 <img src="proof/{v[0][14]}" style="width: 100px; height: auto; margin-top: 10px;">
            </div>
            <div class="col-md-6">
                <label for="ins" class="form-label">Insurance Information</label>
                <input type="file" class="form-control" id="ins" name="ins"><br>
                 <img src="proof/{v[0][15]}" style="width: 100px; height: auto; margin-top: 10px;">
            </div>
            <div class="col-12">
                <input type="submit" class="btn btn-primary" name="upd" value="Update">
            </div>
        </form>
        </center>
    </div>
</body>
</html>
""")
if len(form) != 0:
    submit=form.getvalue('upd')
    if submit!=None:
        Name = form.getvalue('name')
        DOB=form.getvalue('dob')
        Regno = form.getvalue('regno')
        Phno = form.getvalue('phno')
        Altphno = form.getvalue('altphno')
        Email = form.getvalue('email')
        Doorno = form.getvalue('door')
        Address1 = form.getvalue('add1')
        Address2 = form.getvalue('add2')
        City = form.getvalue('city')
        State = form.getvalue('state')
        Pincode = form.getvalue('code')
        img = form['img']
        img1 = form['license']
        img2 = form['ins']
        if img.filename:
            pi2 = os.path.basename(img.filename)
            open("proof/" + pi2, "wb").write(img.file.read())
        else:
            pi2 = v[0][1]
        if img1.filename:
            pi = os.path.basename(img1.filename)
            open("proof/" + pi, "wb").write(img1.file.read())
        else:
            pi = v[0][13]

        if img2.filename:
            pi1 = os.path.basename(img2.filename)
            open("proof/" + pi1, "wb").write(img2.file.read())
        else:
            pi1 = v[0][14]
        update = """update shelterreg set image='%s',Name='%s',DOB='%s',Regno='%s',phno='%s',altphno='%s',Email='%s',Door_no='%s',Address1='%s',Address2='%s',city='%s',state='%s',code='%s',license_no='%s',insurance_no='%s' where id='%s'""" % (pi2, Name,DOB, Regno, Phno, Altphno, Email, Doorno, Address1, Address2, City, State, Pincode, pi,pi1,shelterid)
        cur.execute(update)
        con.commit()
        print(f"""
        <script>
            alert("updated");
            location.href='profile.py?id={shelterid}';
        </script>
        """)