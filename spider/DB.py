import pymysql

class DB:

    def __init__(self):
        self.__host="119.29.185.127"
        self.__dbU="gjz"
        self.__dbP="gjz509"
        self.dbN="bm"
        db=pymysql.connect(self.__host,self.__dbU,self.__dbP,self.dbN,charset="utf8")

# cussor=db.cursor()
# cussor.execute("select * from t_document")
# data=cussor.fetchone()
# print(data)
#
# db.close()