all: README.md sql-based.md

README.md: README.md.jinja render-template.py Makefile data/projects.toml
	./render-template.py README.md.jinja data/projects.toml > $@

sql-based.md: sql-based.md.jinja render-template.py Makefile data/sql-based.toml
	./render-template.py sql-based.md.jinja data/sql-based.toml > $@
