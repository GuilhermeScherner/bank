from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_mixin

db = SQLAlchemy()


@declarative_mixin
class TimestampedMixin:
    """Generate times Created and Updated."""

    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=db.func.now(),
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        onupdate=db.func.now(),
    )


@db.declarative_mixin
class IDMixin:
    """Generate ID."""

    id = db.Column(
        db.Integer,
        autoincrement=True,
        unique=True,
        primary_key=True,
    )


@db.as_declarative()
class BaseMapping(TimestampedMixin, IDMixin, db.Model):  # type: ignore
    """Base Mapping for all class."""

    __abstract__ = True
