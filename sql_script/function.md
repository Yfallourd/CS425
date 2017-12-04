
## User's funciton

### Sign in

```sql
	--input username
	--input password

	select user_id form account
		where username = 'input_username' 
		and password = 'input_password';

--login use email
	select user_id form account
		where email = 'input_email' 
		and password = 'input_password';

```
	

### Sign up
```sql
	--auto generate auto_user_id;
	--input information;
	
	--examine the same username
	select username form account
		where username = 'input username';

	--if username is unique, then create a new account.
	insert into customers 
	values ('auto_user_id',
		'input_first_name',
		 'input_middle_name',
		'input_last_name',
		'phone_number',
		'date_of_birth',
		);
```
	


### Edit information
```sql
	update table customers
	set first_name = 'input_first_name',
	    middle_name = 'input_middle_name',
	    last_name = 'input_last_name',
	    phone_number = 'input_phone_number',
	    date_of_birth = 'input_date_of_birth'
	where user_id = 'the current userid';
```
	

### Set address
```sql
	--auto generate auto_address_id;
	
	insert into address 
	values(	'auto_address_id',
		'address_line_1',
		'address_line_2',
		'city',
		'zipcode',
		'state',
		'current_user_id');
```
	

### Delete address

```sql
	delete from address
	where address_id = 'target_address_id';
```
	

### Set payment method
```sql
	--auto generate auto_payment_id;

	insert into paymentmethod
	values(	'method_id',
		'holdername',
		'card_number',
		'expiration_date',
		'svc',
		'user_id');
```

### Delete payment method 
```sql
	delete from paymentmethod
	where method_id = 'target_method_id';
```


### Check order
```sql
	select * from order 
	where user_id = 'the current userid';
```

### Add to cart
```sql
	insert into cartdetail 
	values ('the current userid',
		'target productid',
		'product_number');

	update cart
	set	shipping_price = 5,
		price = shipping_price + (select sum(product_price * product_number)
			from product natural join cartdetail
			where user_id = 'current_user_id'),
		tax = price * 1.05
	where user_id = 'current_user_id';
```

### Add one in cart
```sql
	update cartdetail
	set product_number = product_number + 1
	where user_id = 'current_user_id' 
	and product_id = 'current_product_id';

	update cart
	set	shipping_price = 5,
		price = shipping_price + (select sum(product_price * product_number)
			from product natural join cartdetail
			where user_id = 'current_user_id'),
		tax = price * 1.05
	where user_id = 'current_user_id';
```

### Minus one in cart
```sql
	update cartdetail
	set product_number = product_number - 1
	where user_id = 'current_user_id' 
	and product_id = 'current_product_id';

	update cart
	set	shipping_price = 5,
		price = shipping_price + (select sum(product_price * product_number)
			from product natural join cartdetail
			where user_id = 'current_user_id'),
		tax = price * 1.05
	where user_id = 'current_user_id';
```


### Delete form cart
```sql
	delete from cartdetail
	where user_id = 'current_user_id'
	and product_id = 'product_id';

	update cart
	set	shipping_price = 5,
		price = shipping_price + (select sum(product_price * product_number)
			from product natural join cartdetail
			where user_id = 'current_user_id'),
		tax = price * 1.05
	where user_id = 'current_user_id';
```

### Check cart
```sql
	--get current cartid
	select user_id from cart 
	where user_id = 'current userid';
	
	--get cart information
	select tax form cart 
	where user_id = 'current userid';
	
	select price form cart 
	where user_id = 'current userid';

	select shipping_price form cart 
	where user_id = 'current userid';

	--get product information
	with current_cart as(
		select product_id form cartdetail
		where user_id = 'current userid'
	)
	select * 
	from product 
	where product_id in current_cart;
```

	

### Search product
```sql
	select * from product
		where prodcut_name like '%key word%';
```


## Employee's function

### Check product
```sql
	select * form product;
```


### Add product
```sql
	insert into product
	values ('productid',
		'product_name',
		'product_price',
--		'prodcut_company',
--		'product_capacity',
		'expiration_date',
		'upc_code');

	--set product store
	insert into inventory
	values ('store_id',
		'product_id',
		'number of product in this store');

	--set product type
	insert into productbelongto
	values ('product_id',
		'category_name');

	--set product brand 
	insert into brandbelongto
	values ('product_id',
		'barnd_name');
```
	
### Delete product
```sql
	delete from product 
	where product_id = 'productid';
```


### Check size from warehouse
	
### Check store
```sql
	select * from store;
```

### Add store 
```sql
	--auto generate auto_store_id;
	insert into store 
	values ('auto_store_id',
		'store_name',
		'store_address',
		'phone_number',
		'open_time',
		'close_time',
		'description');

	--set vendors
	insert into vendors
	values ('store_id',
		'vendor_name');
```

### Delete store
```sql
	delete from store
	where store_id = 'target_store_id';
```
	

### Add product type
```sql
	insert into product_type
	values ('category_name',
		'description');
```
	

### Delete product type
```sql
	delete from product_type
	where category_name = 'target_product_type';
```
	

### Add brand
```sql
	insert into brand
	values ('brand_name',
		'brand_descroption',
		'brand_company');
```
	

### Delete product brand
```sql
	delete from brand
	where brand_name = 'target_brand_name';
```
	
### Delete vendors
```sql
	delete from vendors
	where vendor_name = 'target_vendor_name';
```
	

