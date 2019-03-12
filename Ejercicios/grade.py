import hashlib

def Exo1(guess):
    if hashlib.sha256(str(guess).encode()).hexdigest() == "eabee6aaeeceb344e06c13b827b56eba0b7137b614599d6f46780108af531f82":
        print("Lo lograste! :v")
        return True
    else:
        print("Instarreprobado >:v")
        return False

def Exo2(guess):
    if hashlib.sha256(str(guess).encode()).hexdigest() == "e85a870aeb6eed9e560269c22f3f3d0823a5a1aa6536bb1bf8d90621b9e70fd1":
        print("Lo lograste! :v")
        return True
    else:
        print("Instarreprobado >:v")
        return False