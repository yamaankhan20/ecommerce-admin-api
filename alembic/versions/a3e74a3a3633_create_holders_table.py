"""create_holders_table

Revision ID: a3e74a3a3633
Revises: 6b7e07d16862
Create Date: 2025-03-21 22:01:18.831858

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3e74a3a3633'
down_revision: Union[str, None] = '6b7e07d16862'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'holders',
        sa.Column('id', sa.BigInteger().with_variant(sa.Integer, "sqlite"), primary_key=True, autoincrement=True),
        sa.Column('launchpad_id', sa.BigInteger().with_variant(sa.Integer, "sqlite"), nullable=False),
        sa.Column('user_id', sa.BigInteger().with_variant(sa.Integer, "sqlite"), sa.ForeignKey('users.id'), nullable=True),
        sa.Column('address', sa.String(length=191), nullable=False),
        sa.Column('qty', sa.String(length=191), nullable=False),
        sa.Column('prebond', sa.Boolean(), nullable=False, server_default='0'),
        sa.Column('created_at', sa.TIMESTAMP, nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP, nullable=True),
        sa.Column('deleted_at', sa.TIMESTAMP, nullable=True),
        sa.UniqueConstraint('launchpad_id', 'address', name='holders_launchpad_id_address_unique'),
        sa.Index('holders_user_id_foreign', 'user_id'),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('holders')
