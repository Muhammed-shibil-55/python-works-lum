# 1800-2024 all years append in list

years=[y for y in range(1800,2025)]
# print(years)

century_yr=[y for y in years if y%100==0]

print(century_yr)

noncentury_yrs=[y for y in years if y%100!=0]
print(noncentury_yrs)