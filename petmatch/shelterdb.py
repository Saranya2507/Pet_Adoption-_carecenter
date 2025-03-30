#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="petmatch")
cur = con.cursor()
form = cgi.FieldStorage()
shelterid = form.getvalue('id')

# Fetch shelter name
cur.execute(f"SELECT Name FROM shelterreg WHERE id='{shelterid}'")
shname = cur.fetchone()

# Fetch total pets in the shelter
cur.execute(f"SELECT COUNT(*) FROM addanimal WHERE shelter_id='{shelterid}'")
total_pets = cur.fetchone()[0]

# Fetch total adoption requests for the shelter's pets
cur.execute(f"SELECT COUNT(*) FROM adopt WHERE status='new' AND shelter_id='{shelterid}'")
total_requests = cur.fetchone()[0]

# Fetch total approved adoptions
cur.execute(f"SELECT COUNT(*) FROM adopt WHERE status='accepted' AND shelter_id='{shelterid}'")
approved_adoptions = cur.fetchone()[0]

print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shelter Dashboard</title>

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

    <!-- Main Content -->
    <div class="container text-center mt-4">
        <h1>Welcome, {shname[0]}</h1>

        <!-- Dashboard Cards -->
        <div class="row mt-4">
            <div class="col-md-4 col-sm-6 mb-3">
                <div class="dashboard-card">
                    <h3>Total Pets</h3>
                    <p>{total_pets}</p>
                </div>
            </div>
            <div class="col-md-4 col-sm-6 mb-3">
                <div class="dashboard-card">
                    <h3>Adoption Requests</h3>
                    <p>{total_requests}</p>
                </div>
            </div>
            <div class="col-md-4 col-sm-6 mb-3">
                <div class="dashboard-card">
                    <h3>Approved Adoptions</h3>
                    <p>{approved_adoptions}</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>
""")
