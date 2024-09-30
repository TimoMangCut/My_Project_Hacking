<?php 
    class query {
        public $username;
        public $password;
        function set_username($username){
            $this->username = $username;
        }
        function set_password($password) {
            $this->password = $password;
        }
        public function querylogin($username, $password) {
            $conn = pg_connect("host=localhost dbname=timomangcut port=5432 user=postgres password=1");
            $sql = "SELECT * FROM users WHERE username = '$username' AND password = '$password';";
            $query = pg_query($conn,$sql);
            $result = pg_fetch_assoc($query);
            pg_close($conn);
            return $result;
        }
        


    }


?>