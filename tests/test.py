import random

input_file = r"e:\git_repositories\plotfig\src\plotfig\data\neurodata\atlases\macaque_D99\label.txt"
output_file = r"e:\git_repositories\plotfig\src\plotfig\data\neurodata\atlases\macaque_D99\label1.txt"

with open(input_file, "r", encoding="utf-8") as fin, \
    open(output_file, "w", encoding="utf-8") as fout:

    for idx, line in enumerate(fin, start=1):
        region_name = line.rstrip("\n")
        fout.write(region_name + "\n")

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        # 写格式：序号, r, g, b, 255
        fout.write(f"{idx} {r} {g} {b} 255\n")
