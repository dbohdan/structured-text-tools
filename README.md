# Structured text tools

The following is a list of text-based file formats and command line tools for manipulating each.


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

Awk is a POSIX-standard command line tool and programming language for processing DSV data. If you use Linux, macOS or a BSD, you almost certainly have it installed. See below for Windows.

* If you already know how to program, the nawk [man page](http://www.freebsd.org/cgi/man.cgi?query=nawk&sektion=1) is a great way to learn Awk quickly. What you learn from it will apply to other implementations on different platforms. Read it first if you feel overwhelmed by the sheer size of the [GNU Awk manual](http://www.gnu.org/software/gawk/manual/gawk.html).
* [Awk.info archive](https://web.archive.org/web/20160505033644/http://awk.info/) — an extensive resource on Awk.
* [AWK Vs NAWK Vs GAWK](http://www.thegeekstuff.com/2011/06/awk-nawk-gawk/) — a comparison of implementations' features.
* [busybox-w32](https://frippery.org/busybox/) includes a full implementation of POSIX Awk and other tools like `sed` in a single Windows executable.

### POSIX commands

| Name | Description |
|------|-------------|
| `cut` | Select portions of each line in one or several files. Can work with delimiter-separated fields. (Manual: `man 1 cut` on your system, [GNU](http://linux.die.net/man/1/cut), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=cut&sektion=1).) |
| `join` | Join the lines from two files on a common field. (Manual: `man 1 join`, [GNU](http://linux.die.net/man/1/join), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=join&sektion=1).) |
| `paste` | Combine several consecutive lines in a text file into one. (Manual: `man 1 paste`, [GNU](http://linux.die.net/man/1/paste), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=paste&sektion=1).) |
| `sort` | Sort lines by key fields. (Manual: `man 1 sort`, [GNU](http://linux.die.net/man/1/sort), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=sort&sektion=1).) |
| `uniq` | Find or remove repeated lines. (Manual: `man 1 uniq`, [GNU](http://linux.die.net/man/1/uniq), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=uniq&sektion=1).) |

### Other tools

| Name and link | Description |
|---------------|-------------|
| [GNU datamash](http://www.gnu.org/software/datamash/) | Perform statistical operations on text input. |
| [Miller](https://github.com/johnkerl/miller) | `sed`, `awk`, `cut`, `join` and `sort` for name-indexed data such as CSV and tabular JSON. |
| [rows](https://github.com/turicas/rows) | A Python library with a [CLI](http://turicas.info/rows/command-line-interface.html). Convert between a number of [file formats](http://turicas.info/rows/plugins.html) for tabular data: CSV, XLS, XLSX, ODS, and others. Query the data (via SQLite). Combine tables. Generate schemas. |
| [tab](http://tkatchev.bitbucket.io/tab/) | A non-Turing-complete statically typed programming language for data processing. An alternative to Awk. |
| [eBay's TSV utilities](https://ebay.github.io/tsv-utils-dlang/) | Filter, summarize, join, and perform other operations on TSV files. Written in D. |
| [xsv](https://github.com/BurntSushi/xsv) | Index, slice, analyze, split, and join CSV files. |

### SQL-based utilities

| Name and link | Programming language and database engine | Features | Usage link | License |
|---------------|------------------------------------------|----------|------------|---------|
| [csvkit](https://github.com/wireservice/csvkit) | Python, SQLite 3 | Use header row for column names. Custom input and output encoding. Custom input field separator. Custom output field separator. Custom output formatting. CSV JOINs. Python module. Excel and JSON to CSV. CSV to JSON. SQL queries for CSV. | [Usage](http://csvkit.readthedocs.io/en/latest/) | MIT |
| [q](https://github.com/harelba/q) | Python, SQLite 3 | Use header row for column names. Custom input and output encoding. Gzipped input. Custom input field separator (string literal). Custom output field separator. Custom output formatting. Table JOINs. Python module. | [Usage](https://github.com/harelba/q/blob/master/doc/USAGE.markdown) | GNU GPLv3 |
| [rows](https://github.com/turicas/rows) | Python, SQLite 3 | See the [Other tools](#other-tools) section. | [Usage](http://turicas.info/rows/command-line-interface.html) | GNU LGPLv3 |
| [Sqawk](https://github.com/dbohdan/sqawk) | Tcl, SQLite 3 | Use header row for column names. Custom input field separator (regexp, per-file). Custom input record delimiter (regexp, per-file). Custom output field separator. Custom output record separator. Custom table names. Merge selected columns into one. Skip columns. ASCII/Unicode table output, CSV input and output. JSON output. Keep SQLite file. Tcl input and output. Table JOINs. | [Usage](https://github.com/dbohdan/sqawk#options) | MIT |
| [sqawk](https://github.com/tjunier/sqawk) | C, SQLite 3 | Use header row for column names. Column name aliases. Can skip lines until a regexp matches. Custom input field separator (string literal, per-file). Keep SQLite file. Show generated SQL. Table JOINs. | [Usage](https://github.com/tjunier/sqawk/blob/master/sqawk.1) | ? |
| [Squawk](https://github.com/samuel/squawk) | Python, custom SQL interpreter | Access log and CSV input. JSON and CSV output. Python code generation. | — | Three-clause BSD |
| [termsql](https://github.com/tobimensch/termsql) | Python, SQLite 3 | Use header rows for column names. Custom field separator (regexp). Custom record separator (string literal). Lines as columns. Skip a given number of lines and the beginning and at the end. Merge selected columns into one. HTML, CSV, SQL, and Tcl output. | [Manual](http://tobimensch.github.io/termsql/) | MIT |A
| [trdsql](https://github.com/noborus/trdsql) | Go, MySQL/PostgreSQL/SQLite 3 | Use header row for column names. Custom field separator (string literal). Table JOINs. CSV, [LTSV](http://ltsv.org/), and JSON input. CSV, LTSV, JSON, ASCII table, Markdown output. | [Usage](https://github.com/noborus/trdsql#usage) | MIT |
| [textql](https://github.com/dinedal/textql) | Go, SQLite 3 | Use header rows for column names. Keep SQLite file. Custom input field separator (string literal). | [Usage](https://github.com/dinedal/textql#usage) | MIT |


## XML, HTML

| Name and link | Description |
|---------------|-------------|
| [pup](https://github.com/EricChiang/pup) | Query HTML pages with CSS selectors. Static binaries available for releases. Inspired by [jq](#json). |
| [Saxon](http://saxon.sourceforge.net/) | Query XML and HTML data with [XPath](http://scraping.pro/xpath-review/). [Documentation](http://www.saxonica.com/html/documentation/using-xsl/commandline.html). |
| [Temme](https://github.com/shinima/temme) | Query HTML with CSS-like selectors to extract JSON. Temme extends CSS selectors with value capture patterns. |
| [tq](https://github.com/plainas/tq) | Query HTML with CSS selectors. |
| [Xidel](http://www.videlibri.de/xidel.html) | Query or modify XML and HTML pages with XPath, XQuery 3, and CSS selectors. |
| [xml2](https://web.archive.org/web/20160719191401/http://ofb.net/~egnor/xml2/) | Convert XML and HTML to and from flat, greppable lists of "path=value" statements. [Source code mirror](https://github.com/clone/xml2). |
| [XMLStarlet](http://xmlstar.sourceforge.net/overview.php) | Query, modify, and validate XML documents. |

See also: [Grep and Sed Equivalent for XML Command Line Processing](http://stackoverflow.com/questions/91791/grep-and-sed-equivalent-for-xml-command-line-processing) on StackOverflow.


## JSON

| Name and link | Description |
|---------------|-------------|
| [fx](https://github.com/antonmedv/fx) | Run arbitrary JavaScript on JSON input. Standalone binaries available. |
| [gron](https://github.com/tomnomnom/gron) | Convert JSON to and from flat, greppable lists of "path=value" statements. |
| [jiq](https://github.com/simeji/jid) | Drill down JSON interactively by using filtering queries like jq. |
| [jl](https://github.com/chrisdone/jl) | Query and manipulate JSON using a tiny functional language. |
| [jo](https://github.com/jpmens/jo) | Create JSON objects from the shell. |
| [jp](https://github.com/jmespath/jp) | [JMESPath](http://jmespath.org/) |
| [jq](http://stedolan.github.io/jq/manual/) | Create and manipulate JSON with a functional (as in "functional programming") [DSL](https://en.wikipedia.org/wiki/Domain-specific_language). Can convert JSON to other formats. |
| [jshon](http://kmkeen.com/jshon/) | Create and manipulate JSON using [getopt](https://en.wikipedia.org/wiki/Getopt)-style command-line options. |
| [json2](https://github.com/vi/json2) | Convert JSON to and from flat, greppable lists of "path=value" statements. Modeled after [xml2](#xml-html). |
| [jsonaxe](https://github.com/davvid/jsonaxe) | Create and manipulate JSON with a Python-based DSL. Inspired by jq. |
| [json](https://github.com/trentm/json) | Run arbitrary JavaScript on JSON input. |
| [json-table](https://github.com/micha/json-table) | Convert nested JSON into CSV or TSV for processing in the shell. |
| [json.tool](https://docs.python.org/2/library/json.html) ([Python 3 docs](https://docs.python.org/3/library/json.html)) | Validate and pretty-print JSON. This module is part of the standard library of Python 2/3 and is likely to be available wherever Python is installed. |
| [jsonwatch](https://github.com/dbohdan/jsonwatch) | Track changes in JSON data from the command line. Works like `watch -d`. |
| [lobar](https://github.com/sodiumjoe/lobar) | Explore JSON interactively or process it in batch with a wrapper for `lodash.chain()`. An alternative to jq with a JavaScript syntax. |
| [rq](https://github.com/dflemstr/rq) | Create and manipulate JSON with a DSL inspired by Rust, C and JavaScript. Similar to jq. Supports JSON, YAML and TOML as well as binary formats like Apache Avro and MessagePack. |
| [validjson](http://github.com/martinlindhe/validjson) | Validate or pretty-print JSON. |


## YAML, TOML

With a format converter like Remarshal (below) you can use [JSON](#json) tools to process YAML and TOML, but make sure you do not lose data in the conversion.

| Name and link | Description |
|---------------|-------------|
| [Remarshal](https://github.com/dbohdan/remarshal) | Convert between YAML, TOML, and JSON. Validate or pretty-print each of the three formats. |
| [rq](https://github.com/dflemstr/rq) | See the [JSON section](#json). |
| [shyaml](https://github.com/0k/shyaml) | Query YAML. Can output null-terminated strings for use in shell scripts. |
| [validtoml](http://github.com/martinlindhe/validtoml) | Validate TOML. |
| [validyaml](http://github.com/martinlindhe/validyaml) | Validate or pretty-print YAML. |


## INI

| Name and link | Platform | License | Description |
|---------------|----------|---------|-------------|
| [crudini](https://github.com/pixelb/crudini/) | Any with Python 2.x | GNU GPLv2 | Set and remove properties in INI files. Retrieve properties as shell script commands to set the corresponding variables. Outputs updated INI data or changes files in place. |
| [IniFile](http://www.horstmuc.de/wbat32.htm#inifile) ([DOS version](http://www.horstmuc.de/div.htm#inifile)) | Windows (x86, x86-64), MS-DOS | Closed-source freeware | Set and remove properties in INI files. Retrieve properties as a list of batch file `set` commands to set the corresponding variables. Changes files in place. |
| [initool](https://github.com/dbohdan/initool) | Windows, Linux, FreeBSD | MIT | Set and remove properties in INI files and check for their existence. Retrieve properties' values as plain text. Outputs updated INI data. |


## Configuration files

| Name and link | Description |
|---------------|-------------|
| [Augeas](http://augeas.net) | Query and modify [a number of file formats](http://augeas.net/stock_lenses.html). Not all of the formats are equally well supported by Augeas and for some only a limited subset of all valid files can be parsed. |
| [Elektra](http://libelektra.org) | Query and modify [configuration files](https://github.com/ElektraInitiative/libelektra/tree/master/src/plugins). Shares Augeas' limitations when it comes to application-specific configuration files (it uses the same lenses), but has better support for generic formats such as JSON and INI. |


## Bonus round: CLIs for single-file databases

| Name and link | Description | File format |
|---------------|-------------|-------------|
| [Firebird](https://firebirdsql.org/) | Firebird is a FOSS database that can be used from a single file, like SQLite. "isql is a program that allows the user to issue arbitrary SQL commands". | Binary |
| [GNU Recutils](http://www.gnu.org/software/recutils/) | "[A] set of tools and libraries to access human-editable, plain text databases called recfiles." | Text-based, roughly "key: value" |
| [SDB](https://github.com/radare/sdb) | "[A] simple string key/value database based on djb's cdb disk storage and supports JSON and arrays introspection." | Binary |
| [sqlite3(1)](https://www.sqlite.org/cli.html) | "[A] simple command-line utility [...] that allows the user to manually enter and execute SQL statements against an SQLite database." | Binary |


## License

The contents of this document is licensed under the [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/). By contributing you agree to release your contribution under this license.


## Disclosure

[Sqawk](https://github.com/dbohdan/sqawk), [jsonwatch](https://github.com/dbohdan/jsonwatch), [Remarshal](https://github.com/dbohdan/remarshal) and [initool](https://github.com/dbohdan/initool) are developed by the curator of this document.
