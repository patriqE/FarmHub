import mysql.connector
from passlib.context import CryptContext
import jwt
import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "your_secret_key"

class AuthService:
    JDBC_URL = "localhost"
    USERNAME = "root"
    PASSWORD = "root"
    DATABASE = "farmers_market"

    def register_user(self, username, password):
        hashed_password = pwd_context.hash(password)
        try:
            connection = mysql.connector.connect(
                host=self.JDBC_URL,
                user=self.USERNAME,
                password=self.PASSWORD,
                database=self.DATABASE
            )
            cursor = connection.cursor()
            sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
            cursor.execute(sql, (username, hashed_password))
            connection.commit()
            return True
        except mysql.connector.Error as e:
            print("Registration Failed!", e)
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def authenticate_user(self, username, password):
        try:
            connection = mysql.connector.connect(
                host=self.JDBC_URL,
                user=self.USERNAME,
                password=self.PASSWORD,
                database=self.DATABASE
            )
            cursor = connection.cursor()
            sql = "SELECT password FROM users WHERE username = %s"
            cursor.execute(sql, (username,))
            result = cursor.fetchone()
            if result and pwd_context.verify(password, result[0]):
                token = jwt.encode({
                    "sub": username,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
                }, SECRET_KEY, algorithm="HS256")
                return token
            return None
        except mysql.connector.Error as e:
            print("Authentication Failed!", e)
            return None
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
