#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql,os
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="petmatch")
cur = con.cursor()
form = cgi.FieldStorage()
userid = form.getvalue('id')
w = """select*from userreg"""
cur.execute(w)
usernew = cur.fetchall()
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
            <h2 style="color:white;">User Dashboard</h2>
            <li><a href="usernew.py?id={userid}">Profile</a></li>
            <li><a href="pets.py?id={userid}">Pets</a></li>
            <li><a href="reply.py?id={userid}">Replies</a></li>
            <li><a href="tips.py?id={userid}">Tips for your pet</a></li>
            <li><a href="home.py?id={userid}">Log Out</a></li>
        </ul>
</div>
    <div class="content">
        """)
userid=form.getvalue('id')
s=f"""select*from userreg where id='%s'"""%(userid)
cur.execute(s)
v=cur.fetchall()
print(f"""
    <form class="row g-3"method="post" enctype="multipart/form-data">
        <div class="col-md-6">
                <label for="img" class="form-label">Shelter Image</label>
                <input type="file" class="form-control" id="img" name="img"><br>
                <img src="proof/{v[0][1]}" style="width: 100px; height: auto; margin-top: 10px;">
        </div>
        <div class="col-md-4">
          <label for="fname" class="form-label">First Name</label>
          <input type="text" class="form-control" id="fname" name="fname"value='{v[0][2]}'>
        </div>
        <div class="col-md-4">
          <label for="lname" class="form-label">Last Name</label>
          <input type="text" class="form-control" id="lname" name="lname"value='{v[0][3]}'>
        </div>
        <div class="input-group">
                <label for="Dob" class="form-label">Date of Birth:</label>
                <input type="date" class="form-control" id="Dob" name="Dob" value='{v[0][4]}'>
        </div>
        <div class="col-md-6">
          <label for="Email" class="form-label">Email</label>
          <input type="email" class="form-control" id="Email" name="email"value='{v[0][4]}'>
        </div>
        <div class="col-md-6">
          <label for="door" class="form-label">Door No </label>
          <input type="text" class="form-control" id="door" name="door"value='{v[0][5]}'>
        </div>
        <div class="col-md-6">
          <label for="Address1" class="form-label">Address 1</label>
          <input type="text" class="form-control" id="Address1" name="add1"value='{v[0][6]}'>
        </div>
        <div class="col-md-6">
          <label for="Address2" class="form-label">Address 2</label>
          <input type="text" class="form-control" id="Address2" name="add2"value='{v[0][7]}'>
        </div>
        <div class="col-md-4">
          <label for="City" class="form-label">City</label>
          <input type="text" class="form-control" id="City" name="city"value='{v[0][8]}'>
        </div>
        <div class="col-md-4">
          <label for="State" class="form-label">State</label>
          <input type="text" class="form-control" id="state" name="state"value='{v[0][9]}'>
        </div>
        <div class="col-md-4">
          <label for="country" class="form-label">Country</label>
          <input type="text" class="form-control" id="country" name="country"value='{v[0][10]}'>
        </div>
        <div class="col-md-6">
          <label for="uname" class="form-label">Username</label>
          <input type="text" class="form-control" id="name" name="uname"value='{v[0][11]}'>
        </div>
        <div class="col-md-6">
          <label for="pass" class="form-label">Password</label>
          <input type="text" class="form-control" id="pass" name="pass"value='{v[0][12]}'>
        </div><br>
        <div class="col-md-4">
          <input type="submit" class="btn btn-primary" id="upd" name="upd"value="Update">
        </div>
    </form>
</div>
</body>
</html>
""")
if len(form) != 0:
    submit=form.getvalue('upd')
    if submit!=None:
        img = form['img']
        if img.filename:
            pi2 = os.path.basename(img.filename)
            open("proof/" + pi2, "wb").write(img.file.read())
        else:
            pi2 = v[0][1]
        Fname=form.getvalue('fname')
        Lname=form.getvalue('lname')
        DOB = form.getvalue('Dob')
        Email=form.getvalue('email')
        Doorno=form.getvalue('door')
        Address1=form.getvalue('add1')
        Address2=form.getvalue('add2')
        City=form.getvalue('city')
        State=form.getvalue('state')
        Country=form.getvalue('country')
        Username=form.getvalue('uname')
        Password=form.getvalue('pass')
        update= """update userreg set image='%s', Fname='%s', Lname='%s', DOB='%s',Email='%s', Door_no='%s', Address1='%s', Address2='%s', city='%s', state='%s', country='%s', username='%s', password='%s' where id='%s'"""%(pi2,Fname, Lname,DOB, Email, Doorno, Address1, Address2, City, State, Country, Username, Password, userid)
        cur.execute(update)
        con.commit()
        print(f"""
            <script>
                alert("updated");
                location.href='usernew.py?id={userid}';
            </script>
        """)