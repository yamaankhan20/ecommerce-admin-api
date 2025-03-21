"""create_poolstats_table

Revision ID: 6b7e07d16862
Revises: 6d86979fc8da
Create Date: 2025-03-21 21:56:43.250725

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b7e07d16862'
down_revision: Union[str, None] = '6d86979fc8da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'poolstats',
        sa.Column('id', sa.BigInteger().with_variant(sa.Integer, "sqlite"), primary_key=True, autoincrement=True),
        sa.Column('launchpad_id', sa.BigInteger().with_variant(sa.Integer, "sqlite"), nullable=False),
        sa.Column('token0_price', sa.Numeric(precision=36, scale=18), nullable=False),
        sa.Column('token1_price', sa.Numeric(precision=36, scale=18), nullable=False),
        sa.Column('tvl_usd', sa.Numeric(precision=36, scale=18), nullable=False),
        sa.Column('volume_24h', sa.Numeric(precision=36, scale=18), nullable=False),
        sa.Column('fee_tier', sa.Numeric(precision=5, scale=2), nullable=False),
        sa.Column('transactions_24h', sa.Integer, nullable=False, server_default='0'),
        sa.Column('total_transactions', sa.Integer, nullable=False, server_default='0'),
        sa.Column('liquidity', sa.Numeric(precision=36, scale=18), nullable=False),
        sa.Column('price_change_1h', sa.Numeric(precision=8, scale=4), nullable=False),
        sa.Column('price_change_24h', sa.Numeric(precision=8, scale=4), nullable=False),
        sa.Column('price_change_7d', sa.Numeric(precision=8, scale=4), nullable=False),
        sa.Column('min_price_24h', sa.Numeric(precision=36, scale=18), nullable=False),
        sa.Column('max_price_24h', sa.Numeric(precision=36, scale=18), nullable=False),
        sa.Column('timestamp', sa.TIMESTAMP, nullable=False),
        sa.Column('created_at', sa.TIMESTAMP, nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP, nullable=True),
        sa.Column('deleted_at', sa.TIMESTAMP, nullable=True),
        sa.UniqueConstraint('launchpad_id', 'timestamp', name='poolstats_launchpad_id_timestamp_unique'),
        sa.Index('poolstats_timestamp_index', 'timestamp'),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('poolstats')
