#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql
from datetime import datetime
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="petmatch")
cur = con.cursor()
form = cgi.FieldStorage()
userid = form.getvalue('id')
shelterid=form.getvalue('id')
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pets</title>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <style>
        .sidebar {{
            width: 250px;
            height: 100vh;
            background-color: #333;
            position: fixed;
            top: 0;
            left: 0;
            padding-top: 20px;
            z-index: 1000; 
        }}
        .sidebar ul {{
            list-style-type: none;
        }}
        .sidebar ul li {{
            padding: 15px;
            text-align: center;
        }}
        .sidebar ul li a {{
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
        }}
        .card {{
            width: 18rem;
            margin-bottom: 20px;
        }}
        .card img {{
            width: 100%;
            height: 250px;
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
        <form class="d-flex justify-content-center mt-3" method="get">
            <input type="hidden" name="id" value="{userid}">
            <input type="search" name="search" class="form-control me-2" placeholder="Search for pets" style="max-width: 300px;" required>
            <input type="submit" class="btn btn-outline-success" value="Search">
        </form><br>
        <div class="container text-center">
            <div class="row">
""")
query="""select * from addanimal where status=('enable'&'new')"""
cur.execute(query)
animals=cur.fetchall()
for an in animals:
    print(f"""
        <div class="col-4">
                        <div class="card" class="mt-2 p-2">
                            <p><img src="./proof/{an[9]}" class="card-img-top" alt="..."></p>
                            <div class="card-body">
                                <h2 class="card-title" style="font-size: 100%; font-family: Cambria;">{an[4]}</h2>
                                <p class="card-text">Gender:{an[6]}<br>Health status:{an[7]}<br>Life span:{an[8]}</p>
                                  <form method="post">
                                    <input type="hidden" name="ani_id" value="{an[1]}">
                                    <input type="submit" class="btn btn-primary" value="Adopt" name="adt">
                                  </form><br>
                               <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal{an[1]}">Ask Question</button>
                            <div class="modal fade" id="myModal{an[1]}" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered" role="document">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="exampleModalLongTitle">Ask a Question</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <form method="post" action="">
                                    <input type="hidden" name="ani_id" value="{an[1]}">
                                    <div class="mb-3">
                                        <label for="question" class="form-label">Your Question</label>
                                        <textarea class="form-control" id="question" name="quest" rows="3" required></textarea>
                                    </div>
                                    <input type="submit" class="btn btn-primary" name="askqn" value="Submit">
                                </form>
                            </div>
                        </div>
                    </div>
                   </div>
         </div>
         </div>
         </div>
          """)
submit=form.getvalue('adt')
if submit:
    ani_id=form.getvalue('ani_id')
    z = f"""select shelter_id,Animal_Name,Image from addanimal where Animal_id='{ani_id}'"""
    cur.execute(z)
    sh= cur.fetchall()
    adt_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if sh and adt_time:
        shid=sh[0][0]
        Ani_name=sh[0][1]
        Ani_img=sh[0][2]
        s=f"""select *from userreg where id='{userid}'"""
        cur.execute(s)
        userdet = cur.fetchone()
        if userdet:
            Image=userdet[1]
            Fname=userdet[2]
            Lname=userdet[3]
            DOB=userdet[4]
            Email=userdet[5]
            Door_no=userdet[6]
            Address1=userdet[7]
            Address2=userdet[8]
            city=userdet[9]
            state=userdet[10]
            country=userdet[11]
            m=f"""insert into adopt (Shelter_id, Animal_name, User_image, Animal_id, Fname, Lname, DOB, Email, Door_no, Address1, Address2, city, state, country, User_id,Animal_image,status,adopt_time) values('{shid}', '{Ani_name}','{Image}', '{ani_id}',  '{Fname}', '{Lname}', '{DOB}', '{Email}', '{Door_no}', '{Address1}', '{Address2}', '{city}', '{state}', '{country}','{userid}','{Ani_img}','new','{adt_time}')"""
            cur.execute(m)
            con.commit()
            print("""
                <script>
                     alert("Your request has been passed");
                </script>
             """)
askqn=form.getvalue('askqn')
if askqn:
    ani_id=form.getvalue('ani_id')
    question=form.getvalue('quest')
    if ani_id and question:
        query=f"insert into question (Animal_id,Shelter_id, User_id,Question,status)values('{ani_id}','{shelterid}', '{userid}', '{question}','not replied')"
        cur.execute(query)
        con.commit()
        print("""
            <script>
                alert("Your question has been submitted!");
            </script>
        """)
search=form.getvalue('search')
if search:
    print(f"""
        <script>
            location.href ='search.py?id={userid}&search={search}';
        </script>
    """)

print("""
    </div>
</div>
</body>
</html>
""")
