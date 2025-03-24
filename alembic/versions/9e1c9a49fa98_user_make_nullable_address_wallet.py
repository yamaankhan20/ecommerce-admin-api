"""user_make_nullable_address_wallet

Revision ID: 9e1c9a49fa98
Revises: 11070cf8401e
Create Date: 2025-03-25 00:21:33.543220

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e1c9a49fa98'
down_revision: Union[str, None] = '11070cf8401e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_unique_constraint(
        "uq_users_address",
        "users",
        ["address"]
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        "uq_users_address",
        "users",
        type_="unique"
    )
