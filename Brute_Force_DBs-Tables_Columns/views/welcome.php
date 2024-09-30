<?php 
session_start();
if (!isset($_SESSION['username'])) {
    header("Location: login.php");
    exit();
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome</title>
</head>
<body>
<p>Đăng nhập thành công!</p>
<?php
    echo "<h1>Welcome, " . print_r($_SESSION['result']) . ' '  . "!</h1>";
    // foreach (array($_SESSION['result']) as $row) {
    //     echo $row['result'];
    // }
    // echo json_encode($result);
    ?>
</body>
</html>
