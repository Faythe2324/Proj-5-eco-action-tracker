# 🌍 Eco-Action Tracker

The **Eco-Action Tracker** is a community sustainability engagement system that encourages users to build eco-friendly habits such as recycling, biking, and reducing waste. The platform tracks individual actions, awards eco-points, and visualizes the overall environmental impact of the community.

---

## Project Objectives
- Promote sustainable daily habits among users
- Track, score, and visualize eco-actions
- Encourage participation in community challenges
- Provide a transparent and gamified leaderboard system

---

## Setup Instructions

### Windows Terminal Setup

1. Prerequisites
   - Python 3.8 or higher
   - pip (Python package manager)
   - Git (optional, for cloning the repository)

2. Clone or Download the Project
   ```bash
   git clone <repository-url>
   cd EcoActionTracker
   ```

3. Create Virtual Environment
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

4. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```

5. Database Initialization
   - The SQLite database will be automatically created when you first run the application
   - Sample data (rewards, challenges) will be seeded on startup

## How to Run the Application

### Step 1: Start the Backend Server
```bash
.venv\Scripts\activate
uvicorn backend.main:app --reload
```
The API will be available at: http://127.0.0.1:8000

### Step 2: Start the Frontend Application
```bash
.venv\Scripts\activate
python main_app.py
```

### Step 3: Access the Application
- The desktop application window will open automatically
- For API documentation, visit: http://127.0.0.1:8000/docs

## Dependencies

The project requires the following Python packages:

- flet>=0.10.0
- fastapi>=0.68.0
- uvicorn[standard]>=0.15.0
- requests>=2.25.0
- matplotlib>=3.5.0
- pandas>=1.3.0
- pydantic>=1.8.0

All dependencies are listed in requirements.txt and will be installed automatically when running pip install -r requirements.txt.


---

## System Features

| Use Case | Description |
|---------|-------------|
| **User Registration & Login** | Users can create accounts and securely sign in |
| **Log Eco-Actions** | Users record activities like recycling or biking to earn points |
| **View Personal Statistics** | Users track progress, achievements, and growth trends |
| **Join Community Challenges** | Users join group challenges to motivate collaboration |
| **Leaderboard** | Displays top eco-contributors in the community |
| **Carbon Saved Estimation** | Uses environmental data APIs to estimate carbon impact |

---

## Technologies Used

| Component | Implementation |
|----------|----------------|
| **Programming Language** | Python |
| **Object-Oriented Programming** | Classes for Users, Eco-Actions, Challenges, Rewards |
| **Design Architecture** | MVC (Model - View - Controller) |
| **Database** | SQLite (stores users, actions, points, and challenge data) |
| **Backend API** | FastAPI (handles requests for user data & leaderboard) |
| **Frontend Desktop App** | Flet (User Interface for interactive eco-logging) |
| **Data Visualization** | Matplotlib (progress & community impact graphs) |
| **Environmental Data Integration** | Carbon footprint calculation API |


## 🧑‍🤝‍🧑 Team Members & Roles

| Member Name | Role | Contribution |
|------------|------|---------------|
| **Abigail Kaye Duarte** | Backend & Database Developer | Implemented SQLite data handling, structured the database schema, and managed data CRUD operations. |
| **Faythe Alison Magsombol** | Project Lead & UI/UX & Documentation | Coordinated system design, organized code structure, developed the user interface flow, and prepared documentation and presentation materials. |
| **Joseph Noel Paloma** | Feature Logic & API Integration Developer | Developed eco-action scoring logic, integrated carbon footprint estimation API, and implemented leaderboard and challenge functionality. |

---



