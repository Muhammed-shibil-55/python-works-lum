from json import load
path="C:\\Users\\shibi\\Desktop\\py_lum\\countries\\countries.json"

with open(path,encoding="utf-8") as f:
    countries=load(f)

# print(len(countries))

country_name=[c.get("name") for c in countries]
# print(country_name)

# capital of china
country_capital=[c.get("capital") for c in countries if c.get("name")=="China"]
# print(country_capital)


regions={c.get("region") for c in countries}
# print(regions)

country_borders=[c.get("borders") for c in countries if c.get("name")=="India"][0]
# print(country_borders)
border_names=[c.get("name") for c in countries if c.get("alpha3Code") in country_borders]
# print(border_names)

# print independent country names
independent_countries=[c.get("name") for c in countries if c.get("independent")==True]
# print(independent_countries)

# print currency of india
indian_currency=[c.get("currencies")[0].get("name") for c in countries if c.get("name")=="India"]
# print(indian_currency)

country_no_curr=[c.get("name") for c in countries if "currencies" not in c]
# print(country_no_curr)

country_curr=[c.get("currencies")[0].get("name") for c in countries if "currencies" in c]
print(country_curr)
country_count={}
for c in country_curr:
    if c in country_count:
        country_count[c]+=1
    else:
        country_count[c]=1
print(max((v,k) for k,v in country_count.items()))
