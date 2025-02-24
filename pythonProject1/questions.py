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
    <title>Shelter Dashboard</title>
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
            <h2 style="color:white;">Shelter Dashboard</h2>
            <li><a href="profile.py?id={shelterid}"> Profile</a></li>
        <li class="dropdown-item">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Animal
          </a>
          <ul class="dropdown-menu dropdown-menu-dark">
            <li><a href="shelter.py?id={shelterid}">Add Animal</a></li>
            <li><a href="expet.py?id={shelterid}">Existing Pet</a></li>
          </ul>
        </li>
            <li class="dropdown-item">
          <a class="nav-link dropdown-toggle" href="" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Adopt Request
          </a>
          <ul class="dropdown-menu dropdown-menu-dark">
            <li><a href="adoptreq.py?id={shelterid}"> All Request</a></li>
            <li><a href="adoptaccept.py?id={shelterid}">Accepted</a></li>
            <li><a href="adoptrej.py?id={shelterid}">Rejected</a></li>
          </ul>
        </li>
        <li class="dropdown-item">
          <a class="nav-link dropdown-toggle" href="" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Questions & Replies
          </a>
        <ul class="dropdown-menu dropdown-menu-dark">
            <li><a href="questions.py?id={shelterid}">Questions Asked</a></li>
            <li><a href="replies.py?id={shelterid}">Replies</a></li>
        </ul>
        </li>
            <li><a href="home.py">Log Out</a></li>
      </ul>
</div>
    <div class="content">
        <h1 class="text-center">Questions for Your</h1>
        <table class="table table-bordered table-striped">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Animal ID</th>
                    <th>Question</th>
                    <th></th>
                </tr>
            </thead>
""")
z=f"""select ID from question"""
cur.execute(z)
ID=cur.fetchone()
q=f"""select * from question where status='not replied'"""
cur.execute(q)
questions=cur.fetchall()
i=1
for q in questions:
    print(f"""
        <tr>
            <td>{i}</td>
            <td>{q[2]}</td>
            <td>{q[4]}</td>
             <td>
                <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#replyModal{q[0]}">Reply</button>
                <div class="modal fade" id="replyModal{q[0]}" tabindex="-1" role="dialog" aria-labelledby="replyModalLabel{q[0]}" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered" role="document">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="replyModalLabel{q[0]}">Reply to User</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <form method="post" action="">
                                    <input type="hidden" name="quest" value="{q[4]}">
                                    <div class="mb-3">
                                        <label for="replyMessage" class="form-label">Your Reply</label>
                                        <textarea class="form-control" id="replyMessage" name="reply" rows="3" required></textarea>
                                    </div>
                                    <button type="submit" class="btn btn-success" name="reply">Send Reply</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </td>
        </tr>
    """)
    i+=1
print("""
        </table>
    </div>
</body>
</html>
""")

reply = form.getvalue('reply')
if reply:
      question=form.getvalue('quest')
      reply = form.getvalue('reply')
      update=f"""update question set status='replied'"""
      cur.execute(update)
      con.commit()
      if  question and reply:
            s = f"""insert into reply (Animal_id, User_id, Reply,Question) values('{q[2]}', '{q[3]}', '{reply}','{question}')"""
            cur.execute(s)
            con.commit()
            print(f"""
            <script>
                alert('Your reply has been sent successfully!');
            </script>
 """)