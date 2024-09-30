<?php 
session_start();
include '../model/User.php';
$error ='';
    if (isset($_SERVER["REQUEST_METHOD"]) && $_SERVER["REQUEST_METHOD"] == "POST") {

        $username = $_POST["username"];
        $password = $_POST["password"];
        $query = new query();
        $query->set_username($username);
        $query->set_password($password);

        $result = $query->querylogin($username,$password);
        if ($result) {
            $_SESSION["username"] = $username;
            $_SESSION["result"] = $result;
            header("location: ../views/welcome.php");
            exit();
        }
        else {
            header("location: ../views/login.php");
            $_SESSION['error'] = "<p>Wrong username or password</p>";
        }
        
    }

?>