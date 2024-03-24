"""Updated tables with fake data

Revision ID: 666b9fd2516c
Revises: d57ef1675440
Create Date: 2024-03-24 14:17:41.300315

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '666b9fd2516c'
down_revision: Union[str, None] = 'd57ef1675440'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
