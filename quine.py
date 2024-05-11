import re
o = "import re\\no = \\\"{x}\\\"\\ny = re.sub(r\\\"\\\\\\\\\\\", r\\\"\\\\\\\\\\\\\\\\\\\", o)\\nx = re.sub(r\\\"\\\\\\\"\\\", r\\\"\\\\\\\"\\\", y)\\nprint(f\\\"{o}\\\")"
y = re.sub(r"\\", r"\\\\", o)
x = re.sub(r"\"", r"\"", y)
print(f"import re\no = \"{x}\"\ny = re.sub(r\"\\\\\", r\"\\\\\\\\\", o)\nx = re.sub(r\"\\\"\", r\"\\\"\", y)\nprint(f\"{o}\")")
