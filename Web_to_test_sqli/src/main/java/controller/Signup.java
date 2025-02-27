package controller;

import dao.UserDAO;
import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/signup")
public class Signup extends HttpServlet {
    private static final long serialVersionUID = 1L;
    
    protected void doPost(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        String username = request.getParameter("username");
        String password = request.getParameter("password");
        String confirmPassword = request.getParameter("confirmPassword");

        if (!password.equals(confirmPassword)) {
            request.setAttribute("errorMessage", "❌ Mật khẩu nhập lại không khớp!");
            request.getRequestDispatcher("/view/signup.jsp").forward(request, response);
            return;
        }

        UserDAO userDAO = new UserDAO();
        String result = userDAO.signup(username, password);

        if (result.startsWith("✅")) {
            response.sendRedirect("/view/signin.jsp?success=1");
        } else {
            request.setAttribute("errorMessage", result);
            request.getRequestDispatcher("/view/signup.jsp").forward(request, response);
        }
    }
}
