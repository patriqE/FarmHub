class UserAuthentication:
    def __init__(self):
        self.farmers = {}

    def register_farmer(self, phone_number, farmer):
        self.farmers[phone_number] = farmer

    def is_farmer_registered(self, phone_number):
        return phone_number in self.farmers
