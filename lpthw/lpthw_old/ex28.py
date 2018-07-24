print (True and True,
False and True,
1 == 1 and 2 == 1,
"test" == "test",
1 == 1 or 2 != 1,
True and 1 == 1,
False and 0 != 0,
True or 1 == 1,
"test" == "testing",
1 != 0 and 2 == 1,
"test" != "testing",
"test" == 1,
not (True and False), # 13True
not (1 == 1 and 0 != 1), # 14False
not (10 == 1 or 1000 == 1000), # 15False
not (1 != 10 or 3 == 4), # 16False
not ("testing" == "testing" and "Zed" == "Cool Guy"), # 17True
1 == 1 and (not ("testing" == 1 or 1 == 0)), # 18True
"chunky" == "bacon" and (not (3 == 4 or 3 == 3)), # 19False
3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")) # 20False)
 )