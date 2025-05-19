"""update fields edit

Revision ID: 59f74e6cc8dc
Revises: e669e06d2e1e
Create Date: 2025-05-19 08:40:18.851234

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59f74e6cc8dc'
down_revision: Union[str, None] = 'e669e06d2e1e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        'products', 'updated_at',
        existing_type=sa.TIMESTAMP(),
        server_default=sa.text('NOW()'),
        existing_nullable=True
    )

    op.alter_column(
        'categories', 'updated_at',
        existing_type=sa.TIMESTAMP(),
        server_default=sa.text('NOW()'),
        existing_nullable=True
    )

    op.alter_column(
        'inventory', 'updated_at',
        existing_type=sa.TIMESTAMP(),
        server_default=sa.text('NOW()'),
        existing_nullable=True
    )

    op.alter_column(
        'sales', 'updated_at',
        existing_type=sa.TIMESTAMP(),
        server_default=sa.text('NOW()'),
        existing_nullable=True
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('products', 'updated_at', server_default=None,
                    existing_type=sa.TIMESTAMP(), existing_nullable=True)
    op.alter_column('categories', 'updated_at', server_default=None,
                    existing_type=sa.TIMESTAMP(), existing_nullable=True)
    op.alter_column('inventory', 'updated_at', server_default=None,
                    existing_type=sa.TIMESTAMP(), existing_nullable=True)
    op.alter_column('sales', 'updated_at', server_default=None,
                    existing_type=sa.TIMESTAMP(), existing_nullable=True)
