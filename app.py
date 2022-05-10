from flask import *
from operation import DbOperation
from datetime import *

app = Flask(__name__)
app.secret_key="R23wqsdr2345"

#All Pages that need to rendered

@app.route('/landing_page')
def landing_page():
        obj=DbOperation()
        r=obj.retailer_image()
        f_coupons=obj.featured_coupon_list()
        return render_template('landing_page.html',retailers=r,rows=f_coupons)


@app.route('/customer_index')
def customer_index():
    if 'email' in session:
        email=session['email']
        obj=DbOperation()
        r=obj.retailer_image()
        f_coupons=obj.featured_coupon_list()
        return render_template('customer_index.html',msg=email,retailers=r,rows=f_coupons)
    else :
        msg="Need to login first!"
        return render_template('login.html',ms=msg)

@app.route('/retailer_index')
def retailer_index():
    return render_template('retailer_index.html')

@app.route('/membership')
def membership():
    if 'email' in session:
        email=session['email']
        return render_template('membership.html',msg=email)
    else :
        msg="Need to login first!"
        return render_template('login.html',ms=msg)

@app.route('/customer_login')
def customer_login():
    return render_template('login.html')

@app.route('/retailer_login')
def retailer_login():
    return render_template('retailer_login.html')


@app.route('/customer_profile')
def customer_profile():
    if 'email' in session:
        email=session['email']
        obj=DbOperation()
        r = obj.profile_customer(email)
        return render_template('customer_profile.html',msg=email,row=r)
    else :
        msg="Need to login first!"
        return render_template('login.html',ms=msg)

@app.route('/retailer_profile')
def retailer_profile():
    if 'email' in session:
            email=session['email']
            obj=DbOperation()
            r = obj.profile_retailer(email)
            return render_template('retailer_profile.html',row=r)
    else:
            return render_template('retailer_login.html')

@app.route('/coupon_select',methods=['POST','GET'])
def coupon_select():
    if request.method == 'POST' :
        if 'email' in session :
            email=session['email']
            retail_email=request.form['retail_email']
            obj=DbOperation()
            r=obj.retailer_image()
            p_coupons=obj.coupon_list(retail_email)
            return render_template('coupon.html',msg=email,rows=r,row=p_coupons)
        else :
            msg="Need to login first!"
            return render_template('login.html',ms=msg)

@app.route('/coupon')
def coupon():
    if 'email' in session :
        email=session['email']
        obj=DbOperation()
        r=obj.retailer_image()
        all_coupons=obj.list_All_Coupons()
        return render_template('coupon.html',msg=email,rows=r,row=all_coupons)
    else :
        msg="Need to login first!"
        return render_template('login.html',ms=msg)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    if 'email' in session:
        email=session['email']
        return render_template('contact.html',msg=email)
    else :
        msg="Need to login first!"
        return render_template('login.html',ms=msg)

@app.route('/coupon_delete')
def delete_coupon():
    if 'email' in session:
        email=session['email']
        obj=DbOperation()
        r = obj.coupon_list(email)
        return render_template('coupon_delete.html',row=r)
    else:
            return render_template('retailer_login.html')


@app.route('/coupon_delete_submit',methods=['POST','GET'])
def delete_particular_coupon():
    if 'email' in session:
        if request.method == 'POST' :
            email=session['email']
            coupon_id=request.form['coupon_id']
            obj=DbOperation()
            obj.delete_a_coupon(email,coupon_id)
            return redirect(url_for('delete_coupon'))
    else :
            return render_template('retailer_login.html')

@app.route('/coupon_generate')
def generate_coupon():
    return render_template('coupon_generate.html')

@app.route('/coupon_list')
def list_coupons():
    if 'email' in session:
        email=session['email']
        obj=DbOperation()
        r = obj.coupon_list(email)
        return render_template('coupon_list.html',row=r)
    else:
            return render_template('retailer_login.html')

#---------------------------------------------------
#----New Customer and Retailer Insert--------------------
@app.route('/customer_insert',methods=['POST','GET'])
def cust_insert():
    if request.method=='POST':
        name=request.form["name"]
        email=request.form["email"]
        password=request.form["password"]
        obj=DbOperation()   # object of DbOperation
        obj.insert_customer(name,email,password)
        return render_template('login.html')

@app.route('/retailer_insert',methods=['POST','GET'])
def retailer_insert():
    if request.method=='POST':
        name=request.form["name"]
        email=request.form["email"]
        password=request.form["password"]
        obj=DbOperation()   # object of DbOperation
        obj.insert_retailer(name,email,password)
        return render_template('retailer_login.html')

#--------Customer and Retailer Login Check----------------------

@app.route('/customer_index',methods=['POST','GET'])
def cust_login_check():
    if request.method=='POST':
        email = request.form["email"]
        password = request.form["password"]
        obj=DbOperation()
        m=obj.custlogincheck(email,password)
        if m==0:
                ms="Invalid email or password"
                return render_template('login.html', msg=ms)
        else:
                return redirect(url_for('customer_index'))

@app.route('/retailerlogincheck',methods=['POST','GET'])
def retailer_login_check():
    if request.method=='POST':
        email = request.form["email"]
        password = request.form["password"]
        obj=DbOperation()
        m=obj.retailerlogincheck(email,password)
        if m==0:
                ms="Invalid email or password"
                return render_template('retailer_login.html', msg=ms)
        else:
                return render_template('retailer_index.html')

#--------------------Customer and Retailer Logout------------------------------

@app.route('/customer_logout')
def cust_logout():
       session.clear()
       return render_template('landing_page.html')

@app.route('/retailer_logout')
def retailer_logout():
       session.clear()
       return render_template('landing_page.html')
#-----------------------Update Retailer Profile-------------------
@app.route('/updateretailer_profile',methods=['POST','GET'])
def update_retailer_profile():
    if request.method=='POST':
        if 'email' in session:
            email=session['email']
            name=request.form["name"]
            pname=request.form["pname"]
            address=request.form["address"]
            city=request.form["city"]
            pincode=request.form["pincode"]
            mobile=request.form["mobile"]
            password=request.form["password"]

            f=request.files['image']
            fnm=f.filename

            f.save("static/assets/img/brands/"+f.filename)

            obj=DbOperation()   # object of DbOperation
            obj.update_retailer(email,name,pname,address,city,pincode,mobile,password,fnm)
            #return render_template('retailer_profile.html',msg=email)
            return redirect('/retailer_profile')
        else :
            msg="Need to login first!"
            return render_template('retailer_login.html',msg)


#--------------------Update Customer Profile-----------------------------

@app.route('/updatecustomer_profile',methods=['POST','GET'])
def update_customer_profile():
    if request.method=='POST':
        if 'email' in session:
            email=session['email']
            name=request.form["name"]
            mobile=request.form["mobile"]
            location=request.form["location"]
            dob=request.form["dob"]
            gender=request.form["gender"]
            password=request.form["password"]
            f=request.files['image']
            fnm=f.filename
            f.save("static/assets/img/customerdps/"+f.filename)
            obj=DbOperation()   # object of DbOperation
            obj.update_customer(email,name,mobile,location,dob,gender,password,fnm)
            #return render_template('retailer_profile.html',msg=email)
            return redirect('/customer_profile')
        else :
            msg="Need to login first!"
            return render_template('customer_login.html',msg)


#--------------------Membership----------------------------------------------

@app.route('/membership_submit',methods=['POST','GET'])
def member_submit():
        if 'email' in session:
            if  request.method=='POST':
                email=session['email']
                year=request.form["year"]
                cur_date=date.today()
                exp_date=cur_date+timedelta(days=365*int(year)-1)
                if year=="1":
                    amount="240"
                elif year=="2":
                    amount="360"
                else:
                    amount="480"
                obj=DbOperation()
                obj.member_insert(email,year,cur_date,exp_date,amount)
                return redirect('/customer_profile')
        else:
                return render_template('customer_login.html')



#----------------------Coupon Generate------------------------------------

@app.route('/coupon_submit',methods=['POST','GET'])
def coupon_submit():
        if 'email' in session:
            if  request.method=='POST':
                email=session['email']
                validity=request.form["validity"]
                descp=request.form["descp"]
                couponcode=request.form["couponcode"]
                f=request.files['photo']
                photo=f.filename
                f.save("static/assets/img/coupons/"+f.filename)
                obj=DbOperation()
                obj.coupon_insert(email,validity,descp,couponcode,photo)
                flash("Coupon Generated!")
                return redirect('/coupon_generate')
        else:
                return render_template('retailer_login.html')


#---------------------Retailer Booking slots---------------------------
@app.route('/retailer_booking')
def retailer_booking():
    if 'email' in session:
        email=session['email']
        obj=DbOperation()
        r=obj.retailer_image()
        return render_template('retailer_list_booking.html',msg=email,retailers=r)
    else:
        return redirect(url_for('customer_login'))


@app.route('/retail_book_submit',methods=['POST','GET'])
def slot_booking():
    if 'email' in session:
        if request.method == 'POST' :
            cust_email=session['email']
            retail_email=request.form['retail_email']
            book_date=request.form['book_date']
            persons=request.form['persons']
            book_time=request.form['book_time']
            obj=DbOperation()
            obj.make_booking(cust_email,retail_email,book_date,persons,book_time)
            return redirect(url_for('retailer_booking'))



#--------------------Display coupons according to retailers------------------












if __name__=="__main__":
	app.run(debug=True)
