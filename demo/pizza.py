###调用模块的函数####
def make_pizza(size, *toppings):
    '''调用模块的内容'''
    print('制作一个' + str(size) + "寸的披萨")
    print('需要的陷:')
    for topping in toppings:
        print('--->' + topping)
