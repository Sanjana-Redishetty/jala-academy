class PublicExample:
    def __init__(self):
        self.data = "Public Field"

    def public_method(self):
        print("Public Method Called")

class AnyClass:
    def use_public(self):
        obj = PublicExample()
        print("Accessing public field:", obj.data)
        obj.public_method()

user = AnyClass()
user.use_public()
