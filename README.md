# Sheep Tracker

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

```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "name": "Dolly",
  "birth_date": "2023-01-01",
  "gender": "female",
  "tag_number": "12345"
}' http://localhost:5000/sheep


curl -X PUT -H "Content-Type: application/json" -d '{
"name": "Updated Fluffy",
"birth_date": "2023-01-02",
"gender": "male",
"tag_number": "67890"
}' http://localhost:5000/sheep/1

```