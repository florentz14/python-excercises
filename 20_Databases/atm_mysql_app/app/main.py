from __future__ import annotations

from atm_mysql_app.app.models.user import ATMUser
from atm_mysql_app.app.routers.menu import run_menu_loop
from atm_mysql_app.app.schemas.auth import LoginRequest


def run():
    print("=" * 50)
    print("Welcome to ATM Database System")
    print("=" * 50)

    username = input("Enter your username: ").strip()
    auth_request = LoginRequest(username=username, password="", max_attempts=3)
    user = ATMUser.authenticate(
        username=auth_request.username,
        password=auth_request.password,
        max_attempts=auth_request.max_attempts,
    )
    if not user:
        print("Authentication failed. Exiting...")
        return

    user.create_session()
    run_menu_loop(user)


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting...")
    except Exception as exc:
        print(f"\n\nUnexpected error: {exc}")
