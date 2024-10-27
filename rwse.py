class ClosureClass:
    def __init__(self, value):
        self.value = value

    def create_closure(self):
        def closure():
            return self.value
        return closure

obj = ClosureClass(10)
closure_func = obj.create_closure()

print(closure_func())  
