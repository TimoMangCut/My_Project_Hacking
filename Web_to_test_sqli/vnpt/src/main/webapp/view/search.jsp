<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ page import="java.io.*,java.util.*,javax.servlet.*,javax.servlet.http.*" %>
<%
    // Lấy username từ session
    String username = (String) session.getAttribute("username");

    // Nếu chưa đăng nhập, chuyển hướng về trang đăng nhập
    if (username == null) {
        response.sendRedirect("/view/signin.jsp");
        return;
    }
%>
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
        }
        .search-form {
            margin: 20px 0;
            padding: 20px;
            background: #f5f5f5;
            border-radius: 5px;
        }
        .search-form input[type="text"] {
            padding: 10px;
            width: 70%;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        .search-form button {
            padding: 10px 20px;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .search-results {
            margin-top: 20px;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        .success { color: green; }
        .error { color: red; }
        .logout {
            padding: 10px 20px;
            background: #dc3545;
            color: white;
            text-decoration: none;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h2>Chào mừng, <%= username %>!</h2>
        <a href="/vnpt/view/logout.jsp" class="logout">Đăng xuất</a>
    </div>

    <div class="search-form">
        <h3>Tìm kiếm báo mới</h3>
        <form action="/vnpt/search" method="POST">
            <input type="text" name="search" placeholder="Nhập từ khóa tìm kiếm...">
            <button type="submit">Tìm kiếm</button>
        </form>
    </div>

    <div class="search-results">
        <% 
            String searchResult = (String)request.getAttribute("searchResult");
            if(searchResult != null) {
                searchResult = searchResult.replace("\n", "<br>")
                                        .replace("✅", "<span class='success'>✅</span>")
                                        .replace("❌", "<span class='error'>❌</span>");
                out.println(searchResult);
            }
        %>
    </div>
</body>
</html>