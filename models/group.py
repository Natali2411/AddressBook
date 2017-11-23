class Group:
    def __init__(self, name='', header='', footer='', id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id


    def __str__(self):
        return  "Group: {}, {}, {}, {}".format(self.id, self.name, self.header, self.footer)

    def __repr__(self):
        return "Group: {}, {}, {}, {}".format(self.id, self.name, self.header, self.footer)

    def __eq__(self, other):
        return self.name == other.name and self.header == other.header and self.footer == other.footer

#if __name__ == '__main__':

