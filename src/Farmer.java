public class Farmer {
    public String getPhoneNumber;
    private String name;
    private String phoneNumber;
    private String farmAddress;
    private String utilityBillPath;
//        path to utility bill image

//    Constructors
    public Farmer(String name, String phoneNumber, String farmAddress, String utilityBillPath) {
        this.name = name;
        this.phoneNumber = phoneNumber;
        this.farmAddress = farmAddress;
        this.utilityBillPath = utilityBillPath;
    }
//    GETTERS AND SETTERS FOR ALL ATTRIBUTES
        public String getName() {
            return name;
        }
    public void setName(String name){
        this.name = name;
        }

        public String getPhoneNumber () {
            return phoneNumber;
        }
    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

        public String getFarmAddress() {
            return farmAddress;
        }
    public void setFarmAddress(String farmAddress) {
        this.farmAddress = farmAddress;
    }

        public String getUtilityBillPath() {
        return utilityBillPath;
        }
    public void setUtilityBillPath(String utilityBillPath) {
        this.utilityBillPath = utilityBillPath;
    }
}
