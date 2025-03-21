"""create_factories_table

Revision ID: 6d86979fc8da
Revises: ac2cb4587736
Create Date: 2025-03-21 21:08:28.120383

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql


# revision identifiers, used by Alembic.
revision: str = '6d86979fc8da'
down_revision: Union[str, None] = 'ac2cb4587736'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('factories',
        sa.Column('id', sa.BigInteger().with_variant(sa.Integer, "sqlite"), primary_key=True,
                  autoincrement=True),
        sa.Column('version', sa.String(length=191), nullable=False, server_default='1'),
        sa.Column('chainId', sa.String(length=191), nullable=True),
        sa.Column('foundry', sa.String(length=191), nullable=True),
        sa.Column('contract', sa.String(length=191), nullable=True),
        sa.Column('lock', sa.String(length=191), nullable=True),
        sa.Column('lock_abi', mysql.JSON, nullable=True),
        sa.Column('factory_abi', mysql.JSON, nullable=True),
        sa.Column('abi', mysql.JSON, nullable=True),
        sa.Column('active', sa.Boolean(), nullable=False, server_default='1'),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),

    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('factories')
