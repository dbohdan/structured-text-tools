#! /usr/bin/env -S pipx run
# Requirements:
#     Jinja2==3.*
#     tomli==2.*

import jinja2 as j2
from pathlib import Path
import tomli

DATA = "data/projects.toml"
TEMPLATE = "README.md.jinja2"
OUTPUT = "README.md"


def list_item(proj):
    item = [f"* [{proj['name']}]({proj['url']})"]

    if "descr" in proj:
        item.append(f" **—** {proj['descr']}")

    if "props" in proj:
        item.extend(
            f"\n    * **{prop}:** {value}" for prop, value in proj["props"].items()
        )

    return "".join(item)


def main():
    data = tomli.loads(Path(DATA).read_text())

    env = j2.Environment(
        loader=j2.FileSystemLoader("."),
        autoescape=j2.select_autoescape(),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    def proj_data(tag):
        projects = data["projects"]
        return (proj for proj in projects if tag in proj["tags"])

    def projs_with_tag(tag):
        return "\n".join(list_item(proj) for proj in proj_data(tag))

    env.globals["projs_with_tag"] = projs_with_tag

    template = env.get_template(TEMPLATE)
    rendered = template.render(data)
    print(rendered)


if __name__ == "__main__":
    main()
