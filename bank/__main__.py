from apiflask import APIFlask
from flask_migrate import Migrate

from bank.api.routers import include_router
from bank.settings import settings

app = APIFlask(
    __name__,
    title="Bank API",
    version="0.1.0",
)

app.config["SQLALCHEMY_DATABASE_URI"] = settings.database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


include_router(app)

with app.app_context():
    from bank.db.mappings.base import db  # noqa: WPS433, F401

    db.init_app(app)
    migrate = Migrate(app, db, directory="./bank/db/migrations")

if __name__ == "__main__":
    app.run()
