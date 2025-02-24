package dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class UserDAO {
    private static final String JDBC_URL = "jdbc:postgresql://localhost:5432/phuc";
    private static final String JDBC_USERNAME = "postgres";
    private static final String JDBC_PASSWORD = "123123";

    private Connection getConnection() throws SQLException {
        try {
            Class.forName("org.postgresql.Driver");
        } catch (ClassNotFoundException e) {
            throw new SQLException("Không tìm thấy driver PostgreSQL", e);
        }
        return DriverManager.getConnection(JDBC_URL, JDBC_USERNAME, JDBC_PASSWORD);
    }

    public String signin(String username, String password) {
        String sql = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "';";

        try (Connection conn = getConnection();
             Statement stmt = conn.createStatement()) {

            boolean hasResults = stmt.execute(sql);
            if (hasResults) {
                try (ResultSet rs = stmt.getResultSet()) {
                    if (rs.next()) {
                        return "✅ Đăng nhập thành công!";
                    }
                }
            }
            return "❌ Sai tài khoản hoặc mật khẩu.";
        } catch (SQLException e) {
            return "🚨 Lỗi SQL: " + e.getMessage();
        }
    }

    public String signup(String username, String password) {
        String sql = "INSERT INTO users (username, password) VALUES ('" + username + "', '" + password + "');";

        try (Connection conn = getConnection();
             Statement stmt = conn.createStatement()) {

            stmt.execute(sql);
            return "✅ Đăng ký thành công!";
        } catch (SQLException e) {
            return "🚨 Lỗi SQL: " + e.getMessage();
        }
    }
    public String search(String search) {
        String sql = "SELECT title, content FROM news WHERE title LIKE '%" + search + "%'";
        StringBuilder result = new StringBuilder();
        
        try (Connection conn = getConnection();
             Statement stmt = conn.createStatement()) {
            
            boolean isResultSet = stmt.execute(sql);
            result.append("SQL Query: ").append(sql).append("\n\n");
            
            boolean found = false;
            while (isResultSet) {
                try (ResultSet rs = stmt.getResultSet()) {
                    while (rs.next()) {
                        found = true;
                        String title = rs.getString("title");
                        String content = rs.getString("content");
                        result.append("Tiêu đề: ").append(title)
                              .append("\nNội dung: ").append(content)
                              .append("\n-------------------\n");
                    }
                }
                isResultSet = stmt.getMoreResults();
            }
            
            if (!found) {
                return "❌ Không tìm thấy kết quả.\nSQL Query: " + sql;
            }
            return "✅ Kết quả tìm kiếm:\n" + result.toString();
            
        } catch (SQLException e) {
            return "🚨 SQL Error: " + e.getMessage() + "\nQuery: " + sql;
        }
    }