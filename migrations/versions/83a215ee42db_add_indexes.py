"""add indexes

Revision ID: 83a215ee42db
Revises: 6dda8f948f38
Create Date: 2026-04-30 16:04:11.994958

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "83a215ee42db"
down_revision: Union[str, Sequence[str], None] = "6dda8f948f38"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_index("ix_algorithms_category", "algorithms", ["category"])
    op.create_index("ix_algs_algorithm_id", "algs", ["algorithm_id"])
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
