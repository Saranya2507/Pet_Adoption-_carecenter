#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="petmatch")
cur = con.cursor()
form = cgi.FieldStorage()
userid = form.getvalue('id')
shelterid = form.getvalue('id')
careid = form.getvalue('id')
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
    <!-- Bootstrap CSS -->
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
           <div class="table-responsive mt-4">
    <table class="table table-bordered">
        <thead class="table-dark">
        <tr>
                    <th>ID</th>
                    <th>Animal ID</th>
                    <th>Image</th>
                    <th>Animal Name</th>
                    <th></th>
                    <th></th>
                    <th>Status</th>
                    </tr>
       """)
q=f"""select *from addanimal"""
cur.execute(q)
animal=cur.fetchall()
j=1
for ani in animal:
    print(f"""
    <tr>
        <td>{j}</td>
        <td>{ani[1]}</td>
        <td><img src="{ani[9]}"style="width:80px;height:80px;"</td>
        <td>{ani[2]}</td>
        <td>
            <a href="#" data-bs-toggle="modal" data-bs-target="#staticBackdrop{ani[0]}">More</a><br>
        </td>
        <td>
            <form method="post" style="display:inline-block;">
                <input type="hidden" name="ani_id" value="{ani[1]}">
                <input type="submit" class="btn btn-danger" value="Delete" name="delete">
                <button type="button" class="btn btn-dark" data-bs-toggle="modal" data-bs-target="#editModal{ani[0]}">Edit</button>
            </form>
        </td>
         <td>
            <form method="post" style="display:inline-block;">
                <input type="hidden" name="ani_id" value="{ani[1]}">
                <input type="submit" class="btn btn-success" value="Enable" name="enable">
                <input type="submit" class="btn btn-danger" value="Disable" name="disable">
            </form>
        </td>
</tr>
""")
    j+=1
    print(f"""
                        <div class="modal fade" id="staticBackdrop{ani[0]}" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
                          <div class="modal-dialog">
                            <div class="modal-content">
                              <div class="modal-header">
                                <h1 class="modal-title fs-5" id="staticBackdropLabel">Full Details</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                              </div>
                              <div class="modal-body">
                                    <center><img src="{ani[9]}" style="width:100px;height:80px;"><br></center>
                                    <b>AnimalID:</b>{ani[1]}<br>
                                    <b>Animal Name:</b>{ani[2]}<br>
                                    <b>Species:</b>{ani[3]}<br>
                                    <b>Breed:</b>{ani[4]}<br>
                                    <b>Age:</b>{ani[5]}<br>
                                    <b>Gender:</b>{ani[6]}<br>
                                    <b>Health Status:</b>{ani[7]}<br>
                                    <b>Life Span:</b>{ani[8]}<br>
                              </div>
                            </div>
                          </div>
                        </div>
     <div class="modal fade" id="editModal{ani[0]}" tabindex="-1" aria-labelledby="editModalLabel{ani[0]}" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <form method="post">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="editModalLabel{ani[0]}">Edit Animal Information</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <input type="hidden" name="ani_id" value="{ani[1]}">
                        <div class="input-group">
                            <label for="aniName" class="form-label">Animal Name</label>
                            <input type="text" class="form-control" id="aniName" name="ani_name" value="{ani[2]}" required>
                        </div>
                        <div class="input-group">
                            <label for="species" class="form-label">Species</label>
                            <input type="text" class="form-control" id="species" name="species" value="{ani[3]}" required>
                        </div>
                        <div class="input-group">
                            <label for="breed" class="form-label">Breed</label>
                            <input type="text" class="form-control" id="breed" name="breed" value="{ani[4]}" required>
                        </div>
                        <div class="input-group">
                            <label for="age" class="form-label">Age</label>
                            <input type="text" class="form-control" id="age" name="age" value="{ani[5]}" required>
                        </div>
                        <div class="input-group">
                            <label for="gender" class="form-label">Gender</label>
                            <input type="text" class="form-control" id="gender" name="gender" value="{ani[6]}" required>
                        </div>
                        <div class="input-group">
                            <label for="healthStatus" class="form-label">Health Status</label>
                            <input type="text" class="form-control" id="healthStatus" name="health_status" value="{ani[7]}" required>
                        </div>
                        <div class="input-group">
                            <label for="lifeSpan" class="form-label">Life Span</label>
                            <input type="text" class="form-control" id="lifeSpan" name="life_span" value="{ani[8]}" required>
                        </div>
                    </div>
                   <div class="input-group">
                        <input type="submit" class="btn btn-primary" value="Update" name="edit_animal">
                    </div>
                </form>
            </div>
        </div>
     </div>
</html>
</body>
    """)
More=form.getvalue('more')
if More:
    c=f"""select* from addaminal"""
    cur.execute(c)
    det=cur.fetchall()
Delete=form.getvalue('delete')
if Delete:
    q = f"""select Animal_id from addanimal"""
    cur.execute(q)
    animal = cur.fetchone()
    animalid = animal[0]
    w=f"""Delete from addanimal where Animal_id='%s'"""%(animalid)
    cur.execute(w)
    con.commit()
    print(f"""
        <script>
            alert("Successfully deleted");
            location.href="expet.py?id={shelterid}"
        </script>
    """)
update=form.getvalue('edit_animal')
if update:
    animal_id = form.getvalue('ani_id')
    animal_name = form.getvalue('ani_name')
    species = form.getvalue('species')
    breed = form.getvalue('breed')
    age = form.getvalue('age')
    gender = form.getvalue('gender')
    health_status = form.getvalue('health_status')
    life_span = form.getvalue('life_span')
    update = """update addanimal set Animal_Name = '%s', Species = '%s', Breed = '%s', Age = '%s', Gender = '%s', Health_Status = '%s', Life_Span = '%s' where Animal_id = '%s'"""%(animal_name, species, breed, age, gender, health_status, life_span, animal_id)
    cur.execute(update)
    con.commit()
    print(f"""
        <script>
            alert("Updated successfully");
            location.href="expet.py?id={shelterid}"
        </script>
    """)
enable=form.getvalue('enable')
ani_id=form.getvalue('ani_id')
if enable:
    u=f"""update addanimal set status='enable' where Animal_id='%s'"""%(ani_id)
    cur.execute(u)
    con.commit()
    print("""
        <script>
            alert("Your pet has been enabled");
        </script>
    """)
disable=form.getvalue('disable')
if disable:
    d=f"""update addanimal set status='disable' where Animal_id='%s'"""%(ani_id)
    cur.execute(d)
    con.commit()
    print("""
            <script>
                alert("Your pet has been disabled");
            </script>
        """)