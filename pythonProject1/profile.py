#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi,cgitb,pymysql,os
from datetime import datetime
cgitb.enable()
con=pymysql.connect(host="localhost",user="root",password="",database="petmatch")
cur=con.cursor()
form=cgi.FieldStorage()
shelterid = form.getvalue('id')
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shelter profile</title>
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
.modal-body img{{
    width:50%;
    height:50%;
}}
.content th{{
    background-color:pink;
}}
form {{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 100%;
        padding: 2%;
        margin: auto;
        border-radius: 10px;
        background: rgba(255, 255, 255, 0.3);
    }}
    form p {{
        color:black;
    }}
    label {{
        color:black;
        font-family:Serif;
        font-size:20px;
        margin-right: 10px;
        display: inline-block;
        width: 150px;
    }}
    .input-group {{
        display: flex;
        align-items: center;
        margin-bottom: 15px;
    }}
    .input-group input {{
        width: 100%;
    }}
        </style>
</head>

<body>
        <div class="sidebar">
      <ul>
            <h2 style="color:white;">Shelter Dashboard</h2>
            <li><a href="profile.py?id={shelterid}"> Profile</a></li>
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
             <li class="dropdown-item">
          <a class="nav-link dropdown-toggle" href="" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Questions & Replies
          </a>
        <ul class="dropdown-menu dropdown-menu-dark">
            <li><a href="questions.py?id={shelterid}">Questions Asked</a></li>
            <li><a href="replies.py?id={shelterid}">Replies</a></li>
        </ul>
        </li>
            <li><a href="home.py">Log Out</a></li>
      </ul>
</div>
</div>
    <div class="content">
""")
s = f"""select*from shelterreg where id='%s'""" % (shelterid)
cur.execute(s)
v = cur.fetchall()
for i in v:
    print(f"""
    <center>
    <div class="card" style="width:50%;">
      <img src="{i[1]}" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{i[2]}</h5>
        <p class="card-text"><b>Email:</b>{i[7]}</p>
        <input type="submit" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal{i[0]}" value="Edit Detail">
      </div>
    </div>
    <div class="modal fade" id="myModal{i[0]}" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLongTitle">Details for {i[2]}</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
 <div class="modal-body">
 <form class="row g-3" method="post" enctype="multipart/form-data">
    <div class="input-group">
                <label>Shelter Image:</label>
                <input type="file" class="form-control" name="img" value={i[1]}>
            </div>
            <div class="input-group">
                <label for="shelterName" class="form-label">Shelter Name</label>
                <input type="text" class="form-control" id="shelterName" name="name" value={i[2]}>
            </div>
            <div class="input-group">
                <label for="dob" class="form-label">Date Of Birth</label>
                <input type="date" class="form-control" id="dob" name="dob" value={i[3]}>
            </div>
            <div class="input-group">
                <label>Register Number:</label>
                <input type="text" class="form-control" name="regno"value={i[4]}>
            </div>
            <div class="input-group">
                <label>Phone Number:</label>
                <input type="tel" class="form-control" name="phno" value={i[5]}>
            </div>
            <div class="input-group">
                <label>Alternate Phone Number:</label>
                <input type="tel" class="form-control" name="altphno" value={i[6]}>
            </div>
            <div class="input-group">
                <label for="Email" class="form-label">Email</label>
                <input type="email" class="form-control" id="Email" name="email" value={i[7]}>
            </div>
            <div class="input-group">
                <label for="door" class="form-label">Door No</label>
                <input type="text" class="form-control" id="door" name="door" value={i[8]}>
            </div>
            <div class="input-group">
                <label for="Address1" class="form-label">Address 1</label>
                <input type="text" class="form-control" id="Address1" name="add1" value={i[9]}>
            </div>
            <div class="input-group">
                <label for="Address2" class="form-label">Address 2</label>
                <input type="text" class="form-control" id="Address2" name="add2" value={i[10]}>
            </div>
            <div class="input-group">
                <label for="City" class="form-label">City</label>
                <input type="text" class="form-control" id="City" name="city" value={i[11]}>
            </div>
            <div class="input-group">
                <label for="State" class="form-label">State</label>
                <input type="text" class="form-control" id="state" name="state" value={i[12]}>
            </div>
            <div class="input-group">
                <label>Pincode:</label>
                <input type="number" class="form-control" name="code" value={i[13]}>
            </div>
            <div class="input-group">
                <label>License Document:</label>
                <input type="file" class="form-control" name="license" value={i[14]}>
            </div>
            <div class="input-group">
                <label>Insurance Document:</label>
                <input type="file" class="form-control" name="ins" value={i[15]}>
            </div>
            <div class="input-group">
                <label>Shelter Id:</label>
                <input type="text" class="form-control" name="uname" value={i[17]}>
            </div>
            <div class="input-group">
                <label>Password:</label>
                <input type="text" class="form-control" name="pass" value={i[18]}>
            </div>
            <div class="col-12">
                <input type="submit" class="btn btn-primary" name="upd" value="Update">
            </div>
        </form>
        </center>
    </div>
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
if len(form)!= 0:
    submit=form.getvalue('upd')
    if submit!=None:
        Name=form.getvalue('name')
        DOB=form.getvalue('dob')
        Regno=form.getvalue('regno')
        Phno=form.getvalue('phno')
        Altphno=form.getvalue('altphno')
        Email=form.getvalue('email')
        Doorno=form.getvalue('door')
        Address1=form.getvalue('add1')
        Address2=form.getvalue('add2')
        City=form.getvalue('city')
        State=form.getvalue('state')
        Pincode=form.getvalue('code')
        Uname=form.getvalue('uname')
        Password=form.getvalue('pass')
        img=form['img']
        img1=form['license']
        img2=form['ins']
        if img.filename:
            pi2=os.path.basename(img.filename)
            open("proof/" + pi2, "wb").write(img.file.read())
        else:
            pi2=v[0][1]
        if img1.filename:
            pi=os.path.basename(img1.filename)
            open("proof/" + pi, "wb").write(img1.file.read())
        else:
            pi=v[0][14]
        if img2.filename:
            pi1=os.path.basename(img2.filename)
            open("proof/" + pi1, "wb").write(img2.file.read())
        else:
            pi1=v[0][15]
        dob=(datetime.now().replace(year=datetime.now().year-18)).strftime('%Y-%m-%d')
        if DOB <dob:
            update="""update shelterreg set image='%s',Name='%s',DOB='%s',Regno='%s',phno='%s',altphno='%s',Email='%s',Door_no='%s',Address1='%s',Address2='%s',city='%s',state='%s',code='%s',license_no='%s',insurance_no='%s',username='%s',password='%s' where id='%s'""" % (
            pi2, Name, DOB, Regno, Phno, Altphno, Email, Doorno, Address1, Address2, City, State, Pincode, pi, pi1,
            Uname, Password, shelterid)
            cur.execute(update)
            con.commit()
            print(f"""
                       <script>
                           alert("updated");
                           location.href='profile.py?id={shelterid}';
                       </script>
            """)
        else:
            print("""
                                    <script>
                                        alert("your age should be greater than 18");
                                    </script>
            """)
        q="""select(select count(*) from userreg where Email=%s) +(select count(*) from shelterreg where Email=%s) + (select count(*) from carereg where Email=%s) AS email_count"""
        cur.execute(q, (Email, Email, Email))
        result = cur.fetchone()
        email_exists = result[0]
        if email_exists > 0:
            print("""
                                    <script>
                                        alert("This email is already registered in another account.");
                                    </script>
            """)