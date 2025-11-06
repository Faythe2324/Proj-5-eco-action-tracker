from backend.database import get_connection
import hashlib

class User:
    def __init__(self, username, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                       (self.username, self.email, self.hash_password(self.password)))
        conn.commit()
        conn.close()

    @staticmethod
    def login(username, password):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                       (username, User.hash_password(password)))
        user = cursor.fetchone()
        conn.close()
        return user

    @staticmethod
    def update_points_co2(user_id, points, co2):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET points = points + ?, co2_saved = co2_saved + ? WHERE id=?",
                       (points, co2, user_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_leaderboard():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT username, points FROM users ORDER BY points DESC LIMIT 10")
        leaderboard = cursor.fetchall()
        conn.close()
        return leaderboard

class Action:
    def __init__(self, user_id, name, points, co2):
        self.user_id = user_id
        self.name = name
        self.points = points
        self.co2 = co2

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO actions (user_id, action_name, points, co2) VALUES (?, ?, ?, ?)",
                       (self.user_id, self.name, self.points, self.co2))
        conn.commit()
        conn.close()
        User.update_points_co2(self.user_id, self.points, self.co2)

class Challenge:
    @staticmethod
    def all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM challenges")
        challenges = cursor.fetchall()
        conn.close()
        return challenges

    @staticmethod
    def join(challenge_id, username):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT joined_by FROM challenges WHERE id=?", (challenge_id,))
        joined = cursor.fetchone()['joined_by']
        joined_list = joined.split(",") if joined else []
        if username not in joined_list:
            joined_list.append(username)
        cursor.execute("UPDATE challenges SET joined_by=? WHERE id=?", (",".join(joined_list), challenge_id))
        conn.commit()
        conn.close()
