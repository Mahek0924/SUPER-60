rec={"name":1,"age":2}
id1 = id(rec)
del rec
rec={"name":1,"age":2}
id2 = id(rec)
print(id1 == id2)
#true beacuse it assigns same value