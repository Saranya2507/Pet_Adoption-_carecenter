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
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css"
        integrity="sha512-5A8nwdMOWrSz20fDsjczgUidUBR8liPYU+WymTZP1lmY9G6Oc7HlZv156XqnsgNUzTyMefFTcsFH/tnJE/+xBg=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />
    <style>
        body {{
            font-family: Arial, sans-serif;
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
            padding: 0;
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
        @media (max-width: 768px) {{
            .sidebar {{
                width: 100%;
                height: auto;
                position: relative;
            }}
            .content {{
                margin-left: 0;
            }}
        }}
        .dropdown-menu {{
    background-color: #333 !important;
}}

.dropdown-item {{
    color: white !important;
}}

.dropdown-item:hover {{
    background-color: #575757 !important;
}}

    </style>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark d-lg-none">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">Admin</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item"><a class="nav-link" href="newuser.py">Users</a></li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="shelterDropdown" role="button" data-bs-toggle="dropdown">Shelter</a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="shelternew.py">New Shelter</a></li>
                        <li><a class="dropdown-item" href="shelterex.py">Existing Shelter</a></li>
                        <li><a class="dropdown-item" href="shelterrej.py">Rejected Shelter</a></li>
                    </ul>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="careDropdown" role="button" data-bs-toggle="dropdown">Care Center</a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="carenew.py">New CareCenter</a></li>
                        <li><a class="dropdown-item" href="careex.py">Existing CareCenter</a></li>
                        <li><a class="dropdown-item" href="carerej.py">Rejected CareCenter</a></li>
                    </ul>
                </li>
                 <li class="nav-item"><a class="nav-link" href="request.py">Adopt detail</a></li>
                
             <li class="dropdown">
        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Tips
        </a>
          <ul class="dropdown-menu dropdown-menu-dark">
            <li><a class="dropdown-item" href="alltip.py">Tips</a></li>
            <li><a class="dropdown-item" href="extips.py">Existing Tips</a></li>
          </ul>
      </li>
                <li class="nav-item"><a class="nav-link" href="pet.py">Pets</a></li>
                <li class="nav-item"><a class="nav-link" href="home.py">Log Out</a></li>
            </ul>
        </div>
    </div>
</nav>

<div class="sidebar d-none d-lg-block">
  
        <h2 style="color:white;">Admin</h2>
       <ul class="navbar-nav">
                <li class="nav-item"><a class="nav-link" href="newuser.py">Users</a></li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="shelterDropdown" role="button" data-bs-toggle="dropdown">Shelter</a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="shelternew.py">New Shelter</a></li>
                        <li><a class="dropdown-item" href="shelterex.py">Existing Shelter</a></li>
                        <li><a class="dropdown-item" href="shelterrej.py">Rejected Shelter</a></li>
                    </ul>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="careDropdown" role="button" data-bs-toggle="dropdown">Care Center</a>
                    <ul class="dropdown-menu">
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
                <li class="nav-item"><a class="nav-link" href="pet.py">Pets</a></li>
                <li class="nav-item"><a class="nav-link" href="home.py">Log Out</a></li>
            </ul>
</div>
    <div class="content">
        <div class="table-responsive">
        <table class="table table-bordered">
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
