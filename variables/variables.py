
first_name = " jawad"
last_name = "saleem "
full_name = first_name + last_name

# Change Case
print(full_name.title())
print(full_name.upper())
print(full_name.lower()) 


# Using variables in Strings & using f-strings (Formatted)
name = f"{first_name} {last_name}"
print(name)
print(f"Hello, {name.title()}!")

message = f"Goodbye, {name.title()}!"
print(message)

# addng white spaces \t \n
print("\t"+name)

# stripping white spaces
# lstrip() => left
# rstrip() => right
# strip    => both
print(name.strip())
