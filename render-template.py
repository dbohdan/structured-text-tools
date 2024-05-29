#! /usr/bin/env -S pipx run
# /// script
# dependencies = [
#   "click==8.*",
#   "Jinja2==3.*",
#   "tomli==2.*",
# ]
# requires-python = ">=3.8"
# ///

from __future__ import annotations

from dataclasses import dataclass, field
from itertools import starmap
from pathlib import Path
from typing import Any, Iterator

import click
import jinja2 as j2
import tomli


@dataclass
class Project:
    name: str
    url: str
    tags: list[str]
    descr: str = ""
    props: dict[str, str] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, name: str, d: dict[str, Any]):
        return cls(name=name, **d)


@click.command()
@click.argument("template-name", type=click.Path(exists=True, path_type=Path))
@click.argument("data-path", type=click.Path(exists=True, path_type=Path))
def main(template_name: Path, data_path: Path) -> None:
    data = tomli.loads(data_path.read_text())
    projects = list(starmap(Project.from_dict, data.items()))

    def projs_with_tag(tag: str) -> list[Project]:
        return [proj for proj in projects if tag in proj.tags]

    env = j2.Environment(
        loader=j2.FileSystemLoader("."),
        autoescape=j2.select_autoescape(),
        lstrip_blocks=True,
        trim_blocks=True,
    )

    env.globals["projs_with_tag"] = projs_with_tag

    template = env.get_template(str(template_name))
    rendered = template.render(data)
    click.echo(rendered)


if __name__ == "__main__":
    main()
