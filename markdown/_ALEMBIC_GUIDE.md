# Database migrations (Alembic)

This project ships with **Alembic** (`requirements.txt`) and config under `alembic/` + `alembic.ini`. Migrations live in `alembic/versions/` (create that folder when you add your first revision).

---

## Before you run anything

1. **Virtualenv** active, dependencies installed: `pip install -r requirements.txt`.
2. **Postgres running** and **`.env`** present with a valid `DATABASE_URL` (same as when you run the API locally).
3. **Wire Alembic to your models** (one-time): in `alembic/env.py`, set `target_metadata` to your SQLAlchemy `Base.metadata` and load all model modules so tables are registered. Until that is done, `revision --autogenerate` will not see your tables.

   Minimal pattern:

   ```python
   from app.models.base import Base
   import app.models  # noqa: F401 — side effect: registers models on Base.metadata

   target_metadata = Base.metadata
   ```

   Point Alembic at the same database as the app, either by:

   - setting `sqlalchemy.url` in `alembic.ini` to the same URL as `DATABASE_URL`, or  
   - overriding the URL inside `env.py` from `get_settings().database_url` before creating the engine (avoids duplicating secrets in the ini file).

4. **Create the versions directory** if it does not exist:

   ```bash
   mkdir -p alembic/versions
   ```

   Optionally add `alembic/versions/.gitkeep` so the empty folder is tracked until the first migration file exists.

---

## Generate a migration (autogenerate)

From the **repository root**:

```bash
alembic revision --autogenerate -m "short description of change"
```

- Review the generated file under `alembic/versions/`. Autogenerate can miss renames or add noise; adjust the script before upgrading.
- If nothing changes in the file, your metadata may not match the DB or models are not imported on `Base`.

---

## Apply migrations

```bash
alembic upgrade head
```

To step one revision forward or back during development:

```bash
alembic upgrade +1
alembic downgrade -1
```

---

## Useful checks

| Command | Purpose |
|--------|---------|
| `alembic current` | Show current DB revision |
| `alembic history` | List migration scripts |
| `alembic heads` | Show head revision(s) |

---

## Docker / CI

Use the same `DATABASE_URL` the app uses (e.g. from env in Compose). Run `alembic upgrade head` as a deploy step or init container **before** starting the API when you rely on migrations for schema.

---

## Further reading

- [Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
- [Autogenerate](https://alembic.sqlalchemy.org/en/latest/autogenerate.html)
