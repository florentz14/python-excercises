# -------------------------------------------------
# File Name: ITSE-1003/Examples/logger_mixin.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Mixins for reusable behavior.
# -------------------------------------------------

from datetime import datetime


class TimestampMixin:
    def timestamp(self) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class Logger(TimestampMixin):
    def log(self, message: str) -> None:
        print(f"[{self.timestamp()}] {message}")


def main() -> None:
    logger = Logger()
    logger.log("Application started")
    logger.log("Processing request")


if __name__ == "__main__":
    main()
