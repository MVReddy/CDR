class A:
    def my_func(self):
        print('Inside parent func')


class B(A):
    def my_func(self):
        import pdb; pdb.set_trace()
        print('Inside child func')


b = B()
b.my_func()
