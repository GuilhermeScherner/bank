from apiflask import APIFlask
from dotenv import dotenv_values
from bank.api.routers import include_router
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

config = dotenv_values(".env.local")

app = APIFlask(
    __name__,
    title='Bank API',
    version='1.0.0',
)

include_router(app)

if __name__ == "__main__":
    app.run(
        host=config['BANK_HOST'],
        port=config['BANK_PORT'],
        debug=config['BANK_DEBUG'],
    )
