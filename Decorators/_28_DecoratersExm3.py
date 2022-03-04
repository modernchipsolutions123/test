
def login_required(f1):
    def inner(name,is_login):
        if is_login == False:
            print("Kindly login!")
            return
        return f1(name,is_login)
    return inner


@login_required
def home(name,is_login):
    print("Welcome to home of our website!")

@login_required
def orders(name,is_login):
    print("Welcome to orders of our website!")

def about():
    print("Welcome to about section of our website")


home('User',False)

orders('User',True)
about()