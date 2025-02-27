package controller;

import dao.UserDAO;
import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/signin")
public class Signin extends HttpServlet {
    private static final long serialVersionUID = 1L;
    
    protected void doPost(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        String username = request.getParameter("username");
        String password = request.getParameter("password");

        UserDAO userDAO = new UserDAO();
        String result = userDAO.signin(username, password);

        if (result.startsWith("✅")) {
            HttpSession session = request.getSession();
            session.setAttribute("username", username);
            response.sendRedirect("/vnpt/view/search.jsp");
        } else {
            request.setAttribute("errorMessage", result);
            request.getRequestDispatcher("/view/signin.jsp").forward(request, response);
        }
    }
}
