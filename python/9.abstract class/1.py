from abc import ABC, abstractmethod
class MyAbstractClass(ABC):
    def non_abstract_method(self):
        print("This is a non-abstract method")

    @abstractmethod
    def abstract_method(self):
        pass

#2
class ChildClass(MyAbstractClass):
    def abstract_method(self):
        print("Abstract method implemented in ChildClass")

child = ChildClass()
child.non_abstract_method()

#3.
child = ChildClass()
child.abstract_method()

#4.
child = ChildClass()
child.non_abstract_method()
