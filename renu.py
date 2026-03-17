import os
import re

folder = r"E:\Music Py\Abel"

def safe_rename(path, new_name):
    base, ext = os.path.splitext(new_name)
    counter = 1
    final = new_name

    while os.path.exists(os.path.join(path, final)):
        final = f"{base}_{counter}{ext}"
        counter += 1

    return final

for f in os.listdir(folder):
    new = re.sub(r'^(\d+\s*-\s*)+', '', f)

    if new != f:
        new = safe_rename(folder, new)
        os.rename(
            os.path.join(folder, f),
            os.path.join(folder, new)
        )
