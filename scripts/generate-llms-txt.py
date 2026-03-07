#!/usr/bin/env python3
"""Generate llms.txt from Quarto project metadata.

This script is run as a Quarto pre-render script. It reads YAML front matter
from all .qmd files and generates an llms.txt file following the llmstxt.org
proposed format. See https://llmstxt.org/ for details.
"""

import glob
import os
import re
from pathlib import Path

import yaml

MAIN_PAGES = [
    ("index.qmd", "Home", ""),
    ("book-of-abstracts.qmd", None, "book-of-abstracts.html"),
    ("conference-program.qmd", None, "conference-program.html"),
    ("call-for-contributions.qmd", None, "call-for-contributions.html"),
    ("about.qmd", None, "about.html"),
]


def read_front_matter(filepath):
    """Read YAML front matter from a .qmd file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.match(r"^---\s*\n?(.*?)\n---", content, re.DOTALL)
    if match:
        return yaml.safe_load(match.group(1))
    return {}


def main():
    os.chdir(Path(__file__).resolve().parent.parent)

    with open("_quarto.yml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    site_url = config.get("website", {}).get("site-url", "").rstrip("/")
    site_title = config.get("website", {}).get("title", "")

    index_meta = read_front_matter("index.qmd")
    description = index_meta.get("description-meta", "")

    lines = []
    lines.append(f"# {site_title}")
    lines.append("")
    lines.append(f"> {description}")
    lines.append("")

    # Main pages
    lines.append("## Main Pages")
    lines.append("")
    for qmd_file, override_title, url_path in MAIN_PAGES:
        if not os.path.exists(qmd_file):
            continue
        meta = read_front_matter(qmd_file)
        title = override_title or meta.get("title", os.path.basename(qmd_file).removesuffix(".qmd"))
        lines.append(f"- [{title}]({site_url}/{url_path})")
    lines.append("")

    # Keynote
    keynote_path = "submissions/keynote/index.qmd"
    if os.path.exists(keynote_path):
        meta = read_front_matter(keynote_path)
        title = meta.get("title", "Keynote")
        lines.append("## Keynote")
        lines.append("")
        lines.append(f"- [{title}]({site_url}/submissions/keynote/)")
        lines.append("")

    # Paper submissions
    paper_files = sorted(glob.glob("submissions/[0-9]*/index.qmd"))
    if paper_files:
        lines.append("## Paper Submissions")
        lines.append("")
        for qmd_file in paper_files:
            meta = read_front_matter(qmd_file)
            title = meta.get("title", "")
            sub_dir = os.path.dirname(qmd_file).replace("\\", "/")
            lines.append(f"- [{title}]({site_url}/{sub_dir}/)")
        lines.append("")

    # Poster submissions
    poster_files = sorted(glob.glob("submissions/poster/[0-9]*/index.qmd"))
    if poster_files:
        lines.append("## Poster Submissions")
        lines.append("")
        for qmd_file in poster_files:
            meta = read_front_matter(qmd_file)
            title = meta.get("title", "")
            sub_dir = os.path.dirname(qmd_file).replace("\\", "/")
            lines.append(f"- [{title}]({site_url}/{sub_dir}/)")
        lines.append("")

    with open("llms.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Generated llms.txt with {len(lines)} lines")


if __name__ == "__main__":
    main()
