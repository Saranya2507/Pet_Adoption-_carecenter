#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi,cgitb,pymysql,os
cgitb.enable()
con=pymysql.connect(host="localhost",user="root",password="",database="petmatch")
cur=con.cursor()
form=cgi.FieldStorage()
shelterid = form.getvalue('id')
block =f"""select status from shelterreg where id = %s"""%(shelterid)
cur.execute(block)
status = cur.fetchone()
if status and status[0] == "blocked":
    print("""
        <script>
            alert("You are blocked and cannot add animals.");
            location.href='home.py';
        </script>
    """)
print(f"""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shelter Dashboard</title>
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
 <div class="content">
<div class="container">
    <h2 class="mt-5">Add New Animal</h2>
    <form class="row g-3 mt-3" method="post"enctype="multipart/form-data">
        <div class="col-md-6">
            <label for="aniname" class="form-label">Animal Name</label>
            <input type="text" class="form-control" id="aniname" name="aniname" required>
        </div>
        <div class="col-md-6">
            <label for="species" class="form-label">Species</label>
            <input type="text" class="form-control" id="species" name="species" required>
        </div>
        <div class="col-md-6">
            <label for="breed" class="form-label">Breed</label>
            <input type="text" class="form-control" id="breed" name="breed">
        </div>
        <div class="col-md-6">
            <label for="age" class="form-label">Age(years)</label>
            <input type="text" class="form-control" id="age" name="age"required>
        </div>
        <div class="col-md-6">
            <label for="gender" class="form-label">Gender</label>
            <input type="text" class="form-control" id="gender" name="gender" required>
        </div>
        <div class="col-md-6">
            <label for="life_span" class="form-label">Life_Span</label>
            <input type="text" class="form-control" id="life_span" name="life_span" required>
        </div> 
        <div class="col-md-12">
            <label for="health_status" class="form-label">Health Status</label>
            <textarea id="health_status" name="health_status" rows="5" cols="100"></textarea>
        </div> 
         <div class="col-md-6">
                <label for="img" class="form-label"> Upload Animal Image</label>
                <input type="file" class="form-control" id="img" name="img">
            </div>
             <div class="col-md-6">
            <label for="video" class="form-label">Upload Animal Video</label>
            <input type="file" class="form-control" id="video" name="video" accept="video/*">
        </div>
        <div class="col-12">
            <input type="submit" class="btn btn-primary" value="Add Animal" name="submit">
        </div>
    </form>
</div>
</div>
        </div>
    </div>
</body>
</html>
""")
submit=form.getvalue('submit')
if submit!=None:
    Name=form.getvalue('aniname')
    Species=form.getvalue('species')
    Breed=form.getvalue('breed')
    Age=form.getvalue('age')
    Gender=form.getvalue('gender')
    Health_status=form.getvalue('health_status')
    Life_span=form.getvalue('life_span')
    q="""select max(id) from addanimal"""
    cur.execute(q)
    max = cur.fetchone()
    max_id = max[0]
    if max_id != None:
        final_max = int(max_id) + 1
        if final_max < 9:
            ani_id = "ABC000" + str(final_max )
        elif final_max < 99:
            ani_id = "ABC00" + str(final_max )
        elif final_max < 999:
            ani_id = "ABC0" + str(final_max )
    else:
            ani_id = "ABC001"
    if len(form) != 0:
        image = form['img']
        if image.filename:
            pi = os.path.basename(image.filename)
            open("proof/" + pi, "wb").write(image.file.read())
            video=form['video']
            if video.filename:
                pi1=os.path.basename(video.filename)
                open("proof/"+pi1,"wb").write(video.file.read())
            s=f"""insert into addanimal(Animal_id,Animal_name,Species,Breed,Age,Gender,Health_status,Life_span,Image,Video,shelter_id,status )values('{ani_id}','{Name}','{Species}','{Breed}','{Age}','{Gender}','{Health_status}','{Life_span}','{pi}','{pi1}','{shelterid}','new')"""
            cur.execute(s)
            con.commit()
            print("""
                <script>
                 alert("Added");
                </script>
            """)