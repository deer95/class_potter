class Wizard:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def motion(self, direction):
        hierarchy = hierarchy1 if type(self) == Order else hierarchy2
        dec_degree = hierarchy.index(self.status)
        if direction == '<' and dec_degree != len(hierarchy) - 1:
            self.status = hierarchy[dec_degree + 1]
        elif direction == '>' and self.status != 0:
            self.status = hierarchy[dec_degree - 1]
        else:
            print('You have reached exterme values')

    def is_angry(self, victim, defence):
        if defence == True:
            print('Sorry, the defence is strong today')
        else:
            victim.motion('<')
            if isinstance(victim, Order) is True:
                print('Oh no, Dumbledore is demoted')
            else:
                print('Due to justice Malfoy was demoted')



class Order(Wizard):
    def __init__(self, name, status):
        Wizard.__init__(self, name, status)
        self.status = hierarchy1[status]



class Enemy(Wizard):
    def __init__(self, name, status, satisfied = True):
        Wizard.__init__(self, name, status)
        self.status = hierarchy2[status]
        self.satisfied = satisfied



class SuperWizard(Wizard):
    def __init__(self, name, satisfied = True):
        Wizard.__init__(self, name, status = 'minister for magic')
        self.satisfied = satisfied




hierarchy1 = ['minister for magic',     'headmaster of Hogwarts',   'deputy headmaster',
              'head of a house',        'teacher',                  'Order member',
              'unemployed',             'prisoner of azkaban']

hierarchy2 = ['dark lord',              'right-hand man',           'respected death eater',
              'spy',                    'catchers of the Order',    'usual death eater',
              'prisoner',               'dead']