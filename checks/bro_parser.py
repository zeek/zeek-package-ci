import os
def bro_files(root_dir):
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
    loaded = []
    base_dir = os.path.dirname(bro_script)
    with open(bro_script) as f:
        for line in f:
            if line.lstrip().startswith("@load"):
                arg = line.split("@load")[1]
                arg = arg.split("#")[0] # strip any comment
                arg = arg.strip()
                loaded.append(os.path.join(base_dir, arg))
    return loaded

def expand_load(bro_scripts):
    all_bro_scripts = bro_scripts
    todo = bro_scripts
    while todo:
        next_todo = []
        for f in todo:
            loaded_scripts = extract_load(f)
            all_bro_scripts.extend(loaded_scripts)
            next_todo.extend(loaded_scripts)
        todo = next_todo
    return all_bro_scripts
