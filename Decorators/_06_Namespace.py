'''
NAMESPACE : Namespace is basically a system which will controll all the names in your prg which will be use in
            your prg and it allow us to reuse the name
         It will assure that whatever the names we use is unic.it won't lit to any conflit
         x =4
         print(x)-->4
         x = 5
         print(x) -->5
 When we reuse the name we may loss some data i.e.,we can't acess that data
'''
x =4
print(x)
x = 5
print(x)

#1.Built-in NameSapace -->Python interpeter (dir())
#2.Global Name space -->import module -->Every module has a name(2 files to import another file)
#3.Local Name space -->when we call a function it will create its own namespace