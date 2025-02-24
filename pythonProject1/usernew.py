#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi,cgitb,pymysql,os
from datetime import datetime
cgitb.enable()
con=pymysql.connect(host="localhost",user="root",password="",database="petmatch")
cur=con.cursor()
form=cgi.FieldStorage()
userid=form.getvalue('id')
w="""select*from userreg where id='%s'"""%(userid)
cur.execute(w)
user=cur.fetchall()
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User profile</title>
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
.form {{
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
        padding: 2%;
        margin: auto;
        border-radius: 10px;
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
.card img {{
    width: 100%;
    height:60vh;
    object-fit: cover;
}}
        </style>
</head>

<body>
         <div class="sidebar">
         <ul>
            <h2 style="color:white;">User Dashboard</h2>
            <li><a href="usernew.py?id={userid}">Profile</a></li>
            <li><a href="pets.py?id={userid}">Pets</a></li>
             <li><a href="adopt.py?id={userid}">Adopt status</a></li>
            <li><a href="reply.py?id={userid}">Replies</a></li>
            <li><a href="tips.py?id={userid}">Tips for your pet</a></li>
            <li><a href="home.py?id={userid}">Log Out</a></li>
        </ul>
</div>
    <div class="content">
    """)
for usernew in user:
    print(f"""
    <center>
            <div class="card" style="width:50%;">
      <img src="{usernew[1]}" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title"><b>Name:</b>{usernew[2]}{usernew[3]}</h5>
        <p class="card-text"><b>Email:</b>{usernew[5]}</p>
                <input type="submit" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal{usernew[0]}" value="Edit Detail">
    </div>
    </div>
        <div class="modal fade" id="myModal{usernew[0]}" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLongTitle">Details for {usernew[2]}</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                    """)
    userid=form.getvalue('id')
    s=f"""select*from userreg where id='%s'""" % (userid)
    cur.execute(s)
    v=cur.fetchall()
    print(f"""
    <div class="form">
            <form class="row g-3"method="post" enctype="multipart/form-data">
            <div class="input-group">
                <label> Image:</label>
                <input type="file" class="form-control" name="img" value='{v[0][1]}'>
            </div>
            <div class="input-group">
                <label for="FName" class="form-label">First Name</label>
                <input type="text" class="form-control" id="FName" name="FName"value='{v[0][2]}'>
            </div>
            <div class="input-group">
                <label for="LName" class="form-label">Last Name</label>
                <input type="text" class="form-control" id="LName" name="LName" value='{v[0][3]}'>
            </div>
            <div class="input-group">
                <label for="Dob" class="form-label">Date of Birth:</label>
                <input type="date" class="form-control" id="Dob" name="Dob" value='{v[0][4]}'>
            </div>
            <div class="input-group">
                <label for="Email" class="form-label">Email</label>
                <input type="email" class="form-control" id="Email" name="email"value='{v[0][5]}'>
            </div>
            <div class="input-group">
                <label for="door" class="form-label">Door No</label>
                <input type="text" class="form-control" id="door" name="door" value='{v[0][6]}'>
            </div>
            <div class="input-group">
                <label for="Address1" class="form-label">Address 1</label>
                <input type="text" class="form-control" id="Address1" name="add1" value='{v[0][7]}'>
            </div>
            <div class="input-group">
                <label for="Address2" class="form-label">Address 2</label>
                <input type="text" class="form-control" id="Address2" name="add2" value='{v[0][8]}'>
            </div>
            <div class="input-group">
                <label for="City" class="form-label">City</label>
                <input type="text" class="form-control" id="City" name="city" value='{v[0][9]}'>
            </div>
            <div class="input-group">
                <label for="State" class="form-label">State</label>
                <input type="text" class="form-control" id="state" name="state" value='{v[0][10]}'>
            </div>
            <div class="input-group">
                <label for="country" class="form-label">Country</label>
                <input type="text" class="form-control" id="country" name="country" value='{v[0][11]}'>
            </div>
            <div class="input-group">
                <label for="username" class="form-label">Username</label>
                <input type="text" class="form-control" id="username" name="username" value='{v[0][12]}'>
            </div>
            <div class="input-group">
                <label for="password" class="form-label">Password</label>
                <input type="" class="form-control" id="password" name="password" value='{v[0][13]}'>
            </div>
            <div class="col-12">
                 <input type="submit" class="btn btn-primary" id="upd" name="upd"value="Update">
            </div>
        </form>
    </div>
    </body>
    </html>
          """)
    if len(form)!= 0:
        submit=form.getvalue('upd')
        if submit != None:
            img=form['img']
            if img.filename:
                pi2=os.path.basename(img.filename)
                open("proof/" + pi2, "wb").write(img.file.read())
            else:
                pi2=v[0][1]
            Fname=form.getvalue('FName')
            Lname=form.getvalue('LName')
            DOB=form.getvalue('Dob')
            Email=form.getvalue('email')
            Doorno=form.getvalue('door')
            Address1=form.getvalue('add1')
            Address2=form.getvalue('add2')
            City=form.getvalue('city')
            State=form.getvalue('state')
            Country=form.getvalue('country')
            Username=form.getvalue('username')
            Password=form.getvalue('password')
            q = """select(select count(*) from userreg where Email=%s) +(select count(*) from shelterreg where Email=%s) +(select count(*) from carereg where Email=%s) AS email_count"""
            cur.execute(q, (Email, Email, Email))
            result = cur.fetchone()
            email_exists = result[0]
            dob = (datetime.now().replace(year=datetime.now().year - 18)).strftime('%Y-%m-%d')
            if email_exists > 0:
                print("""
                            <script>
                                alert("This email is already registered in another account.");
                            </script>
                        """)
            if DOB >dob:
                print("""
                                        <script>
                                            alert("Your age should be greater than 18");
                                        </script>
                                 """)
            else:
                update ="""update userreg set image='%s', Fname='%s', Lname='%s',DOB='%s', Email='%s', Door_no='%s', Address1='%s', Address2='%s', city='%s', state='%s', country='%s', username='%s', password='%s' where id='%s'""" % ( pi2, Fname, Lname, DOB, Email, Doorno, Address1, Address2, City, State, Country, Username, Password,userid)
                cur.execute(update)
                con.commit()
                print(f"""
                                    <script>
                                        alert("updated");
                                        location.href='usernew.py?id={userid}';
                                    </script>
                                """)