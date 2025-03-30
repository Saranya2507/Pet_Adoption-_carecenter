#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi,cgitb,pymysql,os
from datetime import datetime
cgitb.enable()
con=pymysql.connect(host="localhost",user="root",password="",database="petmatch")
cur=con.cursor()
form=cgi.FieldStorage()
careid = form.getvalue('id')
q = f"""select Animal_id from addanimal"""
cur.execute(q)
animal = cur.fetchone()
ani_id= animal[0]
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Care center profile</title>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" crossorigin="anonymous"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css" crossorigin="anonymous">

    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }}
        body {{
            background-color: #f8f9fa;
        }}
        /* Navbar */
        .navbar {{
            background-color: #222;
            padding: 15px;
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
        }}
        .navbar h2 {{
            margin: 0;
            font-size: 22px;
            font-weight: bold;
        }}
        .menu-btn {{
            font-size: 24px;
            cursor: pointer;
            background: none;
            border: none;
            color: white;
        }}
        /* Sidebar */
        .sidebar {{
            width: 250px;
            height: 100vh;
            background-color: #222;
            position: fixed;
            top: 0;
            left: -250px;
            transition: all 0.3s ease;
            padding-top: 60px;
            z-index: 999;
        }}
        .sidebar.active {{
            left: 0;
        }}
        .sidebar ul {{
            list-style-type: none;
            padding: 0;
        }}
        .sidebar ul li {{
            padding: 15px;
            text-align: left;
            padding-left: 20px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }}
        .sidebar ul li a {{
            color: white;
            text-decoration: none;
            display: flex;
            align-items: center;
            font-size: 18px;
            transition: all 0.3s ease;
        }}
        .sidebar ul li a i {{
            margin-right: 10px;
        }}
        .sidebar ul li a:hover {{
            background-color: #007bff;
            padding-left: 5px;
        }}
        /* Content */
        .content {{
            margin-top: 60px;
            margin-left: 0;
            padding: 20px;
            transition: margin-left 0.3s;
        }}
        /* Responsive */
        @media screen and (min-width: 768px) {{
            .sidebar {{
                left: 0;
            }}
            .content {{
                margin-left: 250px;
            }}
        }}
    </style>
</head>
<body>

    <!-- Navbar -->
    <nav class="navbar">
        <button class="menu-btn" onclick="toggleSidebar()"><i class="fa fa-bars"></i></button>
        <h2>Care Center Dashboard</h2>
    </nav>

    <!-- Sidebar -->
    <div class="sidebar" id="sidebar">
        <ul>
            <h2 style="color:white; text-align: center;">Care Center Dashboard</h2>
            <li><a href="careprofile.py?id={careid}"><i class="fa fa-user"></i> Profile</a></li>
            <li><a href="adopters.py?id={careid}&ani_id={ani_id}"><i class="fa fa-heart"></i> Adopters</a></li>
            <li class="dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"><i class="fa fa-paw"></i> Tips for a Pet</a>
                <ul class="dropdown-menu dropdown-menu-dark">
                    <li><a class="dropdown-item" href="cctips.py?id={careid}">Give Your Tip</a></li>
                    <li><a class="dropdown-item" href="extip.py?id={careid}">Existing Tips</a></li>
                </ul>
            </li>
            <li><a href="suggestions.py?id={careid}"><i class="fa fa-comments"></i> Suggestions</a></li>
            <li><a href="home.py"><i class="fa fa-sign-out"></i> Log Out</a></li>
        </ul>
    </div>
    <div class="content">
""")
w="""select * from carereg where id='%s'"""%(careid)
cur.execute(w)
cc=cur.fetchall()
for i in cc:
    print(f"""
<center>
    <div class="card" style="width:50%;">
      <img src="{i[1]}" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title"><b>CareCenter Name:</b>{i[2]}</h5>
        <p class="card-text"><b>Email:</b>{i[10]}</p>
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
            <div class="form">
            <center><br>
                <form method="post" enctype="multipart/form-data">
                    <h1>Care Center Registration</h1>
                    <hr>
                    <h3>Basic Information</h3>
                    <div class="input-group">
                        <label for="img" class="form-label">Image:</label>
                        <input type="file" class="form-control" id="imge" name="img" value="{i[1]}">
                    </div>
                    <div class="input-group">
                        <label for="name" class="form-label">Name:</label>
                        <input type="text" class="form-control" id="name" name="name" value="{i[2]}">
                    </div>
                    <div class="input-group">
                        <label for="dob" class="form-label">Date Of Birth:</label>
                        <input type="date" class="form-control" id="dob" name="dob" value="{i[3]}">
                    </div>
                   <div class="input-group">
                        <label for="regno" class="form-label">Register Number:</label>
                        <input type="text" class="form-control" id="regno" name="regno" value="{i[4]}">
                    </div>
                    <div class="input-group">
                        <label for="hour" class="form-label">Hours:</label>
                        <input type="text" class="form-control" id="hour" name="hour" value="{i[5]}">
                    </div>
                    <div class="input-group">
                        <label for="day" class="form-label">Operating Hours:</label>
                        <input type="text" class="form-control" id="day" name="day" value="{i[6]}">
                    </div>
                    <hr>

                    <h3>Contact Information</h3>
                    <div class="input-group">
                        <label for="phno" class="form-label">Phone Number:</label>
                        <input type="tel" class="form-control" id="phno" name="phno" value="{i[7]}">
                    </div>
                    <div class="input-group">
                        <label for="altphno" class="form-label">Alternate PhoneNumber:</label>
                        <input type="tel" class="form-control" id="altphno" name="altphno" value="{i[8]}">
                    </div>
                    <div class="input-group">
                        <label for="email" class="form-label">Email:</label>
                        <input type="email" class="form-control" id="email" name="email"value="{i[9]}">
                    </div>
                    <div class="input-group">
                        <label for="link" class="form-label">Website Link:</label>
                        <input type="text" class="form-control" id="link" name="link" value="{i[10]}">
                    </div>
                    <hr>

                    <h3>Care Center Location</h3>
                    <div class="input-group">
                        <label for="door" class="form-label">Door_No:</label>
                        <input type="text" class="form-control" id="door" name="door" value="{i[11]}">
                    </div>
                    <div class="input-group">
                        <label for="add1" class="form-label">Address1:</label>
                        <input type="text" class="form-control" id="inputAddress1" name="add1" value="{i[12]}">
                    </div>
                    <div class="input-group">
                        <label for="add2" class="form-label">Address2:</label>
                        <input type="text" class="form-control" id="inputAddress2" name="add2" value="{i[13]}">
                    </div>
                    <div class="input-group">
                        <label for="city" class="form-label">City:</label>
                        <input type="text" class="form-control" id="City" name="city" value="{i[14]}">
                    </div>
                    <div class="input-group">
                        <label for="State" class="form-label">State:</label>
                        <input type="text" class="form-control" id="State" name="state" value="{i[15]}">
                    </div>
                    <div class="input-group">
                        <label for="code" class="form-label">Code:</label>
                        <input type="number" class="form-control" id="code" name="code" value="{i[16]}">
                    </div>
                    <hr>
                    <h3>Veterinarian Information</h3>
                    <div class="input-group">
                        <label for="vname" class="form-label">Veterinarian Name:</label>
                        <input type="text" class="form-control" id="vname" name="vname" value="{i[17]}">
                    </div>
                    <div class="input-group">
                        <label for="qual" class="form-label">Qualification:</label>
                        <input type="text" class="form-control" id="qual" name="qual" value="{i[18]}">
                    </div>
                    <div class="input-group">
                        <label for="spec" class="form-label">Specialization</label>
                        <input type="text" class="form-control" id="spec" name="spec" value="{i[19]}">
                    </div>
                    <div class="input-group">
                        <label for="expr" class="form-label">Experiance:</label>
                        <input type="text" class="form-control" id="expr" name="expr" value="{i[20]}">
                    </div>
                    <div class="input-group">
                        <label for="uname" class="form-label">Username:</label>
                        <input type="text" class="form-control" id="uname" name="uname" value="{i[22]}">
                    </div>
                    <div class="input-group">
                        <label for="pass" class="form-label">Password:</label>
                        <input type="text" class="form-control" id="pass" name="pass" value="{i[23]}">
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
    
    <script>
        function toggleSidebar() {{
            document.getElementById("sidebar").classList.toggle("active");
        }}
    </script>
</body>
</html>
""")
if len(form)!= 0:
    update=form.getvalue('upd')
    if update:
        Cname=form.getvalue('name')
        DOB=form.getvalue('dob')
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
        Qualification=form.getvalue('qual')
        Specialize=form.getvalue('spec')
        Experience=form.getvalue('expr')
        Uname=form.getvalue('uname')
        Password=form.getvalue('pass')
        img=form['img']
        if img.filename:
            pi2=os.path.basename(img.filename)
            open("proof/" + pi2, "wb").write(img.file.read())
        else:
            pi2=i[1]
        dob=(datetime.now().replace(year=datetime.now().year-18)).strftime('%Y-%m-%d')
        if DOB<dob:
            update="""update carereg set Image='%s',Cname='%s',DOB='%s',Regno='%s',Hours='%s',Days='%s',Phno='%s',Altphno='%s',Email='%s',Link='%s',Door_no='%s',Address1='%s',Address2='%s',City='%s',State='%s',Code='%s',Vname='%s',Qualification='%s',Specialize='%s',Experience='%s',careid='%s',Password='%s' where id='%s'"""%(pi2,Cname,DOB,Regno,Hours,Days,Phno,Altphno,Email,Weblink,Doorno,Address1,Address2,City,State,Code,VName,Qualification,Specialize,Experience,Uname,Password,careid)
            cur.execute(update)
            con.commit()
            print(f"""
                    <script>
                        alert("updated");
                        location.href='careprofile.py?id={careid}';
                    </script>
                    """)
        else:
            print("""
                <script>
                    alert("Your age should above 18");
                </script>
            """)
        q="""select(select count(*) from userreg where Email=%s) +(select count(*) from shelterreg where Email=%s) + (select count(*) from carereg where Email=%s) AS email_count"""%(Email,Email,Email)
        cur.execute(q)
        result=cur.fetchone()
        email=result[0]
        if email>0:
            print(f"""
                        <script>
                            alert("Email is already used");
                            location.href="careprofile.py?id={careid}";
                        </script>
                    """)
        j=f"""select count(*) from carereg where Phno ='{Phno}' or Altphno ='{Altphno}'"""
        cur.execute(j)
        phone=cur.fetchone()
        phno=phone[0]
        if phno >0:
            print(f"""
                        <script>
                            alert("Phone number already exists. Please use a different phone number.");
                            location.href="careprofile.py?id={careid}";
                        </script>
                    """)