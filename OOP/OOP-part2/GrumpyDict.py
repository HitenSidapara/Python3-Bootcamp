class GrumyDict(dict):
    def __repr__(self):
        print("Local Method __repr__ not printing Dict.")
        return super().__repr__()

    def __missing__(self, key):
        print(f"Your Key {key} is not find in Dict.")

    def __setitem__(self, key, value):
        print("You Are Want To Change Dictionary?")
        print("Ok Fine...")
        return super().__setitem__(key,value)

    def __contains__(self, item):
        print("Checking the item  in list ......")
        return super().__contains__(item)

g = GrumyDict({"name":"Hiten","Age":19})
print(g)
g["city"]="Junagadh"
print(g)

print('city' in g)
print('village' in g)