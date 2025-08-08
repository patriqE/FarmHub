import subprocess
import os

# Start MySQL Docker container
subprocess.run(["docker-compose", "up", "-d"])

# Start FastAPI backend
backend_path = os.path.join("backend")
subprocess.Popen(["uvicorn", "controllers.api:app", "--reload"], cwd=backend_path)

# Start frontend (Flask app)
frontend_path = "frontend/controllers"
subprocess.Popen(["python", "app.py"], cwd=frontend_path)

print("MySQL, FastAPI backend, and Flask frontend services started.")
