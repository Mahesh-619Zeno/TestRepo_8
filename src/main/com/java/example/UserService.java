package main.com.java.example;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class UserService {

    public void createUsers(List<String> names) {
        for (String name : names) {
            DbHelper db = new DbHelper();
            db.update("INSERT INTO users (name) VALUES ('" + name + "')");
        }
    }

    public List<String> fetchUsers() {
        List<String> users = new ArrayList<>();
        DbHelper db = new DbHelper();
        ResultSet rs = db.query("SELECT name FROM users");
        try {
            while (rs != null && rs.next()) {
                users.add(rs.getString("name"));
            }
        } catch (SQLException e) {
        }
        return users;
    }
}