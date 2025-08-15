---
title: Database Tables
category: misc
source_lines: 85554-85675
line_count: 121
---

# Database Tables
Source: https://docs.agno.com/workspaces/workspace-management/database-tables



Agno templates come pre-configured with [SqlAlchemy](https://www.sqlalchemy.org/) and [alembic](https://alembic.sqlalchemy.org/en/latest/) to manage databases. The general workflow to add a table is:

1. Add table definition to the `db/tables` directory.
2. Import the table class in the `db/tables/__init__.py` file.
3. Create a database migration.
4. Run database migration.

## Table Definition

Let's create a `UsersTable`, copy the following code to `db/tables/user.py`

```python db/tables/user.py
from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.expression import text
from sqlalchemy.types import BigInteger, DateTime, String

from db.tables.base import Base


class UsersTable(Base):
    """Table for storing user data."""

    __tablename__ = "dim_users"

    id_user: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True, nullable=False, index=True
    )
    email: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=text("now()")
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), onupdate=text("now()")
    )
```

Update the `db/tables/__init__.py` file:

```python db/tables/__init__.py
from db.tables.base import Base
from db.tables.user import UsersTable
```

## Creat a database revision

Run the alembic command to create a database migration in the dev container:

```bash
docker exec -it ai-api alembic -c db/alembic.ini revision --autogenerate -m "Initialize DB"
```

## Migrate dev database

Run the alembic command to migrate the dev database:

```bash
docker exec -it ai-api alembic -c db/alembic.ini upgrade head
```

### Optional: Add test user

Now lets's add a test user. Copy the following code to `db/tables/test_add_user.py`

```python db/tables/test_add_user.py
from typing import Optional
from sqlalchemy.orm import Session

from db.session import SessionLocal
from db.tables.user import UsersTable
from utils.log import logger


def create_user(db_session: Session, email: str) -> UsersTable:
    """Create a new user."""
    new_user = UsersTable(email=email)
    db_session.add(new_user)
    return new_user


def get_user(db_session: Session, email: str) -> Optional[UsersTable]:
    """Get a user by email."""
    return db_session.query(UsersTable).filter(UsersTable.email == email).first()


if __name__ == "__main__":
    test_user_email = "test@test.com"
    with SessionLocal() as sess, sess.begin():
        logger.info(f"Creating user: {test_user_email}")
        create_user(db_session=sess, email=test_user_email)
        logger.info(f"Getting user: {test_user_email}")
        user = get_user(db_session=sess, email=test_user_email)
        if user:
            logger.info(f"User created: {user.id_user}")
        else:
            logger.info(f"User not found: {test_user_email}")

```

Run the script to add a test adding a user:

```bash
docker exec -it ai-api python db/tables/test_add_user.py
```

## Migrate production database

We recommended migrating the production database by setting the environment variable `MIGRATE_DB = True` and restarting the production service. This runs `alembic -c db/alembic.ini upgrade head` from the entrypoint script at container startup.

### Update the `workspace/prd_resources.py` file

```python workspace/prd_resources.py
...
