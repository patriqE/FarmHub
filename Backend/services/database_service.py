import mysql.connector
from backend.models.farmer import Farmer

class DatabaseService:
    JDBC_URL = "localhost"
    USERNAME = "root"
    PASSWORD = "root"
    DATABASE = "farmers_market"

    def store_farmer(self, farmer):
        try:
            connection = mysql.connector.connect(
                host=self.JDBC_URL,
                user=self.USERNAME,
                password=self.PASSWORD,
                database=self.DATABASE
            )
            cursor = connection.cursor()
            sql = "INSERT INTO farmers (name, phone_number, farm_address, utility_bill_path) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (farmer.get_name(), farmer.get_phone_number(), farmer.get_farm_address(), farmer.get_utility_bill_path()))
            connection.commit()
            print("Registration Successful!")
        except mysql.connector.Error as e:
            print("Registration Failed!", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def fetch_farmers_list(self):
        farmers = []
        try:
            connection = mysql.connector.connect(
                host=self.JDBC_URL,
                user=self.USERNAME,
                password=self.PASSWORD,
                database=self.DATABASE
            )
            cursor = connection.cursor()
            cursor.execute("SELECT name, phone_number, farm_address, utility_bill_path FROM farmers")
            for (name, phone_number, farm_address, utility_bill_path) in cursor:
                farmers.append({
                    "name": name,
                    "phone_number": phone_number,
                    "farm_address": farm_address,
                    "utility_bill_path": utility_bill_path
                })
        except mysql.connector.Error as e:
            print("Error fetching farmers:", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
        return farmers
