# Structured text tools

The following is a list of text-based file formats and command line tools for manipulating each.


## Contents

* [Awk-like](#awk-like)
  * [Awk](#awk)
  * [POSIX commands](#posix-commands)
  * [SQL-based tools](#sql-based-tools)
  * [Other tools](#other-tools)
* [CSV](#csv)
* [JSON](#json)
* [XML, HTML](#xml-html)
* [YAML, TOML](#yaml-toml)
* [Configuration files](#configuration-files)
  * [/etc/hosts](#etchosts)
  * [INI](#ini)
  * [Multiple formats](#multiple-formats)
* [Log files](#log-files)
* [Templating for structured text](#templating-for-structured-text)
* [Bonus round: CLIs for single-file databases](#bonus-round-clis-for-single-file-databases)
* [License](#license)
* [Disclosure](#disclosure)


## Awk-like

Tools that work with lines of fields separated by delimiters but do not necessarily support [CSV field quoting](https://en.wikipedia.org/wiki/Comma-separated_values#Basic_rules).

### Awk

Awk is a POSIX-standard command line tool and programming language.  If you use Linux, macOS, or a BSD, you almost certainly have it installed.  See below for Windows.

* If you already know how to program, the nawk [man page](https://www.freebsd.org/cgi/man.cgi?query=nawk&sektion=1) is a great way to learn Awk quickly.  What you learn from it will apply to other implementations on different platforms.  Read it first if you feel overwhelmed by the sheer size of the [GNU Awk manual](https://www.gnu.org/software/gawk/manual/gawk.html).
* [Awk.info archive](https://web.archive.org/web/20160505033644/http://awk.info/) — an extensive resource on Awk.
* [AWK Vs NAWK Vs GAWK](https://www.thegeekstuff.com/2011/06/awk-nawk-gawk/) — a comparison of features present in different implementations.
* [busybox-w32](https://frippery.org/busybox/) includes a full implementation of POSIX Awk and other tools like `sed` in a single Windows executable.
* [GNU Awk 5 binaries for Windows](https://sourceforge.net/projects/ezwinports/files/) by [EZWinPorts](https://www.gnu.org/software/emacs/manual/html_node/efaq-w32/EZWinPorts.html).

### POSIX commands

| Name | Description |
|------|-------------|
| `comm` | Select the lines common to two sorted files or the lines contained in only one of them.  (Manual: `man 1 comm` on your system, [GNU](https://linux.die.net/man/1/comm), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=comm&sektion=1).) |
| `cut` | Select portions of each line in one or more files.  (Manual: `man 1 cut`, [GNU](https://linux.die.net/man/1/cut), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=cut&sektion=1).) |
| `grep` | Select the lines that match or do not match a pattern from one or more files.  (Manual: `man 1 grep`, [GNU](https://linux.die.net/man/1/grep), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=grep&sektion=1).) |
| `join` | Take two files sorted by a common field and join their lines on the value of that field.  Lines with values that do not appear in the other file are discarded.  (Manual: `man 1 join`, [GNU](https://linux.die.net/man/1/join), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=join&sektion=1).) |
| `paste` | Combine several consecutive lines in a text file into one.  (Manual: `man 1 paste`, [GNU](https://linux.die.net/man/1/paste), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=paste&sektion=1).) |
| `sort` | Sort lines by key fields.  (Manual: `man 1 sort`, [GNU](https://linux.die.net/man/1/sort), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=sort&sektion=1).) |
| `uniq` | Find or remove repeated lines.  (Manual: `man 1 uniq`, [GNU](https://linux.die.net/man/1/uniq), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=uniq&sektion=1).) |

### Other tools

| Name | Description |
|------|-------------|
| [csvquote](https://github.com/dbro/csvquote) | See the [CSV](#csv) section. |
| [GNU datamash](https://www.gnu.org/software/datamash/) | Perform statistical operations on text input. |
| [rq](https://github.com/dflemstr/rq) | See the [JSON section](#json). |


## CSV

CSV, TSV, and other delimiter-separated value formats.  Tools belong on this list if they support [field quoting](https://en.wikipedia.org/wiki/Comma-separated_values#Basic_rules).

| Name and link | Description |
|---------------|-------------|
| [csv-nix-tools](https://github.com/mslusarz/csv-nix-tools) | List \*nix system information such as environment variables, files, processes, network connections, users as CSV.  Manipulate and pretty-print CSV.  Execute CSV rows as commands. |
| [csv2md](https://github.com/pstaender/csv2md) | Convert CSV to Markdown tables. |
| [csv2html](https://github.com/dbohdan/csv2html) | Convert CSV to HTML tables. |
| [csvfaker](https://github.com/pereorga/csvfaker) | Generate CSV files with fake data.  Supports different types of fake data in different locales: names, cities, jobs, email addresses, and others. |
| [csvfix](https://github.com/jheusser/csvfix) (unofficial mirror) | A multitool.  Compare, filter, normalize, split, and validate CSV files.  Reorder, remove, split, and merge fields.  Convert data between fixed-width, multi-line, XML, and DSV format.  Generate SQL statements. |
| [csvkit](https://github.com/wireservice/csvkit) | csvkit is a suite of command-line tools for converting to and working with CSV: convert, clean, cut, grep, join, sort, stack, format, render, query, analyze, etc. |
| [csvquote](https://github.com/dbro/csvquote) | Transform CSV to and from a format processable with [Awk-like](#awk-like) tools. |
| [csvtk](https://github.com/shenwei356/csvtk) | Search, sample, cut, join, transpose, and sort CSV/TSV files.  Rename columns.  Replace fields and generate new fiends from existing fields.  Plot data as vector or raster histograms and box, line, and scatter plots.  Convert CSV to Markdown.  Convert XLSX to CSV.  Split XLSX sheets. |
| [dasel](https://github.com/TomWright/dasel) | See the [JSON section](#json). |
| [jp (sgreben)](https://github.com/sgreben/jp) | Plot data.  See the [JSON](#json) section. |
| [Mario](https://github.com/python-mario/mario) | See the [JSON section](#json). |
| [MCMD (M-Command)](https://github.com/nysol/mcmd) | Select, sample, cut, join, sort, reformat, and generate CSV files.  Contains a large set of commands. |
| [Miller](https://github.com/johnkerl/miller) | `sed`, `awk`, `cut`, `join` and `sort` for name-indexed data such as CSV and tabular JSON. |
| [pawk](https://github.com/alecthomas/pawk) | Process text with Awk-like patterns, but Python code. |
| [rows](https://github.com/turicas/rows) | A Python library with a [CLI](http://turicas.info/rows/cli/).  Convert between a number of [file formats](http://turicas.info/rows/plugins/) for tabular data: CSV, XLS, XLSX, ODS, and others.  Query the data (via SQLite).  Combine tables.  Generate schemas. |
| [rq](https://github.com/dflemstr/rq) | See the [JSON section](#json). |
| [tab](http://tkatchev.bitbucket.io/tab/) | A non-Turing-complete statically typed programming language for data processing.  An alternative to Awk. |
| [eBay's TSV utilities](https://github.com/eBay/tsv-utils) | Filtering, statistics, sampling, joins and other operations on TSV files.  High performance, especially good for large datasets.  Written in D. |
| [tv](https://github.com/codechenx/tv) | View delimited files in the terminal. |
| [VisiData](https://github.com/saulpw/visidata) | Explore interactively data in TSV, CSV, XLS, XLSX, HDF5, JSON, and [other formats](http://visidata.org/man/#loaders).  [Introduction](https://jsvine.github.io/intro-to-visidata/). |
| [xsv](https://github.com/BurntSushi/xsv) | Index, slice, analyze, split, and join CSV files. |

### SQL-based tools

See the [big comparison table](sql-based.md).  It covers

* AlaSQL CLI
* csvq
* csvsql
* fsql
* q
* RBQL
* rows
* Sqawk (dbohdan)
* sqawk (tjunier)
* Squawk
* termsql
* trdsql
* textql


## JSON

| Name and link | Description |
|---------------|-------------|
| [dasel](https://github.com/TomWright/dasel) | Query and update data structures from the command line.  Comparable to jq/yq but supports JSON, TOML, YAML, and XML.  Static binaries available for releases. |
| [fx](https://github.com/antonmedv/fx) | Run arbitrary JavaScript on JSON input.  Standalone binaries available. |
| [gojq](https://github.com/itchyny/gojq) | A pure Go implementation of jq (see below).  Supports YAML input and output. |
| [gron](https://github.com/tomnomnom/gron) | Convert JSON to and from flat, greppable lists of "path=value" statements. |
| [JC](https://github.com/kellyjonbrazil/jc) | Convert the output of standard command line tools to JSON. |
| [jello](https://github.com/kellyjonbrazil/jello) | Query JSON and [JSON Lines](http://jsonlines.org/) with Python code.  Output the result in a line-based format suitable for creating Bash arrays.  Generate a grep-able schema. |
| [jet](https://github.com/borkdude/jet) | Convert between and query JSON, Clojure's [edn](https://github.com/edn-format/edn), and [Transit](https://github.com/cognitect/transit-format). |
| [jfq](https://github.com/blgm/jfq) | Query and transform JSON with the [JSONata](http://jsonata.org/) language. |
| [jid](https://github.com/simeji/jid) | Explore JSON interactively with filtering queries like jq. |
| [jiq](https://github.com/fiatjaf/jiq) | Explore JSON interactively with jq.  Requires jq. |
| [jj](https://github.com/tidwall/jj) | Query and modify values in JSON or JSON Lines with a key path. |
| [jl](https://github.com/chrisdone/jl) | Query and manipulate JSON using a tiny functional language. |
| [jo](https://github.com/jpmens/jo) | Create JSON objects from the shell. |
| [jp (jmespath)](https://github.com/jmespath/jp) | Query JSON with [JMESPath](http://jmespath.org/). |
| [jp (sgreben)](https://github.com/sgreben/jp) | Plot JSON and CSV data in the terminal.  Supports different kinds of plots: bar charts, line charts, scatter plots, histograms, and heatmaps. |
| [jplot](https://github.com/rs/jplot) | Plot real-time JSON data in the terminal (works with terminals supporting graphic rendering). |
| [jq](http://stedolan.github.io/jq/manual/) | Create and manipulate JSON with a functional (as in "functional programming") [DSL](https://en.wikipedia.org/wiki/Domain-specific_language).  Can convert JSON to other formats. |
| [jql](https://github.com/cube2222/jql) | Create and manipulate JSON with a Lisp-syntax DSL. |
| [jtbl](https://github.com/kellyjonbrazil/jtbl) | Format JSON or JSON Lines as a plain-text table. |
| [jtc](https://github.com/ldn-softdev/jtc) | Create, manipulate, search, validate JSON with path expressions.  Can be used as a C++14 library. |
| [emuto](http://kantord.github.io/emuto/) | CLI tool similar to jq.  Create and manipulate JSON and other files.  Can be compiled to JavaScript. |
| [jshon](http://kmkeen.com/jshon/) | Create and manipulate JSON using [getopt](https://en.wikipedia.org/wiki/Getopt)-style command-line options. |
| [json2](https://github.com/vi/json2) | Convert JSON to and from flat, greppable lists of "path=value" statements.  Modeled after [xml2](#xml-html). |
| [jsonaxe](https://github.com/davvid/jsonaxe) | Create and manipulate JSON with a Python-based DSL.  Inspired by jq. |
| [json](https://github.com/trentm/json) | Run arbitrary JavaScript on JSON input. |
| [json-table](https://github.com/micha/json-table) | Convert nested JSON into CSV or TSV for processing in the shell. |
| [json.tool](https://docs.python.org/2/library/json.html) ([Python 3 docs](https://docs.python.org/3/library/json.html)) | Validate and pretty-print JSON.  This module is part of the standard library of Python 2/3 and is likely to be available wherever Python is installed. |
| [jsonwatch](https://github.com/dbohdan/jsonwatch) | Track changes in JSON data from the command line.  Works like `watch -d`. |
| [lobar](https://github.com/sodiumjoe/lobar) | Explore JSON interactively or process it in batch with a wrapper for `lodash.chain()`.  An alternative to jq with a JavaScript syntax. |
| [Mario](https://github.com/python-mario/mario) | Manipulate and convert between CSV, JSON, YAML, TOML, and XML with Python code. |
| [qpyson](https://github.com/mpkocher/qpyson) | Query and manipulate JSON with Python. |
| [query-json](https://github.com/davesnx/query-json) | A faster jq implementation written in Reason Native (OCaml). |
| [quicktype](https://github.com/quicktype/quicktype) | Infer the underlying model of the JSON and output as types for various programming languages or JSON Schema.  CLI and [Web UI](https://app.quicktype.io). |
| [ramda-cli](https://github.com/raine/ramda-cli) | Manipulate JSON with the [Ramda](https://ramdajs.com/) functional library, and either LiveScript or JavaScript syntax. |
| [RecordStream](https://github.com/benbernard/RecordStream) | Create, manipulate, and output a stream of records, or JSON objects.  Can retrieve records from an SQL database, MongoDB, Atom feeds, XML, and other sources. |
| [rq](https://github.com/dflemstr/rq) | Convert between Apache Avro, CBOR, CSV, JSON, MessagePack, Protocol Buffers, TOML, YAML, and Awk-style plain text. |
| [validjson](http://github.com/martinlindhe/validjson) | Validate or pretty-print JSON. |
| [VisiData](https://github.com/saulpw/visidata) | Explore data interactively data.  See the [DSV/Other tools](#other-tools) section. |


## XML, HTML

| Name and link | Description |
|---------------|-------------|
| [dasel](https://github.com/TomWright/dasel) | Supports XML.  See the [JSON section](#json). |
| [hred](https://github.com/danburzo/hred) | Query XML and HTML with a query language based on CSS selectors. |
| [html-xml-utils](https://www.w3.org/Tools/HTML-XML-utils/README) | A number of simple utilities (like `hxcopy`, `hxpipe`, `hxunent`, `hxselect`) for manipulating HTML and XML files from [W3C](https://www.w3.org/).  Written in C, quite old-fashioned, but still relevant and maintained. |
| [Mario](https://github.com/python-mario/mario) | Supports XML.  See the [JSON section](#json). |
| [pup](https://github.com/EricChiang/pup) | Query HTML pages with CSS selectors.  Static binaries available for releases.  Inspired by [jq](#json). |
| [Saxon](http://saxon.sourceforge.net/) | Query XML and HTML data with [XPath](https://devhints.io/xpath).  [Documentation](http://www.saxonica.com/documentation/#!using-xsl). |
| [sml2](https://github.com/JFLarvoire/libxml2) | Convert between XML and [SML](https://htmlpreview.github.io/?https://github.com/JFLarvoire/libxml2/blob/master/SML_presentation.htm), a simplified XML representation. |
| [Temme](https://github.com/shinima/temme) | Query HTML with CSS-like selectors to extract JSON.  Temme extends CSS selectors with value capture patterns. |
| [tidy-html5](http://www.html-tidy.org/) | Validate, fix, and reformat HTML(5), XHTML, and XML documents.  Convert HTML to XHTML. |
| [tq](https://github.com/plainas/tq) | Query HTML with CSS selectors. |
| [Xidel](http://www.videlibri.de/xidel.html) | Query or modify XML and HTML pages with XPath, XQuery 3, and CSS selectors. |
| [xml-to-json-fast](https://github.com/sinelaw/xml-to-json-fast) | Convert XML to JSON.  Can handle very large XML files. |
| [xml2](https://web.archive.org/web/20160719191401/http://ofb.net/~egnor/xml2/) | Convert XML and HTML to and from flat, greppable lists of "path=value" statements.  [Source code mirror](https://github.com/clone/xml2). |
| [xmljson](https://github.com/engali94/XMLJson) | Convert multiple and large XML files to JSON.  Written in Swift. |
| [XMLLint](http://xmlsoft.org/xmllint.html) | Query (including XSLT), validate and reformat XML documents. |
| [XMLStarlet](http://xmlstar.sourceforge.net/overview.php) | Query, modify, and validate XML documents. |
| [xq](https://github.com/kislyuk/yq) | [jq](#json) wrapper for XML documents. |
| [xsltproc](http://xmlsoft.org/XSLT/xsltproc2.html) | Transform XML documents using [XSLT](https://www.w3.org/TR/xslt) and [EXSLT](http://exslt.org). |

### See also

*  [Grep and Sed Equivalent for XML Command Line Processing](http://stackoverflow.com/questions/91791/grep-and-sed-equivalent-for-xml-command-line-processing) on StackOverflow.


## YAML, TOML

With a format converter like Remarshal (below) you can use [JSON](#json) tools to process YAML and TOML, but make sure you do not lose data in the conversion.

| Name and link | Description |
|---------------|-------------|
| [dasel](https://github.com/TomWright/dasel) | Supports TOML and YAML.  See the [JSON section](#json). |
| [gojq](https://github.com/itchyny/gojq) | Supports YAML.  See the [JSON section](#json). |
| [Mario](https://github.com/python-mario/mario) | Supports YAML.  See the [JSON section](#json). |
| [Remarshal](https://github.com/dbohdan/remarshal) | Convert between CBOR, JSON, MessagePack, TOML, and YAML.  Validate each of the formats.  Pretty-print JSON, TOML, and YAML. |
| [rq](https://github.com/dflemstr/rq) | Supports TOML and YAML.  See the [JSON section](#json). |
| [shyaml](https://github.com/0k/shyaml) | Query YAML.  Can output null-terminated strings for use in shell scripts. |
| [validtoml](http://github.com/martinlindhe/validtoml) | Validate TOML. |
| [validyaml](http://github.com/martinlindhe/validyaml) | Validate or pretty-print YAML. |
| [yaml-tools](https://github.com/thecodingmachine/yaml-tools) | A set of CLI tools to manipulate YAML files (merge, delete, etc...) with comment preservation, based on [ruamel.yaml](http://yaml.readthedocs.io/en/latest/). |
| [yq (kislyuk)](https://github.com/kislyuk/yq) | [jq](#json) wrapper for YAML. |
| [yq (mikefarah)](https://github.com/mikefarah/yq) | Query, modify, and merge YAML.  Convert to and from JSON. |


## Configuration files

### /etc/hosts

| Name and link | Description |
|---------------|-------------|
| [hostctl](https://github.com/guumaster/hostctl) | Add and remove entires in `/etc/hosts`.  Disable (comment out) and enable (uncomment) entires.  Not idempotent.  Preserves arbitrary comments above its section of the hosts file.  Works with groups of entries called "profiles". |
| [hostess](https://github.com/cbednarski/hostess) | Add and remove entires in `/etc/hosts`.  Disable (comment out) and enable (uncomment) entires.  Check if a hostname exists.  Reformat the hosts file.  Convert the entries to JSON.  Idempotent.  Removes arbitrary comments. |
| [hosts](https://gitlab.com/dbohdan/hosts) | Add and remove entires in `/etc/hosts`.  Change a hostname's IP address.  Idempotent.  Preserves arbitrary comments.  Can be used as a Tcl library. |

## INI

| Name and link | Platform | License | Description |
|---------------|----------|---------|-------------|
| [cfget](https://packages.debian.org/unstable/cfget) | Any with Python 2.x? | GNU GPLv2+ | Retrieve properties as shell script commands to set the corresponding variables (with `--dump exports`).  Retrieve properties' values as plain text.  Substitute values from an INI file in an Autoconf-style template.  Supports plug-ins.  Chokes on section names and keys with spaces. |
| [confget](https://devel.ringlet.net/textproc/confget/) | Linux, FreeBSD | Two-clause BSD | Retrieve properties and sections as shell script commands to set the corresponding variables.  Retrieve properties' values as plain text.  Check for existence of properties.  List sections.  Find values that match a pattern.  Read-only. |
| [crudini](https://github.com/pixelb/crudini/) | Any with Python 2.x | GNU GPLv2 | Retrieve properties and sections as INI fragments or shell script commands to set the corresponding variables.  Retrieve properties' values as plain text.  Set properties.  Remove properties and sections.  Create empty sections.  Merge INI files.  Changes files in place. |
| [inicomp](https://github.com/JFLarvoire/SysToolsLib/blob/HEAD/C/SRC/inicomp.c) | Windows, \*nix | Apache 2.0 | Compare INI (and also Windows .reg) files. |
| [IniFile](http://www.horstmuc.de/wbat32.htm#inifile) ([DOS version](http://www.horstmuc.de/div.htm#inifile)) | Windows (x86, x86-64), MS-DOS | Closed-source freeware | Retrieve properties and sections as batch file commands to set the corresponding variables.  Set properties.  Remove properties and sections.  Changes files in place. |
| [initool](https://github.com/dbohdan/initool) | Linux, FreeBSD, Windows | MIT | Retrieve properties and sections as INI fragments.  Retrieve properties' values as plain text.  Set properties.  Check for existence of properties and sections.  Remove properties and sections.  Outputs the updated INI file. |

### Multiple formats

| Name and link | Description |
|---------------|-------------|
| [Augeas](http://augeas.net) | Query and modify [a number of file formats](http://augeas.net/stock_lenses.html).  Not all of the formats are equally well supported by Augeas and for some only a limited subset of all valid files can be parsed. |
| [Elektra](http://libelektra.org) | Query and modify [configuration files](https://github.com/ElektraInitiative/libelektra/tree/master/src/plugins).  Shares Augeas' limitations when it comes to application-specific configuration files (it uses the same lenses), but has better support for generic formats such as JSON and INI. |


## Log files

| Name and link | Description |
|---------------|-------------|
| [Squawk](https://github.com/samuel/squawk) | Query Apache and Nginx log files.  See the [SQL-based tool comparison](sql-based.md). |
| [lnav](https://lnav.org) | Query and watch log files.  Has batch and interactive mode.  Supported formats include the Common Log Format, CUPS page_log, syslog, strace, and generic timestamped messages.  Can perform SQL queries. |


## Templating for structured text

Listed below are restricted programming language interpreters and templating tools that produce structured text output.  They are generally intended to remove repetition in configuration files.  They are distinct from unstructed templating tools like the `jinja2` CLI program, which should not be added to this table.

| Name and link | Output format | Turing-complete? | Syntax | I/O | Description |
|---------------|---------------|------------------|--------|-----|-------------|
| [CUE](https://github.com/cuelang/cue) | JSON | Yes? | Extended JSON | ? | A constraint language for JSON configuration data.  Can generate and validates JSON. |
| [Dhall](https://dhall-lang.org/) | JSON, YAML | No | Haskell-inspired | Limited to importing libraries from files and HTTP(S) URLs (with protection against leaking your data to the server) | A statically-typed functional configuration language.  Has a standard formatting tool. |
| [jk](https://github.com/jkcfg/jk) | JSON, YAML, plain text | Yes | JavaScript | Disk I/O | Generate configuration files using JavaScript (V8 VM). |
| [Jsonnet](https://jsonnet.org/) | JSON, INI, XML, YAML, plain text | Yes | Extended JSON | None | A functional configuration language.  Has a standard formatting tool. |
| [rjsone](https://github.com/wryun/rjsone) | JSON, YAML | No? | Extended JSON | None | A CLI tool for the [JSON-e](https://github.com/taskcluster/json-e) templating language. |
| [ytt](https://get-ytt.io/) | YAML | No | YAML/Python hybrid | None? | A templating tool for YAML built upon the [Starlark](https://github.com/bazelbuild/starlark) configuration language. |


## Bonus round: CLIs for single-file databases

| Name and link | Description | File format |
|---------------|-------------|-------------|
| [Firebird](https://firebirdsql.org/) | Firebird is a FOSS database that can be used from a single file, like SQLite.  "isql is a program that allows the user to issue arbitrary SQL commands". | Binary |
| [Fsdb](https://www.isi.edu/~johnh/SOFTWARE/FSDB/perl-Fsdb-2.69_README.html) | A flat-file database for shell scripting. | Text-based, TSV with a header or "key: value" |
| [GNU Recutils](http://www.gnu.org/software/recutils/) | "[A] set of tools and libraries to access human-editable, plain text databases called recfiles." | Text-based, roughly "key: value" |
| [SDB](https://github.com/radare/sdb) | "[A] simple string key/value database based on djb's cdb disk storage and supports JSON and arrays introspection." | Binary |
| [sqlite3(1)](https://www.sqlite.org/cli.html) | "[A] simple command-line utility [...] that allows the user to manually enter and execute SQL statements against an SQLite database." | Binary |


## License

The contents of this document is licensed under the [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).  By contributing you agree to release your contribution under this license.


## Disclosure

[csv2html](https://github.com/dbohdan/csv2html), [hosts](https://gitlab.com/dbohdan/hosts), [Sqawk](https://github.com/dbohdan/sqawk), [jsonwatch](https://github.com/dbohdan/jsonwatch), [Remarshal](https://github.com/dbohdan/remarshal) and [initool](https://github.com/dbohdan/initool) are developed by the curator of this document.
