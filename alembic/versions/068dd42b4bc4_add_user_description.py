"""add_user_description

Revision ID: 068dd42b4bc4
Revises: 9e1c9a49fa98
Create Date: 2025-03-25 21:59:50.992992

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '068dd42b4bc4'
down_revision: Union[str, None] = '9e1c9a49fa98'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
