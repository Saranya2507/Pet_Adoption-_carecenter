#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="petmatch")
cur = con.cursor()
form = cgi.FieldStorage()
userid = form.getvalue('id')

s = f"""SELECT Fname, Lname FROM userreg WHERE id='{userid}'"""
cur.execute(s)
name = cur.fetchall()

print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }}

        /* Navbar */
        .navbar {{
            background-color: #333;
        }}
        .navbar a {{
            color: white !important;
        }}

        /* Sidebar */
        .sidebar {{
            width: 250px;
            height: 100vh;
            background-color: #333;
            position: fixed;
            top: 0;
            left: -250px;
            padding-top: 20px;
            transition: all 0.3s ease-in-out;
            z-index: 1000;
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

        /* Content Area */
        .content {{
            margin-left: 0;
            padding: 70px 20px 20px;
            text-align: center;
            transition: margin-left 0.3s ease-in-out;
        }}

        /* Mobile Sidebar */
        .menu-btn {{
            font-size: 24px;
            color: white;
            cursor: pointer;
        }}

        /* Overlay Effect */
        .overlay {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            z-index: 500;
        }}

        /* Sidebar Active */
        .sidebar.active {{
            left: 0;
        }}
        .overlay.active {{
            display: block;
        }}

        /* Responsive for Desktop */
        @media (min-width: 768px) {{
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

<!-- Overlay for Sidebar -->
<div class="overlay" id="overlay" onclick="toggleSidebar()"></div>

<!-- Navbar -->
<nav class="navbar navbar-dark fixed-top">
    <div class="container-fluid">
        <span class="menu-btn" onclick="toggleSidebar()">&#9776;</span>
        <a class="navbar-brand mx-auto" href="#">User Dashboard</a>
    </div>
</nav>

<!-- Sidebar -->
<div class="sidebar" id="sidebar">
    <ul>
        <h2 style="color:white;">User Dashboard</h2>
        <li><a href="usernew.py?id={userid}">Profile</a></li>
        <li><a href="pets.py?id={userid}">Pets</a></li>
        <li><a href="adopt.py?id={userid}">Adopt Status</a></li>
        <li><a href="reply.py?id={userid}">Replies</a></li>
        <li><a href="tips.py?id={userid}">Tips for Your Pet</a></li>
        <li><a href="home.py?id={userid}">Log Out</a></li>
    </ul>
</div>

<!-- Content Section -->
<div class="content" id="content">
    <center>
        <h1>Welcome {name[0][0]} {name[0][1]}</h1>
    </center>
</div>

<!-- JavaScript for Sidebar Toggle -->
<script>
    function toggleSidebar() {{
        var sidebar = document.getElementById("sidebar");
        var overlay = document.getElementById("overlay");
        var content = document.getElementById("content");

        sidebar.classList.toggle("active");
        overlay.classList.toggle("active");

        if (window.innerWidth > 768) {{
            content.style.marginLeft = sidebar.classList.contains("active") ? "250px" : "0";
        }}
    }}
</script>

</body>
</html>
""")
