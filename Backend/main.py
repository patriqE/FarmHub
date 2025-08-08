from Backend.registration_service import RegistrationService
from Backend.services.user_authentication import UserAuthentication

if __name__ == "__main__":
    user_authentication = UserAuthentication()
    registration_service = RegistrationService()
    farmer = registration_service.register_farmer()

    if farmer:
        user_authentication.register_farmer(farmer.get_phone_number(), farmer)
        print("Is farmer registered?", user_authentication.is_farmer_registered(farmer.get_phone_number()))
    else:
        print("Registration failed!")
