from binascii import b2a_hex, a2b_hex
#
import pymysql
from ecies import encrypt, decrypt
import keyring
# # # 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "shamir_key_two")
# #
# # # 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# # product_id = 1
# # sql = "SELECT * FROM apps_key_db_one WHERE productId = %s" % (product_id)
# # # 使用 execute()  方法执行 SQL 查询
# # cursor.execute(sql)
# #
# # # 使用 fetchone() 方法获取单条数据.
# # data = cursor.fetchone()
# #
# # print(data[2])
# #
# # # print("Database version : %s " % data)
# #
# # # 关闭数据库连接
# # db.close()
#
sql = "SELECT * FROM apps_key_db_two WHERE productId = %s" % (int(5))
cursor.execute(sql)
data = cursor.fetchone()
print(data[2])
# encrypt_key = b2a_hex(encrypt('0xbc52226077d7822be37d446c56408d329f7fdd3c18d416f319d17eebfa8f63292f94191ed126fa268888dd333fc193d654a9b478152a98f0102c5ac4fdf74afa', '1-c23be64e88e9c493233f980ba2f5c87856b336b7000593a048a0008f66f8974a'.encode())).decode()
# print(b2a_hex(a2b_hex(encrypt_key)).decode())
# key = "04357a6a0e583b065ddf32fdb7bb51e9d5c8475258ae08fcb38ee7c9b7f98dfa1c684eedec4c877a2d2251921d92a0f17750b56208cb8d3284df83cf315f4fad69aae0a71a39eefa6c81bfd721034eab8730815feee190e93f13b61c50450e60a6728b99f16b019639ef08226f88507803705e8e103cfc13f71286cb4c665a178c2966b122d06efb0a523b1e44dfd47c80dea437508acb37f6914f7b13e6636cbe67b9"
# print(decrypt(keyring.get_password("DRMDEMO","keyManagerOnePrivate"),a2b_hex(key)))
# print(b'123'.decode())