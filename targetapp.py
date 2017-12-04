from flask import request, render_template, redirect
from flask_api import FlaskAPI, status, response
import cx_Oracle
import json
import time

app = FlaskAPI(__name__)
dsnstr = cx_Oracle.makedsn("krr.science", "1521", "orcl")


connection = cx_Oracle.connect(user="lhz", password="cs170901", dsn=dsnstr)


def generateID(typetoken):
    return typetoken+str(int(time.time()))[1:]


@app.route('/')
def redirect_to_main():
    redirect_to_main = redirect('/main')
    response = app.make_response(redirect_to_main)
    response.set_cookie('auth_user', value='', expires=0)  # Remove cookies
    response.set_cookie('employee', value='', expires=0)  # Remove cookies
    return response


@app.route('/main')
def mainpage():
    if "auth_user" in request.cookies:
        if "employee" in request.cookies:
            if request.cookies["employee"] == "True":
                return render_template('after_sign_in_indexpage_employee.html')
            else:
                return render_template('after_sign_in_indexpage_customer.html')
        else:
            return render_template('after_sign_in_indexpage_customer.html')
    else:
        return render_template('index_light.html')


@app.route('/logout')
def logout():
    redirect_to_main = redirect('/main')
    response = app.make_response(redirect_to_main)
    response.set_cookie('auth_user', value='', expires=0)  # Remove cookies
    response.set_cookie('employee', value='', expires=0)  # Remove cookies
    return response


@app.route('/stores')
def storepage():
    cursor = connection.cursor()
    querystr = "select store_name from store"
    cursor.execute(querystr)
    stores = [x[0] for x in cursor]
    return render_template('stores.html', stores=stores)


@app.route('/customer/cart')
def cartpage():
    if "auth_user" in request.cookies:
        cursor = connection.cursor()
        custID = request.cookies["auth_user"]
        cartID = None
        cart = {}
        querystr = '''
                select user_id from cart
                where user_id = :userid
                '''
        cursor.execute(querystr, userid=custID)
        for each in cursor:
            cartID = each
        if cartID is None:
            return "No CART"
        querystr = '''
                select tax, price, shipping_price from cart 
                where user_id = :userid
                '''
        cursor.execute(querystr, userid=custID)
        for tax, price, sprice in cursor:
            cart = {"tax": tax, "price": price, "shipping_price": sprice}
        querystr = '''
                select * 
                from product natural join ( select product_id from cartdetail
                where user_id = :userid)
                '''
        cursor.execute(querystr, userid=custID)
        products = [x for x in cursor]
        cart["products"] = products
    else:
        return "PLEASE LOG IN"
    return render_template('cart.html', cart=cart)


@app.route('/checkout')
def checkout():
    if "auth_user" in request.cookies:
        cursor = connection.cursor()
        custID = request.cookies["auth_user"]
        return "NOT IMPLEMENTED"

@app.route('/customer/order')
def orderpage():
    if "auth_user" in request.cookies:
        cursor = connection.cursor()
        custID = request.cookies["auth_user"]
        querystr = '''
                select * from orders 
                where user_id = :userid
                '''
        cursor.execute(querystr, {"userid": custID})
        order = [x for x in cursor]
    else:
        return "PLEASE LOG IN"
    return render_template('order.html', orders=order)


@app.route('/customer/signin', methods=['GET', 'POST'])
def signinpage():
    if request.method == 'GET':
        return render_template('customer_sign_in.html')
    if request.method == 'POST':
        # SIGN IN LOGIC
        payload = request.form
        userid = None
        cursor = connection.cursor()
        querystr = '''
            select user_id from account
            where username = :username
            and password = :password
        '''
        cursor.execute(querystr, {"username": payload["inputUsername"], "password":payload["inputPassword"]})
        for id in cursor:
            userid = id[0]
        redirect_to_main = redirect('/main')
        response = app.make_response(redirect_to_main)
        if userid is not None:
            response.set_cookie('auth_user', value=userid.encode())  # Add the username arg
        return response


@app.route('/customer/signup', methods=['GET', 'POST'])
def signuppage():
    if request.method == "GET":
        return render_template('customer_sign_up.html')
    if request.method == "POST":
        # SIGN UP LOGIC
        i = 0
        payload = request.form
        cursor = connection.cursor()
        querystr = '''
        select username from account
        where username = '{0}'
        '''.format(payload["inputCustomerUsername"])
        cursor.execute(querystr)
        for id in cursor:
            i += 1
        if not i == 0:
            return "USERNAME ALREADY EXISTS"
        cursor = connection.cursor()
        userid = generateID("u")
        addressid = generateID("a")
        querystr = '''insert into customers 
                values (:userid,
                :fname,
                :mname,
                :lname,
                :phone
            )        
        '''
        cursor.execute(querystr, {"userid": userid, "fname": payload["inputFName"], "mname": payload["inputMName"],
                                  "lname": payload["inputLName"], "phone": payload["inputPhone"]})
        connection.commit()
        cursor = connection.cursor()
        querystr = '''insert into account 
                values (:password,
                :username,
                :userid,
                :email
            )        
        '''
        cursor.execute(querystr, {"password": payload["inputPassword"], "username": payload["inputCustomerUsername"],
                                  "userid": userid, "email": payload["inputEmail"]})
        connection.commit()
        cursor = connection.cursor()
        querystr = '''insert into address 
                        values (:addressid,
                        :a1,
                        :a2,
                        :city,
                        :code,
                        :state,
                        :userid
                    )        
                '''
        cursor.execute(querystr, {"addressid": addressid, "a1": payload["inputAddress1"],
                                  "a2": payload["inputAddress2"], "city": payload["inputCity"],
                                  "code": payload["inputCode"], "state": payload["inputState"], "userid": userid})
        connection.commit()
        redirect_to = redirect('customer/signup/success')
        response = app.make_response(redirect_to)
        return response


@app.route('/employee/signup', methods=['GET', 'POST'])
def esignuppage():
    if request.method == "GET":
        return render_template('customer_sign_up.html')
    if request.method == "POST":
        # SIGN UP LOGIC
        i = 0
        payload = request.form
        cursor = connection.cursor()
        querystr = '''
        select username from account
        where username = '{0}'
        '''.format(payload["inputCustomerUsername"])
        cursor.execute(querystr)
        for id in cursor:
            i += 1
        if not i == 0:
            return "USERNAME ALREADY EXISTS"
        cursor = connection.cursor()
        userid = generateID("u")
        addressid = generateID("a")
        querystr = '''insert into customers 
                values (:userid,
                :fname,
                :mname,
                :lname,
                :phone
            )        
        '''
        cursor.execute(querystr, {"userid": userid, "fname": payload["inputFName"], "mname": payload["inputMName"],
                                  "lname": payload["inputLName"], "phone": payload["inputPhone"]})
        connection.commit()
        cursor = connection.cursor()
        querystr = '''insert into account 
                values (:password,
                :username,
                :userid,
                :email
            )        
        '''
        cursor.execute(querystr, {"password": payload["inputPassword"], "username": payload["inputCustomerUsername"],
                                  "userid": userid, "email": payload["inputEmail"]})
        connection.commit()
        cursor = connection.cursor()
        querystr = '''insert into address 
                        values (:addressid,
                        :a1,
                        :a2,
                        :city,
                        :code,
                        :state,
                        :userid
                    )        
                '''
        cursor.execute(querystr, {"addressid": addressid, "a1": payload["inputAddress1"],
                                  "a2": payload["inputAddress2"], "city": payload["inputCity"],
                                  "code": payload["inputCode"], "state": payload["inputState"], "userid": userid})
        connection.commit()
        redirect_to = redirect('customer/signup/success')
        response = app.make_response(redirect_to)
        return response


@app.route('/customer/signup/success')
def successpage():
    return render_template('signup_success.html')


@app.route('/test')
def test():
    cursor = connection.cursor()
    querystr = "select * from account"
    cursor.execute(querystr)
    stores = [x for x in cursor]
    return render_template('stores.html', stores=stores)


@app.route('/customer/account')
def accountpage():
    return render_template('update_customerinfo.html')


@app.route('/customer/account/update', methods=['POST'])
def accountUpdate():
    if request.method == 'POST':
        # UPDATE LOGIC
        if "auth_user" in request.cookies:
            custID = request.cookies["auth_user"]
            payload = request.form
            cursor = connection.cursor()
            querystr = '''update customers 
                    set first_name = :fname,
                    middle_name = :mname,
                    last_name = :lname,
                    phone_number = :phone
                    where user_id = :userid    
            '''
            cursor.execute(querystr, {"userid": custID, "fname": payload["inputFName"], "mname": payload["inputMName"],
                                      "lname": payload["inputLName"], "phone": payload["inputPhone"]})
            connection.commit()
            cursor = connection.cursor()
            querystr = '''update account 
                    set password = :password,
                    username = :username,
                    email = :email
                    where user_id = :userid        
            '''
            cursor.execute(querystr, {"password": payload["inputPassword"], "username": payload["inputCustomerUsername"],
                                      "userid": custID, "email": payload["inputEmail"]})
            connection.commit()
            cursor = connection.cursor()
            querystr = '''update address 
                            set address_line_1 = :a1,
                            address_line_2 = :a2,
                            city = :city,
                            zipcode = :code,
                            state = :state
                            where user_id = :userid        
                    '''
            cursor.execute(querystr, {"a1": payload["inputAddress1"],
                                      "a2": payload["inputAddress2"], "city": payload["inputCity"],
                                      "code": payload["inputCode"], "state": payload["inputState"], "userid": custID})
            connection.commit()
            redirect_to_main = redirect('/main')
            response = app.make_response(redirect_to_main)
            return response
        return "PLEASE SIGN IN"


@app.route('/employee/signin', methods=['GET', 'POST'])
def empSignin():
    if request.method == 'GET':
        return render_template('employee_sign_in.html')
    if request.method == 'POST':
        # SIGN IN LOGIC
        payload = request.form
        userid = None
        cursor = connection.cursor()
        querystr = '''
                    select user_id from account
                    where username = :username
                    and password = :password
                '''
        cursor.execute(querystr, {"username": payload["inputUsername"], "password": payload["inputPassword"]})
        for id in cursor:
            userid = id[0]
        redirect_to_main = redirect('/main')
        response = app.make_response(redirect_to_main)
        response.set_cookie('auth_user', value='')  # Add the username arg
        response.set_cookie('employee', value='True')
        return response


@app.route('/employee/product')
def productCheck():
    if ("employee" in request.cookies) & (request.cookies["employee"] == "True"):
        cursor = connection.cursor()
        querystr = "select * from product"
        cursor.execute(querystr)
        products = [x for x in cursor]
        return render_template("employee_check_product.html", products=products)
    else:
        return "FORBIDDEN"


@app.route('/employee/product/update', methods=['GET', 'POST'])
def productUpdate():
    if request.method == 'GET':
        if ("employee" in request.cookies) & (request.cookies["employee"] == "True"):
            return render_template("update_productinfo.html")
        else:
            return "FORBIDDEN"
    if request.method == 'POST':
        payload = request.form
        cursor = connection.cursor()
        querystr = '''update product
                        set product_name = :name,
                        product_price = :price,
                        upc_code = :UPC
                        where product_id = :pid    
                '''
        cursor.execute(querystr, {"pid": payload["inputproductID"],
                                  "UPC": payload["inputproductCode"],
                                  "name": payload["inputName"],
                                  "price": payload["inputPrice"]})
        connection.commit()
        redirect_to_main = redirect('/main')
        response = app.make_response(redirect_to_main)
        response.set_cookie('auth_user', value='')  # Add the username arg
        response.set_cookie('employee', value='True')
        return response


if __name__ == "__main__":
    app.run()
