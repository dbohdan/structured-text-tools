README.md: README.md.jinja2 generate-readme.py GNUmakefile data/projects.toml
	./generate-readme.py > $@

sql-based.md: data/sql-based.csv GNUmakefile
	printf '## SQL-based tools\n\n' > $@
	csv2html $< | tidy -quiet -indent --show-body-only yes >> $@
