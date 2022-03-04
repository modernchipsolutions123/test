def login_required(f1):
    def inner(name,is_login):
        if is_login == False:
            print('Kindly login')
            return
        return f1(name,is_login)
    return inner
@login_required
def home(name,is_login):
    print("Welcome to home page of our website")
@login_required
def orders(name,is_login):
    print('Welcome to order page of our website')
def about():
    print('Welcome to about section of our website')
    #Normal function call
#home("sai",123) #
#orders("gani",456)
#about()
home('user',True)
orders('user',True)
about()