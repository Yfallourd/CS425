	insert into orders 
	values ('o000000002',
			current_date,
			(select price from cart
			where user_id = 'u000000002'),
			'u000000002',
			0);

	-- get product_id,product_number form cartdetail, and save it in an array
	select product_id, product_number 
	from cartdetail
	where user_id = 'u000000002';
	
	--get information from array we saved before, insert data using a loop.
	insert into orderdeatil (order_id, product_id, product_number)

	delete from cartdetail
	where user_id = 'u000000002';

	update cart
	set	shipping_price = 5,
		price = shipping_price + (select sum(product_price * product_number)
			from product natural join cartdetail
			where user_id = 'u000000002'),
		tax = 0.05*(select sum(product_price * product_number)
			from product natural join cartdetail
			where user_id = 'u000000002')
	where user_id = 'u000000002';
