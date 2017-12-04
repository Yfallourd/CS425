from flask import request, render_template, redirect
from flask_api import FlaskAPI, status, response
import cx_Oracle
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
    querystr = '''
                select * from store;
            '''
    cursor.execute(querystr)
    stores = [x for x in cursor]
    return render_template('stores.html', stores=stores)


@app.route('/customer/cart')
def cartpage():
    if "auth_user" in request.cookie:
        cursor = connection.cursor()
        custID = request.cookie["auth_user"]
        cartID = None
        cart = {}
        querystr = '''
                select user_id from cart
                where user_id = {0};
                '''.format(custID)
        cursor.execute(querystr)
        for each in cursor:
            cartID = each
        if cartID is None:
            return "No CART"
        querystr = '''
                select tax, price, shipping_price from cart 
                where user_id = {0};
                '''.format(cartID)
        cursor.execute(querystr)
        for tax, price, sprice in cursor:
            cart = {"tax": tax, "price": price, "shipping_price": sprice}
        querystr = '''
                with current_cart as(
                select product_id from cartdetail
                where user_id = {0}
                )
                select * 
                from product 
                 where product_id in current_cart;
                '''.format(cartID)
        cursor.execute(querystr)
        products = [x for x in cursor]
        cart["products"] = products
    else:
        return "PLEASE LOG IN"
    return render_template('cart.html', cart=cart)


@app.route('/customer/order')
def orderpage():
    if "auth_user" in request.cookie:
        cursor = connection.cursor()
        custID = request.cookie["auth_user"]
        querystr = '''
                select * from order 
                where user_id = {0};
                '''.format(custID)
        cursor.execute(querystr)
        orders = [x for x in cursor]
    else:
        return "PLEASE LOG IN"
    return render_template('orders.html', orders=orders)


@app.route('/customer/signin', methods=['GET', 'POST'])
def signinpage():
    if request.method == 'GET':
        return render_template('customer_sign_in.html')
    if request.method == 'POST':
        # SIGN IN LOGIC
        payload = request.get_json(force=True)
        userid = None
        cursor = connection.cursor()
        querystr = '''
            select user_id from account
            where username = {0}
            and password = {1};
        '''.format(payload["inputUsername"], payload["inputPassword"])
        cursor.execute(querystr)
        for id in cursor:
            userid = id
        redirect_to_main = redirect('/main')
        response = app.make_response(redirect_to_main)
        if userid is not None:
            response.set_cookie('auth_user', value=userid)  # Add the username arg
        return response


@app.route('/customer/signup', methods=['GET', 'POST'])
def signuppage():
    if request.method == "GET":
        return render_template('customer_sign_up.html')
    elif request.method == "POST":
        # SIGN UP LOGIC
        payload = request.get_json(force=True)
        cursor = connection.cursor()
        querystr = '''
        select username from account
        where username = {0};
        '''.format(payload["username"])
        cursor.execute(querystr)
        if len(cursor) != 0:
            return "USERNAME ALREADY EXISTS"
        cursor = connection.cursor()
        userid = generateID("U")
        addressid = generateID("A")
        querystr = '''insert into customers 
                values ({0},
                {1},
                {2},
                {3},
                {4},
                {5}
            );        
        '''.format(userid, payload["inputCustomerUsername"], payload["inputFName"], payload["inputMName"],
                   payload["inputLName"], payload["inputPhone"])
        cursor.execute(querystr)
        cursor = connection.cursor()
        querystr = '''insert into address 
                        values ({0},
                        {1},
                        {2},
                        {3},
                        {4},
                        {5},
                        {6}
                    );        
                '''.format(addressid, payload["inputAddress1"], payload["inputAddress2"], payload["inputCity"],
                           payload["inputState"], payload["inputCode"], userid)
        cursor.execute(querystr)
        redirect_to = redirect('customer/signup/success')
        response = app.make_response(redirect_to)
        return response


@app.route('/customer/signup/success')
def successpage():
    return render_template('signup_success.html')


@app.route('/test')
def test():
    redirect_to_main = redirect('/main')
    response = app.make_response(redirect_to_main)
    response.set_cookie('auth_user', value='test')  # Add the username arg
    return response


@app.route('/customer/account')
def accountpage():
    return render_template('update_customerinfo.html')


@app.route('/customer/account/update', methods=['POST'])
def accountUpdate():
    if request.method == 'POST':
        # UPDATE LOGIC
        payload = request.get_json(force=True)
        cursor = connection.cursor()
        querystr = '''
                select username from account
                where username = {0};
                '''.format(payload["username"])
        cursor.execute(querystr)
        cursor = connection.cursor()
        querystr = '''insert into customers
                        values ({0},
                        {1},
                        {2},
                        {3},
                        {4},
                    );        
                '''.format(payload["inputCustomerUsername"], payload["inputFName"], payload["inputMName"],
                           payload["inputLName"], payload["inputPhone"])
        cursor.execute(querystr)
        cursor = connection.cursor()
        querystr = '''insert into address 
                        values ({0},
                        {1},
                        {2},
                        {3},
                        {4},
                        {5},
                        {6}
                    );        
                '''.format(ADDRESSID, payload["inputAddress1"], payload["inputAddress2"], payload["inputCity"],
                           payload["inputState"], payload["inputCode"], USERID)
        cursor.execute(querystr)
        redirect_to_main = redirect('/main')
        response = app.make_response(redirect_to_main)
        return response


@app.route('/employee/signin', methods=['GET', 'POST'])
def empSignin():
    if request.method == 'GET':
        return render_template('employee_sign_in.html')
    if request.method == 'POST':
        # SIGN IN LOGIC
        payload = request.get_json(force=True)
        userid = None
        cursor = connection.cursor()
        querystr = '''
            select user_id from account
            where username = {0}
            and password = {1};
        '''.format(payload["inputUsername"], payload["inputPassword"])
        cursor.execute(querystr)
        for id in cursor:
            userid = id
        redirect_to_main = redirect('/main')
        response = app.make_response(redirect_to_main)
        response.set_cookie('auth_user', value='')  # Add the username arg
        response.set_cookie('employee', value='True')
        return response


@app.route('/employee/product')
def productCheck():
    #if ("employee" in request.cookies) & (request.cookies["employee"] == "True"):
    return render_template("employee_check_product.html")
    #else:
        #return "FORBIDDEN"


@app.route('/employee/product/update', methods=['GET', 'POST'])
def productUpdate():
    if request.method == 'GET':
        #if ("employee" in request.cookies) & (request.cookies["employee"] == "True"):
        return render_template("update_productinfo.html")
        #else:
        #   return "FORBIDDEN"
    if request.method == 'POST':
        payload = request.get_json(force=True)
        userid = None
        cursor = connection.cursor()
        querystr = '''
                    select user_id from account
                    where username = {0}
                    and password = {1};
                '''.format(payload["inputUsername"], payload["inputPassword"])
        cursor.execute(querystr)
        for id in cursor:
            userid = id
        redirect_to_main = redirect('/main')
        response = app.make_response(redirect_to_main)
        response.set_cookie('auth_user', value='')  # Add the username arg
        response.set_cookie('employee', value='True')


if __name__ == "__main__":
    app.run()
