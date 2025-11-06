#frontend\app.py
import flet as ft
import sqlite3
import matplotlib.pyplot as plt
import io
import base64

# --- Database setup ---
conn = sqlite3.connect("eco_tracker.db", check_same_thread=False)
c = conn.cursor()

# Users table
c.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    email TEXT UNIQUE,
    password TEXT
)
""")

# Challenges table
c.execute("""
CREATE TABLE IF NOT EXISTS challenges(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    reward_points INTEGER
)
""")

# User-Challenges join table
c.execute("""
CREATE TABLE IF NOT EXISTS user_challenges(
    user_id INTEGER,
    challenge_id INTEGER,
    PRIMARY KEY(user_id, challenge_id)
)
""")
conn.commit()

# Insert default challenges if empty
c.execute("SELECT COUNT(*) FROM challenges")
if c.fetchone()[0] == 0:
    challenges_data = [
        ("Zero Waste Week", 100),
        ("Bike 50 km Challenge", 250),
        ("Plant 5 Trees Challenge", 50),
    ]
    c.executemany("INSERT INTO challenges (name, reward_points) VALUES (?, ?)", challenges_data)
    conn.commit()

# --- Global state ---
current_user = None
co2_history = []  # store CO2 saved for plotting

# --- Helper functions ---
def create_user(username, email, password):
    try:
        c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def login_user(username, password):
    c.execute("SELECT id, username FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    if result:
        return {"id": result[0], "username": result[1]}
    return None

def get_user_points(user_id):
    c.execute("SELECT SUM(reward_points) FROM challenges "
              "JOIN user_challenges ON challenges.id = user_challenges.challenge_id "
              "WHERE user_id=?", (user_id,))
    total = c.fetchone()[0]
    return total if total else 0

def join_challenge(user_id, challenge_id):
    try:
        c.execute("INSERT INTO user_challenges (user_id, challenge_id) VALUES (?, ?)", (user_id, challenge_id))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def plot_co2_graph():
    """Generates a Matplotlib graph as base64 PNG"""
    plt.figure(figsize=(4, 2))
    if not co2_history:
        plt.plot([0], [0], marker='o')
    else:
        plt.plot(range(1, len(co2_history)+1), co2_history, marker='o', color='green')
    plt.title("CO₂ Saved Over Time (kg)")
    plt.xlabel("Action #")
    plt.ylabel("CO₂ (kg)")
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    img_b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    return f"data:image/png;base64,{img_b64}"

# --- Flet App ---
def main(page: ft.Page):
    page.title = "Eco Action Tracker"
    page.padding = 20

    action_message = ft.Text("")
    points_text = ft.Text("0", size=18)
    rank_text = ft.Text("#--", size=18)
    co2_text = ft.Text("0 kg", size=18)
    leaderboard_column = ft.Column()
    challenges_column = ft.Column()

    global co2_graph
    co2_graph = ft.Image(src="", width=400, height=200)

    # --- Dashboard update ---
    def build_leaderboard():
        leaderboard_column.controls.clear()
        users_scores = [("UserA", 2100), ("UserB", 1800), ("UserC", 1100)]
        pts = get_user_points(current_user["id"])
        users_scores.append((current_user["username"], pts))
        users_scores.sort(key=lambda x: x[1], reverse=True)
        for idx, (u, score) in enumerate(users_scores, 1):
            leaderboard_column.controls.append(ft.Text(f"{idx}. {u} {score}"))

    def update_dashboard():
        pts = get_user_points(current_user["id"])
        points_text.value = str(pts)
        co2_saved = round(pts * 0.1, 1)
        co2_text.value = f"{co2_saved} kg"
        co2_history.append(co2_saved)
        rank = 1 + sum(1 for u_pts in [2100, 1800, 1100] if pts < u_pts)
        rank_text.value = f"#{rank}"
        build_leaderboard()
        co2_graph.src = plot_co2_graph()
        page.update()

    # --- Quick actions ---
    quick_actions_data = [
        ("Bike to Work", 25, 2.5),
        ("Recycling", 15, 1.5),
        ("Energy Save", 20, 2.0),
        ("Walk", 10, 1.0),
        ("Public Transport", 15, 1.5),
    ]

    def quick_action_handler(action_name, pts, co2):
        c.execute("INSERT INTO challenges (name, reward_points) VALUES (?, ?)", (action_name, pts))
        cid = c.lastrowid
        join_challenge(current_user["id"], cid)
        action_message.value = f"✅ Action Submitted: {action_name} (+{pts} pts, +{co2} kg CO₂)"
        update_dashboard()
        page.update()

    # --- Challenges view ---
    def build_challenges_view():
        challenges_column.controls.clear()
        c.execute("SELECT id, name, reward_points FROM challenges")
        for cid, cname, reward in c.fetchall():
            c.execute("SELECT 1 FROM user_challenges WHERE user_id=? AND challenge_id=?", (current_user["id"], cid))
            joined = c.fetchone()
            btn_text = "✅Joined" if joined else "Join"

            def handle_join(e, ch_id=cid, r=reward):
                if join_challenge(current_user["id"], ch_id):
                    action_message.value = f"✅ Challenge Joined! (+{r} pts applied)"
                    update_dashboard()
                    build_challenges_view()
                    page.update()

            btn = ft.ElevatedButton(btn_text, on_click=handle_join)
            challenges_column.controls.append(
                ft.Row([ft.Text(f"{cname} (+{reward} pts)"), btn], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            )
        challenges_column.controls.append(ft.ElevatedButton("Back", on_click=lambda e: show_dashboard()))

    # --- Login / Signup ---
    username_input = ft.TextField(label="Username")
    email_input = ft.TextField(label="Email")
    password_input = ft.TextField(label="Password", password=True)
    confirm_input = ft.TextField(label="Confirm Password", password=True)

    def do_login():
        global current_user
        user = login_user(username_input.value, password_input.value)
        if user:
            current_user = user
            update_dashboard()
            show_dashboard()
        else:
            action_message.value = "❌ Login failed"
            page.update()

    def do_signup():
        if password_input.value != confirm_input.value:
            action_message.value = "❌ Passwords do not match"
            page.update()
            return
        if create_user(username_input.value, email_input.value, password_input.value):
            action_message.value = "✅ Signup successful! Please login."
            show_login()
        else:
            action_message.value = "❌ Username or Email already exists"
            page.update()

    login_view = ft.Column([
        ft.Text("Welcome Back!", size=20),
        username_input,
        password_input,
        ft.Row([ft.ElevatedButton("Login", on_click=lambda e: do_login()),
                ft.ElevatedButton("Sign Up", on_click=lambda e: show_signup())])
    ])

    signup_view = ft.Column([
        ft.Text("Sign Up", size=20),
        username_input, email_input, password_input, confirm_input,
        ft.ElevatedButton("Create Account", on_click=lambda e: do_signup()),
        ft.TextButton("Switch to Login", on_click=lambda e: show_login())
    ])

    dashboard_view = ft.Column([
        ft.Row([ft.Text("ECO ACTION TRACKER", size=24),
                ft.Text(f"[{current_user['username']}]") if current_user else ft.Text(""),
                ft.ElevatedButton("Logout", on_click=lambda e: show_login())],
               alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        action_message,
        ft.Row([ft.Column([ft.Text("Points"), points_text]),
                ft.Column([ft.Text("Rank"), rank_text]),
                ft.Column([ft.Text("CO₂ Saved"), co2_text])],
               alignment=ft.MainAxisAlignment.SPACE_AROUND),
        ft.Text("Quick Actions:"),
        ft.Row([ft.ElevatedButton(name, on_click=lambda e, n=name, p=pts, c=co: quick_action_handler(n,p,c))
                for name, pts, co in quick_actions_data],
               alignment=ft.MainAxisAlignment.SPACE_AROUND),
        ft.Row([ft.Column([ft.Text("Challenges:"), challenges_column]),
                ft.Column([ft.Text("Leaderboard:"), leaderboard_column])],
               alignment=ft.MainAxisAlignment.SPACE_AROUND),
        co2_graph
    ])

    def show_login():
        page.controls.clear()
        page.add(login_view)
        page.update()

    def show_signup():
        page.controls.clear()
        page.add(signup_view)
        page.update()

    def show_dashboard():
        page.controls.clear()
        page.add(dashboard_view)
        build_challenges_view()
        update_dashboard()
        page.update()

    show_login()

ft.app(target=main)