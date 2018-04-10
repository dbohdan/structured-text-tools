sql-based.md: sql-based.csv Makefile
	printf '## SQL-based tools\n\n' > $@
	csv2html $< | tidy -quiet --indent yes --show-body-only yes >> $@
