# chapter 2.4
# Subject: zagneżdżone if
# Time: 8 minutes
# GO!

def switch(args):
    swicher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return swicher.get(args, "default")

print("#1 switch")
print(switch(1))

def two():
    return "two"

def spok(args):
    return {
        0: "zero",
        1: "one",
        2: two(),
    }.get(args)

print("#2 swich #1 run")
print(spok(1))
print("#2 swich #2 run")
print(spok(2))

