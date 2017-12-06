insert into customers values('u000000001','Hua',null,'Yang','1234567890');
insert into customers values('u000000002','Hao',null,'Ding','1234567890');
insert into customers values('u000000003','Kai',null,'Zhang','1234567890');
insert into customers values('u000000004','Ning',null,'Jia','1234567890');
insert into customers values('u000000005','Hz',null,'Liu','1234567890');

insert into account values('123456','abc1','u000000001','hyang@gmail.com');
insert into account values('123456','abc2','u000000002','hding@gmail.com');
insert into account values('123456','abc3','u000000003','kzhang@gmail.com');
insert into account values('123456','abc4','u000000004','njia@gmail.com');
insert into account values('123456','abc5','u000000005','hliu@gmail.com');

insert into cart values(0.00,0.00,0.00,'u000000001');
insert into cart values(0.00,0.00,0.00,'u000000002');
insert into cart values(0.00,0.00,0.00,'u000000003');
insert into cart values(0.00,0.00,0.00,'u000000004');
insert into cart values(0.00,0.00,0.00,'u000000005');

insert into product values('p111111111','toy car',19.99,DATE '2020-12-31','LJFDIHAJSDSA213HJH');
insert into product values('p111111112','Bunny',20.00,DATE '2020-12-31','LJFJDFKLS392813HJH');
insert into product values('p111111113','ToyCat',23.00,DATE '2020-12-31','LJFDIHAjJKLDSJFHJH');
insert into product values('p111111114','Dragon',14.99,DATE '2020-12-31','LJFDDFJ284KJ23RKJ3');
insert into product values('p111111115','Superman model',29.99,DATE '2020-12-31','LJFDIFJIFKDN283H32');

insert into CARTDETAIL values('u000000002','p111111111',2);
insert into CARTDETAIL values('u000000003','p111111114',3);

insert into ORDERS values('o000000001',DATE '2020-12-31',113.00,'u000000001',1);
insert into ORDERS values('o000000002',DATE '2020-12-31',33.00,'u000000001',1);

--insert into orderdetail values();

insert into PRODUCT_TYPE values('TOYS','Have fun!');

insert into PRODUCTBELONGTO values('p111111111','TOYS');
insert into PRODUCTBELONGTO values('p111111112','TOYS');
insert into PRODUCTBELONGTO values('p111111113','TOYS');
insert into PRODUCTBELONGTO values('p111111114','TOYS');
insert into PRODUCTBELONGTO values('p111111115','TOYS');

insert into BRAND values('KAA','toys manufactor','SCCC');
insert into BRAND values('SBA','toys manufactor','SCCC');

insert into BRANDBELONGTO values('p111111111','KAA');
insert into BRANDBELONGTO values('p111111112','KAA');
insert into BRANDBELONGTO values('p111111113','KAA');
insert into BRANDBELONGTO values('p111111114','SBA');
insert into BRANDBELONGTO values('p111111115','SBA');

insert into store values('abc0000000','Toysmart','Chicago IL 60616','8000001111','9:00am','9:00pm','Find your toys');

insert into INVENTORY values('abc0000000','p111111111',40);
insert into INVENTORY values('abc0000000','p111111112',10);
insert into INVENTORY values('abc0000000','p111111113',52);
insert into INVENTORY values('abc0000000','p111111114',44);
insert into INVENTORY values('abc0000000','p111111115',80);

insert into VENDORS values('abc0000000','toys product');

insert into PAYMENTMETHOD values('DJFI12L4KX','DING HAO','1111222233334444',DATE '2030-01-01','123','u000000002');

insert into ADDRESS values('JDER8J23SK','333 X 33TH ST',null,'CHICAGO','60601','IL','u000000002');
