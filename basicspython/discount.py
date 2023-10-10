crnt_prc=89
dsct_perc=5
print("current price=",crnt_prc)
print("discount =",dsct_perc,"%")
dic_amt=(dsct_perc*crnt_prc)/100  #amount=(discount prcentage*whole amount)/100
sel_prc=crnt_prc-dic_amt
print("payable price=",sel_prc)