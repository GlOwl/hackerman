<?php
$n = isset($_GET["n"]) ? $_GET["n"] : 1;
$f = isset($_GET["f"]) ? $_GET["f"] : "json";

if($n < 0) $n = 1;
if($n > 100) $n = 100;
if($f != "json" && $f != "csv") $f = "json";

if($f == "json") {
  header('Content-type: application/json');
} else if($f == "csv") {
  header('Content-type: text/csv');
}

echo shell_exec("python3 ../../generator/hackergenerator.py ".$n." ".$f);
?>
