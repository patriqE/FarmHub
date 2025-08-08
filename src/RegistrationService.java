import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Scanner;

public class RegistrationService {
    private static final String JDBC_URL = "jdbc:mysql://localhost:3306/farmers_market?serverTimezone=Africa/Lagos";
    private static final String USERNAME = "root";
    private static final String PASSWORD = "root";

    private final Scanner scanner;

    public RegistrationService() {
        scanner = new Scanner(System.in);
    }

    public Farmer registerFarmer() throws ClassNotFoundException {
        System.out.println("Welcome! Please provide the following information to welcome you as a farmer: ");
        System.out.println("Name: ");
        String name = scanner.nextLine();

        System.out.println("Phone Number: ");
        String phoneNumber = scanner.nextLine();

        System.out.println("Farm Address: ");
        String farmAddress = scanner.nextLine();

        System.out.println("Utility bill photo path: ");
        String utilityBillPath = scanner.nextLine();

        if (isValidPhoneNumber(phoneNumber)
                && isValidFarmAddress(farmAddress)
                && isValidUtilityBillPath(utilityBillPath)) {
            System.out.println("Registration successful! ");
            storeFarmer(new Farmer(name, phoneNumber, farmAddress, utilityBillPath));
            scanner.close();
            return new Farmer(name, phoneNumber, farmAddress, utilityBillPath);
        } else {
            System.out.println("Registration failed! Please try again... ");
            return null;
        }
    }

    private boolean isValidPhoneNumber(String phoneNumber) {
        return phoneNumber.matches("\\d{11}");
    }

    private boolean isValidFarmAddress(String farmAddress) {
        return !farmAddress.isEmpty();
    }

    private boolean isValidUtilityBillPath(String utilityBillPath) {
        return !utilityBillPath.isEmpty();
    }

    public void storeFarmer(Farmer farmer)  {

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

                } else {
                    System.out.println("Registration Failed! ");
                }
            } catch (SQLException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}