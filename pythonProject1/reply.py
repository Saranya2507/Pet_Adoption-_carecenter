#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="petmatch")
cur = con.cursor()
form = cgi.FieldStorage()
userid = form.getvalue('id')
shelterid = form.getvalue('id')
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
         <h1 class="text-center my-4">Your Questions and Replies</h1>
        <table class="table table-bordered table-striped">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Animal ID</th>
                    <th>Your Question</th>
                    <th>Reply</th>
                </tr>
            </thead>
            <tbody>
""")
z=f"""select ID,Animal_id, Question from question where Shelter_id ='{shelterid}'"""
cur.execute(z)
re=cur.fetchall()
i=1
for r in re:
    Animal_id = r[1]
    question = r[2]
    id=r[0]
    b = f"""select * from reply where ID='{id}'"""
    cur.execute(b)
    l = cur.fetchone()
    reply = l[3]
    print(f"""
        <tr>
            <td>{i}</td>
            <td>{Animal_id}</td>
            <td>{question}</td>
            <td>{reply}</td>
        </tr>
    """)
    i += 1

else:
    print("""
    <script>
        alert("You didn't ask any questions.");
    </script>
    </div>
    </body>
    </html>
    """)
