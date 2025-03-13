import sys
import pandas as pd

file_list = sys.argv
file_list.pop(0)

if len(file_list) > 5:
    sys.exit(f"Too many files expected: {len(file_list)}")

columns = ["Name"]
dfs = []
name_set = set()
for i, f in enumerate(file_list):
    df = pd.read_json(f)
    dfs.append(df)
    columns.append(f"Value{i+1}")
    for n in df.name:
        name_set.add(n)
columns.append("SlotSetting")

values = []
for n in name_set:
    setting = dfs[0].query(f'name == "{n}"').slotSetting
    cols = []
    cols.append(n)
    for d in dfs:
        col = d.query(f'name == "{n}"').value
        cols.append("" if col.empty else col.iloc[-1])
    if not setting.empty:
        cols.append("○" if setting.iloc[-1] else "")
    else:
        cols.append("")
    values.append(cols)

merged_df = pd.DataFrame(values, columns=columns)
print(merged_df.sort_values("Name").to_csv(index=None))