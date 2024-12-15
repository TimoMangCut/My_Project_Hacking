<?php
class signin{
    public $username;
    public $password;
    function __construct($user, $pass){
        $this->username=$user;
        $this->password=$pass;
    }
    function login() {
        $conn = pg_connect("host=localhost dbname=phuc port=5432 user=postgres password=1");
        $sql = "SELECT username FROM users where username = '$this->username' AND password = '$this->password'";
        $pg_query = pg_query($conn,$sql);
        $result = pg_fetch_assoc($pg_query);
        pg_close($conn);
        return $result;
    }
}