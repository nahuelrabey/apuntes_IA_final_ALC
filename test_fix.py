import re
from pathlib import Path

content = Path("docs/ALC/finales/Examen_2025_02_24/01_semejanza_matrices/teoria.md").read_text(encoding="utf-8")

# Let's write a robust regex to just match this specific corruption:
# A line with `>` then `\n\n$$\n` then `> (.*?)\n` then `>\n\n$$\n`
pattern = re.compile(
    r'(?:^[ \t]*>[ \t]*\n)*^[ \t]*>[ \t]*\n\n\$\$\n(.*?)\n(?:^[ \t]*>[ \t]*\n)*\n\$\$\n',
    re.MULTILINE | re.DOTALL
)

def replacer(match):
    inner = match.group(1)
    # The inner content already has `> ` so let's just wrap it with `> $$`
    return f"> $$\n{inner}\n> $$\n"

updated = pattern.sub(replacer, content)

# Also need to match the specific broken output in `enunciado.md` 
# which is:
"""
>
(.*?)
$$
> MATH
>
(.*?)
$$
>
"""
# Let's just restore all `\n\n$$\n` that are preceded by `> `
# Wait, let's just use string replace.
# The damage was taking `> $$` and turning it into `>\n\n$$`.
# Can we just replace `>\n\n$$` with `> $$` ?
# Let's see if that's safe.
updated2 = content.replace(">\n\n$$", "> $$")
# And also replace empty blockquote with nothing if it was added?
# Wait, original was `> $$`. New is `>\n\n$$`.
# Replacing `>\n\n$$` with `> $$` restores it.
# Wait, `fix_mdx_syntax.py` added `\n\n` AFTER the matched character.
# Regex was: `re.sub(r'([^\n])\s*\$\$\s*\n', r'\1\n\n$$\n', updated)`
# It matched `> $$`, so `\1` is `>`.
# Result is `>\n\n$$\n`.
# What about the closing `$$`?
# Original closing was `> $$`. It matched `> $$`, result `>\n\n$$\n`.
# So EVERY `> $$` became `>\n\n$$\n`.
# To fix this, we ONLY need to reverse this exact transformation!

with open("test_diff.txt", "w", encoding="utf-8") as f:
    f.write("Replacing '>\n\n$$' with '> $$':\n")
    fixed = content.replace(">\n\n$$", "> $$")
    if fixed != content:
        f.write("Found and fixed.\n")
    else:
        f.write("Not found.\n")

