class CppFaker:
    def __init__(self, initial):
        self.fakes = initial

    def get_fakes(self):
        return self.fakes

    def insert_member(self, parent, member):
        for fake in self.fakes:
            if fake['name'] == parent:
                if 'members' not in fake:
                    fake['members'] = []
                for m in fake['members']:
                    if 'name' in m and m['name'] == member['name']:
                        return
                fake['members'].append(member)
                return
        print '{} not found'.format(parent)

    def update_type(self, fakename, newtype):
        for fake in self.fakes:
            if fake['name'] == fakename:
                fake['type'] = newtype
                return
        print '{} not found'.format(fakename)

    def update_declaration(self, fakename, decl):
        for fake in self.fakes:
            if fake['name'] == fakename:
                fake['declaration'] = decl
                return
        print '{} not found'.format(fakename)

    def insert_definition(self, definition):
        for fake in self.fakes:
            if fake['name'] == definition['name']:
                return
        self.fakes.append(definition)

    def process_line(self, line):
        filename, linenum, position, msgtype, errmsg = line
        if msgtype != 'error':
            pass
        elif errmsg[0] == 'unknown type name':
            fake = {"type": "class", "name": errmsg[1]}
            self.insert_definition(fake)
        elif errmsg[0] == 'use of undeclared identifier':
            fake = {"type": "class", "name": errmsg[1], "members":[]}
            self.insert_definition(fake)
        elif errmsg[0] == 'no member named' and errmsg[2] == 'in':
            member = {
                "type": 'method',
                "access": 'public',
                "declaration":"void ()",
                "name": errmsg[1]
            }
            self.insert_member(errmsg[3], member)
        elif errmsg[0] == '' and errmsg[2] == 'does not refer to a value':
            self.update_type(errmsg[1], 'field')
            self.update_declaration(errmsg[1], 'int')
