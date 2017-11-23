import pymysql
from models.group import Group

class AddressBookDB:
    def __init__(self, **config):
        self.connection = pymysql.connect(**config, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    def get_groups(self):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT group_name, group_header, group_footer, group_id FROM `group_list` order by 'group_id' desc"
            cursor.execute(sql)
            groups = []
            for g in cursor:
                groups.append(Group(id=g["group_id"], name=g['group_name'], header=g['group_header'], footer=g['group_footer']))
        self.connection.commit()
        return groups
'''
    def get_groups_id(self):
        id_list = []
        for t in self.get_groups():
            if str(t).startswith("Group:"):
                id_list.append(t[7])
        return id_list
        '''

    def close(self):
        self.connection.close()