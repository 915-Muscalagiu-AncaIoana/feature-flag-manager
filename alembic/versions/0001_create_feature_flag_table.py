from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'feature_flags',
        sa.Column('id', sa.String(), primary_key=True),
        sa.Column('name', sa.String(), unique=True, nullable=False),
        sa.Column('enabled', sa.Boolean(), nullable=False, default=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False)
    )

def downgrade():
    op.drop_table('feature_flags')
