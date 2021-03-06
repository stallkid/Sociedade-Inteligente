"""empty message

Revision ID: d2aa003a921b
Revises: 988cee505eeb
Create Date: 2019-03-29 16:28:12.969954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2aa003a921b'
down_revision = '988cee505eeb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuarios', sa.Column('permissao_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'usuarios', 'permissoes', ['permissao_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'usuarios', type_='foreignkey')
    op.drop_column('usuarios', 'permissao_id')
    # ### end Alembic commands ###
