<?php

// $str = "";
// $data = array(
//   array("animal"=>"dog", "name"=>"Jack"),
//   array("animal"=>"cat", "name"=>"Didi")
// );

// Write a foreach statement for the array to update the variable $str to:

// The name of the dog is Jack
// The name of the cat is Didi

$str = "";
$data = array(
  array("animal" => "dog", "name" => "Jack"),
  array("animal" => "cat", "name" => "Didi")
);

foreach ($data as $element) {
    $str .= "The name of the {$element['animal']} is {$element['name']}";
}

echo $str;
?>