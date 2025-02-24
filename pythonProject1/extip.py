#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql
cgitb.enable()
con=pymysql.connect(host="localhost", user="root", password="", database="petmatch")
cur=con.cursor()
form=cgi.FieldStorage()
userid=form.getvalue('id')
shelterid=form.getvalue('id')
careid=form.getvalue('id')
q=f"""select id from addanimal"""
cur.execute(q)
animal=cur.fetchone()
ani_id=animal[0]
q=f"""select id from tip"""
cur.execute(q)
tip=cur.fetchone()
tip_id=tip[0]
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
form {{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 100%;
        max-width: 900px;
        padding: 2%;
        margin: auto;
        border-radius: 10px;
        background: rgba(255, 255, 255, 0.3);
    }}
    form p {{
        color: black;
    }}
    .form-row {{
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        margin-bottom: 10px;
    }}
    .form-row label {{
        flex: 1;
        margin-right: 10px;
        font-family: Serif;
        font-size: 20px;
        color: black;
    }}
    .form-row input {{
        flex: 2;
        width:100%;
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
          <li><a class="dropdown-item" href="cctips.py?id={careid}">Give your Tip</a></li>
            <li><a class="dropdown-item" href="extip.py?id={careid}">Existing Tip</a></li>
          </ul>
      </li>
            <li><a href="suggestions.py?id={careid}"">Suggestions</a></li>
            <li><a href="home.py">Log Out</a></li>
        </ul>
</div>
    <div class="content">
        <div class="container text-center">
            <div class="row">
    """)
q=f"""select* from tip where Care_id='{careid}'"""
cur.execute(q)
tips=cur.fetchall()
for t in tips:
    list=t[4].split(',')
    content=t[5]
    print(f"""
        <div class="col-md-3 col-sm-6 p-3">
            <div class="card mt-2 p-2">
                <div class="card-body">
                    <h2 class="card-title" style="font-size: 100%; font-family: Cambria;">{t[2]}</h2><br>
    """)
    for tip_for in list:
        print(f"""<b>{tip_for.strip()}:</b>{content[:25]}...<br>""")
    print(f"""
                    <input type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#moreModal{t[0]}" value="More">
                    <input type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal1{t[0]}" value="Edit Tip">
                    <form method="post" style="display:inline;">
                        <input type="hidden" name="del_id" value="{t[0]}">
                        <input type="submit" class="btn btn-danger" name="del" value="Delete">
                    </form>
                </div>
            </div>
        </div>
        <div class="modal fade" id="moreModal{t[0]}" tabindex="-1" role="dialog" aria-labelledby="moreModalCenterTitle" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="moreModalLongTitle">Full Tips for {t[2]}</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
    """)
    q=f"""select Tip_for, Tip from tip where Animal_type='{t[2]}'"""
    cur.execute(q)
    all_tips = cur.fetchall()
    for full_tip in all_tips:
        for_all=full_tip[0].split(',')
        tip_content=full_tip[1]
        for tip in for_all:
            print(f"""
                        <b>{tip.strip()}:</b> {tip_content}<br><br>
                    """)
    print(f"""
                    </div>
                </div>
            </div>
        </div>
         <div class="modal fade" id="myModal1{t[0]}" tabindex="-1" role="dialog" aria-labelledby="moreModalCenterTitle" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="form">
                            <form class="row g-3" method="post" enctype="multipart/form-data">
                                <h2> Modify Your Tip</h2>
                                <input type="hidden" name="idd" value="{t[0]}">
                                <input type="hidden" name="cid" value="{t[1]}">
                                <div class="input-group">
                                    <label for="anitype" class="form-label">Animal Type</label>
                                    <input type="text" class="form-control" name="type" value="{t[2]}">
                                </div><br>
                                <div class="input-group">
                                    <label for="tipfor" class="form-label">Tip for:</label>
                                    <input type="text" class="form-control" name="tipfor" value="{t[4]}">
                                </div>
                                <div class="input-group">
                                    <label for="tip" class="form-label">Give Your Tip :</label>
                                    <textarea id="tip" name="tip" rows="5" cols="100">{t[5]}</textarea>
                                </div>
                                <div class="col-12">
                                <input type="submit" class="btn btn-primary" value="Update" name="upd">
                            </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
         </div>       
    """)
print(f"""
        
        </div>
    </div>
</body>
</html>
      """)
tip_id=form.getvalue('idd')
careid=form.getvalue('cid')
type= form.getvalue('type')
tipfor=','.join(form.getlist('tipfor'))
tip=form.getvalue('tip')
update=form.getvalue('upd')
if update!= None:
    update=f"""update tip set Animal_type='{type}',Tip_for='{tipfor}',Tip='{tip}' where Care_id='{careid}' and ID='{tip_id}'"""
    cur.execute(update)
    con.commit()
    print(f"""
        <script>
            alert("Tip updated successfully");
            location.href="extip.py?id={careid}";
        </script>
    """)
delete=form.getvalue('del')
del_id=form.getvalue('del_id')
if delete and del_id:
    d=f"""delete from tip where ID='{del_id}'"""
    cur.execute(d)
    con.commit()
    print(f"""
        <script>
            alert("Deleted Successfully");
            location.href="extip.py?id={careid}";
        </script>
    """)