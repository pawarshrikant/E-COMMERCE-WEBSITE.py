MAIN.PHP
<!DOCTYPE html>
<html lang = "en">
<head>
	<title>Bootstrap Website Tutorial</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="">
</head>
<body>

</body>
</html>


CONTACT PHP

<!DOCTYPE html>
<html lang="en">
<!-- min-height: 55px;
  	padding: 0 15px 15px; 

  	.navbar-brand{
  	float: left;
  	
  	min-height: 55px;
  	padding: 0 15px 15px;
  	
  }-->
<head>
  <title>Electricks Electronic parts</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <style>

  h1.header1{
  		color: #660000;
  }
  body{

  	font-family: Verdana, Geneva, sans-serif;
	}
  .navbar {
  		margin-bottom: 0;
  		border-radius: 0;
  		background-color: #660000;
  		color: #FFF;
  		padding: 1% 0%;
  		font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol";
  		font-size: 1.3em;
  		border: 0;
  }
  .left{

  	float: left;
  }
 
  
  .navbar-inverse .navbar-nav .active a, .navbar-inverse .navbar-nav .active a:focus, .navbar-inverse .navbar-nav .active a:hover{
  	color: #FFF;
  	background-color: #660000;
  	



  }
  

  .navbar-inverse .navbar-nav li a{

  	color: #D5D5D5;
  }
  .carousel-caption{
  	top: 50%;
  	transform: translateY(-50%);
  	text-transform: uppercase;
  }
  .btn{
  	font-size: 18px;
  	color: #FFF;
  	padding: 12px 22px;
  	background-color: orange;
  	border: 2px solid #FFF; 
  }
  .container{
  	margin: 4% auto;
  }
  #icon{
  	max-width: 200px;
  	margin: 1% auto;
  }
  footer{
  	width: 100%;
  	background-color: orange;
  	padding: 5%;
  	color: #FFF;
  }
  .fa{
  	padding: 15px;
  	font-size: 25px;
  	color: #FFF;
  }
  .fa:hover{
  	color: #D5D5D5;
  	text-decoration: none;

  }
  .fa-facebook{
  	color: #365899;
  }
  .fa-twitter{

  	color: #1da1f2
  }
 


  

  @media (max-width: 900px){
   .fa{
   		font-size: 20px;
   		padding: 10px;
   }
  }


  @media (max-width: 600px){
  	.carousel-caption{
  		display: none;
  	}
  	#icon{
  		max-width: 150px;
  	}
  	h4{
  		font-size: 1.7em;
  	}

  }


  </style>
</head>
<body>
	<nav class="navbar navbar-inverse">
		<div class="container-fluid">
			<div class="navbar-header">
				<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#MyNavbar">
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				</button>
				
			</div>

			<div class="collapse navbar-collapse" id="MyNavbar">
				<a class="left" href="index.html"><img src="img/logo.png"></a>
					<ul class="nav navbar-nav navbar-left">
						<li class="active"><a href="index.html">Home</a></li>
						<li class="active"><a href="manage.php">Management</a></li>
						<li class="active"><a href="product.php">Products</a></li>
						<li class="active"><a href="../../../Electricks-shop/index.php">Buy Here!</a></li>
						<li class="active"><a href="contact.php">Contact Us</a></li>
					</ul>			
			</div>

		</div>
	</nav>

	<div id="myCarousel" class="carousel slide" data-ride="carousel">
		<ol class="carousel-indicators">
			<li data-target="#myCarousel" data-slide-to="0" class="active"></li>
			<li data-target="#myCarousel" data-slide-to="1" class="active"></li>
			<li data-target="#myCarousel" data-slide-to="2" class="active"></li>
		</ol>

		<div class="carousel-inner" role="listbox">
			<div class="item active">
				<img src="img/mountains.png">
				<div class="carousel-caption">
					
					<br>
				</div>

			</div>

			 <!--End Active-->
			<div class="item">
				<img src="img/snow.png">
				<div class="carousel-caption">
					
					<br>
				</div>
			</div>	
			<div class="item">
				<img src="img/red.png">
				<div class="carousel-caption">
					
					<br>
				</div>
			</div>	
		</div>	
		 <!--start slider controls -->

		<a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
			<span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
			<span class="sr-only">Previous</span>
		</a>

		<a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
			<span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
			<span class="sr-only">Next</span>
		</a>
	</div><!--end slider -->

	<div class="container text-center">
		
			
		
		<div class="row">
			<div class="col-sm-12">
			<img src="img/logofinal.png">
			</div>

			<div class="col-sm-12">
				<h1 class="header1">Electricks</h1>
				<h1>Overview of the Company</h1>		
				<h3>The name of our sister company of SERVES is ELECTRICKS. We come up in name of our sister company because SERVES offer services and solution to the problem of the client in their computer and ELECTRICKS offer product needed by the client to make a project or needed parts to repair their product. The company goals to become the best seller of electronics components and materials. The mission of company is to provide a quality and affordable product to fulfill the needs of customers. The vision is to give the quality and high standard product to satisfy the needs of the customers. </h3>
			</div>

			<div class="col-sm-4">
				<img src="img/bootstrap.png" id="icon">
				<h4>Boostrap</h4>
			</div>

			<div class="col-sm-4">
			<img src="img/css3.png" id="icon">
				<h4>Css3</h4>
			</div>
			
		</div>
	</div>

	<div class="container">
		<div class="row">
			<div class="col-md-6">
				<h4>qweqweqweqw</h4>
				<p>qweqweqweqw</p>
				<p>weqweqweqweq</p>
			</div>
			<div class="col-md-6">
				<img src="img/bootstrap2.jpg" class="img-responsive">
			</div>
		</div>
	</div>

	<div class="container">
			<div class="row">
				<div class="col-lg-3 col-md-3 col-sm-6 col-xs-12">
					<h4>gergerger</h4>
					<p>ergergergergeerger</p>
				</div>
				<div class="col-lg-3 col-md-3 col-sm-6 col-xs-12">
					<img src="img/sass.png" class="img-responsive">
				</div>
				<div class="col-lg-3 col-md-3 col-sm-6 col-xs-12">
					<h4>gdfgdfgdfg</h4>
					<p>dfgdfgdfgdf</p>
				</div>
				<div class="col-lg-3 col-md-3 col-sm-6 col-xs-12">
					<img src="img/less.png" class="img-responsive">
				</div>
			</div>
		</div>

	<div class="container">
		<div class="row">
			<h4><a href="#hidden" data-toggle="collapse">Care to learn Boostrap?</a></h4>
			<div id="hidden" class="collapse">
				<h4>qweqweqweqw</h4>
				<p>qweqweqweqw</p>
				<p>weqweqweqweq</p>
			</div>
		</div>
	</div>
	<!--footer-->

	<footer class="container-fluid text-center">
		<div class="row">
			<div class="col-sm-4">
				<h3> Develop By </h3>
				<br>
				<h4>Team ABC</h4>
			</div>
			<div class="col-sm-4">
				<h3>Connect</h3>
				<a href="#" class="fa fa-facebook"></a>
				<a href="#" class="fa fa-twitter"></a>
				<a href="#" class="fa fa-google"></a>
				<a href="#" class="fa fa-linkedin"></a>
				<a href="#" class="fa fa-youtube"></a>
			</div>
			<div class="col-sm-4">
				<img src="img/ironman2.png" class="icon">
			</div>

		</div>
	</footer>


</body>
</html>

HOME.PHP



<!DOCTYPE html>
<html lang="en">
<!-- min-height: 55px;
  	padding: 0 15px 15px; 

  	.navbar-brand{
  	float: left;
  	
  	min-height: 55px;
  	padding: 0 15px 15px;
  	
  }-->
<head>

  <title>Serves Web Tech Solution and Services</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <style>

  h1.header1{
  		color: #660000;
  }
  h1.header2{
  	background-color: #0000cc;
  	color: #FFF;
  }
  body{

  	font-family: Verdana, Geneva, sans-serif;
	}
  .navbar {
  		margin-bottom: 0;
  		border-radius: 0;
  		background-color: #0000cc;
  		color: #FFF;
  		padding: 1% 0%;
  		font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol";
  		font-size: 1.3em;
  		border: 0;
  }
  .left{

  	float: left;
  }
	 
 
  .navbar-inverse .navbar-nav .active a, .navbar-inverse .navbar-nav .active a:focus, .navbar-inverse .navbar-nav {
  	color: #FFF;
  	background-color: #0000cc;
  	



  }

  

  .navbar-inverse .navbar-nav li a{

  	color: #D5D5D5;
  }
  .carousel-caption{
  	top: 50%;
  	transform: translateY(-50%);
  	text-transform: uppercase;
  }
  .btn{
  	font-size: 18px;
  	color: #D3D3D3;
  	padding: 12px 22px;
  	background-color: orange;
  	border: 2px solid #FFF; 
  }
  .container{
  	margin: 4% auto;
  }
  #icon{
  	max-width: 200px;
  	margin: 1% auto;
  }
  footer{
  	width: 100%;
  	background-color: #0000cc;
  	padding: 5%;
  	color: #FFF;
  }
  .fa{
  	padding: 15px;
  	font-size: 25px;
  	color: #FFF;
  }
  .fa:hover{
  	color: #D5D5D5;
  	text-decoration: none;

  }
  .fa-facebook{
  	color: #365899;
  }
  .fa-twitter{

  	color: #1da1f2
  }
  .color{
  		color: #0000cc;
  		font-size: 5rem;
  }
  div.line{
  	background-color: #0000cc;
  }
 


  

  @media (max-width: 900px){
   .fa{
   		font-size: 20px;
   		padding: 10px;
   }
  }


  @media (max-width: 600px){
  	.carousel-caption{
  		display: none;
  	}
  	#icon{
  		max-width: 150px;
  	}
  	h4{
  		font-size: 1.7em;
  	}

  }


  </style>
</head>
<body>
	<nav class="navbar navbar-inverse">
		<div class="container-fluid">
			<div class="navbar-header">
				<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#MyNavbar">
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				</button>
				
			</div>

			<div class="collapse navbar-collapse" id="MyNavbar">
				
				
				
				<a class="left" href="home.php"><img src="img/serve.png"></a>
					<ul class="nav navbar-nav navbar-left">
						<li class="active"><a href="home.php">Home</a></li>
						<li class="active"><a href="management.php">Management</a></li>
						<li class="active"><a href="services.php">Services</a></li>
						<li class="active"><a href="product.php">Products</a></li>
						<li class="active"><a href="../../../Electricks-shop/index.php">Buy Here!</a></li>
						
					</ul>		
					<ul class="nav navbar-nav navbar-right">
						<li class="active"><a>Contact Us</a></li>
						<li class="active"><a href="https://www.facebook.com/Serves-Web-Tech-Solution-and-Services-207908169756361/" class="fa fa-facebook"></a></li>
						<li class="active"><a href="https://twitter.com/mark_angelo503" class="fa fa-twitter"></a></li>
						<li class="active"><a href="#" class="fa fa-google"></a></li>
					</ul>		
			</div>
		</div>
	</nav>

	<!--end slider -->
	<div class="container text-center">
		<div class="row">
			<div>
			<h1 class="header2">Home</h1>
			</div>
		</div>
	</div>


	<div class="container">
		<div class="row">
			<div class="col-md-6">
				<h1 class="color">Serves</h1>
				<h3>“Serving with quality and sufficiency”</h3>
				<h4>We are a company open to serve the needs of the clients and provide solutions that can help people understand the technology.</h4>
				<h1>Mission</h1>
				<h4>Providing High-quality solutions and services fulfilling the needs in development and technology by being one of the best companies wherever we are.</h4>
				<h1>Vision</h1>
				<h4><li>To satisfy the clients need and desired service</li></h4>
				<h4><li>To develop not only the service but also the skills of the employees</li></h4>
				<h4><li>And be known in our field of business</li></h4>
			</div>
			<div class="col-md-6">
				<img src="img/logoserves.png" class="img-responsive">
			</div>
		</div>
	</div>

	
	<!--<div class="container">
		<div class="row">
			<h4><a href="#hidden" data-toggle="collapse">Care to learn Boostrap?</a></h4>
			<div id="hidden" class="collapse">
				<h4>qweqweqweqw</h4>
				<p>qweqweqweqw</p>
				<p>weqweqweqweq</p>
			</div>
		</div>
	</div>
	footer-->

	<footer class="container-fluid text-center">
		<div class="row">
			<div class="col-sm-6">
				<h3> Develop By </h3>
				<br>
				<h4>Team ABC</h4>
				<h4>Team AAbsent</h4>
			</div>
			<!--<div class="col-sm-">
				<h3>Connect</h3>
				<a href="#" class="fa fa-facebook"></a>
				<a href="#" class="fa fa-twitter"></a>
				<a href="#" class="fa fa-google"></a>
				<a href="#" class="fa fa-linkedin"></a>
				<a href="#" class="fa fa-youtube"></a>
			</div>-->
			<div class="col-sm-6">
				<img src="img/ironman2.png" class="icon">
			</div>

		</div>
	</footer>


</body>
</html>

MANAGE.PHP


<!DOCTYPE html>
<html lang="en">
<!-- min-height: 55px;
  	padding: 0 15px 15px; -->
<head>
  <title>Electricks Electronic parts</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <style>
  
  .navbar {
  		margin-bottom: 0;
  		border-radius: 0;
  		background-color: #660000;
  		color: #FFF;
  		padding: 1% 0;
  		font-family: "Times New Roman", Times, serif;

  		font-size: 1.2em;
  		border: 0;
  }
 
  
  .navbar-inverse .navbar-nav .active a, .navbar-inverse .navbar-nav .active a:focus, .navbar-inverse .navbar-nav .active a:hover{
  	color: #FFF;
  	background-color: #660000;

  	

  }
  

  .navbar-inverse .navbar-nav li a{

  	color: #D5D5D5;
  }
  .carousel-caption{
  	top: 50%;
  	transform: translateY(-50%);
  	text-transform: uppercase;
  }
  .btn{
  	font-size: 18px;
  	color: #FFF;
  	padding: 12px 22px;
  	background-color: orange;
  	border: 2px solid #FFF; 
  }
  .container{
  	margin: 4% auto;
  }
  #icon{
  	max-width: 200px;
  	margin: 1% auto;
  }
  footer{
  	width: 100%;
  	background-color: orange;
  	padding: 5%;
  	color: #FFF;
  }
  .fa{
  	padding: 15px;
  	font-size: 25px;
  	color: #FFF;
  }
  .fa:hover{
  	color: #D5D5D5;
  	text-decoration: none;

  }
  .fa-facebook{
  	color: #365899;
  }
  .fa-twitter{

  	color: #1da1f2
  }



  @media (max-width: 900px){
   .fa{
   		font-size: 20px;
   		padding: 10px;
   }
  }


  @media (max-width: 600px){
  	.carousel-caption{
  		display: none;
  	}
  	#icon{
  		max-width: 150px;
  	}
  	h4{
  		font-size: 1.7em;
  	}

  }


  </style>
</head>
<body>
	<nav class="navbar navbar-inverse">
		<div class="container-fluid">
			<div class="navbar-header">
				<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#MyNavbar">
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				</button>
				<a class="navbar-brand" href="index.html"><img src="img/logofinal.png"></a>
			</div>
			<div class="collapse navbar-collapse" id="MyNavbar">
					<ul class="nav navbar-nav navbar-left">
						<li class="active"><a href="home.php">Home</a></li>
						<li class="active"><a href="manage.php">Management</a></li>
						<li class="active"><a href="product.php">Products</a></li>
						<li class="active"><a href="../../../Electricks-shop/index.php">Buy Here!</a></li>
						<li class="active"><a href="contact.php">Contact</a></li>
					</ul>			
			</div>
		</div>
	</nav>

	<div id="myCarousel" class="carousel slide" data-ride="carousel">
		<ol class="carousel-indicators">
			<li data-target="#myCarousel" data-slide-to="0" class="active"></li>
			<li data-target="#myCarousel" data-slide-to="1" class="active"></li>
			<li data-target="#myCarousel" data-slide-to="2" class="active"></li>
		</ol>
		<div class="carousel-inner" role="listbox">
			<div class="item active">
				<img src="img/TeamABC.jpg">
				<div class="carousel-caption">
					<h1>About Us Developers </h1>
					<br>
				</div>

			</div>
			<!-- End Active-->
			<div class="item">
				<img src="img/snow.png">
				<div class="carousel-caption">
					<h1>Electricks </h1>
					<br>
				</div>
			</div>	
			<div class="item">
				<img src="img/red.png">
				<div class="carousel-caption">
					<h1>About Us Developers</h1>
					<br>
				</div>
			</div>	
		</div>	
		<!-- start slider controls -->
		<a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
			<span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
			<span class="sr-only">Previous</span>
		</a>

		<a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
			<span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
			<span class="sr-only">Next</span>
		</a>
	</div>
	<!--end slider -->
	<div class="container text-center">
		<h2>Senior Management</h2>
		<div class="row">
			<div class="col-sm-12">
				<img src="img/gelo.jpg" id="icon">
				<h4>Mark Angelo B. Eleazar</h4>
				<h4>CEO</h4>
					<div class="col-sm-12">
						<a href="https://www.facebook.com/markgeloe" class="fa fa-facebook"></a>
						<a href="https://twitter.com/mark_angelo503" class="fa fa-twitter"></a>
					</div>
			</div>
			<h2>Middle Management</h2>
			<div class="col-sm-6">
				<img src="img/carl.jpg" id="icon">
				<h4>Carl Darren M. Apelacion</h4>
				<h4>System Administrator</h4>
				<div class="col-sm-12">
						<a href="https://www.facebook.com/carl.apelacion" class="fa fa-facebook"></a>
						<a href="#" class="fa fa-twitter"></a>
				</div>
			</div>
			<div class="col-sm-6">
				<img src="img/billy.png" id="icon">
				<h4>Billy P. Revellame</h4>
				<h4>Developer</h4>
					<div class="col-sm-12">
						<a href="https://www.facebook.com/billybluerevellame.3" class="fa fa-facebook"></a>
						<a href="#" class="fa fa-twitter"></a>
					</div>
			</div>

		</div>
		<div class="row">
			<h2>Lower-Level Management</h2>
			<div class="col-sm-6">
				<img src="img/clark.jpg" id="icon">
				<h4>Clark Patrick C. Banaag</h4>
				<h4>Project Manager</h4>
				<div class="col-sm-12">
						<a href="https://www.facebook.com/shaoranbanaag69" class="fa fa-facebook"></a>
						<a href="#" class="fa fa-twitter"></a>
				</div>
			</div>
			<div class="col-sm-6">
				<img src="img/melo2.jpg" id="icon">
				<h4>Karmelo Leandrey R. Arenas</h4>
				<h4>I.T. Support</h4>
					<div class="col-sm-12">
						<a href="https://www.facebook.com/olemrak.arenas" class="fa fa-facebook"></a>
						<a href="#" class="fa fa-twitter"></a>
					</div>
			</div>
			
		</div>
	</div>

	<div class="container">
		<div class="row">
			<div class="col-md-6">
				<h4>qweqweqweqw</h4>
				<p>qweqweqweqw</p>
				<p>weqweqweqweq</p>
			</div>
			<div class="col-md-6">
				<img src="img/bootstrap2.jpg" class="img-responsive">
			</div>
		</div>
	</div>

	<div class="container">
			<div class="row">
				<div class="col-lg-3 col-md-3 col-sm-6 col-xs-12">
					<h4>gergerger</h4>
					<p>ergergergergeerger</p>
				</div>
				<div class="col-lg-3 col-md-3 col-sm-6 col-xs-12">
					<img src="img/sass.png" class="img-responsive">
				</div>
				<div class="col-lg-3 col-md-3 col-sm-6 col-xs-12">
					<h4>gdfgdfgdfg</h4>
					<p>dfgdfgdfgdf</p>
				</div>
				<div class="col-lg-3 col-md-3 col-sm-6 col-xs-12">
					<img src="img/less.png" class="img-responsive">
				</div>
			</div>
		</div>

	<div class="container">
		<div class="row">
			<h4><a href="#hidden" data-toggle="collapse">Care to learn Boostrap?</a></h4>
			<div id="hidden" class="collapse">
				<h4>qweqweqweqw</h4>
				<p>qweqweqweqw</p>
				<p>weqweqweqweq</p>
			</div>
		</div>
	</div>
	<!--footer-->

	<footer class="container-fluid text-center">
		<div class="row">
			<div class="col-sm-4">
				<h3> Contact Us</h3>
				<br>
				<h4>Our address and contact</h4>
			</div>
			<div class="col-sm-4">
				<h3>Connect</h3>
				<a href="#" class="fa fa-facebook"></a>
				<a href="#" class="fa fa-twitter"></a>
				<a href="#" class="fa fa-google"></a>
				<a href="#" class="fa fa-linkedin"></a>
				<a href="#" class="fa fa-youtube"></a>
			</div>
			<div class="col-sm-4">
				<img src="img/ironman2.jpg" class="icon">
			</div>

		</div>
	</footer>


</body>
</html>

MANAGEMENT.PHP




<!DOCTYPE html>
<html lang="en">
<!-- min-height: 55px;
  	padding: 0 15px 15px; 

  	.navbar-brand{
  	float: left;
  	
  	min-height: 55px;
  	padding: 0 15px 15px;
  	
  }-->
<head>

  <title>Serves Web Tech Solution and Services</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <style>

  h1.header1{
  		color: #660000;
  }
  h1.header2{
  	background-color: #0000cc;
  	color: #FFF;
  }
  body{

  	font-family: Verdana, Geneva, sans-serif;
	}
  .navbar {
  		margin-bottom: 0;
  		border-radius: 0;
  		background-color: #0000cc;
  		color: #FFF;
  		padding: 1% 0%;
  		font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol";
  		font-size: 1.3em;
  		border: 0;
  }
  .left{

  	float: left;
  }
	 
 
  .navbar-inverse .navbar-nav .active a, .navbar-inverse .navbar-nav .active a:focus, .navbar-inverse .navbar-nav {
  	color: #FFF;
  	background-color: #0000cc;
  	



  }

  

  .navbar-inverse .navbar-nav li a{

  	color: #D5D5D5;
  }
  .carousel-caption{
  	top: 50%;
  	transform: translateY(-50%);
  	text-transform: uppercase;
  }
  .btn{
  	font-size: 18px;
  	color: #D3D3D3;
  	padding: 12px 22px;
  	background-color: orange;
  	border: 2px solid #FFF; 
  }
  .container{
  	margin: 4% auto;
  }
  #icon{
  	max-width: 200px;
  	margin: 1% auto;
  }
  footer{
  	width: 100%;
  	background-color: #0000cc;
  	padding: 5%;
  	color: #FFF;
  }
  .fa{
  	padding: 15px;
  	font-size: 25px;
  	color: #FFF;
  }
  .fa:hover{
  	color: #D5D5D5;
  	text-decoration: none;

  }
  .fa-facebook{
  	color: #365899;
  }
  .fa-twitter{

  	color: #1da1f2
  }
  .color{
  		color: #0000cc;
  		font-size: 5rem;
  }
  div.line{
  	background-color: #0000cc;
  }
 


  

  @media (max-width: 900px){
   .fa{
   		font-size: 20px;
   		padding: 10px;
   }
  }


  @media (max-width: 600px){
  	.carousel-caption{
  		display: none;
  	}
  	#icon{
  		max-width: 150px;
  	}
  	h4{
  		font-size: 1.7em;
  	}

  }


  </style>
</head>
<body>
	<nav class="navbar navbar-inverse">
		<div class="container-fluid">
			<div class="navbar-header">
				<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#MyNavbar">
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				</button>
				
			</div>

			<div class="collapse navbar-collapse" id="MyNavbar">
				
				
				
				<a class="left" href="home.php"><img src="img/serve.png"></a>
					<ul class="nav navbar-nav navbar-left">
						<li class="active"><a href="home.php">Home</a></li>
						<li class="active"><a href="management.php">Management</a></li>
						<li class="active"><a href="services.php">Services</a></li>
						<li class="active"><a href="product.php">Products</a></li>
						<li class="active"><a href="../../../Electricks-shop/index.php">Buy Here!</a></li>
						
					</ul>		
					<ul class="nav navbar-nav navbar-right">
						<li class="active"><a>Contact Us</a></li>
						<li class="active"><a href="https://www.facebook.com/Serves-Web-Tech-Solution-and-Services-207908169756361/" class="fa fa-facebook"></a></li>
						<li class="active"><a href="https://twitter.com/mark_angelo503" class="fa fa-twitter"></a></li>
						<li class="active"><a href="#" class="fa fa-google"></a></li>
					</ul>		
			</div>
		</div>
	</nav>

	<!--end slider -->
	<div class="container text-center">
		<div class="row">
			<div>
			<h1 class="header2">Management</h1>
			</div>
		</div>
	</div>


	<div class="container text-center">
		<h2>Senior Management</h2>
		<div class="row">
			<div class="col-sm-12">
				<img src="img/gelo.jpg" id="icon">
				<h4>Mark Angelo B. Eleazar</h4>
				<h4>CEO</h4>
					<div class="col-sm-12">
						<a href="https://www.facebook.com/markgeloe" class="fa fa-facebook"></a>
						<a href="https://twitter.com/mark_angelo503" class="fa fa-twitter"></a>
					</div>
			</div>
			<h2>Middle Management</h2>
			<div class="col-sm-6">
				<img src="img/carl.jpg" id="icon">
				<h4>Carl Darren M. Apelacion</h4>
				<h4>System Administrator</h4>
				<div class="col-sm-12">
						<a href="https://www.facebook.com/carl.apelacion" class="fa fa-facebook"></a>
						<a href="#" class="fa fa-twitter"></a>
				</div>
			</div>
			<div class="col-sm-6">
				<img src="img/billy.png" id="icon">
				<h4>Billy P. Revellame</h4>
				<h4>Developer</h4>
					<div class="col-sm-12">
						<a href="https://www.facebook.com/billybluerevellame.3" class="fa fa-facebook"></a>
						<a href="#" class="fa fa-twitter"></a>
					</div>
			</div>

		</div>
		<div class="row">
			<h2>Lower-Level Management</h2>
			<div class="col-sm-6">
				<img src="img/clark.jpg" id="icon">
				<h4>Clark Patrick C. Banaag</h4>
				<h4>Project Manager</h4>
				<div class="col-sm-12">
						<a href="https://www.facebook.com/shaoranbanaag69" class="fa fa-facebook"></a>
						<a href="#" class="fa fa-twitter"></a>
				</div>
			</div>
			<div class="col-sm-6">
				<img src="img/melo2.jpg" id="icon">
				<h4>Karmelo Leandrey R. Arenas</h4>
				<h4>I.T. Support</h4>
					<div class="col-sm-12">
						<a href="https://www.facebook.com/olemrak.arenas" class="fa fa-facebook"></a>
						<a href="#" class="fa fa-twitter"></a>
					</div>
			</div>
			
		</div>
	</div>

	<footer class="container-fluid text-center">
		<div class="row">
			<div class="col-sm-6">
				<h3> Develop By </h3>
				<br>
				<h4>Team ABC</h4>
				<h4>Team AAbsent</h4>
			</div>
			<!--<div class="col-sm-">
				<h3>Connect</h3>
				<a href="#" class="fa fa-facebook"></a>
				<a href="#" class="fa fa-twitter"></a>
				<a href="#" class="fa fa-google"></a>
				<a href="#" class="fa fa-linkedin"></a>
				<a href="#" class="fa fa-youtube"></a>
			</div>-->
			<div class="col-sm-6">
				<img src="img/ironman2.png" class="icon">
			</div>

		</div>
	</footer>


</body>
</html>

PRODCT.PHP



<!DOCTYPE html>
<html lang="en">
<!-- min-height: 55px;
    padding: 0 15px 15px; 

    .navbar-brand{
    float: left;
    
    min-height: 55px;
    padding: 0 15px 15px;
    
  }-->
<head>

  <title>Serves Web Tech Solution and Services</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <style>

  h1.header1{
      color: #660000;
  }
  h1.header2{
    background-color: #0000cc;
    color: #FFF;
  }
  body{

    font-family: Verdana, Geneva, sans-serif;
  }
  .navbar {
      margin-bottom: 0;
      border-radius: 0;
      background-color: #0000cc;
      color: #FFF;
      padding: 1% 0%;
      font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol";
      font-size: 1.3em;
      border: 0;
  }
  .left{

    float: left;
  }
   
 
  .navbar-inverse .navbar-nav .active a, .navbar-inverse .navbar-nav .active a:focus, .navbar-inverse .navbar-nav {
    color: #FFF;
    background-color: #0000cc;
    



  }

  

  .navbar-inverse .navbar-nav li a{

    color: #D5D5D5;
  }
  .carousel-caption{
    top: 50%;
    transform: translateY(-50%);
    text-transform: uppercase;
  }
  .btn{
    font-size: 18px;
    color: #D3D3D3;
    padding: 12px 22px;
    background-color: orange;
    border: 2px solid #FFF; 
  }
  .container{
    margin: 4% auto;
  }
  #icon{
    max-width: 200px;
    margin: 1% auto;
  }
  footer{
    width: 100%;
    background-color: #0000cc;
    padding: 5%;
    color: #FFF;
  }
  .fa{
    padding: 15px;
    font-size: 25px;
    color: #FFF;
  }
  .fa:hover{
    color: #D5D5D5;
    text-decoration: none;

  }
  .fa-facebook{
    color: #365899;
  }
  .fa-twitter{

    color: #1da1f2
  }
  .color{
      color: #0000cc;
      font-size: 5rem;
  }
  div.line{
    background-color: #0000cc;
  }
 


  

  @media (max-width: 900px){
   .fa{
      font-size: 20px;
      padding: 10px;
   }
  }


  @media (max-width: 600px){
    .carousel-caption{
      display: none;
    }
    #icon{
      max-width: 150px;
    }
    h4{
      font-size: 1.7em;
    }

  }


  </style>
</head>
<body>
  <nav class="navbar navbar-inverse">
    <div class="container-fluid">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#MyNavbar">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        
      </div>

      <div class="collapse navbar-collapse" id="MyNavbar">
        
        
        
        <a class="left" href="home.php"><img src="img/serve.png"></a>
          <ul class="nav navbar-nav navbar-left">
            <li class="active"><a href="home.php">Home</a></li>
            <li class="active"><a href="management.php">Management</a></li>
            <li class="active"><a href="services.php">Services</a></li>
            <li class="active"><a href="product.php">Products</a></li>
            <li class="active"><a href="../../../Electricks-shop/index.php">Buy Here!</a></li>
            
          </ul>   
          <ul class="nav navbar-nav navbar-right">
            <li class="active"><a>Contact Us</a></li>
            <li class="active"><a href="https://www.facebook.com/Serves-Web-Tech-Solution-and-Services-207908169756361/" class="fa fa-facebook"></a></li>
            <li class="active"><a href="https://twitter.com/mark_angelo503" class="fa fa-twitter"></a></li>
            <li class="active"><a href="#" class="fa fa-google"></a></li>
          </ul>   
      </div>
    </div>
  </nav>

  <!--end slider -->
  <div class="container text-center">
    <div class="row">
      <div>
      <h1 class="header2">Product</h1>
      </div>
    </div>
  </div>


  <div class="container text-center">
    <div class="row">
      <h1>Arduino</h1>
      <div class="col-md-6">
        <img src="img/uno.png" class="img-responsive">
      </div>
      <div class="col-md-6">
        <h1>Arduino Uno</h1>
        <h2>The Arduino Uno is a microcontroller board based on the ATmega328 (datasheet). It has 14 digital input/output pins (of which 6 can be used as PWM outputs), 6 analog inputs, a 16 MHz ceramic resonator, a USB connection, a power jack, an ICSP header, and a reset button.</h2>
      </div>
    </div>

    <div class="row">
      <div class="col-md-6">
        <img src="img/redboard.jpg" class="img-responsive">
      </div>
      <div class="col-md-6">
        <h1>RedBoard Arduino</h1>
        <h2>The SparkFun RedBoard is an Arduino-compatible development platform that enables quick-and-easy project prototyping. It can interact with real-world sensors, control motors, display information, and perform near-instantaneous calculations.</h2>
      </div>
    </div>

    <div class="row">
      <div class="col-md-6">
        <img src="img/shield.jpg" class="img-responsive">
      </div>
      <div class="col-md-6">
        <h1>Arduino Shield</h1>
        <h2>Shields are boards that can be plugged on top of the Arduino PCB extending its capabilities. The different shields follow the same philosophy as the original toolkit: they are easy to mount, and cheap to produce.</h2>
      </div>
    </div>

    <div class="row">
      <div class="col-md-6">
        <img src="img/raspi.jpg" class="img-responsive">
      </div>
      <div class="col-md-6">
        <h1>Raspberry pi</h1>
        <h2>The Raspberry Pi is a series of small single-board computers developed in the United Kingdom by the Raspberry Pi Foundation to promote the teaching of basic computer science in schools and in developing countries.</h2>
      </div>
    </div>

    <h1>Capacitor</h1>
    <div class="row">
      <div class="col-md-6">
        <img src="img/ceramic.jpeg" class="img-responsive">
      </div>
      <div class="col-md-6">
        <h1>Ceramic Capacitor</h1>
        <h2>A ceramic capacitor is a fixed-value capacitor in which ceramic material acts as the dielectric. It is constructed of two or more alternating layers of ceramic and a metal layer acting as the electrodes. The composition of the ceramic material defines the electrical behavior and therefore applications.</h2>
      </div>
    </div>

    <div class="row">
      <div class="col-md-6">
        <img src="img/electrocapacitor.jpg" class="img-responsive">
      </div>
      <div class="col-md-6">
        <h1>Electrolytic Capacitor</h1>
        <h2>An electrolytic capacitor is a type of capacitor that uses an electrolyte as one of its plates, to achieve a larger capacitance per unit volume than other types of capacitors.</h2>
      </div>
    </div>

     <div class="row">
      <div class="col-md-6">
        <img src="img/tamtalum.jpg" class="img-responsive">
      </div>
      <div class="col-md-6">
        <h1>Tamtalum Capacitor</h1>
        <h2>A tantalum capacitor is a type of electrolytic capacitor and usually consists of a pellet of tantalum metal that acts as an anode, is covered by an insulating oxide layer which forms the dielectric and is surrounded by conductive material that acts as a cathode.</h2>
      </div>
    </div>

    <div class="row">
      <div class="col-md-6">
        <img src="img/resistor.jpg" class="img-responsive">
      </div>
      <div class="col-md-6">
        <h1>Resistor</h1>
        <h2>A resistor is an electrical component that limits or regulates the flow of electrical current in an electronic circuit. Resistors can also be used to provide a specific voltage for an active device such as a transistor.</h2>
      </div>
    </div>


  </div>

  
  <!--<div class="container">
    <div class="row">
      <h4><a href="#hidden" data-toggle="collapse">Care to learn Boostrap?</a></h4>
      <div id="hidden" class="collapse">
        <h4>qweqweqweqw</h4>
        <p>qweqweqweqw</p>
        <p>weqweqweqweq</p>
      </div>
    </div>
  </div>
  footer-->

  <footer class="container-fluid text-center">
    <div class="row">
      <div class="col-sm-6">
        <h3> Develop By </h3>
        <br>
        <h4>Team ABC</h4>
        <h4>Team AAbsent</h4>
      </div>
      <!--<div class="col-sm-">
        <h3>Connect</h3>
        <a href="#" class="fa fa-facebook"></a>
        <a href="#" class="fa fa-twitter"></a>
        <a href="#" class="fa fa-google"></a>
        <a href="#" class="fa fa-linkedin"></a>
        <a href="#" class="fa fa-youtube"></a>
      </div>-->
      <div class="col-sm-6">
        <img src="img/ironman2.png" class="icon">
      </div>

    </div>
  </footer>


</body>
</html>

SERVICES.PHP




<!DOCTYPE html>
<html lang="en">
<!-- min-height: 55px;
  	padding: 0 15px 15px; 

  	.navbar-brand{
  	float: left;
  	
  	min-height: 55px;
  	padding: 0 15px 15px;
  	
  }-->
<head>

  <title>Serves Web Tech Solution and Services</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <style>

  h1.header1{
  		color: #660000;
  }
  h1.header2{
  	background-color: #0000cc;
  	color: #FFF;
  }
  body{

  	font-family: Verdana, Geneva, sans-serif;
	}
  .navbar {
  		margin-bottom: 0;
  		border-radius: 0;
  		background-color: #0000cc;
  		color: #FFF;
  		padding: 1% 0%;
  		font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol";
  		font-size: 1.3em;
  		border: 0;
  }
  .left{

  	float: left;
  }
	 
 
  .navbar-inverse .navbar-nav .active a, .navbar-inverse .navbar-nav .active a:focus, .navbar-inverse .navbar-nav {
  	color: #FFF;
  	background-color: #0000cc;
  	



  }

  

  .navbar-inverse .navbar-nav li a{

  	color: #D5D5D5;
  }
  .carousel-caption{
  	top: 50%;
  	transform: translateY(-50%);
  	text-transform: uppercase;
  }
  .btn{
  	font-size: 18px;
  	color: #D3D3D3;
  	padding: 12px 22px;
  	background-color: orange;
  	border: 2px solid #FFF; 
  }
  .container{
  	margin: 4% auto;
  }
  #icon{
  	max-width: 200px;
  	margin: 1% auto;
  }
  footer{
  	width: 100%;
  	background-color: #0000cc;
  	padding: 5%;
  	color: #FFF;
  }
  .fa{
  	padding: 15px;
  	font-size: 25px;
  	color: #FFF;
  }
  .fa:hover{
  	color: #D5D5D5;
  	text-decoration: none;

  }
  .fa-facebook{
  	color: #365899;
  }
  .fa-twitter{

  	color: #1da1f2
  }
  .color{
  		color: #0000cc;
  		font-size: 5rem;
  }
  div.line{
  	background-color: #0000cc;
  }
 


  

  @media (max-width: 900px){
   .fa{
   		font-size: 20px;
   		padding: 10px;
   }
  }


  @media (max-width: 600px){
  	.carousel-caption{
  		display: none;
  	}
  	#icon{
  		max-width: 150px;
  	}
  	h4{
  		font-size: 1.7em;
  	}

  }


  </style>
</head>
<body>
	<nav class="navbar navbar-inverse">
		<div class="container-fluid">
			<div class="navbar-header">
				<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#MyNavbar">
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				</button>
				
			</div>

			<div class="collapse navbar-collapse" id="MyNavbar">
				
				
				
				<a class="left" href="home.php"><img src="img/serve.png"></a>
					<ul class="nav navbar-nav navbar-left">
						<li class="active"><a href="home.php">Home</a></li>
						<li class="active"><a href="management.php">Management</a></li>
						<li class="active"><a href="services.php">Services</a></li>
						<li class="active"><a href="product.php">Products</a></li>
						<li class="active"><a href="../../../Electricks-shop/index.php">Buy Here!</a></li>
						
					</ul>		
					<ul class="nav navbar-nav navbar-right">
						<li class="active"><a>Contact Us</a></li>
						<li class="active"><a href="https://www.facebook.com/Serves-Web-Tech-Solution-and-Services-207908169756361/" class="fa fa-facebook"></a></li>
						<li class="active"><a href="https://twitter.com/mark_angelo503" class="fa fa-twitter"></a></li>
						<li class="active"><a href="#" class="fa fa-google"></a></li>
					</ul>		
			</div>
		</div>
	</nav>

	<!--end slider -->
	<div class="container text-center">
		<div class="row">
			<div>
			<h1 class="header2">Services</h1>
			</div>
		</div>
	</div>


	<div class="container text-center">
		<div class="row">
			<h1>Services Offered</h1>
			<div class="col-sm-12">
				<img src="img/services.png" id="icon">
			</div>
			<div class="col-sm-4">
				<h2>Web Designing Services</h2>
				
						<h3><a href="#hidden1" data-toggle="collapse">Details</a></h3>
					<div id="hidden1" class="collapse">
							
							<p>Web design encompasses many different skills and disciplines in the production and maintenance of websites. The different areas of web design include web graphic design; interface design; authoring, including standardised code and proprietary software; user experience design; and search engine optimization.</p>
					</div>
			</div>
			<div class="col-sm-4">
						<h2>Software Development Services</h2>
				
						<h3><a href="#hidden2" data-toggle="collapse">Details</a></h3>
						<div id="hidden2" class="collapse">
							
							<p>Software development is the process of computer programming, documenting, testing, and bug fixing involved in creating and maintaining applications and frameworks resulting in a software product. ... The waterfall model is a traditional version, contrasted with the more recent innovation of agile software development.</p>
						</div>
			</div>

				<div class="col-sm-4">
					<h2>Web Hosting Services</h2>
				
						<h3><a href="#hidden3" data-toggle="collapse">Details</a></h3>
					<div id="hidden3" class="collapse">
							
							<p>A web hosting service is a type of Internet hosting service that allows individuals and organizations to make their website accessible via the World Wide Web.</p>
					</div>
				</div>

		</div>
		<div class="container">	
		<div class="row">
				<div class="col-sm-6">
					<h2>Website Maintenance Service</h2>
				
						<h3><a href="#hidden4" data-toggle="collapse">Details</a></h3>
					<div id="hidden4" class="collapse">
							
							<p>Performing all the tasks necessary to keep a website up to date and in good, working order so that it works and shows up correctly with the latest web browsers and mobile devices. ... Checking website error logs.</p>
					</div>
				</div>

				<div class="col-sm-6">
					<h2>Hardware Maintenance Service</h2>
				
						<h3><a href="#hidden5" data-toggle="collapse">Details</a></h3>
					<div id="hidden5" class="collapse">
							<p>These are preventive and remedial services that physically repair or optimize hardware, including basic installation, contract maintenance and per-incident repair — both on-site and at a centralized repair depot. Hardware support also includes telephone technical troubleshooting and assistance for setup and all fee-based hardware warranty upgrades. Exclusive of parts bundled into maintenance contracts, sales of all parts used to repair high-tech equipment in carry-in, mail-in or per-incident on-site delivery models, or purchased by the internal staff to perform the repair, are included.</p>
					</div>
				</div>

		</div>
	</div>
			

		
			

		</div>
	</div>

	
	<!--<div class="container">
		<div class="row">s
			<h4><a href="#hidden" data-toggle="collapse">Care to learn Boostrap?</a></h4>
			<div id="hidden" class="collapse">
				<h4>qweqweqweqw</h4>
				<p>qweqweqweqw</p>
				<p>weqweqweqweq</p>
			</div>
		</div>
	</div>
	footer-->

	<footer class="container-fluid text-center">
		<div class="row">
			<div class="col-sm-6">
				<h3> Develop By </h3>
				<br>
				<h4>Team ABC</h4>
				<h4>Team AAbsent</h4>
			</div>
			<!--<div class="col-sm-">
				<h3>Connect</h3>
				<a href="#" class="fa fa-facebook"></a>
				<a href="#" class="fa fa-twitter"></a>
				<a href="#" class="fa fa-google"></a>
				<a href="#" class="fa fa-linkedin"></a>
				<a href="#" class="fa fa-youtube"></a>
			</div>-->
			<div class="col-sm-6">
				<img src="img/ironman2.png" class="icon">
			</div>

		</div>
	</footer>


</body>
</html>
