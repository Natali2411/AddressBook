import pymysql.cursors
from models.group import Group

# Connect to the database
connection = pymysql.connect(host='192.168.0.195',
                             user='root',
                             password='',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `group_name`, 'group_header', 'group_footer', 'group_id' FROM `group_list`"
        cursor.execute(sql)
        result = cursor.fetchall()
        groops = []
        for g in result:
            groops.append(Group(name=g['group_name'], header=g['group_header'], footer=g['group_footer']))
        print(groops)
        connection.commit()
finally:
    connection.close()