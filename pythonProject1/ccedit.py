#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql,os
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="petmatch")
cur = con.cursor()
form = cgi.FieldStorage()
careid=form.getvalue('id')
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
            <h2 style="color:white;">Care Center Dashboard</h2>
            <li><a href="careprofile.py?id={careid}">Profile</a></li>
            <li><a href="adopters.py?id={careid}">Adopters</a></li>
            <li class="dropdown">
          <a class="nav-link dropdown-toggle" href="cctip.py" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Tips for a pet
          </a>
          <ul class="dropdown-menu dropdown-menu-dark">
            <li><a class="dropdown-item" href="extip.py">Existing Pet</a></li>
          </ul>
      </li>
            <li><a href="home.py">Log Out</a></li>
        </ul>
</div>
    <div class="content">
        """)
s=f"""select*from carereg where id='%s'"""%(careid)
cur.execute(s)
v=cur.fetchall()
print(f"""
       <div class="form">
            <center><br>
                <form method="post" enctype="multipart/form-data">
                    <h1>Care Center Registration</h1>
                    <hr>
                    <h3>Basic Information</h3>

                    <div class="form-row">
                        <input type="file" class="form-control" id="imge" name="img" placeholder="Care Center Image">
                        <img src="proof/{v[0][1]}" style="width: 100px; height: auto; margin-top: 10px;">
                    </div>
                    <div class="form-row">
                        <input type="text" class="form-control" id="name" name="name" placeholder="Care Center Name"value="{v[0][2]}">
                    </div>
                    <div class="form-row">
                        <input type="text" class="form-control" id="regno" name="regno" placeholder="Certificate Reg.No" value="{v[0][3]}">
                    </div>
                    <div class="form-row">
                        <input type="text" class="form-control" id="hour" name="hour" placeholder="Operating Hours" value="{v[0][4]}">
                    </div>
                    <div class="form-row">
                        <input type="text" class="form-control" id="day" name="day" placeholder="Operating Days"value="{v[0][5]}">
                    </div>
                    <hr>

                    <h3>Contact Information</h3>
                    <div class="form-row">
                        <input type="tel" class="form-control" id="phno" name="phno" placeholder="Phone Number"value="{v[0][6]}">
                    </div>
                    <div class="form-row">
                        <input type="tel" class="form-control" id="altphno" name="altphno" placeholder="Alternate PhoneNumber"value="{v[0][7]}">
                    </div>
                    <div class="form-row">
                        <input type="email" class="form-control" id="email" name="email"placeholder="Email"value="{v[0][8]}">
                    </div>
                    <div class="form-row">

                        <input type="text" class="form-control" id="link" name="link" placeholder="Website Link"value="{v[0][9]}">
                    </div>
                    <hr>

                    <h3>Care Center Location</h3>
                    <div class="form-row">
                        <input type="text" class="form-control" id="inputdoor" name="door" placeholder="Door no"value="{v[0][10]}">
                    </div>
                    <div class="form-row">
                        <input type="text" class="form-control" id="inputAddress1" name="add1" placeholder="Address1"value="{v[0][11]}">
                    </div>
                    <div class="form-row">
                        <input type="text" class="form-control" id="inputAddress2" name="add2" placeholder="Address2"value="{v[0][12]}">
                    </div>
                    <div class="form-row">
                        <input type="text" class="form-control" id="City" name="city" placeholder="City"value="{v[0][13]}">
                    </div>
                    <div class="form-row">
                        <input type="text" class="form-control" id="State" name="state" placeholder="State" value="{v[0][14]}">
                    </div>
                    <div class="form-row">
                        <input type="number" class="form-control" id="code" name="code" placeholder="Code"value="{v[0][15]}">
                    </div>

                    <hr>
                    <h3>Veterinarian Information</h3>
                    <div class="form-row">
                        <input type="text" class="form-control" id="vname" name="vname" placeholder="Veterinarian Name" value="{v[0][16]}">
                    </div>
                    <div class="form-row">
                        <input type="text" class="form-control" id="qual" name="qual" placeholder="Qualification"value="{v[0][17]}">
                    </div>
                    <div class="form-row">
                        <input type="text" class="form-control" id="spec" name="spec" placeholder="Specialization"value="{v[0][18]}">
                    </div>
                    <div class="form-row">
                        <input type="text" class="form-control" id="expr" name="expr" placeholder="Experience"value="{v[0][19]}">
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
        Cname = form.getvalue('name')
        Regno = form.getvalue('regno')
        Hours = form.getvalue('hour')
        Days = form.getvalue('day')
        Phno = form.getvalue('phno')
        Altphno = form.getvalue('altphno')
        Email = form.getvalue('email')
        Weblink = form.getvalue('link')
        Doorno = form.getvalue('door')
        Address1 = form.getvalue('add1')
        Address2 = form.getvalue('add2')
        City = form.getvalue('city')
        State = form.getvalue('state')
        Code = form.getvalue('code')
        VName = form.getvalue('vname')
        Qualification = form.getvalue('qual')
        Specialize = form.getvalue('spec')
        Experience = form.getvalue('expr')
        img= form['img']
        if img.filename:
            pi1 = os.path.basename(img.filename)
            open("proof/" + pi1, "wb").write(img.file.read())
        else:
            pi1 = v[0][1]
        query = f"""update carereg set Image='%s',Cname='%s',Regno='%s',Hours='%s',Days='%s',Phno='%s',Altphno='%s',Email='%s',Link='%s',Door_no='%s',Address1='%s',Address2='%s',City='%s',State='%s',Code='%s',Vname='%s',Qualification='%s',Specialize='%s',Experience='%s'"""%(pi1,Cname,Regno,Hours,Days,Phno,Altphno,Email,Weblink,Doorno,Address1,Address2,City,State,Code,VName,Qualification,Specialize,Experience,)
        cur.execute(query)
        con.commit()
        print(f"""
        <script>
            alert("updated");
            location.href='careprofile.py?id={careid}';
        </script>
        """)