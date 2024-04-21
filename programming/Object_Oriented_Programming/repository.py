# The Python Package Index (PyPI) is a repository of packages/software for the Python programming language.
# https://pypi.org/ -> Homepage( Documentation and GitHub page) and ChangeLog

# To use others code using packages. -> Each file in our project is a module in itself. Package -> Lots of file/modules
# to achieve a goal.

from prettytable import * # select 'go to' in settings and see implementations, etc. Note you can see main usage in
# documentations.

# Use Refactor -> Rename
table = PrettyTable()  # Creating a object of class  PrettyTable from prettytable package.
print(table)

print(table.field_names)  # empty
# NOTE: Attributes can be changed outside of objects methods , but avoid it generally. Use methods to change attributes, instead of doing directly
table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]  # Adding column names to attribute field_names
# of 'x'
table.add_row(["Adelaide", 1295, 1158259, 600.5])  # calling a method of our object 'x'
table.add_row(["Brisbane", 5905, 1857594, 1146.4])
table.add_row(["Darwin", 112, 120900, 1714.7])
table.add_row(["Hobart", 1357, 205556, 619.5])
table.add_row(["Sydney", 2058, 4336374, 1214.8])
table.add_row(["Melbourne", 1566, 3806092, 646.9])
table.add_row(["Perth", 5386, 1554769, 869.4])

# Can directly use this function
# x.add_column("City name",
# ["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
# x.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
# x.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092,
# 1554769])
# x.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9,
# 869.4])

# Changing objects attributes, people generally make getters and setters to change object attributes :
print(table.align)
table.align = "l"  # We changed the attribute from default "c" to "l".


print(table)


