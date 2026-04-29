from __future__ import annotations

from atm_mysql_app.app.routers.user_menu import run_user_admin_menu


def run():
    run_user_admin_menu()


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Exiting...")
