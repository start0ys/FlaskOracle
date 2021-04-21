from typing import Text
import cx_Oracle

def getConnection():
    connection = cx_Oracle.connect("hr", "1234", "localhost:1521/xe")
    return connection


def test():
    connection = getConnection()
    cursor = connection.cursor()


    sql = "select * from writertext order by create_date"
   
    cursor.execute(sql)
    connection.commit()

        
    return cursor

def test2(name,password,content):
    connection = getConnection()
    cursor = connection.cursor()


    sql1="insert into writertext(id,writer,text,pw) values (auto_id.nextval,:1,:2,:3)"
    add_db = []
    add_db.append(name)
    add_db.append(content)
    add_db.append(password)
    cursor.execute(sql1,add_db)
    
    connection.commit()
    cursor.close()

def test3(id):
    connection = getConnection()
    cursor = connection.cursor()
    id = int(id)

    sql1="delete writertext where id = :1"
   
    cursor.execute(sql1,(id,))
    
    connection.commit()
    cursor.close()

def test4(id,content):
    connection = getConnection()
    cursor = connection.cursor()
    id = int(id)


    sql1="update writertext set text = :1 where id = :2"
   
    cursor.execute(sql1,(content,id,))
    
    connection.commit()
    cursor.close()
    
    
 
        
 
  
   

    
test()
  
        
  

   
   
   




    # sql = "select * from departments where department_id = :dno"
    # cursor.execute(sql, (80,))
    # for result in cursor :
    #     print(result)

    # try:
        
    #     return cursor
  
    # except:
    #     return False