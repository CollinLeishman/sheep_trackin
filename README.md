# Sheep Tracker

## Running the app

It only runs locally. Run the prepare.sh script, source the virtual environment, then make migrate_latest, and run make
start_app.

```bash
## Migrations

Peewee doesn't support database versioning natively, so I've implemented it because they're useful for collaboration.
All migrations are generated via the make command and resulting file is in the "migrations" folder.
Migration naming convention is entity_action. For example, 'sheep_table_create'.
The make command is: `make migration "sheep_table_create"`
To run all migrations, use `make migrate_latest`. You may notice that it runs `db.create_tables` in each one, but it
only
actually creates the table if it doesn't already exist.
This approach allows us to put all migrations (including schema changes) in the same directory.

**TODO:**

- Create a migration backbone template importing peewee, db connection, and provide a warning about model redefinition
  in `app.py`.
- Add ability to create and delete sheep
- Check that ewe is indeed a female, ram is male and that they exist
- Figure out why EMPTY is being inserted into the database instead of NULL, it should error out because of the null contraint
- Consolidate url redirect logic, a bunch is happening in javascript, some in app.py