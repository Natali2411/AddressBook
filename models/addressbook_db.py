import pymysql
from models.group import Group
import csv

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

    def get_groups_id(self):
         id_list = []
         with self.connection.cursor() as cursor:
                # Read a single record
             sql = "SELECT group_id FROM `group_list`"
             cursor.execute(sql)
             for g in cursor:
                id_list.append(g["group_id"])
         self.connection.commit()
         return id_list

    def imoprt_groups(self):
        with self.connection.cursor() as cursor:
            with open('groups.csv', 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Skip the header row.
                for row in reader:
                    cursor.execute("INSERT INTO `group_list` (group_name, group_header, group_footer) VALUES (%s, %s, %s)", row)
                    cursor.execute("commit")
            count_gr = cursor.execute("SELECT count(*) FROM `group_list`")
        self.connection.commit()
        return count_gr

    def clean_groups(self):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "DELETE * FROM `group_list`"
            cursor.execute(sql)
            cursor.execute("commit")
            count_gr = cursor.execute("SELECT count(*) FROM `group_list`")
        self.connection.commit()
        return count_gr

    def close(self):
        self.connection.close()