<?php
include_once './../db/database.php';
$parse = file_get_contents('php://input');
$data = json_decode($parse,true);
if (isset($data['username']) && isset($data['password'])) {
    $username = $data['username'];
    $password = $data['password'];
    $login = new signin ($username,$password);
    $result = $login->login();
    if($result) {
        $token = base64_encode($username . ':' . time());
        echo json_encode(['status' => 'success', 'token' => $token]);
        exit();
    }
    else {
        echo json_encode(['status' => 'error', 'message' => 'wrong username or password']);
    }
}

// if (isset($_GET['username']) && isset($_GET['password'])) {
//         $username = $_GET['username'];
//         $password = $_GET['password'];
//         $login = new signin ($username,$password);
//         $result = $login->login();
//         if($result) {
//             $token = base64_encode($username . ':' . time());
//             echo json_encode(['status' => 'success', 'token' => $token]);
//             exit();
//         }
//         else {
//             echo json_encode(['status' => 'error', 'message' => 'wrong username or password']);
//         }
//     }