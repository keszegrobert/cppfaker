class CppFaker:
    def __init__(self, filename):
        self.fakes = []

    def get_fakes(self):
        return self.fakes

    def insert_member(self, parent, member):
        for fake in self.fakes:
            if fake['name'] == parent:
                if 'members' not in fake:
                    fake['members'] = []
                fake['members'].append(member)
                return

    def process_line(self, line):
        filename, linenum, position, msgtype, errmsg = line
        if msgtype != 'error':
            pass
        elif errmsg[0] == 'unknown type name':
            fake = {"type": "class", "name": errmsg[1]}
            self.fakes.append(fake)
        elif errmsg[0] == 'use of undeclared identifier':
            fake = {"type": "class", "name": errmsg[1]}
            self.fakes.append(fake)
        elif errmsg[0] == 'no member named' and errmsg[2] == 'in':
            member = {"type": 'void', "name": errmsg[1]}
            self.insert_member(errmsg[3], member)
