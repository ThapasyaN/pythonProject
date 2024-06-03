# functions with outputs

def function_output(f_name, l_name):
    if f_name == "" or l_name == "":
        return "invalid input"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    # print(f"{formated_f_name} {formated_l_name}")
    #     or
    return f"{formated_f_name} {formated_l_name}"


print(function_output((input("Enter your first name- ")), input("Enter your last name- ")))









# the word return replaces the function_output with the result
# function_output("ThaPASYA", "NadigoTTI")
# or
# formated_string = function_output("ThaPASYA", "NadigoTTI")
# print(formated_string)
# or
# you can directly print
# print(function_output("ThaPASYA", "NadigoTTI"))
