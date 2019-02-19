# Anthony Magno - 2019/02/18
# Quick script to output an annoying discord command from provided data
###############################################################################

def printCommand():
    print("input blob or EXIT to quit: ")
    blob = []
    while True:
        try:
            line = input("")
            if not line:
                raise EOFError
        except EOFError:
            break
        blob.append(line)
    if(blob[0] == "EXIT"):
        return False

    name = blob[0].split(' ')[-1]
    hp = int(blob[4].split(' ')[-1].split('/')[0])
    hp -= 1 if hp >0 else 0
    atk = int(blob[5].split(' ')[-1].split('/')[0])
    atk -= 1 if atk >0 else 0
    defense = int(blob[6].split(' ')[-1].split('/')[0])
    defense -= 1 if defense >0 else 0
    spatk = int(blob[7].split(' ')[-1].split('/')[0])
    spatk -= 1 if spatk >0 else 0
    spdef = int(blob[8].split(' ')[-1].split('/')[0])
    spdef -= 1 if spdef >0 else 0
    speed = int(blob[9].split(' ')[-1].split('/')[0])
    speed -= 1 if speed >0 else 0
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
