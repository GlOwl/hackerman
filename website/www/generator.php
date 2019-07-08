<?php
$title = "Generator";
$quote =  json_decode(shell_exec("python ../../generator/hackergenerator.py 1"))->quotes[0];
include("../base.php");
?>
