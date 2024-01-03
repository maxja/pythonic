"""
Uname output processor

This is a simple processor, that awaits `uname -a` output as an input
parse line and output as a attributes table.

This is a format uname -a produces:
`{sysname} {nodename} {release} {version} {machine}\n`

Use:
uname -a | python .
"""
sysname, nodename, release, rest = input()\
  .split(' ', 3) # (1)

_, machine = rest\
  .rstrip(' ()/1GLMNSUWdgiilmnnosuwx')\
  .rsplit(' ', 1) # (2)

uname_params = {
  'sysname': sysname,
  'nodename': nodename,
  'release': release,
  'machine': machine
} # (3)

columns_widths = tuple(
  map(
    max,
    zip(
      map(len, uname_params.keys()),
      map(len, uname_params.values())
    ) # (4)
  ) # (5)
) # (6)

separator_row = """|-{0:-<{1}}-|-{0:-<{2}}-|-{0:->{3}}-|-{0:-<{4}}-|""".format(
  '-',
  *columns_widths  # (7)
)  # (8)

head_row = """| {0: <{4}} | {1: <{5}} | {2: >{6}} | {3: <{7}} |""".format(
  *(tuple(
      map(str.capitalize, uname_params.keys()) # (9)
  ) + columns_widths) # (10)
)

value_row = f"| %(sysname) -{columns_widths[0]}s \
| %(nodename) -{columns_widths[1]}s \
| %(release) +{columns_widths[2]}s \
| %(machine) -{columns_widths[3]}s |" % uname_params # (11)

print(
  '\n'.join([
    separator_row,
    head_row,
    separator_row,
    value_row,
    separator_row,
  ]) # (12)
) # (13)
