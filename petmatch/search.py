#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="petmatch")
cur = con.cursor()
form = cgi.FieldStorage()
userid = form.getvalue('id')
shelterid = form.getvalue('id')
search = form.getvalue('search')
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
    font-family: Arial, sans-serif;
    align-items: center;
    justify-content: center;
    margin-top: 20px; 
}}
h1 {{
    font-size: 32px;
}}
p {{
    font-size: 18px;
}}
.card {{
    width: 18rem;
    height:100%;
    margin-bottom: 20px;
    display: flex;
    flex-direction: column;
    border-radius: 10px;
}}
.card img {{
    width: 100%;
    height: 350px; 
    object-fit: cover; 
}}
.container {{
    display: flex;
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
            <form class="d-flex justify-content-center align-items-center mt-3" method="get">
                <input type="search"  name="search" class="form-control me-2" placeholder="Search" style="max-width: 300px;">
                <input type="submit" class="btn btn-outline-success" value="Search">
            </form><br>
        <div class="container text-center">
            <div class="row">

""")
query=f"""select* from addanimal where Species like'%{search}%'or Breed like '%{search}%' or Age like '%{search}%'"""
cur.execute(query)
animals=cur.fetchall()
for an in animals:
    print(f"""
                   <div class="col-6">
                        <div class="card" class="mt-2 p-2">
                            <p><img src="./proof/{an[9]}" class="card-img-top" alt="..."></p>
                            <div class="card-body">
                                <h2 class="card-title" style="font-size: 100%; font-family: Cambria;">{an[4]}</h2>
                                <p class="card-text">Gender:{an[6]}<br>Health status:{an[7]}<br>Life span:{an[8]}</p>
                                  <form  method="post" action="">
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
    askqn=form.getvalue('askqn')
    if askqn:
        ani_id=form.getvalue('ani_id')
        question=form.getvalue('quest')
        if ani_id and question:
            query=f"insert into question (Animal_id,Shelter_id, User_id,Question)values('{ani_id}','{shelterid}', '{userid}', '{question}')"
            cur.execute(query)
            con.commit()
            print("""
                <script>
                    alert("Your question has been submitted!");
                </script>
            """)
    submit=form.getvalue('adt')
    if submit:
        ani_id=form.getvalue('ani_id')
        z=f"""select shelter_id from addanimal where Animal_id='{ani_id}'"""
        cur.execute(z)
        shelid=cur.fetchone()
        if shelid:
            shid=shelid[0]
            s=f"""select* from userreg where id='{userid}'"""
            cur.execute(s)
            userdet=cur.fetchone()
            if userdet:
                Fname=userdet[2]
                Lname=userdet[3]
                Email=userdet[4]
                Door_no=userdet[5]
                Address1=userdet[6]
                Address2=userdet[7]
                city=userdet[8]
                state=userdet[9]
                country=userdet[10]
                m=f"""insert into adopt (Shelter_id,Animal_id, Fname, Lname, Email, Door_no, Address1, Address2, city, state, country, status) values('{shid}','{ani_id}', '{Fname}', '{Lname}', '{Email}', '{Door_no}', '{Address1}', '{Address2}', '{city}', '{state}', '{country}', 'new')"""
                cur.execute(m)
                con.commit()
                print("""
                    <script>
                         alert("Your request has been passed");
                    </script>
                 """)

