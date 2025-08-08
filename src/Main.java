public class Main {
    public static void main(String[] args) throws ClassNotFoundException {
//        create new farmer
//        Farmer farmer = new Farmer( " Efe Patriq", " 09051063556", "4F farm, owhelogbo, " +
//                "delta state.", "/path/to/utility/bill.jpg");
//        create a new user authentication object
        UserAuthentication userAuthentication = new UserAuthentication();



        // Register the farmer
        RegistrationService registrationService = new RegistrationService();
        Farmer farmer=  registrationService.registerFarmer();

        if (farmer != null) {
        userAuthentication.registerFarmer( farmer.getPhoneNumber(), farmer);
            System.out.println(" Is farmer registered? " + userAuthentication.isFarmerRegistered(farmer.getPhoneNumber()));
        } else {
            System.out.println( " Registration failed! ");
        }
    }
}
