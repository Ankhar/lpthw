tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
#\t is escape sentence that doing horisontal tab(TAB)
fat_cat = """
I'll do a list:
\t* Cat food 
\t* Fishies
\t* \nCatnip\n\t* Grass
"""
#print in one string with ecape sentence \n
print "%s\n%s\n%s\n%s" % (tabby_cat, persian_cat, backslash_cat, fat_cat)