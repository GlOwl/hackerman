<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>Hackerman Quote <?php echo "$title"; ?></title>

  <meta name="description" content="Get your daily dose of hackerman!">

  <link href="css/bootstrap.min.css" rel="stylesheet" type="text/css">
  <link href="css/style.css" rel="stylesheet" type="text/css">
</head>

<body>

  <div id="navbackgrond"></div>
  <div class="container-fluid">
    <div class="row">
      <div class="col-lg-2 col-sm-1"> </div>
      <div class="col-lg-8 col-sm-10">

        <nav class="navbar navbar-dark bg-primary" id="navbar">
          <a class="navbar-brand" href="/generator">Hackerman Quote Generator</a>
        </nav>

        <?php if($title == "Generator") include("content/generator.php"); ?>
        <?php if($title == "API") include("content/api-doc.php"); ?>
        <?php if($title == "About") include("content/about.php"); ?>

        <hr>

        <ul class="nav justify-content-end pb-3">
          <li class="nav-item">
            <a class="nav-link <?php if($title == "Generator") echo "active";?>" href="generator">Generator</a>
          </li>
          <li class="nav-item">
            <a class="nav-link <?php if($title == "API") echo "active";?>" href="api-doc">API</a>
          </li>
          <li class="nav-item">
            <a class="nav-link <?php if($title == "About") echo "active";?>" href="about">About</a>
          </li>
        </ul>

      </div>
      <div class="col-lg-2 col-sm-1"> </div>
    </div>
  </div>

  <script src="js/jquery-3.4.1.min.js"></script>
  <script src="js/popper.min.js"></script>
  <script src="js/bootstrap.min.js"></script>

  <?php
    if($title == "Generator") {
      echo "<script src=\"js/generator.js\"></script>";
    }
  ?>
</html>
