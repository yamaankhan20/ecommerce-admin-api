"""create_launchpads_table

Revision ID: ac2cb4587736
Revises: 37bf5e212bf2
Create Date: 2025-03-21 20:44:16.446147

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac2cb4587736'
down_revision: Union[str, None] = '37bf5e212bf2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('launchpads',
        sa.Column('id', sa.BigInteger().with_variant(sa.Integer, "sqlite"), primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), index=True, nullable=False),
        sa.Column('factory_id', sa.Integer, index=True, nullable=False),
        sa.Column('contract', sa.String(length=44), nullable=True),
        sa.Column('token', sa.String(length=44), nullable=True),
        sa.Column('pool', sa.String(length=44), nullable=True),
        sa.Column('graph', sa.String(600), nullable=True),
        sa.Column('name', sa.String(32), nullable=False),
        sa.Column('symbol', sa.String(10), nullable=False),
        sa.Column('description', sa.Text, nullable=False),
        sa.Column('chainId', sa.String(191), nullable=False),
        sa.Column('twitter', sa.String(191), nullable=True),
        sa.Column('discord', sa.String(191), nullable=True),
        sa.Column('telegram', sa.String(191), nullable=True),
        sa.Column('website', sa.String(191), nullable=True),
        sa.Column('livestreamId', sa.String(191), nullable=True),
        sa.Column('status', sa.String(length=191), nullable=False, server_default='pending'),
        sa.Column('logo', sa.String(length=191), nullable=True),
        sa.Column('featured', sa.Boolean(), nullable=False, server_default='0'),
        sa.Column('kingofthehill', sa.Boolean(), nullable=False, server_default='0'),
        sa.Column('active', sa.Boolean(), nullable=False, server_default='1'),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=True, onupdate=sa.func.now()),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('launchpads')
