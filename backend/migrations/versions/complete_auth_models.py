"""empty message

Revision ID: 96c9149c665e
Revises: 4a3b4bfc7887
Create Date: 2024-08-03 14:55:06.687894

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "96c9149c665e"
down_revision: Union[str, None] = "4a3b4bfc7887"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f("ix_roles_name"), "roles", ["name"], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_roles_name"), table_name="roles")
    # ### end Alembic commands ###
