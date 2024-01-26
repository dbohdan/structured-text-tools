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

from dataclasses import dataclass
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
    descr: str | None = None
    props: dict[str, str] | None = None

    @classmethod
    def from_dict(cls, name: str, d: dict[str, Any]):
        return cls(name=name, **d)


def list_item(proj: Project) -> str:
    item = [f"* [{proj.name}]({proj.url})"]

    if proj.descr is not None:
        item.append(f" **—** {proj.descr}")

    if proj.props is not None:
        item.extend(
            f"\n    * **{prop}:** {value}" for prop, value in proj.props.items()
        )

    return "".join(item)


@click.command()
@click.argument("template-name", type=click.Path(exists=True, path_type=Path))
@click.argument("data-path", type=click.Path(exists=True, path_type=Path))
def main(template_name: Path, data_path: Path) -> None:
    data = tomli.loads(data_path.read_text())
    projects = [Project.from_dict(name, d) for name, d in data.items()]

    def proj_data(tag: str) -> Iterator[Project]:
        return (proj for proj in projects if tag in proj.tags)

    def projs_with_tag(tag: str) -> str:
        return "\n".join(list_item(proj) for proj in proj_data(tag))

    env = j2.Environment(
        loader=j2.FileSystemLoader("."),
        autoescape=j2.select_autoescape(),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    env.globals["projs_with_tag"] = projs_with_tag

    template = env.get_template(str(template_name))
    rendered = template.render(data)
    click.echo(rendered)


if __name__ == "__main__":
    main()
