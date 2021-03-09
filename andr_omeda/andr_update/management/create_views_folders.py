import os
import environ
from pathlib import Path
from os.path import isfile, join

curr_dir = Path(__file__).resolve(strict=True).parent.parent
models_dir = curr_dir / "models"
views_dir = curr_dir / "views"

defined_types = [f_name for f_name in os.listdir(models_dir) if isfile(join(models_dir, f_name))]
defined_types.remove('__init__.py')
defined_types = [f[:-3] for f in defined_types]

for file in defined_types:
    path = views_dir / file
    if os.path.isdir(path):
        if not len(os.listdir(path)) == 0:
            print("skipping directory %s \n DIRECTORY NOT EMPTY \n" % path.absolute())
            continue
        os.rmdir(path)
    else:
        os.mkdir(path)

    with open(os.path.join(path, "serializers.py"), 'w+') as temp_file:
        temp_file.write("# automatically created")
    with open(os.path.join(path, "views.py"), 'w+') as temp_file:
        temp_file.write("# automatically created")
    with open(os.path.join(path, "__init__.py"), 'w+') as temp_file:
        temp_file.write("# automatically created")

print("Done !")
