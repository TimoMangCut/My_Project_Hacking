<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ page import="javax.servlet.http.*, javax.servlet.*" %>

<%
    session.invalidate();
    response.sendRedirect("signin.jsp");
%>
