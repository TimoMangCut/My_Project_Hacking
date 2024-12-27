<?php
include_once './db/database.php';
if(isset($_POST['comment'])) {
    $comment = $_POST['comment'];
    $insert_comment = new insert($comment);
    $result = $insert_comment->comment();
    echo "<script>alert('Bình luận thành công!'); window.location.href='detail_product.php?id=1';</script>";
    exit;
}
?>
