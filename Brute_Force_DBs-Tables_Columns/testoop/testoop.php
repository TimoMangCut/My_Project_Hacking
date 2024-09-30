<?php 
    class conca {
        public $cakeo;
        private $cachim;
        protected $cabong;

        public $color;

        public function __construct($cakeo,$color) {
            $this->cakeo = $cakeo;
            $this->color = $color;
        }
        public function get_color() {
            return $this->color;
        }
        // public function ($cabong,$color) {
        //     $this->cabong = $cabong;
        //     $this->color = $color;
        // }
        public function display() {
            return $this->cakeo;
        }


    }

    // $conca = new conca("Ca keo vui ve ", "mau trang");
    // $result = "day la 1 " . $conca->display() . $conca->get_color();
    // echo $result;
?>