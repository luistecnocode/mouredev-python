### Type Hints ###
### Es una forma de forzar el tipo de dato dado que Python es tipado dinámico
### En realidad no sirve más que para ayudar al editor y a FASTApi
### Segurirá siendo de tipado dinámico
# Para hacer un type, se pone variable: str = "Hola"

my_string_variable = "My String variable"
print(my_string_variable)
print(type(my_string_variable))

my_string_variable = 5
print(my_string_variable)
print(type(my_string_variable))

my_typed_variable: str = "My typed Dtring variable"
print(my_typed_variable)
print(type(my_typed_variable))

my_typed_variable = 5
print(my_typed_variable)
print(type(my_typed_variable))