#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="petmatch")
cur = con.cursor()
form = cgi.FieldStorage()
careid=form.getvalue('id')
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
        .table table-bordered mt-4 th{{
        width:20%;
        }}
    </style>
</head>
<body>
    <div class="sidebar">
          <ul>
            <h2 style="color:white;">Admin</h2>
            <li><a href="newuser.py"> Users</a></li>
      <li class="dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Shelter
          </a>
          <ul class="dropdown-menu dropdown-menu-dark">
            <li><a class="dropdown-item" href="shelternew.py">New Shelter</a></li>
            <li><a class="dropdown-item" href="shelterex.py">Existing Shelter</a></li>
            <li><a class="dropdown-item" href="shelterrej.py">Rejected Shelter</a></li>
          </ul>
      </li>
      <li class="dropdown">
        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Care Center
        </a>
          <ul class="dropdown-menu dropdown-menu-dark">
            <li><a class="dropdown-item" href="carenew.py">New CareCenter</a></li>
            <li><a class="dropdown-item" href="careex.py">Existing CareCenter</a></li>
            <li><a class="dropdown-item" href="carerej.py">Rejected CareCenter</a></li>
          </ul>
      </li>
       <li><a  href="request.py">Adopt detail</a></li>
            <li class="dropdown">
        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Tips
        </a>
          <ul class="dropdown-menu dropdown-menu-dark">
            <li><a class="dropdown-item" href="alltip.py">Tips</a></li>
            <li><a class="dropdown-item" href="extips.py">Existing Tips</a></li>
          </ul>
      </li>
            <li><a href="pet.py">Pets</a></li>
            <li><a href="home.py">Log Out</a></li>
    </ul>
    </div>
    <div class="content">
          <table class="table table-bordered mt-4"border=1px;>
                    <tr>
                    <th>ID</th>
                    <th>Animal ID</th>
                    <th style="width:20%;">Image</th>
                    <th>Animal Name</th>
                    <th></th>
                    </tr>
""")
query="""select * from addanimal"""
cur.execute(query)
animals=cur.fetchall()
j=1
for ani in animals:
    print(f"""
        <tr>
        <td>{j}</td>
        <td>{ani[1]}</td>
        <td><img src="{ani[9]}"style="width:80%;height:80px;"</td>
        <td>{ani[2]}</td>
        <td>
            <input type="submit" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop{ani[0]}" value="More"><br>
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
                                    <b>Shelter ID:</b>{ani[11]}
                              </div>
                            </div>
                          </div>
                        </div>
</html>
</body>
""")
print("""
    </div>
</body>
</html>
""")
