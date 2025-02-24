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
    display:flex;
    font-family: Arial, sans-serif;
}}
h1 {{
    font-size: 32px;
}}

p {{
    font-size: 18px;
}}
.card {{
    width: 18rem;
    height: auto;
    margin-bottom: 20px;
    display: flex;
    flex-direction: column;
    border-radius: 10px;
}}
.card img {{
    width: 100%;
    height: 200px; 
    object-fit: cover; 
}}
.container {{
    display: flex;
    justify-content:center;
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
            <table class="table table-bordered mt-4"border=1px;>
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