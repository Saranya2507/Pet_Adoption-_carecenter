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
    <!-- Bootstrap CSS -->
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css">

    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
        }}
        /* Navbar */
        .navbar {{
            background-color: #343a40;
        }}
        .navbar-brand, .navbar-nav .nav-link {{
            color: white;
            font-size: 18px;
        }}
        .navbar-nav .nav-link:hover {{
            color: #f8f9fa;
        }}
        .dropdown-menu-dark {{
            background-color: #343a40;
        }}
        .dropdown-menu-dark .dropdown-item {{
            color: white;
        }}
        .dropdown-menu-dark .dropdown-item:hover {{
            background-color: #495057;
        }}
        /* Dashboard Cards */
        .dashboard-card {{
            padding: 20px;
            border-radius: 10px;
            background: white;
            box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.1);
            text-align: center;
        }}
        .dashboard-card h3 {{
            font-size: 22px;
            margin-bottom: 10px;
        }}
        .dashboard-card p {{
            font-size: 18px;
            font-weight: bold;
            color: #007bff;
        }}
    </style>
</head>

<body>

    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Shelter Dashboard</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="profile.py?id={shelterid}">Profile</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="animalDropdown" role="button" data-bs-toggle="dropdown">
                            Animal
                        </a>
                        <ul class="dropdown-menu dropdown-menu-dark">
                            <li><a class="dropdown-item" href="shelter.py?id={shelterid}">Add Animal</a></li>
                            <li><a class="dropdown-item" href="expet.py?id={shelterid}">Existing Pet</a></li>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="adoptDropdown" role="button" data-bs-toggle="dropdown">
                            Adopt Request
                        </a>
                        <ul class="dropdown-menu dropdown-menu-dark">
                            <li><a class="dropdown-item" href="adoptreq.py?id={shelterid}">All Requests</a></li>
                            <li><a class="dropdown-item" href="adoptaccept.py?id={shelterid}">Accepted</a></li>
                            <li><a class="dropdown-item" href="adoptrej.py?id={shelterid}">Rejected</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="questions.py?id={shelterid}">Questions Asked</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-danger" href="home.py">Log Out</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

 <div class="content">
<div class="container">
    <h2 class="mt-4 text-center">Add New Animal</h2>
    <form class="row g-3 mt-3" method="post" enctype="multipart/form-data">
        <div class="col-md-6 col-sm-12">
            <label for="aniname" class="form-label">Animal Name</label>
            <input type="text" class="form-control" id="aniname" name="aniname" required>
        </div>
        <div class="col-md-6 col-sm-12">
            <label for="species" class="form-label">Species</label>
            <input type="text" class="form-control" id="species" name="species" required>
        </div>
        <div class="col-md-6 col-sm-12">
            <label for="breed" class="form-label">Breed</label>
            <input type="text" class="form-control" id="breed" name="breed">
        </div>
        <div class="col-md-6 col-sm-12">
            <label for="age" class="form-label">Age (years)</label>
            <input type="text" class="form-control" id="age" name="age" required>
        </div>
        <div class="col-md-6 col-sm-12">
            <label for="gender" class="form-label">Gender</label>
            <input type="text" class="form-control" id="gender" name="gender" required>
        </div>
        <div class="col-md-6 col-sm-12">
            <label for="life_span" class="form-label">Life Span</label>
            <input type="text" class="form-control" id="life_span" name="life_span" required>
        </div> 
        <div class="col-12">
            <label for="health_status" class="form-label">Health Status</label>
            <textarea id="health_status" name="health_status" rows="4" class="form-control"></textarea>
        </div> 
        <div class="col-md-6 col-sm-12">
            <label for="img" class="form-label">Upload Animal Image</label>
            <input type="file" class="form-control" id="img" name="img">
        </div>
        <div class="col-md-6 col-sm-12">
            <label for="video" class="form-label">Upload Animal Video</label>
            <input type="file" class="form-control" id="video" name="video" accept="video/*">
        </div>
        <div class="col-12 text-center">
            <input type="submit" class="btn btn-primary w-100" value="Add Animal" name="submit">
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