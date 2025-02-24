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
.card{{
    height:100%;
    width:100%;
}}
        </style>
</head>
<body>
 <div class="sidebar">
         <ul>
            <h2 style="color:white;">User Dashboard</h2>
            <li><a href="usernew.py?id={userid}">Profile</a></li>
            <li><a href="pets.py?id={userid}">Pets</a></li>
             <li><a href="adopt.py?id={userid}">Adopt status</a></li>
            <li><a href="reply.py?id={userid}">Replies</a></li>
            <li><a href="tips.py?id={userid}">Tips for your pet</a></li>
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
</body>
</html>
      """)
