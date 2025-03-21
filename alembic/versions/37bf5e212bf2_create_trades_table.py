"""create_trades_table

Revision ID: 37bf5e212bf2
Revises: a7fcc3fd3bee
Create Date: 2025-03-21 20:35:13.713753

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '37bf5e212bf2'
down_revision: Union[str, None] = 'a7fcc3fd3bee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'trades',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('launchpad_id', sa.BigInteger().with_variant(sa.Integer, "sqlite"), nullable=False, index=True),
        sa.Column('txid', sa.String(255), nullable=False, index=True),
        sa.Column('address', sa.String(length=255), nullable=False),
        sa.Column('qty', sa.String(length=191), nullable=False),
        sa.Column('amount', sa.String(length=191), nullable=False),
        sa.Column('usd', sa.String(length=191), nullable=False, default='0.00'),
        sa.Column('type', sa.Boolean(), nullable=False, default=True),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP, server_default=sa.func.now(), nullable=False),
        sa.Column('deleted_at', sa.TIMESTAMP, server_default=sa.func.now(), nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('trades')
