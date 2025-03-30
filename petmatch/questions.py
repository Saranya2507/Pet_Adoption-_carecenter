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
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css">

    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
        }}
        /* Navbar */
        .navbar {{
            background-color: #343a40;
        }}
        .navbar-brand, .navbar-nav .nav-link {{
            color: white;
            font-size: 18px;
        }}
        .navbar-nav .nav-link:hover {{
            color: #f8f9fa;
        }}
        .dropdown-menu-dark {{
            background-color: #343a40;
        }}
        .dropdown-menu-dark .dropdown-item {{
            color: white;
        }}
        .dropdown-menu-dark .dropdown-item:hover {{
            background-color: #495057;
        }}
        /* Dashboard Cards */
        .dashboard-card {{
            padding: 20px;
            border-radius: 10px;
            background: white;
            box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.1);
            text-align: center;
        }}
        .dashboard-card h3 {{
            font-size: 22px;
            margin-bottom: 10px;
        }}
        .dashboard-card p {{
            font-size: 18px;
            font-weight: bold;
            color: #007bff;
        }}
    </style>
</head>

<body>

    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Shelter Dashboard</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="profile.py?id={shelterid}">Profile</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="animalDropdown" role="button" data-bs-toggle="dropdown">
                            Animal
                        </a>
                        <ul class="dropdown-menu dropdown-menu-dark">
                            <li><a class="dropdown-item" href="shelter.py?id={shelterid}">Add Animal</a></li>
                            <li><a class="dropdown-item" href="expet.py?id={shelterid}">Existing Pet</a></li>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="adoptDropdown" role="button" data-bs-toggle="dropdown">
                            Adopt Request
                        </a>
                        <ul class="dropdown-menu dropdown-menu-dark">
                            <li><a class="dropdown-item" href="adoptreq.py?id={shelterid}">All Requests</a></li>
                            <li><a class="dropdown-item" href="adoptaccept.py?id={shelterid}">Accepted</a></li>
                            <li><a class="dropdown-item" href="adoptrej.py?id={shelterid}">Rejected</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="questions.py?id={shelterid}">Questions Asked</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-danger" href="home.py">Log Out</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
  <div class="content">
           <div class="table-responsive mt-4">
    <table class="table table-bordered">
        <thead class="table-dark">
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