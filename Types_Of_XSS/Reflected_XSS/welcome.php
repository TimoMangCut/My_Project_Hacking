<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reflected XSS</title>
</head>
<body>
    <form action="./welcome.php" method="get">
    <label for="name">Ten cua ban la:</label>
    <input type = 'text' id = 'name' name="ten">
    <input type="submit">
    </form>
</body>
</html>
<?php
    if(isset($_GET['ten'])){
        echo 'Hello' . " ". $_GET['ten'];
    }
?>