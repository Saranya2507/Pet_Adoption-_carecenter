#!C:/Users/saran/AppData/Local/Programs/Python/Python311-32/python.exe
print("content-type:text/html \r\n\r\n")
import cgi,cgitb,pymysql
cgitb.enable()
con=pymysql.connect(host="localhost",user="root",password="",database="petmatch")
cur=con.cursor()
form=cgi.FieldStorage()
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Adop Your Pet</title>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
    crossorigin="anonymous"></script>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" 
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css"
    integrity="sha512-5A8nwdMOWrSz20fDsjczgUidUBR8liPYU+WymTZP1lmY9G6Oc7HlZv156XqnsgNUzTyMefFTcsFH/tnJE/+xBg=="
    crossorigin="anonymous">
</head>
<style>
  .head {{
    text-align: center;
  }}
  .head a {{
    color:black;
    text-decoration:none;
    font-family:Serif;
    font-size:150%;
  }}
  .carousel-inner img {{
    width: 100%; 
    height: 700px;
    object-fit: cover;
    }}
  .card-img-overlay h2{{
    color:white;
  }}
  .footer-content{{
    display:flex
  }}
  .card {{
    width: 18rem;
    height:100%;
    margin-bottom: 20px;
    display: flex;
    flex-direction: column;
    border-radius: 10px;
}}
.card img {{
    width: 100%;
    height: 200px;
    object-fit: cover;
}}
</style>
<body>
  <div class="head d-flex align-items-center">
  <div class="logo1">
    <img src="./logo.jpg" style="width:60px; height:60px;">
  </div>
  <ul class="nav ms-auto">
    <li class="nav-item dropdown">
      <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">Login</a>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="userlog.py">User</a></li>
         <li><a class="dropdown-item" href="shelterlog.py">Shelter</a></li>
          <li><a class="dropdown-item" href="carelog.py">Care center</a></li>
          <a class="nav-link active" aria-current="page" href="adminlog.py">Admin</a>
        
      </ul>
    </li>
    <li class="nav-item dropdown">
      <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">Registration</a>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="userreg.py">User</a></li>
        <li><a class="dropdown-item" href="shelterreg.py">Shelter</a></li>
        <li><a class="dropdown-item" href="carereg.py">Care center</a></li>
      </ul>
    </li>
  </ul>
</div>
<br>
  <div class="logo">
    <div id="carouselExample" class="carousel slide">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="./cat1.jpg" class="d-block w-100" alt="...">
       <div class="card-img-overlay" style="padding:8%;">
        <h2>"Every pet deserves a loving home, and every heart deserves the joy of unconditional love. Find your perfect match with PetMatch."</h2>
      </div>
    </div>
    <div class="carousel-item">
      <img src="user1.jpg" class="d-block w-100" alt="...">
      <div class="card-img-overlay" style="padding:8%;padding-top:15%;">
        <h3 style="padding-left:38%;color:red">"Discover the joy<br> of companionship<br>find a furry friend <br>who's waiting <br>just for you."</h3>
      </div>
    </div>
    <div class="carousel-item">
      <img src="./shelter.jpg" class="d-block w-100" alt="...">
      <div class="card-img-overlay" style="padding-left:8%;padding-top:3%;">
        <h3 style="color:#002D62;">"Every rescue tells a story of hope-be the bridge to a loving forever home."</h3>
      </div>
      
    </div>
    <div class="carousel-item">
      <img src="./cc.jpg" class="d-block w-100" alt="...">
      <div class="card-img-overlay" style="padding-left:6%;padding-top:10%;">
        <h3 style="color:">"Healthy pets,<br> happy homes<br>because every life<br> deserves the best care."</h3>
      </div>
    </div>
    
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
  </div><br>
  """)
print(f"""
<div class="container text-center">
  <div class="row">
    <div class="col-md-3 col-sm-6 p-3">
      <div class="card mt-2 p-2">
        <img src="dog.jpg" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">Labrador Dog</h5>
          <p class="card-text">Some tips for the Labrador dogs.</p>
          <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal">Click for tips</button>
          <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered" role="document">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title" id="exampleModalLongTitle">Tip for Labrador Dog</h5>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  <b>Exercise:</b> Labrador puppies are energetic and need regular physical activity.<br>
                  <b>Socialization:</b> Expose your puppy to different people and situations.<br>
                  <b>Positive reinforcement:</b> Reward good behaviors with treats, games, or cuddles.<br>
                  <b>Training:</b> Establish consistent behavioral expectations.<br>
                  <b>Potty training:</b> Establish a potty spot.<br>
                  <b>Grooming:</b> Brush your puppy's coat a few times a week.<br>
                  <b>Bonding:</b> Form a strong bond with your puppy.<br>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="col-md-3 col-sm-6 p-3">
      <div class="card mt-2 p-2">
        <img src="cat.jpg" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">Somali Cat</h5>
          <p class="card-text">Some tips for the Somali Cat.</p>
          <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal1">Click for tips</button>
          <div class="modal fade" id="myModal1" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered" role="document">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title" id="exampleModalLongTitle">Tip for Somali Cat</h5>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  <b>Grooming:</b> Somali cats need regular grooming to keep their coats tangle-free.<br>
                  <b>Health checks:</b> Regular vaccinations, parasite control, and health checks are important.<br>
                  <b>Choosing a Somali:</b> Learn about the pros and cons of buying versus adopting.<br>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
<div class="col-md-3 col-sm-6 p-3">
      <div class="card mt-2 p-2">
        <img src="parrot.jpg" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title"> Blue-and-yellow Macaw</h5>
          <p class="card-text">Some tips for the  Blue-and-yellow Macaw.</p>
          <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal2">Click for tips</button>
          <div class="modal fade" id="myModal2" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered" role="document">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title" id="exampleModalLongTitle">Tip for Somali Cat</h5>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  <b>Provide toys:</b>Blue-and-yellow Macaws are known for chewing, so provide toys that can withstand their beak strength. Rotate toys regularly to keep them interesting.<br> 
<b>Allow time outside the cage:</b>Blue-and-yellow Macaws need at least 3–4 hours outside of their cage each day. This helps keep them active, exploring, and flying, which prevents obesity and ensures their emotional well-being.<br> 
<b>Provide mental stimulation:</b>Blue-and-yellow Macaws thrive on attention and need adequate mental stimulation. If they don't get enough, they might scream out of boredom.<br>
<b>Provide a quality diet:</b>Feed your Blue-and-yellow Macaw a quality macaw nut, a specially formulated macaw blend, and fresh fruit and vegetables. You can also add vitamin supplements to their water two or three times a week.<br> 
<b>Avoid certain foods:</b>Don't feed your Blue-and-yellow Macaw lettuce, avocado, or apple seeds.<br> 
<b>Remove hazards:</b>Remove electrical wires, jewelry, and wooden furniture from the bird's environment.<br>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
<div class="col-md-3 col-sm-6 p-3">
      <div class="card mt-2 p-2">
        <img src="rabbit.jpg" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title"> Soviet Chinchilla</h5>
          <p class="card-text">Some tips for the  Soviet Chinchilla.</p>
          <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal3">Click for tips</button>
          <div class="modal fade" id="myModal3" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered" role="document">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title" id="exampleModalLongTitle">Tip for Somali Cat</h5>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  <b>Feeding:</b>Feed rabbits a regular schedule so they don't get stressed. You can give concentrated feed twice a day, once in the morning and once in the afternoon, and greens in the evening. Pellets that are 3-4 mm in diameter and 10-15 mm long are better than ground feed.<br> 
<b>Housing:</b>The ideal temperature for rabbits is 10-20°C and the ideal humidity is 55-65%.<br> 
<b>Handling:</b>Handle rabbits firmly but gently. You can pick up a rabbit by gripping the loose skin on its neck with one hand and supporting its hindquarters with the other. <br>
<b>Dust baths:</b>Chinchillas need dust baths a couple of times a week to keep their fur clean and oil-free.<br> 
<b>Wetting:</b>Avoid getting your chinchilla wet because it can take a long time for their thick fur to dry. Damp fur can cause inflammation of the skin underneath.<br>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

  """)
print("""
  </div>
</div><br>
<footer>
<div class="container text-center">
  <div class="row row-cols-1 row-cols-sm-2 row-cols-md-4">
    <div class="col">
        <h3>About Us</h3>
    <p class="para">Welcome</p>
    </div>
    <div class="col"><h3>Quick Links</h3>
            <ul>
                <li>About</li>
                <li>Services</li>
                <li>Portfolio</li>
                <li>Contact</li>
            </ul>
    </div>
    <div class="col"><h3>Contact Us</h3>
            <p>Email: petmatch@gmail.com
            <p>Phone: 987654327</p>
            <p>Address:Happy street, salem-12</p>
    </div>
    <div class="col"><h3>Follow Us</h3>
            <p>Facebook</p>
            <p>Twitter</p>
            <p>Instagram</p>
    </div>
  </div>
</div>
</div>
</footer>
</body>

</html>
      """)
