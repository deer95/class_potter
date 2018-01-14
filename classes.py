import Class_Wizards as wiz


def demote(causator, victim, defenders):
    defence = all([member.satisfied for member in defenders])
    causator.is_angry(victim, defence)

    print(victim.name, victim.status, sep=', ')
    print(causator.name, causator.status, sep=', ')


dumbledore  = wiz.Order('Albus Dumbledore', 1)
moody       = wiz.Order('Alastor Moody', 5)
order = {dumbledore, moody}

malfoy      = wiz.Enemy('Lucius Malfoy', 1)
voldemort   = wiz.Enemy('Voldemort', 0)
enemies = {malfoy, voldemort}

fudge = wiz.SuperWizard('Cornelius Fudge')
high_wizards = {fudge}

print('Persons who acting are:')
for person in (order | enemies | high_wizards):
    print(person.name, person.status, sep=', ')


while True:
    answer = input('\nWho is acting? If tired print "tired" ').lower()
    if answer == 'tired':
        break

    else:
        if answer == 'dumbledore':
            print('Now Voldemort is uneasy')
            voldemort.satisfied = False

        elif answer == 'lucius':
            demote(malfoy, dumbledore, high_wizards)
            voldemort.satisfied = True

        elif answer == 'fudge':
            print('Oh no, Dumbledore is in trouble')
            fudge.satisfied = False
            voldemort.satisfied = True

        elif answer == 'moody':
            demote(moody, malfoy, {voldemort})
            fudge.satisfied = True

        else:
            print('The answer wasn\'t recognized, please try again')