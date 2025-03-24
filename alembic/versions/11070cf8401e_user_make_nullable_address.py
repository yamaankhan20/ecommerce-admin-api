"""user_make_nullable_address

Revision ID: 11070cf8401e
Revises: 27d0b2cd6aa3
Create Date: 2025-03-25 00:17:25.119675

"""
from enum import unique
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '11070cf8401e'
down_revision: Union[str, None] = '27d0b2cd6aa3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        'users',
        'address',
        existing_type=sa.String(length=255),
        unique=True
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        'users',
        'address',
        existing_type=sa.String(length=255),
        unique=False
    )
