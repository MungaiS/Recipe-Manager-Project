"""Add new table

Revision ID: d57ef1675440
Revises: fb3bdc54574b
Create Date: 2024-03-24 14:03:19.000111

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd57ef1675440'
down_revision: Union[str, None] = 'fb3bdc54574b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
