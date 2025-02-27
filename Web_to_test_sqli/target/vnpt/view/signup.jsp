<%@ page contentType="text/html; charset=UTF-8" %>
<!DOCTYPE html>
<html>
<head>
    <title>Đăng ký</title>
</head>
<body>
    <h2>Đăng ký tài khoản</h2>
    <form action="/vnpt/signup" method="POST">
        <label for="username">Tên đăng nhập:</label>
        <input type="text" name="username" required><br>

        <label for="password">Mật khẩu:</label>
        <input type="password" name="password" required><br>

        <label for="confirmPassword">Nhập lại mật khẩu:</label>
        <input type="password" name="confirmPassword" required><br>

        <button type="submit">Đăng ký</button>
    </form>
    <button type="button" onclick="window.location.href='signin.jsp'">Đăng Nhập</button>

    <% if (request.getAttribute("errorMessage") != null) { %>
        <p style="color: red;"><%= request.getAttribute("errorMessage") %></p>
    <% } %>
</body>
</html>
