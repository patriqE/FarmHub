import java.sql.*;

public class DatabaseService {
    private static final String JDBC_URL = "jdbc:mysql://localhost:3306/farmers_market?serverTimezone=Africa/Lagos";
    private static final String USERNAME = "root";
    private static final String PASSWORD = "root";

    public static void main(String[] args) throws ClassNotFoundException {
        Class.forName("com.mysql.cj.jdbc.Driver");
        try (Connection connection = DriverManager.getConnection(JDBC_URL, USERNAME, PASSWORD)) {
//            CREATE STATEMENT
            Statement statement = connection.createStatement();
//            EXECUTE QUERY
            ResultSet resultSet = statement.executeQuery("SELECT * FROM farmers ");
//            PROCESS RESULTS
            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                String name = resultSet.getString("name");
                String phoneNumber = resultSet.getString("phone_number");
                String farmAddress = resultSet.getString("farm_address");
                String utilityBillPath = resultSet.getString("utility_bill_path");
        System.out.println( "ID: " + id + ", Name: " + name + "PHONE NUMBER: " + phoneNumber + "FARM ADDRESS: " + farmAddress + "UTILITY BILL PATH: " + utilityBillPath);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void storeFarmer(Farmer farmer) throws ClassNotFoundException {

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection connection = DriverManager.getConnection(JDBC_URL, USERNAME, PASSWORD);

            System.out.println("Connected to driver successfully!");
            String sql = "INSERT INTO farmers (name, phone_number, farm_address, utility_bill_path) VALUES (?, ?, ?, ?)";

            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setString(1, farmer.getName());
            preparedStatement.setString(2, farmer.getPhoneNumber());
            preparedStatement.setString(3, farmer.getFarmAddress());
            preparedStatement.setString(4, farmer.getUtilityBillPath());


            int rowsAffected = preparedStatement.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("Registration Successful! ");
                connection.close();
            } else {
                System.out.println("Registration Failed! ");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

}
