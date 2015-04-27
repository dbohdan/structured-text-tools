What follows is a list of text-based file formats with command line tools for Linux for manipulating each.

## CSV, TSV

| Name | Programming language | Database engine | Features | Usage link | License |
|------|----------------------|-----------------|----------|------------|---------|
| [q](https://github.com/harelba/q) | Python | SQLite 3 | Use header row for column names, custom input and output encoding, gzipped input, custom input field separator (string literal), custom output field separator, custom output formatting, table JOINs, Python module. | [Usage](https://github.com/harelba/q/blob/master/doc/USAGE.markdown) | GNU GPL 3 |
| [sqawk](https://github.com/tjunier/sqawk) | C | SQLite 3 | Use header row for column names, column name aliases, can skip lines until a regexp matches, custom input field separator (string literal, per-file), keep SQLite file, show generated SQL, table JOINs. | [Usage](https://github.com/tjunier/sqawk/blob/master/sqawk.1) | ? |
| [Sqawk](https://github.com/dbohdan/sqawk) | Tcl | SQLite 3 | Use header row for column names, custom input field separator (regexp, per-file), custom input record delimiter (regexp, per-file), custom table names, custom output field separator, custom output record separator, merge selected columns into one, CSV input and output, Tcl output, table JOINs. | [Usage](https://github.com/dbohdan/sqawk#options) | MIT |
| [Squawk](https://github.com/samuel/squawk) | Python | Custom SQL interpreter | Access log and CSV input, JSON and CSV output, Python code generation. | — | Three-clause BSD |
| [termsql](https://github.com/tobimensch/termsql) | Python | SQLite 3 | Use header rows for column names, custom field separator (regexp), custom record separator (string literal), lines as columns, skip a given number of lines and the beginning and at the end, merge selected columns into one, HTML, CSV, SQL and Tcl output. | [Manual](http://tobimensch.github.io/termsql/) | MIT |
| [textql](https://github.com/dinedal/textql) | Go | SQLite 3 | Use header rows for column names, keep SQLite file, custom input field separator (string literal). | [Usage](https://github.com/dinedal/textql#usage) | MIT |

## XML, HTML

* [XMLStarlet](http://xmlstar.sourceforge.net/overview.php)

* [xml2](http://www.ofb.net/~egnor/xml2/) — convert XML and HTML to and from flat, greppable lists of "path=value" statements.

See also: [Grep and Sed Equivalent for XML Command Line Processing](http://stackoverflow.com/questions/91791/grep-and-sed-equivalent-for-xml-command-line-processing) on StackOverflow.

## JSON

* [jq](http://stedolan.github.io/jq/manual/)

## YAML, TOML

Using jq with a format converter (like [mine](https://github.com/dbohdan/remarshal)) appears to be the best option.

## Configuration files

* [Augeas](http://augeas.net) — can extract data from and modify [a number of file formats](http://augeas.net/stock_lenses.html). However, not all format are equally well supported by Augeas and for some formats only a limited subset of all valid files can be parsed.

## Bonus round: CLIs for single-file databases

| Name | Description | File format |
|------|-------------|-------------|
| [GNU Recutils](http://www.gnu.org/software/recutils/) | "[A] set of tools and libraries to access human-editable, plain text databases called recfiles." | Text-based, roughly "key: value" |
| [SDB](https://github.com/radare/sdb) | "[A] simple string key/value database based on djb's cdb disk storage and supports JSON and arrays introspection." | Binary |
| [sqlite3(1)](https://www.sqlite.org/cli.html) | "[A] simple command-line utility [...] that allows the user to manually enter and execute SQL statements against an SQLite database." | Binary |

## License

The contents of this repository is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).
