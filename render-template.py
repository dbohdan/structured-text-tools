#! /usr/bin/env -S pipx run
# Requirements:
#     click==8.*
#     Jinja2==3.*
#     tomli==2.*

import click
import jinja2 as j2
import pathlib
import tomli
from typing import Iterator, TypedDict


class Project(TypedDict):
    name: str
    url: str
    tags: list[str]
    descr: str | None
    props: dict[str, str] | None


def list_item(proj: Project) -> str:
    item = [f"* [{proj['name']}]({proj['url']})"]

    if "descr" in proj:
        item.append(f" **—** {proj['descr']}")

    if "props" in proj:
        # Necessary for mypy.
        assert proj["props"] is not None

        item.extend(
            f"\n    * **{prop}:** {value}" for prop, value in proj["props"].items()
        )

    return "".join(item)


@click.command()
@click.argument("template-name", type=click.Path(exists=True, path_type=pathlib.Path))
@click.argument("data-path", type=click.Path(exists=True, path_type=pathlib.Path))
def main(template_name: pathlib.Path, data_path: pathlib.Path) -> None:
    data = tomli.loads(data_path.read_text())

    env = j2.Environment(
        loader=j2.FileSystemLoader("."),
        autoescape=j2.select_autoescape(),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    def proj_data(tag: str) -> Iterator[Project]:
        projects = data["projects"]
        return (proj for proj in projects if tag in proj["tags"])

    def projs_with_tag(tag: str) -> str:
        return "\n".join(list_item(proj) for proj in proj_data(tag))

    env.globals["projs_with_tag"] = projs_with_tag

    template = env.get_template(str(template_name))
    rendered = template.render(data)
    click.echo(rendered)


if __name__ == "__main__":
    main()
