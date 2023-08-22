# Makefile
include required_environment_variables

start_app:
	flask run --debug -h 0.0.0.0

migration:
	@if [ -z "$(ARGS)" ]; then \
		echo "See the README section 'Migrations."; \
	else \
		current_number_of_migrations=$$(ls -1 migrations | wc -l); \
		new_migration_index=$$(($$current_number_of_migrations + 1)); \
		new_migration_filename=`printf "%03d" $$new_migration_index`_$(ARGS).py; \
		touch migrations/$$new_migration_filename; \
		chmod 755 migrations/$$new_migration_filename; \
		echo "Created migration: $$new_migration_filename"; \
	fi

migrate_latest:
	@for file in migrations/*; do \
  echo "Executing $$file"; \
  $(PYTHON_VENV_PATH) $$file; \
  done
