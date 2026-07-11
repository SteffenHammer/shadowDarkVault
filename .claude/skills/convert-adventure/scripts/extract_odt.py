"""Extract .odt files to markdown on stdout.

Usage: python extract_odt.py <file.odt> [more.odt ...]

Preserves headings (outline level -> #), paragraphs, lists, and tables.
"""
import sys
import zipfile
import xml.etree.ElementTree as ET

NS = {
    "office": "urn:oasis:names:tc:opendocument:xmlns:office:1.0",
    "text": "urn:oasis:names:tc:opendocument:xmlns:text:1.0",
    "table": "urn:oasis:names:tc:opendocument:xmlns:table:1.0",
}


def q(prefix, tag):
    return "{%s}%s" % (NS[prefix], tag)


def text_of(el):
    parts = []

    def walk(e):
        if e.tag == q("text", "s"):
            parts.append(" " * int(e.get(q("text", "c"), "1")))
        elif e.tag == q("text", "tab"):
            parts.append("\t")
        elif e.tag == q("text", "line-break"):
            parts.append("\n")
        if e.text:
            parts.append(e.text)
        for c in e:
            walk(c)
            if c.tail:
                parts.append(c.tail)

    walk(el)
    return "".join(parts)


def emit(el, out, depth=0):
    tag = el.tag
    if tag == q("text", "h"):
        lvl = int(el.get(q("text", "outline-level"), "1"))
        out.append("#" * min(lvl, 6) + " " + text_of(el).strip())
        out.append("")
    elif tag == q("text", "p"):
        out.append(text_of(el).strip())
        out.append("")
    elif tag == q("text", "list"):
        for item in el.findall(q("text", "list-item")):
            for child in item:
                if child.tag == q("text", "list"):
                    emit(child, out, depth + 1)
                else:
                    t = text_of(child).strip()
                    if t:
                        out.append("  " * depth + "- " + t)
        if depth == 0:
            out.append("")
    elif tag == q("table", "table"):
        rows = []
        for tr in el.iter(q("table", "table-row")):
            cells = [
                text_of(tc).strip().replace("\n", " ")
                for tc in tr.findall(q("table", "table-cell"))
            ]
            rows.append("| " + " | ".join(cells) + " |")
        if rows:
            ncols = rows[0].count("|") - 1
            out.append(rows[0])
            out.append("|" + " --- |" * ncols)
            out.extend(rows[1:])
            out.append("")


def convert(path):
    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read("content.xml"))
    body = root.find(q("office", "body")).find(q("office", "text"))
    out = []
    for el in body:
        emit(el, out)
    lines, prev_blank = [], False
    for line in out:
        blank = line == ""
        if blank and prev_blank:
            continue
        lines.append(line)
        prev_blank = blank
    return "\n".join(lines).strip() + "\n"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    for p in sys.argv[1:]:
        if len(sys.argv) > 2:
            print("\n===== %s =====\n" % p)
        sys.stdout.write(convert(p))
