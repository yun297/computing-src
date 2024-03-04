<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=100%, initial-scale=1.0">
	<title>form</title>
	<style>
@import url(https://fonts.googleapis.com/css?family=Lato:100,300,400);

header {
  margin: 100px 0 25px 0;
  font-size: 2.3em;
  text-align: center;
  letter-spacing: 7px;
}
input::placeholder{
  color: #bbb5af;
  font-size: 0.875em;
}
input:hover::placeholder{
  color: #5e5c5b;
  font-size: 0.875em;
}
input:hover {
  background: #e2b99b7a;
  color: #291505;
}
body {
  font-family: 'Lato', sans-serif;
  background: #fdf4f4;
  color: #462b17;
}
form {
  width: 500px;
  margin: 50px auto;
}
input {
  font-family: 'Lato', sans-serif;
  font-size: 0.875em;
  width: 470px;
  height: 50px;
  padding: 0px 15px;
  background: transparent;
  outline: none;
  color: #150b01;
  border: solid 1px #f5ad79;
  border-bottom: none;
  transition: all 0.3s ease-in-out;
}

[type=submit] {
  width: 502px;
  padding: 0;
  margin: -5px 0px 0px 0px;
  font-size: 0.875em;
  color: #210903;
  background-color: #71e360;
  
  outline:none;
  cursor: pointer;
  
  border: solid 1px #b3aca7;
  border-top: none;
}
	</style>
</head>
<body>
	<header>MINIMALISTIC FORM</header>
	<form action="process-form.php" method="request">
		  <input name="firstname" type="text" placeholder="First Name">
		  <input name="lastname" type="text" placeholder="Last Name">
		  <input name="email" type="text" placeholder="E-MAIL">
		  <input name="form_submitted" type="hidden" value="1">
  		<input name="submit" type="submit" value="GO!">
  	</form>	
</body>
</html>