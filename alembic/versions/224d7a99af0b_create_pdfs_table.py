"""create pdfs table

Revision ID: 224d7a99af0b
Revises: bad11d84ac1a
Create Date: 2025-02-06 16:23:59.295099

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '224d7a99af0b'
down_revision: Union[str, None] = 'bad11d84ac1a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() 
op.create_table(
         'pdfs',
         sa.Column('id', sa.BigInteger, primary_key=True),
         sa.Column('name', sa.Text, nullable=False),
         sa.Column('file', sa.Text, nullable=False),
         sa.Column('selected', sa.Boolean, nullable=False, default=False)
     )


def downgrade() 
op.drop_table('pdfs')
