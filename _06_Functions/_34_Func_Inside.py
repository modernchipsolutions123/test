def get_data():
    resp = medium(foo,10)
    return resp
def medium(fun_name,var):
    out = fun_name(var)
    return out
def foo(var):
    return var + 2
final_res = get_data()
print(final_res)

def dis():
    re1 = msg(f1,str)
    return re1
def msg(f1,str):
    re2 = f1('gani')
    return re2
def f1(str):
    return str + ' Kadali'
op = dis()
print(op)
