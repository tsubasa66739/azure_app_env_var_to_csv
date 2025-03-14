# Usage

Get json from App Service environment variable and save it locally.

Run the script.

```bash
$ python azure_app_env_var_to_csv.py file1.json file2.json file3.json
Name,Value1,Value2,Value3,SlotSetting
<key-1>,<value-1>,<value-1>,,○
<key-2>,<value-2>,<value-2>,,
<key-3>,<value-3>,<value-3>,,○
<key-4>,,,<value-4>,○
<key-5>,,<value-5>,,○
```
