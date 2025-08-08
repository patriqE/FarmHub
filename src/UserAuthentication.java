import  java.util.HashMap;
import  java.util.Map;

public class UserAuthentication {
        private final Map< String, Farmer > farmers;
//        map of phone numbers to farmer object

        public UserAuthentication() {
            farmers = new HashMap<>();
        }

        public void registerFarmer ( String phoneNumber, Farmer farmer) {
            farmers.put(phoneNumber, farmer);
        }

        public boolean isFarmerRegistered(String phoneNumber) {
            return
                    farmers.containsKey(phoneNumber);
        }
}
