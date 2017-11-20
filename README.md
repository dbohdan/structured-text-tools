# Structured text tools

What follows is a list of text-based file formats with command line tools for manipulating each (with a focus on Linux).

## Contents

* [DSV](#dsv)
* [XML, HTML](#xml-html)
* [JSON](#json)
* [YAML, TOML](#yaml-toml)
* [INI](#ini)
* [Configuration files](#configuration-files)
* [Bonus round: CLIs for single-file databases](#bonus-round-clis-for-single-file-databases)
* [License](#license)
* [Disclosure](#disclosure)

## DSV

[Delimiter-separated values](https://en.wikipedia.org/wiki/Delimiter-separated_values), including [CSV](https://en.wikipedia.org/wiki/Comma-separated_values), [TSV](https://en.wikipedia.org/wiki/Tab-separated_values), etc.

### Awk

Awk is a POSIX-standard command line tool and programming language for processing DSV data. A list of Awk links follows.

* [Awk.info](https://web.archive.org/web/20160505033644/http://awk.info/) — an extensive resource on Awk.
* [AWK Vs NAWK Vs GAWK](http://www.thegeekstuff.com/2011/06/awk-nawk-gawk/) — a comparison of implementations.
* If you already know how to program in some language, the nawk [man page](http://www.freebsd.org/cgi/man.cgi?query=nawk&sektion=1) is a great way to learn Awk quickly. What you learn from it will apply to other implementations on different platforms. Read it first if you feel overwhelmed by the sheer size of the [GNU Awk manual](http://www.gnu.org/software/gawk/manual/gawk.html).

### POSIX commands

| Name | Description |
|------|-------------|
| `cut` | Select portions of each line in a file or several. Can work with delimiter-separated fields. See `man 1 cut` on your system ([GNU](http://linux.die.net/man/1/cut), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=cut&sektion=1)). |
| `join` | Join the lines of two files on a common field. See `man 1 join` on your system ([GNU](http://linux.die.net/man/1/join), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=join&sektion=1)). |
| `paste` | Combine consecutive lines in a text file into one. See `man 1 paste` on your system ([GNU](http://linux.die.net/man/1/paste), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=paste&sektion=1)). |
| `sort` | Sort lines by key fields. See `man 1 sort` on your system ([GNU](http://linux.die.net/man/1/sort), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=sort&sektion=1)). |
| `uniq` | Find or remove repeated lines. See `man 1 uniq` on your system ([GNU](http://linux.die.net/man/1/uniq), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=uniq&sektion=1)). |

### Other tools

| Name and link | Description |
|---------------|-------------|
| [GNU datamash](http://www.gnu.org/software/datamash/) | Perform statistical operations on text input. |
| [Miller](https://github.com/johnkerl/miller) | `sed`, `awk`, `cut`, `join` and `sort` for name-indexed data such as CSV and tabular JSON. |
| [rows](https://github.com/turicas/rows) | A Python library with a [CLI](http://turicas.info/rows/command-line-interface.html). Convert between a number of [file formats](http://turicas.info/rows/plugins.html) for tabular data: CSV, XLS, XLSX, ODS, and others. Query the data (via SQLite). Combine tables. Generate schemas. |
| [tab](http://tkatchev.bitbucket.io/tab/) | A non-Turing-complete programming language for data processing. An alternative to Awk. |
| [eBay's TSV utilities](https://ebay.github.io/tsv-utils-dlang/) | Filter, summarize, join, and other data manipulation operations on TSV files. Written in D. |
| [xsv](https://github.com/BurntSushi/xsv) | Index, slice, analyze, split and join CSV files. |

### SQL-based utilities

| Name and link | Programming language and database engine | Features | Usage link | License |
|---------------|------------------------------------------|----------|------------|---------|
| [csvkit](https://github.com/wireservice/csvkit) | Python, SQLite 3 | Use header row for column names. Custom input and output encoding. Custom input field separator. Custom output field separator. Custom output formatting. CSV JOINs. Python module. Excel and JSON to CSV. CSV to JSON. SQL queries for CSV. | [Usage](http://csvkit.readthedocs.io/en/latest/) | MIT |
| [q](https://github.com/harelba/q) | Python, SQLite 3 | Use header row for column names. Custom input and output encoding. Gzipped input. Custom input field separator (string literal). Custom output field separator. Custom output formatting. Table JOINs. Python module. | [Usage](https://github.com/harelba/q/blob/master/doc/USAGE.markdown) | GNU GPL 3 |
| [rows](https://github.com/turicas/rows) | Python, SQLite 3 | See the [Other tools](#other-tools) section. | [Usage](http://turicas.info/rows/command-line-interface.html) | GNU LGPL 3.0 |
| [Sqawk](https://github.com/dbohdan/sqawk) | Tcl, SQLite 3 | Use header row for column names. Custom input field separator (regexp, per-file). Custom input record delimiter (regexp, per-file). Custom output field separator. Custom output record separator. Custom table names. Merge selected columns into one. Skip columns. ASCII/Unicode table output, CSV input and output. JSON output. Keep SQLite file. Tcl input and output. Table JOINs. | [Usage](https://github.com/dbohdan/sqawk#options) | MIT |
| [sqawk](https://github.com/tjunier/sqawk) | C, SQLite 3 | Use header row for column names. Column name aliases. Can skip lines until a regexp matches. Custom input field separator (string literal, per-file). Keep SQLite file. Show generated SQL. Table JOINs. | [Usage](https://github.com/tjunier/sqawk/blob/master/sqawk.1) | ? |
| [Squawk](https://github.com/samuel/squawk) | Python, custom SQL interpreter | Access log and CSV input. JSON and CSV output. Python code generation. | — | Three-clause BSD |
| [termsql](https://github.com/tobimensch/termsql) | Python, SQLite 3 | Use header rows for column names. Custom field separator (regexp). Custom record separator (string literal). Lines as columns. Skip a given number of lines and the beginning and at the end. Merge selected columns into one. HTML, CSV, SQL, and Tcl output. | [Manual](http://tobimensch.github.io/termsql/) | MIT |
| [textql](https://github.com/dinedal/textql) | Go, SQLite 3 | Use header rows for column names. Keep SQLite file. Custom input field separator (string literal). | [Usage](https://github.com/dinedal/textql#usage) | MIT |

## XML, HTML

| Name and link | Description |
|---------------|-------------|
| [pup](https://github.com/EricChiang/pup) | Filter HTML pages using CSS selectors. Inspired by [jq](#json). |
| [Saxon](http://saxon.sourceforge.net/) | Scrape XML and HTML data using [XPath](http://scraping.pro/xpath-review/). [Documentation](http://www.saxonica.com/html/documentation/using-xsl/commandline.html). |
| [tq](https://github.com/plainas/tq) | Retrieve content from HTML using CSS selectors. |
| [Xidel](http://www.videlibri.de/xidel.html) | Scrape or transform XML and HTML pages with XPath, XQuery 3 and CSS selectors. |
| [xml2](https://web.archive.org/web/20160719191401/http://ofb.net/~egnor/xml2/) | Convert XML and HTML to and from flat, greppable lists of "path=value" statements. [Source code mirror](http://pkgs.fedoraproject.org/repo/pkgs/xml2/xml2-0.5.tar.gz/48eacf64b01ca3a4a5afb1a36f5906e6/). |
| [XMLStarlet](http://xmlstar.sourceforge.net/overview.php) | Transform, query, validate and edit XML documents. |

See also: [Grep and Sed Equivalent for XML Command Line Processing](http://stackoverflow.com/questions/91791/grep-and-sed-equivalent-for-xml-command-line-processing) on StackOverflow.

## JSON

| Name and link | Description |
|---------------|-------------|
| [gron](https://github.com/tomnomnom/gron) | Convert JSON to and from flat, greppable lists of "path=value" statements. |
| [jo](https://github.com/jpmens/jo) | Create JSON objects from the shell. |
| [jq](http://stedolan.github.io/jq/manual/) | Create and manipulate JSON with a functional (as in "functional programming") [DSL](https://en.wikipedia.org/wiki/Domain-specific_language). Can convert JSON to other formats. |
| [jshon](http://kmkeen.com/jshon/) | Create and manipulate JSON using [getopt](https://en.wikipedia.org/wiki/Getopt)-style command-line options. |
| [json2](https://github.com/vi/json2) | Convert JSON to and from flat, greppable lists of "path=value" statements. Modeled after [xml2](#xml-html). |
| [jsonaxe](https://github.com/davvid/jsonaxe) | A JSON processor similar to jq with a Python-based DSL. |
| [json](https://github.com/trentm/json) | Similar to jq but written in JavaScript. Can run arbitrary JavaScript on the JSON input. |
| [json-table](https://github.com/micha/json-table) | Transform JSON data structures into tables of columns and rows for processing in the shell. |
| [json.tool](https://docs.python.org/2/library/json.html) ([Python 3 docs](https://docs.python.org/3/library/json.html)) | Validate and pretty-print JSON data. This module is part of the standard library of Python 2/3 and so is likely available wherever Python is installed. |
| [jsonwatch](https://github.com/dbohdan/jsonwatch) | Track changes in JSON data live from the command line. Works like `watch -d`. |
| [lobar](https://github.com/sodiumjoe/lobar) | Explore JSON interactively or process it in batch with a wrapper for `lodash.chain()`. An alternative to jq with a JavaScript syntax. |
| [rq](https://github.com/dflemstr/rq) | Similar to jq. DSL inspired by Rust, C and JavaScript. Supports JSON, YAML and TOML as well as binary formats like Apache Avro and MessagePack. |
| [validjson](http://github.com/martinlindhe/validjson) | Validate or pretty-print JSON data. |

## YAML, TOML

With a format converter like Remarshal (below) you can use [JSON](#json) tools to process YAML and TOML but beware that you don't lose data in the conversion ([example](https://github.com/dbohdan/remarshal/issues/2)).

| Name and link | Description |
|---------------|-------------|
| [Remarshal](https://github.com/dbohdan/remarshal) | Convert between YAML, TOML and JSON. Validate or pretty-print each of the three formats. |
| [rq](https://github.com/dflemstr/rq) | See the [JSON section](#json). |
| [shyaml](https://github.com/0k/shyaml) | Read data from YAML files. Can output null-terminated strings for use in shell scripts. |
| [validtoml](http://github.com/martinlindhe/validtoml) | Validate TOML data. |
| [validyaml](http://github.com/martinlindhe/validyaml) | Validate or pretty-print YAML data. |

## INI

| Name and link | Platform | License | Description |
|---------------|----------|---------|-------------|
| [crudini](https://github.com/pixelb/crudini/) | Any with Python 2.x | GNU GPLv2 | Set and remove properties in INI files. Retrieve properties as shell script commands to set the corresponding variables. Outputs updated INI data or changes files in place. |
| [IniFile](http://www.horstmuc.de/wbat32.htm#inifile) ([DOS version](http://www.horstmuc.de/div.htm#inifile)) | Windows (x86, x86-64), MS-DOS | Closed-source freeware | Set and remove properties in INI files. Retrieve properties as a list of batch file `set` commands to set the corresponding variables. Changes files in place. |
| [initool](https://github.com/dbohdan/initool) | Windows, Linux, FreeBSD | MIT | Set and remove properties in INI files and check for their existence. Outputs updated INI data. |

## Configuration files

| Name and link | Description |
|---------------|-------------|
| [Augeas](http://augeas.net) | Extract data from and modify [a number of file formats](http://augeas.net/stock_lenses.html). Note that not all formats are equally well supported by Augeas and for some only a limited subset of all valid files can be parsed. |
| [Elektra](http://libelektra.org) | Manipulate [configuration files](https://github.com/ElektraInitiative/libelektra/tree/master/src/plugins). Shares Augeas' limitations when it comes to application-specific configuration files (it uses the same lenses) but has better support for generic formats such as JSON or INI. |

## Bonus round: CLIs for single-file databases

| Name and link | Description | File format |
|---------------|-------------|-------------|
| [GNU Recutils](http://www.gnu.org/software/recutils/) | "[A] set of tools and libraries to access human-editable, plain text databases called recfiles." | Text-based, roughly "key: value" |
| [SDB](https://github.com/radare/sdb) | "[A] simple string key/value database based on djb's cdb disk storage and supports JSON and arrays introspection." | Binary |
| [sqlite3(1)](https://www.sqlite.org/cli.html) | "[A] simple command-line utility [...] that allows the user to manually enter and execute SQL statements against an SQLite database." | Binary |

## License

The contents of this document is licensed under the [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/). By contributing you agree to release your contribution under this license.

## Disclosure

[Sqawk](https://github.com/dbohdan/sqawk), [jsonwatch](https://github.com/dbohdan/jsonwatch), [Remarshal](https://github.com/dbohdan/remarshal) and [initool](https://github.com/dbohdan/initool) were written by the curator of this document.
