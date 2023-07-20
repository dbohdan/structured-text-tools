all: README.md sql-based.md

README.md: README.md.jinja2 render-template.py Makefile data/projects.toml
	./render-template.py README.md.jinja2 data/projects.toml > $@

sql-based.md: sql-based.md.jinja2 render-template.py Makefile data/sql-based.toml
	./render-template.py sql-based.md.jinja2 data/sql-based.toml > $@
