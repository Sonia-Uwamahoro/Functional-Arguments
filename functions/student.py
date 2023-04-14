

def year_of_birth(name, age):
    year = 2023 - age
    print(f"hello {name}, you were born in {year}")


# a function have an optional return keyword which return an output and ends the function.


# -- keyword and positional arguments -- #


# position arguments are passed to the function based on their order in the function definition.
# keyword arguments are passed to the function by explicity specifying the name of the argument.  
                             
# positional arguments (each argument must be in the same position as you defined them when calling)
 
year_of_birth("sonia", 10)
year_of_birth(name ="sonia", age=10)


def concatenate_kwargs(**kwargs):
    languages = ""
    for key, value in kwargs.items():
        languages += (f"{key}:{value}")
    print(languages)

concatenate_kwargs(one="hdgdg", two="ghdhd")













