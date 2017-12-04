insert into customers values('0000000001','Hua',null,'Yang','1234567890',DATE '2000-01-01');
insert into customers values('0000000002','Hao',null,'Ding','1234567890',DATE '1990-01-01');
insert into customers values('0000000003','Kai',null,'Zhang','1234567890',DATE '1992-01-01');
insert into customers values('0000000004','Ning',null,'Jia','1234567890',DATE '2000-01-01');
insert into customers values('0000000005','Hz',null,'Liu','1234567890',DATE '2000-01-01');

insert into account values('123456','abc1','0000000001','hyang@gmail.com');
insert into account values('123456','abc2','0000000002','hding@gmail.com');
insert into account values('123456','abc3','0000000003','kzhang@gmail.com');
insert into account values('123456','abc4','0000000004','njia@gmail.com');
insert into account values('123456','abc5','0000000005','hliu@gmail.com');

insert into cart values(0.00,0.00,0.00,'0000000001');
insert into cart values(0.00,0.00,0.00,'0000000002');
insert into cart values(0.00,0.00,0.00,'0000000003');
insert into cart values(0.00,0.00,0.00,'0000000004');
insert into cart values(0.00,0.00,0.00,'0000000005');

insert into product values('1111111111','toy car',19.99,DATE '2020-12-31','LJFDIHAJSDSA213HJH');

insert into CARTDETAIL values('0000000002','1111111111',2);

insert into PRODUCT_TYPE values('TOYS','Have fun!');

insert into PRODUCTBELONGTO values('1111111111','TOYS');

insert into BRAND values('KAA','toys manufactor','SCCC');

insert into BRANDBELONGTO values('1111111111','KAA');

insert into store values('abc0000000','Toysmart','Chicago IL 60616','8000001111','9:00am','9:00pm','Find your toys');

insert into INVENTORY values('abc0000000','1111111111',40);

insert into VENDORS values('abc0000000','toys product');

insert into PAYMENTMETHOD values('DJFI12L4KX','DING HAO','1111222233334444',DATE '2030-01-01','123','0000000002');

insert into ADDRESS values('JDER8J23SK','333 X 33TH ST',null,'CHICAGO','60601','IL','0000000002');
