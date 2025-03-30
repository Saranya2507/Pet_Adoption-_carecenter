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
    
    <script>
        function toggleSidebar() {{
            document.getElementById("sidebar").classList.toggle("active");
        }}
    </script>
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