# 🚔 Smart Barrier Backend 🚦

A **RESTful API** for a **police checkpoint system** built with **Django** and **Django REST Framework (DRF)**.  

🔒 **Secure authentication** | 🛂 **Officer & Driver management** | 🚗 **Vehicle tracking** | 📍 **Checkpoint logs** | 📝 **Reports & Criminal Records**  

## 🚀 Features
- 🔑 **JWT authentication** for officers.  
- 🛠️ **Full CRUD operations** for officers, drivers, vehicles, checkpoints, criminal records, and reports.  
- 🏛 **Role-based access control**:  
  - 👮‍♂️ **Officers** log activities.  
  - 🛡 **Admins** manage everything.  

## 🏗 Project Structure
smart_barrier/
├── backend/              # ⚙️ Settings and URLs
├── apps/
│   ├── officer_auth/     # 👮 Officer authentication & management
│   ├── drivers/          # 🚗 Driver management
│   ├── vehicles/         # 🚙 Vehicle CRUD
│   ├── checkpoints/      # 📍 Checkpoint logs
│   ├── criminals/        # 🚨 Criminal records
│   ├── reports/          # 📝 Reports & case logs
├── manage.py
├── requirements.txt
└── .env.example


## 🔧 Prerequisites
- 🐍 **Python** 3.11+  
- 🛢 **MySQL** 8.0+  
- 🌿 **Git**  

## ⚡ Installation
1️⃣ **Clone the repo**  
```bash
git clone https://github.com/yourusername/smart_barrier.git && cd smart_barrier

2️⃣ Set up a virtual environment
bash

python -m venv _venv && source _venv/bin/activate  # Linux/Mac
_venv\Scripts\activate  # Windows

3️⃣ Install dependencies
bash
pip install -r requirements.txt

4️⃣ Set up MySQL database
sql
CREATE DATABASE smart_barrier;

5️⃣ Configure environment variables
Copy .env.example to .env and update the values:

SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=smart_barrier
DB_USER=root
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=3308

6️⃣ Run migrations
python manage.py makemigrations && python manage.py migrate

7️⃣ Start the server
python manage.py runserver
🔗 Access API at: http://127.0.0.1:8000/

🔗 API Endpoints
🌐 Base URL: /api/
🛡 Use Bearer Token for authentication

Officer Auth 👮: /officer_auth/login/, /officer_auth/logout/, /officer_auth/refresh/, /officer_auth/officers/, /officer_auth/officers/<uuid:id>/
Drivers 🚗: /drivers/, /drivers/<uuid:id>/
Vehicles 🚙: /vehicles/, /vehicles/<str:plate_number>/
Checkpoints 📍: /checkpoints/, /checkpoints/<uuid:id>/
Criminal Records 🚨: /criminals/, /criminals/<uuid:id>/
Reports 📝: /reports/, /reports/<uuid:id>/

🏛 Database Schema
Model	Fields
Officer 👮	UUID, name, badge_number, email, username, password_hash, role
Driver 🚗	UUID, name, license_number, address
Vehicle 🚙	plate_number, owner (FK), make, model, year, color
CheckpointLog 📍	UUID, plate_number (FK), officer (FK), location, timestamp
CriminalRecord 🚨	UUID, plate_number (FK), status, notes
Report 📝	UUID, checkpoint (FK), officer (FK), findings, actions_taken, timestamps, status
⚠️ Foreign keys use on_delete=models.CASCADE.

🛠 Testing
🛠 Tools: Postman, curl
📌 Steps:

Login
Create resources
Test CRUD operations
🤝 Contributing
🚀 Contributions are welcome! To contribute:

Fork the repo
Create a feature branch (feature/your-feature)
Commit changes (follow PEP 8)
Push & open a PR
