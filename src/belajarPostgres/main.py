from abc import ABCMeta,abstractmethod
import psycopg2,sys
class KerangkaDatabase(metaclass=ABCMeta):
    @abstractmethod
    def insert(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def delete(self):
        pass
class Database(KerangkaDatabase):
    def __init__(self,insertIdBarang=None,insertNamaBarang=None,insertQtyBarang=None,insertValueBarang=None):
        self.__idBarang = insertIdBarang
        self.__namaBarang = insertNamaBarang
        self.__qtyBarang = insertQtyBarang
        self.__valuesBarang = insertValueBarang
    def getIdBarang(self):
        return self.__idBarang
    def getNamaBarang(self):
        return self.__namaBarang
    def getQtyBarang(self):
        return self.__qtyBarang
    def getValuesBarang(self):
        return self.__valuesBarang
    def setIdBarang(self,insertIdBarang):
        self.__idBarang = insertIdBarang
    def setNamaBarang(self,insertNamaBarang):
        self.__namaBarang = insertNamaBarang
    def setQtyBarang(self,insertQtyBarang):
        self.__qtyBarang = insertQtyBarang
    def setValueBarang(self,insertValueBarang):
        self.__valuesBarang = insertValueBarang
    def insert(self):
        try:
            conn = psycopg2.connect(
                database = 'db_belajar_postgres',
                host = 'localhost',
                port = '5432',
                user = 'postgres',
                password = 'Seger123'
            )
            curr = conn.cursor()
            data = (self.__namaBarang,self.__qtyBarang,self.__valuesBarang)
            sql = '''
                insert into barang(nama_barang,qty_barang,value_barang)
                 VALUES(%s,%s,%s);
            '''
            try:
                curr.execute(sql, data)
            except:
                conn.rollback()
                sys.exit()
            else:
                conn.commit()
                curr.close()
        except:
            print('Can\'t Reach Database')
        else:
            conn.close()
    def update(self):
        pass
    def delete(self):
        pass
    def getAll(self):
        try:
            conn = psycopg2.connect(
                database='db_belajar_postgres',
                host='localhost',
                port='5432',
                user='postgres',
                password=''
            )
            curr = conn.cursor()
            sql = '''
                SELECT * FROM barang
            '''
            curr.execute(sql)
            result = curr.fetchall()
            return result
        except psycopg2.DatabaseError as e:
            print('Error : %s'%e)

def main():
    myDatabase = Database()
    result =  myDatabase.getAll()
    for row in result:
        idBarang = row[0]
        namaBarang = row[1]
        qtyBarang = row[2]
        valueBarang = row[3]
        print(idBarang,'\t',namaBarang,'\t',qtyBarang,'\t',valueBarang)
    insertNamaBarang = input('Nama Barang : ')
    insertQtyBarang = input('Qty Barang : ')
    insertValueBarang = input('Value Barang : ')
    myDatabase.setNamaBarang(insertNamaBarang)
    myDatabase.setQtyBarang(insertQtyBarang)
    myDatabase.setValueBarang(insertValueBarang)
    myDatabase.insert()
    for row in result:
        idBarang = row[0]
        namaBarang = row[1]
        qtyBarang = row[2]
        valueBarang = row[3]
        print(idBarang, '\t', namaBarang, '\t', qtyBarang, '\t', valueBarang)


if __name__ == "__main__":
    main()