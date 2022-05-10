import mysql.connector
from flask import session
from datetime import date
from datetime import timedelta

class DbOperation:

    def myconnection(self):
        db=mysql.connector.connect(host="localhost" ,user="root" ,password="root" ,database="binarybudget")
        return db

    def insert_customer(self,name,email,password):

          con=self.myconnection()
          sq="insert into customer(name,email,password) values(%s,%s,%s)"
          record = [name,email,password]
          mycursor=con.cursor()
          mycursor.execute(sq, record)
          con.commit()
          mycursor.close()
          con.close()
          return

    def custlogincheck(self,email,password):
             con=self.myconnection()
             sql="select email,password from customer where email=%s and password=%s"
             record=[email, password]
             mycursor=con.cursor()
             mycursor.execute(sql,record)
             row=mycursor.fetchall()
             rc=mycursor.rowcount
             mycursor.close()
             con.close()
             if rc==0:
                 return 0
             else:
                 session['email']=email       # from flask import session
                 return 1

    def insert_retailer(self,name,email,password):

          con=self.myconnection()
          sq="insert into retailer(name,email,password) values(%s,%s,%s)"
          record = [name,email,password]
          mycursor=con.cursor()
          mycursor.execute(sq, record)
          con.commit()
          mycursor.close()
          con.close()
          return

    def retailerlogincheck(self,email,password):
             con=self.myconnection()
             sql="select email,password from retailer where email=%s and password=%s"
             record=[email, password]
             mycursor=con.cursor()
             mycursor.execute(sql,record)
             row=mycursor.fetchall()
             rc=mycursor.rowcount
             mycursor.close()
             con.close()
             if rc==0:
                 return 0
             else:
                 session['email']=email       # from flask import session
                 return 1

    def update_retailer(self,email,name,pname,address,city,pincode,mobile,password,fnm):
          con=self.myconnection()
          sq="update retailer set name=%s,pname=%s,address=%s,city=%s,pincode=%s,mobile=%s,password=%s,image=%s where email=%s"
          record = [name,pname,address,city,pincode,mobile,password,fnm,session['email']]
          mycursor=con.cursor()
          mycursor.execute(sq, record)
          con.commit()
          mycursor.close()
          con.close()
          return

    def profile_retailer(self,email):
             con=self.myconnection()
             sql="select name,pname,address,city,pincode,mobile,password,image,banner from retailer where email=%s"
             record=[email]
             mycursor=con.cursor()
             mycursor.execute(sql,record)
             row=mycursor.fetchall()
             mycursor.close()
             con.close()
             return row

    def update_customer(self,email,name,mobile,location,dob,gender,password,fnm):
          con=self.myconnection()
          sq="update customer set name=%s,mobile=%s,location=%s,dob=%s,gender=%s,password=%s,dp=%s where email=%s"
          record = [name,mobile,location,dob,gender,password,fnm,session['email']]
          mycursor=con.cursor()
          mycursor.execute(sq, record)
          con.commit()
          mycursor.close()
          con.close()
          return

    def profile_customer(self,email):
             con=self.myconnection()
             sql="select name,mobile,location,dob,gender,dp,password from customer where email=%s"
             record=[email]
             mycursor=con.cursor()
             mycursor.execute(sql,record)
             row=mycursor.fetchall()
             mycursor.close()
             con.close()
             return row

    def member_insert(self,email,year,cur_date,exp_date,amount):
          con=self.myconnection()
          sq="insert into membership(cust_email,year,cur_date,exp_date,price) values(%s,%s,%s,%s,%s)"
          record = [email,year,cur_date,exp_date,amount]
          mycursor=con.cursor()
          mycursor.execute(sq, record)
          con.commit()
          mycursor.close()
          con.close()
          return

    def coupon_insert(self,email,validity,descp,couponcode,photo):
          con=self.myconnection()
          sq="insert into coupon(retail_email,validity,desp,couponcode,photo) values(%s,%s,%s,%s,%s)"
          record = [email,validity,descp,couponcode,photo]
          mycursor=con.cursor()
          mycursor.execute(sq, record)
          con.commit()
          mycursor.close()
          con.close()
          return

    def coupon_list(self,email):
             con=self.myconnection()
             sql="select desp,couponcode,photo,validity,idcoupon from coupon where retail_email=%s "
             record=[email]
             mycursor=con.cursor()
             mycursor.execute(sql,record)
             row=mycursor.fetchall()
             mycursor.close()
             con.close()
             return row

    def list_All_Coupons(self):
        con=self.myconnection()
        sql="select desp,couponcode,photo,validity from coupon "
        mycursor=con.cursor()
        mycursor.execute(sql)
        row=mycursor.fetchall()
        mycursor.close()
        con.close()
        return row

    def retailer_image(self):
        con=self.myconnection()
        sql="select image,name,email,banner from retailer"
        mycursor=con.cursor()
        mycursor.execute(sql)
        row=mycursor.fetchall()
        mycursor.close()
        con.close()
        return row

    def featured_coupon_list(self):
         con=self.myconnection()
         sql="select desp,couponcode,photo,validity from coupon limit 0,3"
         mycursor=con.cursor()
         mycursor.execute(sql)
         row=mycursor.fetchall()
         mycursor.close()
         con.close()
         return row


    def make_booking(self,cust_email,retail_email,book_date,persons,book_time):
        con=self.myconnection()
        sq="insert into booking(retail_email,cust_email,book_date,persons,book_time) values(%s,%s,%s,%s,%s)"
        record = [retail_email,cust_email,book_date,persons,book_time]
        mycursor=con.cursor()
        mycursor.execute(sq, record)
        con.commit()
        mycursor.close()
        con.close()
        return

    def delete_a_coupon(self,email,coupon_id):
        con=self.myconnection()
        sq="delete from coupon where retail_email=%s and idcoupon=%s"
        record = [email,coupon_id]
        mycursor=con.cursor()
        mycursor.execute(sq, record)
        con.commit()
        mycursor.close()
        con.close()
        return
