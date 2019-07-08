<?php
header('Content-type: application/json');
$n = isset($_GET["n"]) ? $_GET["n"] : 1;
echo shell_exec("python ../../generator/hackergenerator.py ".$n);
?>
