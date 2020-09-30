def info_kwargs(**kwargs):
    for k,v in sorted(kwargs.items()):
        print(k, '=', v)

    
info_kwargs(first_name="John", last_name="Doe", age=33) 
