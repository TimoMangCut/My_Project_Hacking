<?php
include_once './db/database.php';
if(isset($_GET['id'])) {
    $id = $_GET['id'];
    $list = new query($id);
    $comments = [];
    $comments[] = $list->list();
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Details</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .comment-box {
            border: 1px solid #ddd;
            padding: 10px;
            margin-bottom: 10px;
            background-color: #f9f9f9;
        }
        .comment-box h3 {
            margin-top: 0;
        }
        .comment-form {
            margin-top: 20px;
            border: 1px solid #ddd;
            padding: 10px;
            background-color: #f9f9f9;
        }
    </style>
</head>
<body>
<button onclick="window.location.href='./welcome.html'">Trở về trang chủ</button>
    <Center><H1>Chân gà sả tắc Timo House ngon tuyệt vời</H1></Center>
    <br>
    <Center><img src="./image_product/changa.jpg" width="400" height="350"></Center>
    <br>
    <Center><h2>Giá : 50.000 VND</h2></Center>
    <br>
    <Center><Button onclick="alert('Số dư của bạn không đủ, hãy nạp lần đầu')">Mua ngay</Button></Center>
    <Center><?php if ($comments): ?>
        <?php foreach ($comments as $comment): ?>
            <?php foreach ($comment as $commentss): ?>
            <div class="comment-box">
                <p>
                <?php echo 'User: '. $commentss['nguoidung']. '<br>';?>
                <?php echo 'Comment: ' . $commentss['comment'] . '<br>';?>
                </p>
            </div>
            <?php endforeach; ?>
            <?php endforeach; ?>
    <?php else: ?>
        <p>Chưa có bình luận nào cho sản phẩm này</p>
    <?php endif; ?>
    <div class="comment-form">
        <h3>Hãy để lại lời bình luận:</h3>
        <form action="insert_comment.php" method="POST">
            <textarea name="comment" rows="4" cols="50" required></textarea><br>
            <input type="submit" value="Submit">
        </form>
    </div></Center>
</body>
</html>