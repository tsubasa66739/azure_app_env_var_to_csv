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
    cols = []
    cols.append(n)

    # Append values
    for d in dfs:
        col = d.query(f'name == "{n}"').value
        cols.append("" if col.empty else col.iloc[-1])

    # Append slotSettings
    settings = []
    for df in dfs:
        setting = df.query(f'name == "{n}"').slotSetting
        settings.append(False if setting.empty else setting.iloc[-1])
    cols.append("○" if True in settings else "")

    values.append(cols)

merged_df = pd.DataFrame(values, columns=columns)

print(merged_df.sort_values("Name").to_csv(index=None))

# Comment out if you want to output to excel file.
# merged_df.sort_values("Name").to_excel("output.xlsx", index=None)