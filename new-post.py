#!/usr/bin/env python3
"""
Create a new blog post for spapestronaut.com

Usage:
  python3 new-post.py "My Post Title"

This will:
  1. Create a new HTML file in posts/
  2. Add the post to the top of the list on index.html
"""

import sys
import os
import re
from datetime import date

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(SCRIPT_DIR, "posts")
INDEX_FILE = os.path.join(SCRIPT_DIR, "index.html")
TEMPLATE_FILE = os.path.join(SCRIPT_DIR, "posts", "_template.html")


def slugify(title):
    slug = title.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def create_post(title):
    slug = slugify(title)
    today = date.today().isoformat()
    filename = f"{slug}.html"
    filepath = os.path.join(POSTS_DIR, filename)

    if os.path.exists(filepath):
        print(f"Error: {filepath} already exists.")
        sys.exit(1)

    # Read template
    with open(TEMPLATE_FILE, "r") as f:
        template = f.read()

    # Fill in template
    content = template.replace("{{TITLE}}", title).replace("{{DATE}}", today)

    # Write post file
    with open(filepath, "w") as f:
        f.write(content)

    # Add to index.html
    with open(INDEX_FILE, "r") as f:
        index = f.read()

    new_entry = (
        f'      <li class="post-item">\n'
        f'        <a href="posts/{filename}" class="post-link">\n'
        f'          <span class="post-title">{title}</span>\n'
        f'          <span class="post-date">{today}</span>\n'
        f'        </a>\n'
        f'      </li>'
    )

    marker = "<!-- POSTS:START (do not remove this comment — the new-post script uses it) -->"
    index = index.replace(marker, marker + "\n" + new_entry)

    with open(INDEX_FILE, "w") as f:
        f.write(index)

    print(f"Created: posts/{filename}")
    print(f"Added to: index.html")
    print(f"\nNext steps:")
    print(f"  1. Open posts/{filename} and write your article")
    print(f"  2. Preview locally: python3 serve.py")
    print(f"  3. Deploy to your host")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 new-post.py \"My Post Title\"")
        sys.exit(1)

    title = " ".join(sys.argv[1:])
    create_post(title)
