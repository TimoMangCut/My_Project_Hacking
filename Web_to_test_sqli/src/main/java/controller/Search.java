package controller;

import dao.UserDAO;
import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/search")
public class Search extends HttpServlet {
    private static final long serialVersionUID = 1L;
    
    protected void doPost(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {

        response.setContentType("text/html;charset=UTF-8");
        request.setCharacterEncoding("UTF-8");
        
        String searchTerm = request.getParameter("search");
        
        UserDAO userDAO = new UserDAO();
        String result = userDAO.search(searchTerm);
        
        request.setAttribute("searchResult", result);
        
        request.getRequestDispatcher("/view/search.jsp").forward(request, response);
    }
}