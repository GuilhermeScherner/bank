from apiflask import APIFlask
from dotenv import dotenv_values
from flask_httpauth import HTTPBasicAuth

from bank.api.routers import include_router

auth = HTTPBasicAuth()

config = dotenv_values(".env.local")

app = APIFlask(
    __name__,
    title="Bank API",
    version="0.1.0",
)

include_router(app)

if __name__ == "__main__":
    port = int(config.get("BANK_PORT")) or None  # type: ignore
    debug = bool(config.get("BANK_DEBUG", False))
    app.run(
        host=config.get("BANK_HOST"),
        port=port,
        debug=debug,
    )
