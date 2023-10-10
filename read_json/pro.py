from json import load

path="C:\\Users\\shibi\\Desktop\\py_lum\\read_json\\data.json"
with open(path) as f:
    records=load(f)

print(records)

print(len(records))

fw_names=[f.get("name") for f in records]
print(fw_names)

top_fw=max(records,key=lambda d:d.get("rating"))
print(top_fw)

# print python frameworks
py_fw=[r.get("name") for r in records if r.get("language")=="python"]
print(py_fw)
# backend frameworks
bckend_fw=[r.get("name") for r in records if r.get("side")=="backend"]
print(bckend_fw)