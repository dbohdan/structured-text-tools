## SQL-based tools

<table>
  <tr>
    <th>Name</th>
    <th>Link</th>
    <th>Documentation link</th>
    <th>Programming language</th>
    <th>Database</th>
    <th>Column names from header row</th>
    <th>Custom character encoding</th>
    <th>Custom input field separator</th>
    <th>Custom input record separator</th>
    <th>Custom output field separator</th>
    <th>Custom output record separator</th>
    <th>JOINs</th>
    <th>Use as library</th>
    <th>Input formats</th>
    <th>Output formats</th>
    <th>Custom table names</th>
    <th>Custom column names</th>
    <th>Keep database file (for SQLite 3)</th>
    <th>Skip input fields</th>
    <th>Skip input records (lines)</th>
    <th>Merge input fields</th>
    <th>Database table customization</th>
    <th>SQL dump</th>
    <th>Other</th>
  </tr>
  <tr>
    <td>AlaSQL CLI</td>
    <td>https://github.com/agershun/alasql</td>
    <td>https://github.com/agershun/alasql/wiki/AlaSQL-CLI</td>
    <td>JavaScript</td>
    <td>AlaSQL</td>
    <td>yes, optional</td>
    <td>no</td>
    <td>yes, string</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>yes</td>
    <td>yes, JavaScript</td>
    <td>lines, DSV, XLS, XLSX, HTML tables, JSON</td>
    <td>lines, DSV, XLS, XLSX, HTML tables, JSON</td>
    <td>yes</td>
    <td>yes</td>
    <td>n/a</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>yes, can create custom table then import into it</td>
    <td>yes</td>
    <td></td>
  </tr>
  <tr>
    <td>csvq</td>
    <td>https://github.com/mithrandie/csvq</td>
    <td>https://mithrandie.github.io/csvq/reference</td>
    <td>Go</td>
    <td>custom SQL interpreter</td>
    <td>yes, optional</td>
    <td>yes, input and output</td>
    <td>yes, character</td>
    <td>no</td>
    <td>yes</td>
    <td>no</td>
    <td>yes</td>
    <td>yes, Go</td>
    <td>CSV, TSV, LTSV, fixed-width, JSON</td>
    <td>CSV, TSV, LTSV, fixed-width, JSON, Markdown-style table,
    Org-mode, ASCII table</td>
    <td>yes</td>
    <td>yes</td>
    <td>n/a</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>yes, ALTER TABLE</td>
    <td>no</td>
    <td></td>
  </tr>
  <tr>
    <td>csvsql</td>
    <td>https://github.com/wireservice/csvkit</td>
    <td>http://csvkit.readthedocs.io/en/latest/</td>
    <td>Python</td>
    <td>Firebird/MS SQL/MySQL/Oracle/PostgreSQL/SQLite
    3/Sybase</td>
    <td>yes, optional</td>
    <td>yes, input and output</td>
    <td>yes, string</td>
    <td>no</td>
    <td>yes</td>
    <td>no</td>
    <td>yes</td>
    <td>yes, Python</td>
    <td>delimited without quotes, DSV, Excel, JSON, SQL,
    fixed-width, DBF, and others (separate converters)</td>
    <td>delimited without quotes, DSV, JSON, Markdown-style table,
    SQL (separate converters)</td>
    <td>yes</td>
    <td>no</td>
    <td>yes</td>
    <td>yes (separate tool)</td>
    <td>no</td>
    <td>no?</td>
    <td>yes, UNIQUE constraints, database schema name, automatic
    column datatype or text</td>
    <td>yes</td>
    <td></td>
  </tr>
  <tr>
    <td>fsql</td>
    <td>https://metacpan.org/release/App-fsql</td>
    <td>
    https://metacpan.org/pod/distribution/App-fsql/bin/fsql</td>
    <td>Perl</td>
    <td>custom SQL interpreter</td>
    <td>yes, always</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>yes</td>
    <td>yes, Perl</td>
    <td>CSV, TSV, LTSV, Perl, JSON, YAML</td>
    <td>CSV, TSV, LTSV, Perl, JSON, YAML</td>
    <td>yes</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td></td>
  </tr>
  <tr>
    <td>q</td>
    <td>https://github.com/harelba/q</td>
    <td>
    https://github.com/harelba/q/blob/master/doc/USAGE.markdown</td>
    <td>Python</td>
    <td>SQLite 3</td>
    <td>yes, optional</td>
    <td>yes, input and output</td>
    <td>yes, string</td>
    <td>no</td>
    <td>yes</td>
    <td>no</td>
    <td>yes</td>
    <td>yes, Python</td>
    <td>delimited without quotes, DSV</td>
    <td>delimited without quotes, DSV, custom using Python
    formatting string</td>
    <td>no</td>
    <td>no</td>
    <td>yes</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>yes, automatic column datatype or text</td>
    <td>no</td>
    <td></td>
  </tr>
  <tr>
    <td>RBQL</td>
    <td>https://github.com/mechatroner/RBQL</td>
    <td>https://rbql.org/</td>
    <td>JavaScript, Python</td>
    <td>custom SQL interpreter</td>
    <td>yes, optional</td>
    <td>yes, input</td>
    <td>yes, string</td>
    <td>no</td>
    <td>yes</td>
    <td>no</td>
    <td>yes</td>
    <td>yes, JavaScript and Python</td>
    <td>DSV</td>
    <td>DSV</td>
    <td>no</td>
    <td>no</td>
    <td>n/a</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td></td>
  </tr>
  <tr>
    <td>rows</td>
    <td>https://github.com/turicas/rows</td>
    <td>http://turicas.info/rows/command-line-interface.html</td>
    <td>Python</td>
    <td>SQLite 3</td>
    <td>yes, always?</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>yes, Python</td>
    <td>CSV, JSON, XLS, XLSX, ODS, and others</td>
    <td>CSV, JSON, XLS, XLSX, ODS, and others</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td></td>
  </tr>
  <tr>
    <td>Sqawk</td>
    <td>https://github.com/dbohdan/sqawk</td>
    <td>https://github.com/dbohdan/sqawk#options</td>
    <td>Tcl</td>
    <td>SQLite 3</td>
    <td>yes, optional</td>
    <td>no</td>
    <td>yes, regexp, per-file</td>
    <td>yes, regexp, per-file</td>
    <td>yes</td>
    <td>yes</td>
    <td>yes</td>
    <td>yes, Tcl</td>
    <td>delimited without quotes, DSV, Tcl</td>
    <td>delimited without quotes, CSV, JSON, ASCII/Unicode table,
    Tcl</td>
    <td>yes</td>
    <td>yes</td>
    <td>yes</td>
    <td>yes, any</td>
    <td>no</td>
    <td>yes, any consecutive</td>
    <td>yes, column datatypes</td>
    <td>no</td>
    <td></td>
  </tr>
  <tr>
    <td>sqawk</td>
    <td>https://github.com/tjunier/sqawk</td>
    <td>https://github.com/tjunier/sqawk/blob/master/sqawk.1</td>
    <td>C</td>
    <td>SQLite 3</td>
    <td>yes, optional</td>
    <td>no</td>
    <td>yes, string, per-file</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>yes</td>
    <td>no</td>
    <td>DSV</td>
    <td>CSV</td>
    <td>yes</td>
    <td>no</td>
    <td>yes</td>
    <td>no</td>
    <td>yes, until regexp matches</td>
    <td>no</td>
    <td>yes, primary key, indexes, foreign key constraints,
    automatic column datatype or text</td>
    <td>yes</td>
    <td>chunked mode (read and process only N lines at a time)</td>
  </tr>
  <tr>
    <td>Squawk</td>
    <td>https://github.com/samuel/squawk</td>
    <td></td>
    <td>Python</td>
    <td>custom SQL interpreter</td>
    <td>yes, always</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>yes, Python</td>
    <td>CSV, Apache and Nginx log files</td>
    <td>table, CSV, JSON</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>yes</td>
    <td></td>
  </tr>
  <tr>
    <td>termsql</td>
    <td>https://github.com/tobimensch/termsql</td>
    <td>http://tobimensch.github.io/termsql/</td>
    <td>Python</td>
    <td>SQLite 3</td>
    <td>yes, optional</td>
    <td>no</td>
    <td>yes, regexp</td>
    <td>no</td>
    <td>yes</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>DSV, “vertical” DSV (lines as columns)</td>
    <td>delimited without quotes, CSV, TSV, HTML, SQL, Tcl</td>
    <td>yes</td>
    <td>yes</td>
    <td>yes</td>
    <td>no</td>
    <td>yes, N first and M last</td>
    <td>yes, Nth to last</td>
    <td>yes, primary key</td>
    <td>yes</td>
    <td></td>
  </tr>
  <tr>
    <td>trdsql</td>
    <td>https://github.com/noborus/trdsql</td>
    <td>https://github.com/noborus/trdsql#usage</td>
    <td>Go</td>
    <td>MySQL/PostgreSQL/SQLite 3</td>
    <td>yes, optional</td>
    <td>no</td>
    <td>yes, string</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>yes</td>
    <td>no</td>
    <td>CSV, LTSV, JSON</td>
    <td>delimited without quotes, CSV, LTSV, JSON, ASCII table,
    Markdown</td>
    <td>no</td>
    <td>no</td>
    <td>yes</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td></td>
  </tr>
  <tr>
    <td>textql</td>
    <td>https://github.com/dinedal/textql</td>
    <td>https://github.com/dinedal/textql#usage</td>
    <td>Go</td>
    <td>SQLite 3</td>
    <td>yes, optional</td>
    <td>no</td>
    <td>yes, string</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>DSV</td>
    <td>DSV</td>
    <td>no</td>
    <td>no</td>
    <td>yes</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td>no</td>
    <td></td>
  </tr>
</table>
