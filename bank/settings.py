import os

from dotenv import load_dotenv

PORT_DEFAULT = 5000
HOST_DEFAULT = "127.0.0.1"
ENVIRONMENT_DEFAULT = "development"


class Settings:  # noqa: WPS230
    """Settings for the bank application."""

    def __init__(self) -> None:
        load_dotenv(".env")
        self.database_url: str = "mysql+pymysql://admin:admin@localhost:3306/bank"
        self.bank_reload: bool = os.getenv("BANK_RELOAD") == "True"
        self.bank_host: str = os.getenv("BANK_HOST") or HOST_DEFAULT
        self.bank_port: int = (
            os.getenv("BANK_PORT")
            if os.getenv("BANK_PORT") or not os.getenv("BANK_PORT").isdigit()  # type: ignore
            else PORT_DEFAULT
        )
        self.bank_environment: str = (
            os.getenv("BANK_ENVIRONMENT") or ENVIRONMENT_DEFAULT
        )
        self.bank_debug: bool = os.getenv("BANK_DEBUG") == "True"
        self.bank_secret_key: str = os.getenv("BANK_SECRET_KEY") or "secret"


settings = Settings()
