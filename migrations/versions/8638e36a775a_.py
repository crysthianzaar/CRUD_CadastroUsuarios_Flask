"""empty message

Revision ID: 8638e36a775a
Revises: 
Create Date: 2021-12-20 23:52:00.990614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8638e36a775a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('endereco_usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pais', sa.String(length=80), nullable=False),
    sa.Column('estado', sa.String(length=80), nullable=False),
    sa.Column('municipio', sa.String(length=80), nullable=False),
    sa.Column('cep', sa.String(length=10), nullable=False),
    sa.Column('rua', sa.String(length=80), nullable=False),
    sa.Column('numero', sa.String(length=15), nullable=True),
    sa.Column('complemento', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('pis', sa.String(length=11), nullable=False),
    sa.Column('senha', sa.String(length=512), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('nome'),
    sa.UniqueConstraint('pis')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuario')
    op.drop_table('endereco_usuario')
    # ### end Alembic commands ###