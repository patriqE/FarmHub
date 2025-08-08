import re
from backend.models.farmer import Farmer

class RegistrationService:
    def __init__(self):
        pass

    def register_farmer_manual(self, name, phone_number, farm_address, utility_bill_path):
        if self.is_valid_phone_number(phone_number) and self.is_valid_farm_address(farm_address) and self.is_valid_utility_bill_path(utility_bill_path):
            return Farmer(name, phone_number, farm_address, utility_bill_path)
        else:
            return None

    def is_valid_phone_number(self, phone_number):
        return re.fullmatch(r'\d{11}', phone_number) is not None

    def is_valid_farm_address(self, farm_address):
        return bool(farm_address)

    def is_valid_utility_bill_path(self, utility_bill_path):
        return bool(utility_bill_path)
