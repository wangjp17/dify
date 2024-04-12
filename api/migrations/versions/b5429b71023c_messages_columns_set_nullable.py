"""messages columns set nullable

Revision ID: b5429b71023c
Revises: 42e85ed5564d
Create Date: 2024-03-07 09:52:00.846136

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'b5429b71023c'
down_revision = '42e85ed5564d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.alter_column('model_provider',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('model_id',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.alter_column('model_id',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('model_provider',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)

    # ### end Alembic commands ###