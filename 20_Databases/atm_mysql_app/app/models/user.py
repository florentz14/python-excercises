from __future__ import annotations

from typing import Optional

import bcrypt

from atm_mysql_app.app.database import DatabaseConnection


class ATMUser:
    """Represents an ATM user with authentication/session methods."""

    def __init__(self, user_id: int, username: str, full_name: str, current_balance: float):
        self.user_id = user_id
        self.username = username
        self.full_name = full_name
        self.current_balance = current_balance
        self.session_id: Optional[int] = None

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

    @staticmethod
    def hash_password(password: str) -> str:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")

    @classmethod
    def authenticate(cls, username: str, password: str, max_attempts: int = 3) -> Optional["ATMUser"]:
        attempts_left = max_attempts

        while attempts_left > 0:
            entered_password = password if attempts_left == max_attempts else input("Enter your password: ").strip()

            with DatabaseConnection() as db:
                query = "SELECT id, username, password_hash, full_name, current_balance, is_active FROM atm_users WHERE username = %s"
                db.execute(query, (username,))
                user_data = db.cursor.fetchone()

                if not user_data:
                    cls._log_login_attempt(username, None, "failed", "User not found")
                    print("User not found.")
                    return None

                if not user_data["is_active"]:
                    cls._log_login_attempt(username, user_data["id"], "blocked", "Account inactive")
                    print("Account is inactive. Contact support.")
                    return None

                if cls.verify_password(entered_password, user_data["password_hash"]):
                    user = cls(
                        user_id=user_data["id"],
                        username=user_data["username"],
                        full_name=user_data["full_name"],
                        current_balance=float(user_data["current_balance"]),
                    )
                    update_query = """
                        UPDATE atm_users
                        SET failed_login_attempts = 0, last_login_at = NOW()
                        WHERE id = %s
                    """
                    db.execute(update_query, (user.user_id,))
                    db.commit()
                    cls._log_login_attempt(username, user.user_id, "success", None)
                    print(f"Login successful! Welcome, {user.full_name}\n")
                    return user

                attempts_left -= 1
                update_query = """
                    UPDATE atm_users
                    SET failed_login_attempts = failed_login_attempts + 1
                    WHERE id = %s
                """
                db.execute(update_query, (user_data["id"],))
                db.commit()
                cls._log_login_attempt(username, user_data["id"], "failed", "Incorrect password")

                if attempts_left > 0:
                    print(f"Incorrect password. Attempts left: {attempts_left}")
                else:
                    print("Too many incorrect attempts. Program will exit.")

        return None

    @staticmethod
    def _log_login_attempt(username: str, user_id: Optional[int], status: str, reason: Optional[str]):
        try:
            with DatabaseConnection() as db:
                query = """
                    INSERT INTO atm_login_attempts (username, id_user, attempt_status, failure_reason)
                    VALUES (%s, %s, %s, %s)
                """
                db.execute(query, (username, user_id, status, reason))
                db.commit()
        except Exception as exc:
            print(f"Warning: Could not log login attempt: {exc}")

    def create_session(self) -> int:
        with DatabaseConnection() as db:
            query = "INSERT INTO atm_sessions (id_user) VALUES (%s)"
            db.execute(query, (self.user_id,))
            db.commit()
            self.session_id = db.cursor.lastrowid
            if self.session_id is None:
                raise RuntimeError("Session creation failed: no session_id returned.")
            return self.session_id

    def close_session(self):
        if self.session_id:
            with DatabaseConnection() as db:
                query = """
                    UPDATE atm_sessions
                    SET logout_at = NOW(),
                        session_duration = TIMESTAMPDIFF(SECOND, login_at, NOW())
                    WHERE id = %s
                """
                db.execute(query, (self.session_id,))
                db.commit()
