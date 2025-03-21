"""create_users_table

Revision ID: a7fcc3fd3bee
Revises: 
Create Date: 2025-03-21 20:33:43.784741

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a7fcc3fd3bee'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(255), nullable=False, index=True),
        sa.Column('email', sa.String(255), unique=True, nullable=False, index=True),
        sa.Column('address', sa.String(length=255), nullable=False),
        sa.Column('email_verified_at', sa.String(length=255), nullable=False),
        sa.Column('profile_photo_path', sa.String(length=191), nullable=True),
        sa.Column('otp', sa.String(length=191), nullable=True),
        sa.Column('otp_expires_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('active', sa.Boolean(), nullable=False, default=True),
        sa.Column('banned', sa.Boolean(), nullable=False, default=False),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP, server_default=sa.func.now(), nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
