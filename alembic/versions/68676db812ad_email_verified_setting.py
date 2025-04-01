"""email_verified_setting

Revision ID: 68676db812ad
Revises: 068dd42b4bc4
Create Date: 2025-04-01 03:40:00.458336

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '68676db812ad'
down_revision: Union[str, None] = '068dd42b4bc4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        'users',
        'email_verified_at',
        existing_type=sa.VARCHAR(length=255),
        type_=sa.TIMESTAMP(),
        existing_nullable=True,
        postgresql_using='email_verified_at::timestamp without time zone'  # Add the USING clause
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        'users',
        'email_verified_at',
        existing_type=sa.TIMESTAMP(),
        type_=sa.VARCHAR(length=255),
        existing_nullable=True
    )
