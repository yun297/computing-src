<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>PHP arrays</title>
	<style>
		body { margin:0}
		h1 {
			text-align: center;
			padding : 0.5em;
			color: #fff;
			background:#000;
			margin:0;
		}
		table {
			margin: 2em auto;
			border-collapse: collapse;
			border : 2px solid #999;
		}
		thead { background : #999; color : #fff; }
		td, th { padding: 0.5em; text-align: center; }
		tbody td:first-child {text-align:left; color : #666;}
		tbody tr:nth-child(odd) { background : #fef; }
	</style>
</head>
<h1>Subject scores</h1>
<body>
<!--
<?php
$data = array(
array("Name"=>"Bob", "EL"=>80, "CL"=>65, "CH"=>90, "PH"=>78, "MA"=>92),
array("Name"=>"Tom", "EL"=>88, "MA"=>72, "PH"=>92, "CH"=>81, "CL"=>89),
array("Name"=>"Alan", "PH"=>80, "MA"=>69, "CH"=>77, "EL"=>62, "CL"=>74),
array("Name"=>"Dick", "CH"=>79, "CL"=>69, "EL"=>89, "PH"=>59, "MA"=>91)
);
?>
-->
<table>
<thead>
<?php
// print the HTML table header row
/*
 write a loop, using foreach, to print out the HTML template below :
 <tr>
   <th>subject_1_name</th>
   <th>subject_2_name</th>
   . . . . 
 </tr>
*/

foreach($data[0] as $key => $value){
	echo "<th>$key</th>";
}

echo "<th>Mean</th>"


?>
</thead>
<tbody>
<?php
//print the rows of data
/*
use foreach to loop through $data and for every student, print out their data.
HTML template :
<tr>
<td>Name</td>
<td>subject_1_score</td>
. . . . 
</tr>
*/

foreach($data as $value){
	echo "<tr>";
	$mean = 0;
	foreach($value as $key => $score){
		echo "<td>$score</td>";
		if(gettype($score) == "integer"){
			$mean += $score;
		}
	}
	$mean = round($mean/5);
	echo "<td>$mean</td>";
	echo "</tr>";
}

?>
</tbody>
</table>
</body>
</html>