"""user_make_nullable

Revision ID: 27d0b2cd6aa3
Revises: a3e74a3a3633
Create Date: 2025-03-24 23:22:03.607912

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '27d0b2cd6aa3'
down_revision: Union[str, None] = 'a3e74a3a3633'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        'users',
        'name',
        existing_type=sa.String(length=255),
        nullable=True
    )
    op.alter_column(
        'users',
        'email_verified_at',
        existing_type=sa.String(length=255),
        nullable=True
    )
    op.alter_column(
        'users',
        'email',
        existing_type=sa.String(length=255),
        nullable=True
    )
    op.alter_column(
        'users',
        'address',
        existing_type=sa.String(length=255),
        nullable=True
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        'users',
        'name',
        existing_type=sa.String(length=255),
        nullable=False
    )
    op.alter_column(
        'users',
        'email_verified_at',
        existing_type=sa.String(length=255),
        nullable=False
    )
    op.alter_column(
        'users',
        'address',
        existing_type=sa.String(length=255),
        nullable=False
    )
    op.alter_column(
        'users',
        'email',
        existing_type=sa.String(length=255),
        nullable=False
    )
