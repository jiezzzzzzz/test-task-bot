"""create account table

Revision ID: 32f41138470c
Revises: 
Create Date: 2022-11-11 12:50:28.152842

"""


# revision identifiers, used by Alembic.
revision = '32f41138470c'
down_revision = None
branch_labels = None
depends_on = None
from alembic import op
import sqlalchemy as sa
from sqlalchemy import String, Column
from sqlalchemy.sql import table, column

from alembic import context


def upgrade():
    schema_upgrades()
    if context.get_x_argument(as_dictionary=True).get('data', None):
        data_upgrades()


def downgrade():
    if context.get_x_argument(as_dictionary=True).get('data', None):
        data_downgrades()
    schema_downgrades()


def schema_upgrades():
    """schema upgrade migrations go here."""
    op.create_table("roles", Column('name', String))


def schema_downgrades():
    """schema downgrade migrations go here."""
    op.drop_table("my_table")


def data_upgrades():
    """Add any optional data upgrade migrations here!"""

    my_table = table('roles',
        column('name', String),
    )

    op.bulk_insert(my_table,
        [
            {'name': 'Грузчик'},
            {'name': 'Дворник'}
        ]
    )


def data_downgrades():
    """Add any optional data downgrade migrations here!"""

    op.execute("delete from my_table")