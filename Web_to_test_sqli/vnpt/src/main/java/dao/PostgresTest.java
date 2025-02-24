package dao;

import java.sql.*;
import java.util.Scanner;

public class PostgresTest {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/phuc";
        String user = "postgres";
        String password = "phuciutram123";

        try (Connection conn = DriverManager.getConnection(url, user, password);
             Scanner scanner = new Scanner(System.in)) {

            System.out.println("✅ Kết nối thành công!");
            System.out.print("Nhập câu truy vấn SQL: ");
            String query = scanner.nextLine();

            try (Statement stmt = conn.createStatement();
                 ResultSet rs = stmt.executeQuery(query)) {

                // Lấy thông tin cột
                ResultSetMetaData metaData = rs.getMetaData();
                int columnCount = metaData.getColumnCount();

                System.out.println("✅ Truy vấn thành công!");
                System.out.println(columnCount);
                while (rs.next()) {
                    for (int i = 1; i <= columnCount; i++) {
                        System.out.print(metaData.getColumnName(i) + ": " + rs.getString(i) + " | ");
                    }
                    System.out.println();
                }
            }

        } catch (SQLException e) {
            System.err.println("❌ Lỗi SQL: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
