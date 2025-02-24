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
    form {{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 60%;
        padding: 2%;
        margin: auto;
        border:5px black solid;
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
            <h2 style="color:white;">Care Center Dashboard</h2>
            <li><a href="careprofile.py?id={careid}">Profile</a></li>
            <li><a href="adopters.py?id={careid}&ani_id={ani_id}">Adopters</a></li>
             <li class="dropdown">
          <a class="nav-link dropdown-toggle" href="" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Tips for a pet
          </a>
          <ul class="dropdown-menu dropdown-menu-dark">
          <li><a class="dropdown-item" href="cctip.py?id={careid}">Give your Tip</a></li>
            <li><a class="dropdown-item" href="extip.py?id={careid}">Existing Tip</a></li>
          </ul>
      </li>
            <li><a href="suggestions.py?id={careid}"">Suggestions</a></li>
            <li><a href="home.py">Log Out</a></li>
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