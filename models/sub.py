from datetime import datetime
import functools
import pytz
import sqlalchemy as sa

import gino
db = gino.Gino()


class Subscription(db.Model):
    """User subscription data"""
    __tablename__ = 'subscription'

    id = sa.Column(sa.Integer(), primary_key=True, autoincrement=True)
    token = sa.Column(sa.String(length=255), unique=True, nullable=False)
    user_agent = sa.Column(sa.String(length=500), nullable=False)
    ip = sa.Column(sa.String(length=19), nullable=False)
    is_mobile = sa.Column(sa.Boolean())
    country_code = sa.Column(sa.String(length=2))
    timezone = sa.Column(sa.String(length=255))
    source_id = sa.Column(sa.Integer(), default=1)
    source = sa.Column(sa.String())  # TODO: remove
    campaign_id = sa.Column(sa.SmallInteger(), nullable=False)
    version = sa.Column(sa.SmallInteger(), nullable=False)
    language = sa.Column(sa.Text())
    is_adult = sa.Column(sa.Boolean())
    created_at = sa.Column(
        sa.DateTime(timezone=True),
        default=functools.partial(datetime.now, pytz.UTC),
        server_default=sa.func.now(),
        nullable=False,
    )

    def __repr__(self):
        """ Show user object info. """
        return f'{self.id}: {self.token}'
