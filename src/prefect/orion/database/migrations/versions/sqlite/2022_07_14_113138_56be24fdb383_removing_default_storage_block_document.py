"""Removing default storage block document.

Revision ID: 56be24fdb383
Revises: 061c7e518b40
Create Date: 2022-07-14 11:31:38.843301

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "56be24fdb383"
down_revision = "061c7e518b40"
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("block_document", schema=None) as batch_op:
        batch_op.drop_index("ix_block_document__is_default_storage_block_document")
        batch_op.drop_column("is_default_storage_block_document")


def downgrade():
    with op.batch_alter_table("block_document", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "is_default_storage_block_document",
                sa.BOOLEAN(),
                server_default=sa.text("'0'"),
                nullable=True,
            )
        )
        batch_op.create_index(
            "ix_block_document__is_default_storage_block_document",
            ["is_default_storage_block_document"],
            unique=False,
        )
