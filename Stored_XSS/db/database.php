<?php
Class query {
    public $productid;

    function __construct($id) {
        $this->productid = $id;
    }
    function list(){
        $conn = pg_connect("host=localhost dbname=phuc port=5432 user=postgres password=phuciutram123");
        $sql = "select nguoidung, comment from products where product_id = $this->productid";
        $query = pg_query($conn,$sql);
        $result = [];
        while ($row = pg_fetch_assoc($query)) {
            $result[] = $row;
        }
        // var_dump($result);
        pg_close($conn);
        return $result;
    }
}
class insert {
    public $comment;
    function __construct($comment){
        $this->comment = $comment;
    }
    function comment(){
        $conn = pg_connect("host=localhost dbname=phuc port=5432 user=postgres password=phuciutram123");
        $sql = "INSERT INTO products (comment) VALUES('$this->comment')";
        $query = pg_query($conn,$sql);
        $result = pg_fetch_assoc($query);
        pg_close($conn);
        return $result;
    }
}
?>