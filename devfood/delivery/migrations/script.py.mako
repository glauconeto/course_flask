"""${message}
Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}

"""

from alembic import op
import sqlachemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
resivion = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(depends_on)}


def upgrade():
    ${upgrades if upgrades else "pass"}

def downgrade():
    ${downgrades if downgrades else "pass"}