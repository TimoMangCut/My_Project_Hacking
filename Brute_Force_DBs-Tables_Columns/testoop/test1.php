<?php 
include_once("testoop.php");
        $conca = new conca("Ca keo vui ve ", "mau trang");
        $result = "day la 1 " . $conca->display() . $conca->get_color();
        echo $result;
?>