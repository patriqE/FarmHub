from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from backend.services.database_service import DatabaseService
from backend.services.registration_service import RegistrationService
from backend.services.auth_service import AuthService
from backend.models.user import User

app = FastAPI()

db_service = DatabaseService()
reg_service = RegistrationService()
auth_service = AuthService()


class UserModel(BaseModel):
    username: str
    password: str
    confirm_password: str
    user_type: str  # 'buyer' or 'business'
    full_name: str = None
    email: str = None
    business_name: str = None
    business_email: str = None


@app.post("/register", response_model=dict)
def register_user(user: UserModel):
    if user.password != user.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")
    if user.user_type not in ["buyer", "business"]:
        raise HTTPException(status_code=400, detail="Invalid user type")
    # Validate required fields for buyer/business
    if user.user_type == "buyer":
        if not user.full_name or not user.email:
            raise HTTPException(status_code=400, detail="Full name and email required for buyer")
    if user.user_type == "business":
        if not user.business_name or not user.business_email:
            raise HTTPException(status_code=400, detail="Business name and email required for business")
    success = auth_service.register_user(
        user.username,
        user.password,
        user.user_type,
        user.full_name,
        user.email,
        user.business_name,
        user.business_email
    )
    if not success:
        raise HTTPException(status_code=400, detail="Registration failed")
    return {"message": "User registered successfully"}

@app.post("/login", response_model=dict)
def login_user(user: UserModel):
    token = auth_service.authenticate_user(user.username, user.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}

class FarmerModel(BaseModel):
    name: str
    phone_number: str
    farm_address: str
    utility_bill_path: str

@app.post("/farmers", response_model=FarmerModel)
def register_farmer(farmer: FarmerModel):
    farmer_obj = reg_service.register_farmer_manual(
        farmer.name, farmer.phone_number, farmer.farm_address, farmer.utility_bill_path
    )
    if not farmer_obj:
        raise HTTPException(status_code=400, detail="Invalid farmer data")
    db_service.store_farmer(farmer_obj)
    return farmer

@app.get("/farmers", response_model=List[FarmerModel])
def get_farmers():
    farmers_list = db_service.fetch_farmers_list()
    return farmers_list
