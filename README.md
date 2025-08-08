# FarmHarvestHub

A Python-based farm management system for registering farmers, authenticating users, and storing farmer data in a MySQL database (via Docker).

## Features

- Farmer registration with validation
- User authentication
- MySQL database integration (Dockerized)

## Setup

### 1. Clone the repository

```
git clone https://github.com/patriqE/FarmHub.git
cd FarmHub
```

### 2. Install Python dependencies

```
pip install -r requirements.txt
```

### 3. Start MySQL with Docker

```
docker-compose up -d
```

### 4. Run the application

```
python py_src/main.py
```

## Configuration

- Database credentials and settings are in `py_src/database_service.py` and `docker-compose.yml`.
- Default MySQL credentials: user `root`, password `root`, database `farmers_market`.

## Project Structure

```
FarmHarvestHub/
├── py_src/
│   ├── farmer.py
│   ├── user_authentication.py
│   ├── registration_service.py
│   ├── database_service.py
│   └── main.py
├── requirements.txt
├── docker-compose.yml
└── README.md
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT
