all: README.md sql-based.md

README.md: README.md.jinja Makefile data/projects.toml macros.md.jinja render-template.py
	./render-template.py README.md.jinja data/projects.toml > $@

sql-based.md: sql-based.md.jinja Makefile data/sql-based.toml macros.md.jinja render-template.py
	./render-template.py sql-based.md.jinja data/sql-based.toml > $@
