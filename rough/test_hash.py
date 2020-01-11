int_val = 4
name_1 = "sankarshan"
name_2 = "sudipa"

M = 30
print(hash(int_val))
print(hash(name_1)%M)
print(hash(name_2)%M)

assert hash(name_1) == hash(name_1), "Object not same"
