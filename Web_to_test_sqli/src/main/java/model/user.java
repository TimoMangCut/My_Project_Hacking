package model;

public class user {
    private String username;
    private String password;

    public user(String username, String password) {
        this.username = username;
        this.password = password;
    }

    public String getusername() {
        return username;
    }
    public String getpassword() {
        return password;
    }
}
