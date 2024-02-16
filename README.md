# Structured text tools

The following is a list of text-based file formats and command-line tools for manipulating each.


## Contents

- [awk-like](#awk-like)
  - [awk](#awk)
  - [POSIX commands](#posix-commands)
  - [SQL-based tools](#sql-based-tools)
  - [Other tools](#other-tools)
- [CSV](#csv)
- [HTML](#html)
- [JSON](#json)
- [TOML](#toml)
- [XML](#xml)
- [YAML](#yaml)
- [Configuration files](#configuration-files)
  - [/etc/hosts](#etchosts)
  - [INI](#ini)
  - [Multiple formats](#multiple-formats)
- [Log files](#log-files)
- [Templating for structured text](#templating-for-structured-text)
- [Extra: interactive TUIs](#extra-interactive-tuis)
- [Extra: CLIs for single-file databases](#extra-clis-for-single-file-databases)
- [License](#license)
- [Disclosure](#disclosure)


## awk-like

Tools that work with lines of fields separated by delimiters but do not necessarily support [CSV field quoting](https://en.wikipedia.org/wiki/Comma-separated_values#Basic_rules).

### awk

AWK/awk is a programming language and a POSIX-standard command-line tool. (You will sometimes see "awk" used for the tool and "AWK" for the language. This document follows this convention. GNU Awk uses "Awk".) If you run Linux, macOS, or a BSD, you almost certainly have it installed. See below for Windows.

- If you already know how to program, the nawk [man page](https://www.freebsd.org/cgi/man.cgi?query=nawk&sektion=1) is a great way to learn AWK quickly. What you learn from it will apply to other implementations on different platforms. Read it first if you feel overwhelmed by the sheer size of the [GNU Awk manual](https://www.gnu.org/software/gawk/manual/gawk.html).
- [awk.info archive](https://web.archive.org/web/20160505033644/http://awk.info/) **—** an extensive resource on Awk.
- ["AWK Vs NAWK Vs GAWK"](https://www.thegeekstuff.com/2011/06/awk-nawk-gawk/) **—** a comparison of features present in different implementations.
- [busybox-w32](https://frippery.org/busybox/) includes a full implementation of POSIX awk and other tools like `sed` in a single Windows executable.
- [frawk](https://github.com/ezrosent/frawk) is a Rust implementation of a language partially compatible with AWK that supports [parallelism](https://github.com/ezrosent/frawk/blob/master/info/parallelism.md) and CSV input and output.
- [GNU Awk 5 binaries for Windows](https://sourceforge.net/projects/ezwinports/files/) by [EZWinPorts](https://www.gnu.org/software/emacs/manual/html_node/efaq-w32/EZWinPorts.html).
- [GoAWK](https://github.com/benhoyt/goawk) is a cross-platform implementation of awk with added support for CSV. The project provides binaries for many platforms, including Windows.

### POSIX commands

- `comm` **—** Select the lines common to two sorted files or the lines contained in only one of them. (Manual: `man 1 comm` on your system, [GNU](https://linux.die.net/man/1/comm), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=comm&sektion=1).)
- `cut` **—** Select portions of each line in one or more files. (Manual: `man 1 cut`, [GNU](https://linux.die.net/man/1/cut), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=cut&sektion=1).)
- `grep` **—** Select the lines that match or do not match a pattern from one or more files. (Manual: `man 1 grep`, [GNU](https://linux.die.net/man/1/grep), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=grep&sektion=1).)
- `join` **—** Take two files sorted by a common field and join their lines on the value of that field. Lines with values that do not appear in the other file are discarded. (Manual: `man 1 join`, [GNU](https://linux.die.net/man/1/join), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=join&sektion=1).)
- `paste` **—** Combine several consecutive lines in a text file into one. (Manual: `man 1 paste`, [GNU](https://linux.die.net/man/1/paste), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=paste&sektion=1).)
- `sort` **—** Sort lines by key fields. (Manual: `man 1 sort`, [GNU](https://linux.die.net/man/1/sort), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=sort&sektion=1).)
- `uniq` **—** Find or remove repeated lines. (Manual: `man 1 uniq`, [GNU](https://linux.die.net/man/1/uniq), [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=uniq&sektion=1).)

### Other tools

- [csvquote](https://github.com/dbro/csvquote) **—** Transform CSV to and from a format processable with [awk-like](#awk-like) tools.
- [GNU datamash](https://www.gnu.org/software/datamash/) **—** Perform statistical operations on text input.
- [Hawk](https://github.com/gelisam/hawk) **—** Transform text from the command-line using Haskell expressions.
- [pyp](https://github.com/hauntsaninja/pyp) **—** Transform input (as text lines or as a whole) using Python code with automatic module imports. Can generate a Python script equivalent to its invocation. In Python 3.11 or later supports TOML through [tomllib](https://docs.python.org/3.11/library/tomllib.html).
- [rq](https://github.com/dflemstr/rq) **—** Convert between Apache Avro, CBOR, CSV, JSON, MessagePack, Protocol Buffers, TOML, YAML, and awk-style plain text.
- [vnlog](https://github.com/dkogan/vnlog/) **—** Process labelled tabular ASCII data using normal UNIX tools. Can plot data with gnuplot.


## CSV

CSV, TSV, and other delimiter-separated value formats. Tools belong on this list if they support [field quoting](https://en.wikipedia.org/wiki/Comma-separated_values#Basic_rules).

- [csv-nix-tools](https://github.com/mslusarz/csv-nix-tools) **—** List \*nix system information such as environment variables, files, processes, network connections, users as CSV. Manipulate and pretty-print CSV. Execute CSV rows as commands.
- [csv2html](https://github.com/dbohdan/csv2html) **—** Convert CSV to HTML tables.
- [csv2md](https://github.com/pstaender/csv2md) **—** Convert CSV to Markdown tables.
- [csvfaker](https://github.com/pereorga/csvfaker) **—** Generate CSV files with fake data. Supports different types of fake data in different locales: names, cities, jobs, email addresses, and others.
- [csvfix](https://github.com/jheusser/csvfix) **—** A multitool. Compare, filter, normalize, split, and validate CSV files. Reorder, remove, split, and merge fields. Convert data between fixed-width, multi-line, XML, and DSV format. Generate SQL statements. (Unofficial mirror.)
- [csvkit](https://github.com/wireservice/csvkit) **—** csvkit is a suite of command-line tools for converting to and working with CSV: convert, clean, cut, grep, join, sort, stack, format, render, query, analyze, etc.
- [csvquote](https://github.com/dbro/csvquote) **—** Transform CSV to and from a format processable with [awk-like](#awk-like) tools.
- [csvtk](https://github.com/shenwei356/csvtk) **—** Search, sample, cut, join, transpose, and sort CSV/TSV files. Rename columns. Replace fields and generate new fiends from existing fields. Plot data as vector or raster histograms and box, line, and scatter plots. Convert CSV to Markdown. Convert XLSX to CSV. Split XLSX sheets.
- [CSVtoTable](https://github.com/vividvilla/csvtotable) **—** Convert CSV to a searchable and sortable HTML table.
- [dasel](https://github.com/TomWright/dasel) **—** Query and update data structures from the command line. Comparable to jq/yq but supports CSV, JSON, TOML, YAML, and XML. Static binaries available for releases.
- [eBay's TSV utilities](https://github.com/eBay/tsv-utils) **—** Filtering, statistics, sampling, joins and other operations on TSV files. High performance, especially good for large datasets. Written in D.
- [frawk](https://github.com/ezrosent/frawk) **—** a Rust implementation of a language partially compatible with AWK that supports [parallelism](https://github.com/ezrosent/frawk/blob/master/info/parallelism.md) and CSV input and output. frawk is an awk-derived language with a CSV mode for input and for output.
- [GoAWK](https://github.com/benhoyt/goawk) **—** a cross-platform implementation of awk with added support for CSV. The project provides binaries for many platforms, including Windows. GoAWK is an awk implementation that adds a CSV mode for input and for output.
- [Graphtage](https://github.com/trailofbits/graphtage) **—** Compare and merge tree-like structures semantically. Supports JSON, JSON5, XML, HTML, YAML, and CSV. Can be used as a Python library.
- [jp (sgreben)](https://github.com/sgreben/jp) **—** Plot JSON and CSV data in the terminal. Supports different kinds of plots: bar charts, line charts, scatter plots, histograms, and heatmaps.
- [Mario](https://github.com/python-mario/mario) **—** Manipulate and convert between CSV, JSON, YAML, TOML, and XML with Python code.
- [MCMD (M-Command)](https://github.com/nysol/mcmd) **—** Select, sample, cut, join, sort, reformat, and generate CSV files. Contains a large set of commands.
- [Miller](https://github.com/johnkerl/miller) **—** `sed`, `awk`, `cut`, `join` and `sort` for name-indexed data such as CSV and tabular JSON.
- [Nushell](https://github.com/nushell/nushell) **—** A command shell. Can natively [load data](https://www.nushell.sh/book/loading_data.html) from CSV, INI, JSON, TOML, TSV, XML, YAML, and other formats.
- [pawk](https://github.com/alecthomas/pawk) **—** Process text with AWK-like patterns, but Python code.
- [qsv](https://github.com/jqnatividad/qsv) **—** Index, slice, analyze, split, and join CSV files. A fork of xsv that adds subcommands and features.
- [ReadStat](https://github.com/WizardMac/ReadStat) **—** Convert statistics package datasets between SAS (SAS7BDAT, XPORT), SPSS (POR, SAV, ZSAV), and Stata (DTA). Convert those formats to CSV and XLSX. Can be used as a C library with bindings for Julia, Python, and R.
- [rows](https://github.com/turicas/rows) **—** A Python library with a [CLI](http://turicas.info/rows/cli/). Convert between a number of [file formats](http://turicas.info/rows/plugins/) for tabular data: CSV, XLS, XLSX, ODS, and others. Query the data (via SQLite). Combine tables. Generate schemas.
- [rq](https://github.com/dflemstr/rq) **—** Convert between Apache Avro, CBOR, CSV, JSON, MessagePack, Protocol Buffers, TOML, YAML, and awk-style plain text.
- [scrubcsv](https://github.com/faradayio/scrubcsv) **—** Remove bad lines from a CSV file and normalize the rest. Written in Rust.
- [Skeem](https://github.com/daq-tools/skeem) **—** Infer SQL DDL statements from tabular data. Supports CSV, JSON, JSON Lines, ODS, XLSX, and other formats.
- [tab](http://tkatchev.bitbucket.io/tab/) **—** A non-Turing-complete statically typed programming language for data processing. An alternative to awk.
- [teip](https://github.com/greymd/teip) **—** Select fields, character ranges, or regular expression matches from standard input. Replace them with the output of a command.
- [tv](https://github.com/codechenx/tv) **—** View delimited files in the terminal.
- [xsv](https://github.com/BurntSushi/xsv) **—** Index, slice, analyze, split, and join CSV files.
- [zsv](https://github.com/liquidaty/zsv) **—** Slice, combine, reformat, flatten/unflatten CSV (TSV, DSV) files. Query them with SQL and jq filters. Convert between them, JSON, and SQLite 3. Also a C library.

### SQL-based tools

See the [big comparison list](sql-based.md). It covers

- AlaSQL CLI
- csvq
- csvsql
- fsql
- Musoq
- q
- RBQL
- rows
- Sqawk (dbohdan)
- sqawk (tjunier)
- Squawk
- termsql
- trdsql
- textql


## HTML

- [Graphtage](https://github.com/trailofbits/graphtage) **—** Compare and merge tree-like structures semantically. Supports JSON, JSON5, XML, HTML, YAML, and CSV. Can be used as a Python library.
- [hred](https://github.com/danburzo/hred) **—** Query XML and HTML with a query language based on CSS selectors.
- [html-xml-utils](https://www.w3.org/Tools/HTML-XML-utils/README) **—** A number of simple utilities (like `hxcopy`, `hxpipe`, `hxunent`, `hxselect`) for manipulating HTML and XML files from [W3C](https://www.w3.org/). Written in C, quite old-fashioned, but still relevant and maintained.
- [htmlq](https://github.com/mgdm/htmlq) **—** Query HTML with CSS selectors. Can remove elements in the output.
- [pup](https://github.com/EricChiang/pup) **—** Query HTML pages with CSS selectors. Static binaries available for releases. Inspired by [jq](#json).
- [Saxon](http://saxon.sourceforge.net/) **—** Query XML and HTML data with [XPath](https://devhints.io/xpath). [Documentation](http://www.saxonica.com/documentation/#!using-xsl).
- [Temme](https://github.com/shinima/temme) **—** Query HTML with CSS-like selectors to extract JSON. Temme extends CSS selectors with value capture patterns.
- [tidy-html5](http://www.html-tidy.org/) **—** Validate, fix, and reformat HTML(5), XHTML, and XML documents. Convert HTML to XHTML.
- [tq](https://github.com/plainas/tq) **—** Query HTML with CSS selectors.
- [Xidel](http://www.videlibri.de/xidel.html) **—** Query or modify XML and HTML pages with XPath, XQuery 3, and CSS selectors.
- [xml2](https://web.archive.org/web/20160719191401/http://ofb.net/~egnor/xml2/) **—** Convert XML and HTML to and from flat, greppable lists of "path=value" statements. [Source code mirror](https://github.com/clone/xml2).
- [xpe](https://github.com/charmparticle/xpe) **—** Query HTML and XML with XPath expressions.


## JSON

- [Cels](https://github.com/pacha/cels) **—** Patch JSON, TOML, and YAML with patches in the same format with some special values. Can be used as a Python library.
- [clconf](https://github.com/pastdev/clconf) **—** Merge multiple config files and extract values from them using path string. Supports JSON and YAML. Can be used as a Go library.
- [dasel](https://github.com/TomWright/dasel) **—** Query and update data structures from the command line. Comparable to jq/yq but supports CSV, JSON, TOML, YAML, and XML. Static binaries available for releases.
- [emuto](http://kantord.github.io/emuto/) **—** CLI tool similar to jq. Create and manipulate JSON and other files. Can be compiled to JavaScript.
- [fastgron](https://github.com/adamritter/fastgron) **—** Convert JSON to and from GRON, a flat, greppable list of `path=value` statements. Much faster than the original gron on large files.
- [fx](https://github.com/antonmedv/fx) **—** Run arbitrary JavaScript on JSON input. Standalone binaries available.
- [gojq](https://github.com/itchyny/gojq) **—** A pure Go implementation of jq. Supports YAML input and output.
- [Graphtage](https://github.com/trailofbits/graphtage) **—** Compare and merge tree-like structures semantically. Supports JSON, JSON5, XML, HTML, YAML, and CSV. Can be used as a Python library.
- [gron](https://github.com/tomnomnom/gron) **—** Convert JSON to and from GRON, a flat, greppable list of `path=value` statements.
- [jaq](https://github.com/01mf02/jaq) **—** A Rust implementation of jq with minor changes to the language to make it more predictable.
- [JC](https://github.com/kellyjonbrazil/jc) **—** Convert the output of standard command-line tools to JSON.
- [jello](https://github.com/kellyjonbrazil/jello) **—** Query JSON and [JSON Lines](http://jsonlines.org/) with Python code. Output the result in a line-based format suitable for creating Bash arrays. Generate a grep-able schema.
- [jet](https://github.com/borkdude/jet) **—** Convert between JSON, YAML, Clojure's [edn](https://github.com/edn-format/edn), and [Transit](https://github.com/cognitect/transit-format). Transform them with Clojure code.
- [jfq](https://github.com/blgm/jfq) **—** Query and transform JSON with the [JSONata](http://jsonata.org/) language.
- [jj](https://github.com/tidwall/jj) **—** Query and modify values in JSON or JSON Lines with a key path.
- [jl](https://github.com/chrisdone/jl) **—** Query and manipulate JSON using a tiny functional language.
- [jo](https://github.com/jpmens/jo) **—** Create JSON objects from the shell.
- [jp (jmespath)](https://github.com/jmespath/jp) **—** Query JSON with [JMESPath](http://jmespath.org/).
- [jp (sgreben)](https://github.com/sgreben/jp) **—** Plot JSON and CSV data in the terminal. Supports different kinds of plots: bar charts, line charts, scatter plots, histograms, and heatmaps.
- [jplot](https://github.com/rs/jplot) **—** Plot real-time JSON data in the terminal (works with terminals supporting graphic rendering).
- [jq](http://stedolan.github.io/jq/manual/) **—** Create and manipulate JSON with a functional (as in "functional programming") [DSL](https://en.wikipedia.org/wiki/Domain-specific_language). Can convert JSON to other formats.
- [jql](https://github.com/cube2222/jql) **—** Create and manipulate JSON with a Lisp-syntax DSL.
- [jshon](http://kmkeen.com/jshon/) **—** Create and manipulate JSON using [getopt](https://en.wikipedia.org/wiki/Getopt)-style command-line options.
- [json](https://github.com/trentm/json) **—** Run arbitrary JavaScript on JSON input.
- [json-patch](https://github.com/evanphx/json-patch) **—** Apply [RFC 6902](https://tools.ietf.org/html/rfc6902) JSON Patches to JSON. The CLI tool is secondary to a Go library that also creates and applies [RFC 7386](https://tools.ietf.org/html/rfc7396) JSON merge patches.
- [json-table](https://github.com/micha/json-table) **—** Convert nested JSON into CSV or TSV for processing in the shell.
- [json.tool](https://docs.python.org/2/library/json.html) **—** Validate and pretty-print JSON. This module is part of the standard library of Python 2/3 and is likely to be available wherever Python is installed. ([Python 3 docs](https://docs.python.org/3/library/json.html).)
- [json2](https://github.com/vi/json2) **—** Convert JSON to and from flat, greppable lists of "path=value" statements. Modeled after [xml2](#xml).
- [jsonaxe](https://github.com/davvid/jsonaxe) **—** Create and manipulate JSON with a Python-based DSL. Inspired by jq.
- [jsonwatch](https://github.com/dbohdan/jsonwatch) **—** Track changes in JSON data from the command line. Works like `watch -d`.
- [jtbl](https://github.com/kellyjonbrazil/jtbl) **—** Format JSON or JSON Lines as a plain-text table.
- [jtc](https://github.com/ldn-softdev/jtc) **—** Create, manipulate, search, validate JSON with path expressions. Can be used as a C++14 library.
- [lobar](https://github.com/sodiumjoe/lobar) **—** Process JSON and explore it interactively with a wrapper for `lodash.chain()`. An alternative to jq with JavaScript syntax.
- [madato](https://github.com/inosion/madato) **—** Convert ODS and XLSX spreadsheets to JSON, Markdown, and YAML.
- [Mario](https://github.com/python-mario/mario) **—** Manipulate and convert between CSV, JSON, YAML, TOML, and XML with Python code.
- [Nushell](https://github.com/nushell/nushell) **—** A command shell. Can natively [load data](https://www.nushell.sh/book/loading_data.html) from CSV, INI, JSON, TOML, TSV, XML, YAML, and other formats.
- [pyp](https://github.com/hauntsaninja/pyp) **—** Transform input (as text lines or as a whole) using Python code with automatic module imports. Can generate a Python script equivalent to its invocation. In Python 3.11 or later supports TOML through [tomllib](https://docs.python.org/3.11/library/tomllib.html).
- [qpyson](https://github.com/mpkocher/qpyson) **—** Query and manipulate JSON with Python.
- [query-json](https://github.com/davesnx/query-json) **—** A faster jq implementation written in Reason Native (OCaml).
- [quicktype](https://github.com/quicktype/quicktype) **—** Infer the underlying model of the JSON and output as types for various programming languages or JSON Schema. CLI and [Web UI](https://app.quicktype.io).
- [ramda-cli](https://github.com/raine/ramda-cli) **—** Manipulate JSON with the [Ramda](https://ramdajs.com/) functional library, and either LiveScript or JavaScript syntax.
- [RecordStream](https://github.com/benbernard/RecordStream) **—** Create, manipulate, and output a stream of records, or JSON objects. Can retrieve records from an SQL database, MongoDB, Atom feeds, XML, and other sources.
- [Remarshal](https://github.com/dbohdan/remarshal) **—** Convert between CBOR, JSON, MessagePack, TOML, and YAML. Validate each of the formats. Pretty-print JSON, TOML, and YAML.
- [rq](https://github.com/dflemstr/rq) **—** Convert between Apache Avro, CBOR, CSV, JSON, MessagePack, Protocol Buffers, TOML, YAML, and awk-style plain text.
- [Skeem](https://github.com/daq-tools/skeem) **—** Infer SQL DDL statements from tabular data. Supports CSV, JSON, JSON Lines, ODS, XLSX, and other formats.
- [validjson](http://github.com/martinlindhe/validjson) **—** Validate or pretty-print JSON.
- [xml-to-json-fast](https://github.com/sinelaw/xml-to-json-fast) **—** Convert XML to JSON. Can handle very large XML files.
- [xmljson](https://github.com/engali94/XMLJson) **—** Convert multiple and large XML files to JSON. Written in Swift.
- [yaml-diff-patch](https://github.com/grantila/yaml-diff-patch) **—** Patch YAML with [RFC 6902](https://datatracker.ietf.org/doc/html/rfc6902) JSON Patches. Generate a JSON Patch from two JSON documents or a YAML and a JSON document. Preserves style. Can be used as a TypeScript library.
- [yamlpath](https://github.com/wwkimball/yamlpath) **—** Query, modify, diff, merge, and validate YAML and JSON with [YAML Paths](https://github.com/wwkimball/yamlpath/wiki/Segments-of-a-YAML-Path). Also a Python library.


## TOML

With a format converter like Remarshal you can use [JSON](#json) tools to process TOML and YAML, but make sure you do not lose data in the conversion.

- [Cels](https://github.com/pacha/cels) **—** Patch JSON, TOML, and YAML with patches in the same format with some special values. Can be used as a Python library.
- [dasel](https://github.com/TomWright/dasel) **—** Query and update data structures from the command line. Comparable to jq/yq but supports CSV, JSON, TOML, YAML, and XML. Static binaries available for releases.
- [Mario](https://github.com/python-mario/mario) **—** Manipulate and convert between CSV, JSON, YAML, TOML, and XML with Python code.
- [Nushell](https://github.com/nushell/nushell) **—** A command shell. Can natively [load data](https://www.nushell.sh/book/loading_data.html) from CSV, INI, JSON, TOML, TSV, XML, YAML, and other formats.
- [pyp](https://github.com/hauntsaninja/pyp) **—** Transform input (as text lines or as a whole) using Python code with automatic module imports. Can generate a Python script equivalent to its invocation. In Python 3.11 or later supports TOML through [tomllib](https://docs.python.org/3.11/library/tomllib.html).
- [Remarshal](https://github.com/dbohdan/remarshal) **—** Convert between CBOR, JSON, MessagePack, TOML, and YAML. Validate each of the formats. Pretty-print JSON, TOML, and YAML.
- [rq](https://github.com/dflemstr/rq) **—** Convert between Apache Avro, CBOR, CSV, JSON, MessagePack, Protocol Buffers, TOML, YAML, and awk-style plain text.
- [taplo-cli](https://github.com/tamasfe/taplo) **—** Query, format, and validate (lint) TOML.
- [validtoml](http://github.com/martinlindhe/validtoml) **—** Validate TOML.
- [yq (kislyuk)](https://github.com/kislyuk/yq) **—** [jq](#json) wrapper for YAML, XML, and TOML.


## XML

- [dasel](https://github.com/TomWright/dasel) **—** Query and update data structures from the command line. Comparable to jq/yq but supports CSV, JSON, TOML, YAML, and XML. Static binaries available for releases.
- [Graphtage](https://github.com/trailofbits/graphtage) **—** Compare and merge tree-like structures semantically. Supports JSON, JSON5, XML, HTML, YAML, and CSV. Can be used as a Python library.
- [hred](https://github.com/danburzo/hred) **—** Query XML and HTML with a query language based on CSS selectors.
- [html-xml-utils](https://www.w3.org/Tools/HTML-XML-utils/README) **—** A number of simple utilities (like `hxcopy`, `hxpipe`, `hxunent`, `hxselect`) for manipulating HTML and XML files from [W3C](https://www.w3.org/). Written in C, quite old-fashioned, but still relevant and maintained.
- [Mario](https://github.com/python-mario/mario) **—** Manipulate and convert between CSV, JSON, YAML, TOML, and XML with Python code.
- [Nushell](https://github.com/nushell/nushell) **—** A command shell. Can natively [load data](https://www.nushell.sh/book/loading_data.html) from CSV, INI, JSON, TOML, TSV, XML, YAML, and other formats.
- [Saxon](http://saxon.sourceforge.net/) **—** Query XML and HTML data with [XPath](https://devhints.io/xpath). [Documentation](http://www.saxonica.com/documentation/#!using-xsl).
- [sml2](https://github.com/JFLarvoire/libxml2) **—** Convert between XML and [SML](https://htmlpreview.github.io/?https://github.com/JFLarvoire/libxml2/blob/master/SML_presentation.htm), a simplified XML representation.
- [tidy-html5](http://www.html-tidy.org/) **—** Validate, fix, and reformat HTML(5), XHTML, and XML documents. Convert HTML to XHTML.
- [Xidel](http://www.videlibri.de/xidel.html) **—** Query or modify XML and HTML pages with XPath, XQuery 3, and CSS selectors.
- [xml-to-json-fast](https://github.com/sinelaw/xml-to-json-fast) **—** Convert XML to JSON. Can handle very large XML files.
- [xml2](https://web.archive.org/web/20160719191401/http://ofb.net/~egnor/xml2/) **—** Convert XML and HTML to and from flat, greppable lists of "path=value" statements. [Source code mirror](https://github.com/clone/xml2).
- [xmljson](https://github.com/engali94/XMLJson) **—** Convert multiple and large XML files to JSON. Written in Swift.
- [XMLLint](http://xmlsoft.org/xmllint.html) **—** Query (including XSLT), validate and reformat XML documents.
- [XMLStarlet](http://xmlstar.sourceforge.net/overview.php) **—** Query, modify, and validate XML documents.
- [xpe](https://github.com/charmparticle/xpe) **—** Query HTML and XML with XPath expressions.
- [xq](https://github.com/kislyuk/yq) **—** [jq](#json) wrapper for XML documents.
- [xsltproc](http://xmlsoft.org/XSLT/xsltproc2.html) **—** Transform XML documents using [XSLT](https://www.w3.org/TR/xslt) and [EXSLT](http://exslt.org).
- [yq (kislyuk)](https://github.com/kislyuk/yq) **—** [jq](#json) wrapper for YAML, XML, and TOML.

### See also

- ["Grep and Sed Equivalent for XML Command Line Processing"](http://stackoverflow.com/questions/91791/grep-and-sed-equivalent-for-xml-command-line-processing) on Stack Overflow.


## YAML

- [Cels](https://github.com/pacha/cels) **—** Patch JSON, TOML, and YAML with patches in the same format with some special values. Can be used as a Python library.
- [clconf](https://github.com/pastdev/clconf) **—** Merge multiple config files and extract values from them using path string. Supports JSON and YAML. Can be used as a Go library.
- [dasel](https://github.com/TomWright/dasel) **—** Query and update data structures from the command line. Comparable to jq/yq but supports CSV, JSON, TOML, YAML, and XML. Static binaries available for releases.
- [dy](https://github.com/sampointer/dy) **—** Construct YAML from a directory tree .
- [gojq](https://github.com/itchyny/gojq) **—** A pure Go implementation of jq. Supports YAML input and output.
- [Graphtage](https://github.com/trailofbits/graphtage) **—** Compare and merge tree-like structures semantically. Supports JSON, JSON5, XML, HTML, YAML, and CSV. Can be used as a Python library.
- [jet](https://github.com/borkdude/jet) **—** Convert between JSON, YAML, Clojure's [edn](https://github.com/edn-format/edn), and [Transit](https://github.com/cognitect/transit-format). Transform them with Clojure code.
- [madato](https://github.com/inosion/madato) **—** Convert ODS and XLSX spreadsheets to JSON, Markdown, and YAML.
- [Mario](https://github.com/python-mario/mario) **—** Manipulate and convert between CSV, JSON, YAML, TOML, and XML with Python code.
- [Nushell](https://github.com/nushell/nushell) **—** A command shell. Can natively [load data](https://www.nushell.sh/book/loading_data.html) from CSV, INI, JSON, TOML, TSV, XML, YAML, and other formats.
- [Remarshal](https://github.com/dbohdan/remarshal) **—** Convert between CBOR, JSON, MessagePack, TOML, and YAML. Validate each of the formats. Pretty-print JSON, TOML, and YAML.
- [rq](https://github.com/dflemstr/rq) **—** Convert between Apache Avro, CBOR, CSV, JSON, MessagePack, Protocol Buffers, TOML, YAML, and awk-style plain text.
- [shyaml](https://github.com/0k/shyaml) **—** Query YAML. Can output null-terminated strings for use in shell scripts.
- [validyaml](http://github.com/martinlindhe/validyaml) **—** Validate or pretty-print YAML.
- [yaml-diff-patch](https://github.com/grantila/yaml-diff-patch) **—** Patch YAML with [RFC 6902](https://datatracker.ietf.org/doc/html/rfc6902) JSON Patches. Generate a JSON Patch from two JSON documents or a YAML and a JSON document. Preserves style. Can be used as a TypeScript library.
- [yaml-tools](https://github.com/thecodingmachine/yaml-tools) **—** A set of CLI tools to manipulate YAML files (merge, delete, etc...) with comment preservation, based on [ruamel.yaml](http://yaml.readthedocs.io/en/latest/).
- [yamlpath](https://github.com/wwkimball/yamlpath) **—** Query, modify, diff, merge, and validate YAML and JSON with [YAML Paths](https://github.com/wwkimball/yamlpath/wiki/Segments-of-a-YAML-Path). Also a Python library.
- [yq (kislyuk)](https://github.com/kislyuk/yq) **—** [jq](#json) wrapper for YAML, XML, and TOML.
- [yq (mikefarah)](https://github.com/mikefarah/yq) **—** Query, modify, and merge YAML. Convert to and from JSON.


## Configuration files

### /etc/hosts

- [hostctl](https://github.com/guumaster/hostctl) **—** Add and remove entries in `/etc/hosts`. Disable (comment out) and enable (uncomment) entries. Idempotent. Preserves arbitrary comments above its section of the hosts file. Works with groups of entries called "profiles".
- [hostess](https://github.com/cbednarski/hostess) **—** Add and remove entries in `/etc/hosts`. Disable (comment out) and enable (uncomment) entries. Check if a hostname exists. Reformat the hosts file. Convert the entries to JSON. Idempotent. Removes arbitrary comments.
- [hosts](https://gitlab.com/dbohdan/hosts) **—** Add and remove entries in `/etc/hosts`. Change a hostname's IP address. Idempotent. Preserves arbitrary comments. Can be used as a Tcl library.

### INI

- [cfget](https://packages.debian.org/source/buster/cfget)
    - **Platform:** Any with Python 2.6-2.7?
    - **License:** GPL-2.0-or-later
    - **Description:** Retrieve properties as shell script commands to set the corresponding variables (with `--dump exports`). Retrieve properties' values as plain text. Substitute values from an INI file in an Autoconf-style template. Supports plug-ins. Chokes on section names and keys with spaces.
- [confget](https://devel.ringlet.net/textproc/confget/)
    - **Platform:** Free/Net/OpenBSD, Linux, likely others
    - **License:** BSD-2-Clause
    - **Description:** Retrieve properties and sections as shell script commands to set the corresponding variables. Retrieve properties' values as plain text. Check for existence of properties. List sections. Find values that match a pattern. Read-only. Has a C, Python, and Rust implementation. The Rust implementation can be installed with `cargo install confget`.
- [crudini](https://github.com/pixelb/crudini/)
    - **Platform:** Any with Python 2.6–2.7 or 3.x
    - **License:** GPL-2.0
    - **Description:** Retrieve properties and sections as INI fragments or shell script commands to set the corresponding variables. Retrieve properties' values as plain text. Set properties. Remove properties and sections. Create empty sections. Merge INI files. Changes files in place.
- [inicomp](https://github.com/JFLarvoire/SysToolsLib/blob/HEAD/C/SRC/inicomp.c)
    - **Platform:** Windows, POSIX
    - **License:** Apache-2.0
    - **Description:** Compare INI (and also Windows .reg) files.
- [IniFile](http://www.horstmuc.de/wbat32.htm#inifile)
    - **Platform:** Windows (x86, x86-64), [MS-DOS](http://www.horstmuc.de/div.htm#inifile)
    - **License:** Closed-source freeware
    - **Description:** Retrieve properties and sections as batch file commands to set the corresponding variables. Set properties. Remove properties and sections. Changes files in place.
- [initool](https://github.com/dbohdan/initool)
    - **Platform:** FreeBSD, Linux, Windows
    - **License:** MIT
    - **Description:** Retrieve properties and sections as INI fragments. Retrieve properties' values as plain text. Set properties. Check for existence of properties and sections. Remove properties and sections. Outputs the updated INI file.
- [Nushell (`from ini`)](https://github.com/nushell/nushell)
    - **Platform:** Free/Net/OpenBSD, Linux, macOS, Windows
    - **License:** MIT
    - **Description:** Query and transform data with the Nushell language.

### Multiple formats

- [Augeas](http://augeas.net) **—** Query and modify [a number of file formats](http://augeas.net/stock_lenses.html). Not all of the formats are equally well supported by Augeas and for some only a limited subset of all valid files can be parsed.
- [Elektra](http://libelektra.org) **—** Query and modify [configuration files](https://github.com/ElektraInitiative/libelektra/tree/master/src/plugins). Shares Augeas' limitations when it comes to application-specific configuration files (it uses the same lenses), but has better support for generic formats such as JSON and INI.


## Log files

- [lnav](https://lnav.org) **—** Query and watch log files. Has batch and interactive mode. Supported formats include the Common Log Format, CUPS page_log, syslog, strace, and generic timestamped messages. Can perform SQL queries.
- [Squawk](https://github.com/samuel/squawk) **—** Query Apache and Nginx log files. See the [SQL-based tool comparison](sql-based.md).


## Templating for structured text

Listed below are restricted programming language interpreters and templating tools that produce structured text output. They are generally intended to remove repetition in configuration files. They are distinct from unstructed templating tools like the `jinja2` CLI program, which should not be added to this table.

- [CUE](https://github.com/cuelang/cue)
    - **Output format:** JSON
    - **Turing-complete:** No
    - **Syntax:** Extended JSON
    - **I/O:** ?
    - **Description:** A constraint language for JSON configuration data. Can generate and validates JSON.
- [Dhall](https://dhall-lang.org/)
    - **Output format:** JSON, YAML
    - **Turing-complete:** No
    - **Syntax:** Haskell-inspired
    - **I/O:** Limited to importing libraries from files and HTTP(S) URLs (with protection against leaking your data to the server)
    - **Description:** A statically-typed functional configuration language. Has a standard formatting tool.
- [jk](https://github.com/jkcfg/jk)
    - **Output format:** JSON, YAML, plain text
    - **Turing-complete:** Yes
    - **Syntax:** JavaScript
    - **I/O:** Disk I/O
    - **Description:** Generate configuration files using JavaScript (V8 VM).
- [Jsonnet](https://jsonnet.org/)
    - **Output format:** JSON, INI, XML, YAML, plain text
    - **Turing-complete:** Yes
    - **Syntax:** Extended JSON
    - **I/O:** None
    - **Description:** A functional configuration language. Has a standard formatting tool.
- [Nickel](https://nickel-lang.org/)
    - **Output format:** JSON, TOML, YAML
    - **Turing-complete:** Yes
    - **Syntax:** Inspired by ML and JSON
    - **I/O:** Limited input is to be implemented
    - **Description:** A gradually-typed functional configuration language with contracts.
- [Pkl](https://pkl-lang.org/)
    - **Output format:** JSON, YAML, macOS property list, Java `.properties`
    - **Turing-complete:** Yes
    - **Syntax:** Swift-inspired
    - **I/O:** The CLI can read environment variables and files, `GET` HTTP(S) URLs. It can import modules from files and HTTP(S) URLs.
    - **Description:** A command-line tool, Java library, and build tool plugin. Can generate code for Go, Java, Kotlin, and Swift. ["Pkl vs. Other Config Languages"](https://pkl-lang.org/main/current/introduction/comparison.html#other-config-langs).
- [rjsone](https://github.com/wryun/rjsone)
    - **Output format:** JSON, YAML
    - **Turing-complete:** No?
    - **Syntax:** Extended JSON
    - **I/O:** None
    - **Description:** A CLI tool for the [JSON-e](https://github.com/taskcluster/json-e) templating language.
- [ytt](https://get-ytt.io/)
    - **Output format:** YAML
    - **Turing-complete:** No
    - **Syntax:** YAML/Python hybrid
    - **I/O:** None?
    - **Description:** A templating tool for YAML built upon the [Starlark](https://github.com/bazelbuild/starlark) configuration language.

### See also

- [A comparison table of Nickel and other configuration languages](https://github.com/tweag/nickel/blob/master/RATIONALE.md#comparison-with-other-configuration-languages).


## Extra: interactive TUIs

- [jid](https://github.com/simeji/jid) **—** Explore JSON interactively with filtering queries like jq.
- [jiq](https://github.com/fiatjaf/jiq) **—** Explore JSON interactively with jq. Requires jq.
- [lobar](https://github.com/sodiumjoe/lobar) **—** Process JSON and explore it interactively with a wrapper for `lodash.chain()`. An alternative to jq with JavaScript syntax.
- [sc-im](https://github.com/andmarti1424/sc-im) **—** A Vim-like spreadsheet calculator for CSV and TSV files.
- [VisiData](https://github.com/saulpw/visidata) **—** Explore interactively data in TSV, CSV, XLS, XLSX, HDF5, JSON, and [other formats](http://visidata.org/man/#loaders). [Introduction](https://jsvine.github.io/intro-to-visidata/).


## Extra: CLIs for single-file databases

- [Firebird](https://firebirdsql.org/)
    - **Description:** Firebird is a FOSS database that can be used from a single file, like SQLite. "isql is a program that allows the user to issue arbitrary SQL commands".
    - **File format:** Binary
- [Fsdb](https://www.isi.edu/~johnh/SOFTWARE/FSDB/perl-Fsdb-2.69_README.html)
    - **Description:** A flat-file database for shell scripting.
    - **File format:** Text-based, TSV with a header or "key: value"
- [GNU Recutils](http://www.gnu.org/software/recutils/)
    - **Description:** "[A] set of tools and libraries to access human-editable, plain text databases called recfiles."
    - **File format:** Text-based, roughly "key: value"
- [SDB](https://github.com/radare/sdb)
    - **Description:** "[A] simple string key/value database based on djb's cdb disk storage and supports JSON and arrays introspection."
    - **File format:** Binary
- [sqlite3(1)](https://www.sqlite.org/cli.html)
    - **Description:** "[A] simple command-line utility [...] that allows the user to manually enter and execute SQL statements against an SQLite database."
    - **File format:** Binary


## License

The contents of this document is licensed under the [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/). By contributing you agree to release your contribution under this license.


## Disclosure

[csv2html](https://github.com/dbohdan/csv2html), [hosts](https://gitlab.com/dbohdan/hosts), [Sqawk](https://github.com/dbohdan/sqawk), [jsonwatch](https://github.com/dbohdan/jsonwatch), [Remarshal](https://github.com/remarshal-project/remarshal), and [initool](https://github.com/dbohdan/initool) are developed by the curator of this document.
