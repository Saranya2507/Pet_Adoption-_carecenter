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
q = f"""select Animal_id from addanimal"""
cur.execute(q)
animal = cur.fetchone()
ani_id= animal[0]
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
    <div class="content">
        <form class="d-flex justify-content-center mt-3" method="get">
            <input type="hidden" name="id" value="{careid}">
            <input type="search" name="search" class="form-control me-2" placeholder="Search for pets" style="max-width: 300px;" required>
            <input type="submit" class="btn btn-outline-success" value="Search">
        </form><br>
        <div class="container text-center">
            <div class="row">
    
    """)
q="""select* from tip"""
cur.execute(q)
tips=cur.fetchall()
for t in tips:
    list=t[4].split(',')
    content=t[5][:50]
    print(f"""
        <div class="col-md-3 col-sm-6 p-3">
            <div class="card mt-2 p-2">
                <div class="card-body">
                    <h2 class="card-title" style="font-size: 100%; font-family: Cambria;">{t[2]}</h2><br>
                    <b>{', '.join(list)}:</b> {content}...<br>
                    <button type="button" class="btn btn-primary mt-2" data-bs-toggle="modal" data-bs-target="#tipModal{t[0]}">
                        More
                    </button>
                </div>
            </div>
        </div>
        <div class="modal fade" id="tipModal{t[0]}" tabindex="-1" aria-labelledby="tipModalLabel{t[0]}" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="tipModalLabel{t[0]}">{t[2]}</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <b>Tip for:</b>{', '.join(list)}<br>
                        <b>Tip:</b> {t[5]}<br>
                    </div>
                </div>
            </div>
        </div>
    """)

search=form.getvalue('search')
if search:
    print(f"""
        <script>
            location.href ='search_result.py?id={userid}&search={search}';
        </script>
    """)

print(f"""
        </div>
            </div>
    </div>
    
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
