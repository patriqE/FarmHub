class Farmer:
    def __init__(self, name, phone_number, farm_address, utility_bill_path):
        self.name = name
        self.phone_number = phone_number
        self.farm_address = farm_address
        self.utility_bill_path = utility_bill_path

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_farm_address(self):
        return self.farm_address

    def set_farm_address(self, farm_address):
        self.farm_address = farm_address

    def get_utility_bill_path(self):
        return self.utility_bill_path

    def set_utility_bill_path(self, utility_bill_path):
        self.utility_bill_path = utility_bill_path
