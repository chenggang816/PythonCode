class Student(object):
    def __init__(self,name):
        self.name = name

    def print_name(self):
        print self.name

if __name__=='__main__':
    a = Student('cg')
    a.print_name()
    print a.name
    a.age = 23
    print a.age