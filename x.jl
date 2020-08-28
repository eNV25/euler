function input(prompt::String, type::Type=String)
    print(prompt)
    inp = readline()
    type == String ? inp : parse(type, inp)
end