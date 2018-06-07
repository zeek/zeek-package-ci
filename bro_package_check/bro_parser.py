import os
import sys

def bro_files(root_dir):
    """Return all .bro scripts inside root_dir
       including scripts that are @load'ed from other bro scripts
       but do not have a .bro extension
    """
    all_bro_scripts = []
    other_files = []
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            full_path = os.path.join(root, f)
            if full_path.lower().endswith(".bro"):
                all_bro_scripts.append(full_path)
            else:
                other_files.append(full_path)

    if not other_files:
        return all_bro_scripts
    else:
        return expand_load(all_bro_scripts)

def extract_load(bro_script):
    if not os.path.exists(bro_script):
        return []
    loaded = []
    base_dir = os.path.dirname(bro_script)
    with open(bro_script, errors='replace') as f:
        for line in f:
            if line.lstrip().startswith("@load"):
                arg = line.split("@load")[1]
                arg = arg.split("#")[0] # strip any comment
                arg = arg.strip()
                full_path = os.path.join(base_dir, arg)
                if os.path.isfile(full_path + ".bro"):
                    full_path = full_path + ".bro"

                if os.path.isdir(full_path):
                    # Nothing to do, as this directory would have been included already by bro_files
                    pass
                else:
                    loaded.append(full_path)
    return loaded

def expand_load(bro_scripts):
    all_bro_scripts = bro_scripts
    todo = bro_scripts
    while todo:
        next_todo = []
        for f in todo:
            loaded_scripts = extract_load(f)
            normalized = [os.path.normpath(fn) for fn in loaded_scripts]
            not_seen = set(normalized) - set(all_bro_scripts)
            next_todo.extend(not_seen)
            all_bro_scripts.extend(not_seen)
        todo = next_todo
    return all_bro_scripts

DELIMS = set("\t (){}|:;")
def tokenize_line(line):
    """Tokenize a bro line.
    This sucks, but should work well enough to tell code from 
    comments and strings"""

    in_string = False
    tok = ''
    prev_ch = ''
    for idx, ch in enumerate(line):
        if ch == '"' and prev_ch != '\\':
            in_string = not in_string
            if not in_string:
                yield 'STRING', tok
                tok=''
        elif ch == '#' and not in_string:
            yield 'COMMENT', line[idx:]
            return
        elif in_string:
            tok += ch
        elif ch in DELIMS:
            if tok:
                yield 'TOKEN', tok
            tok=''
        else:
            tok += ch
        prev_ch = ch
            

def bro_tokens(fn):
    if not os.path.exists(fn):
        return
    with open(fn, errors='replace') as f:
        for n, line in enumerate(f, start=1):
            line = line.rstrip()
            yield n, line, list(tokenize_line(line))
