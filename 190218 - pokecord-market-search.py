# Anthony Magno - 2019/02/18
# Quick script to output an annoying discord command from provided data
###############################################################################

def printCommand():
    name = input("input species name or EXIT to quit: ")
    if(name == "EXIT"):
        return False
    hp = int(input("HP: "))
    hp -= 1
    atk = int(input("ATK: "))
    atk -= 1
    defense = int(input("DEF: "))
    defense -= 1
    spatk = int(input("SPATK: "))
    spatk -= 1
    spdef = int(input("SPDEF: "))
    spdef -= 1
    speed = int(input("SPEED: "))
    speed -= 1
    while True:
        print("p!market search --name %s --hpiv > %s --atkiv > %s --defiv > %s --spatkiv > %s --spdefiv > %s --speediv > %s --order price a --showiv" % (name, hp, atk, defense, spatk, spdef, speed))
        decrement = input("Decrement numbers? (y/n) ")
        if(decrement == "y"):
            hp -= 1 if hp >0 else 0
            atk -= 1 if atk >0 else 0
            defense -= 1 if defense >0 else 0
            spatk -= 1 if spatk >0 else 0
            spdef -= 1 if spdef >0 else 0
            speed -= 1 if speed >0 else 0
        else:
           break
    return True

loop = True
while(loop):
    loop = printCommand()
