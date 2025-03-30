#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="petmatch")
cur = con.cursor()
form = cgi.FieldStorage()
careid = form.getvalue('id')
q = f"""select Animal_id from addanimal"""
cur.execute(q)
animal = cur.fetchone()
if animal:
      ani_id= animal[0]
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
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
""")
print(f"""
    <div class="content">
        <div class="form">
           <center> <br>
            <form class="row g-3" method="post" enctype="multipart/form-data">
                <h2>Tip For A Pet</h2>
                <input type="hidden" name="ani_id" value="{ani_id}">
                <div class="input-group">
                    <label for="anitype" class="form-label">Animal Type</label>
                    <input type="text" class="form-control" name="type" required>
                </div><br>
                <div class="input-group">
                    <label for="tipfor" class="form-label">Tip for:</label>
                    <input type="text" class="form-control" name="tipfor" required>
                </div>
                <div class="input-group">
                    <label for="tip" class="form-label">Give Your Tip :</label>
                    <textarea id="tip" name="tip" rows="5" cols="100"></textarea>
                </div>
                <div class="col-12">
                    <input type="submit" class="btn btn-primary" value="Submit" name="sub">
                </div>
            </form>
            <center>
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
submit=form.getvalue('sub')
if submit:
    Type=form.getvalue('type')
    ani_id=form.getvalue('ani_id')
    Tip=','.join(form.getlist('tipfor'))
    Tips=form.getvalue('tip')
    q=f"""insert into tip (Care_id,Animal_type,Animal_id,Tip_for,Tip)values('{careid}','{Type}','{ani_id}','{Tip}','{Tips}')"""
    cur.execute(q)
    con.commit()
    print("""
        <script>
            alert("Your tip has been submitted");
        </script>
    """)