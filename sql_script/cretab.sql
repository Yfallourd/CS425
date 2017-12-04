
  CREATE TABLE CUSTOMERS                                            
   (	USER_ID CHAR(10) NOT NULL ,                                             
	FIRST_NAME VARCHAR2(20) NOT NULL ,                                     
	MIDDLE_NAME VARCHAR2(20),
	LAST_NAME VARCHAR2(20) NOT NULL ,
	PHONE_NUMBER VARCHAR2(20),
--	DATE_OF_BIRTH DATE,
	 PRIMARY KEY (USER_ID)                                            
   );
                                                                                
                                                                                
                                                                                
  CREATE TABLE ORDERS                                               
   (	ORDER_ID CHAR(10) NOT NULL ,                                       
	ORDER_DATE VARCHAR2(20) NOT NULL ,
	TOTAL_PRICE NUMERIC(10,2),
   	USER_ID CHAR(10) NOT NULL,
	PAYMENT_STATUS NUMERIC(1) DEFAULT 0 NOT NULL,
	 PRIMARY KEY (ORDER_ID) ,
	 FOREIGN KEY (USER_ID)
	 REFERENCES CUSTOMERS (USER_ID) ON DELETE CASCADE
   );
                                                                                

  CREATE TABLE ACCOUNT                                              
   (	PASSWORD VARCHAR2(20) NOT NULL ,                                   
	USERNAME VARCHAR2(20) NOT NULL ,                                       
	USER_ID CHAR(10) ,
	EMAIL VARCHAR2(30),
	 PRIMARY KEY (USER_ID),                                
	 FOREIGN KEY (USER_ID)
	 REFERENCES CUSTOMERS (USER_ID) ON DELETE CASCADE
   );                                                  
                                                                                

  CREATE TABLE CART                                                 
   (	TAX NUMERIC(10,2),
	PRICE NUMERIC(10,2),
	SHIPPING_PRICE NUMERIC(10,2),
   	USER_ID CHAR(10),
	 PRIMARY KEY (USER_ID) ,
	 FOREIGN KEY (USER_ID)                          
	  REFERENCES CUSTOMERS (USER_ID) ON DELETE CASCADE 
   );

  CREATE TABLE PRODUCT                                              
   (	PRODUCT_ID CHAR(10),
	PRODUCT_NAME VARCHAR2(20),
	PRODUCT_PRICE NUMERIC(10,2),
	EXPIRATION_DATE DATE,
	UPC_CODE VARCHAR2(20),
	 PRIMARY KEY (PRODUCT_ID)
   );


  CREATE TABLE ORDERDETAIL                                          
   (	ORDER_ID CHAR(10),
	PRODUCT_ID CHAR(10),
	PRODUCT_NUMBER INT,
	 PRIMARY KEY (ORDER_ID, PRODUCT_ID) ,
	 FOREIGN KEY (ORDER_ID)                         
	  REFERENCES ORDERS  ON DELETE CASCADE ,
	 FOREIGN KEY (PRODUCT_ID)                        
	  REFERENCES PRODUCT (PRODUCT_ID)                          
   );                                                  
                                                                                
                                                                                
                                                                                
  CREATE TABLE CARTDETAIL                                           
   (	USER_ID CHAR(10),
	PRODUCT_ID CHAR(10),
	PRODUCT_NUMBER INT,
	 PRIMARY KEY (USER_ID, PRODUCT_ID) ,
	 FOREIGN KEY (USER_ID)                           
	  REFERENCES CART (USER_ID) ON DELETE CASCADE ,
	 FOREIGN KEY (PRODUCT_ID)                        
	  REFERENCES PRODUCT (PRODUCT_ID)                          
   );                                                  
                                                                                
                                                                                
                                                                               
                                                                                

  CREATE TABLE PRODUCT_TYPE                                         
   (	CATEGORY_NAME VARCHAR2(20),
	DESCRIPTION VARCHAR2(20),
	 PRIMARY KEY (CATEGORY_NAME)                       
   );                                                  
                                                                                

                                                                                
                                                                                
  CREATE TABLE PRODUCTBELONGTO                                      
   (	PRODUCT_ID CHAR(10),
	CATEGORY_NAME VARCHAR2(20),
	 PRIMARY KEY (PRODUCT_ID, CATEGORY_NAME) ,
	 FOREIGN KEY (PRODUCT_ID)                   
	  REFERENCES PRODUCT (PRODUCT_ID) ON DELETE CASCADE ,
	 FOREIGN KEY (CATEGORY_NAME)                
	  REFERENCES PRODUCT_TYPE (CATEGORY_NAME)                  
   );                                                  
                                                                                
                                                                                
                                                                                
  CREATE TABLE BRAND                                                
   (	BRAND_NAME VARCHAR2(20),
	BRAND_DESCRIPTION VARCHAR2(20),
	BRAND_COMPANY VARCHAR2(20),
	 PRIMARY KEY (BRAND_NAME)                                 
   );                                                  
                                                                                
                                                                                
                                                                                

  CREATE TABLE BRANDBELONGTO                                        
   (	PRODUCT_ID CHAR(10),
	BRAND_NAME VARCHAR2(20),
	 PRIMARY KEY (BRAND_NAME, PRODUCT_ID) ,
	 FOREIGN KEY (PRODUCT_ID)                     
	  REFERENCES PRODUCT (PRODUCT_ID) ON DELETE CASCADE ,
	 FOREIGN KEY (BRAND_NAME)                     
	  REFERENCES BRAND (BRAND_NAME)                            
   );                                                  
                                                                                
                                                                                
                                                                                
  CREATE TABLE STORE                                                
   (	STORE_ID CHAR(10),
	STORE_NAME VARCHAR2(20),
	STORE_ADDRESS VARCHAR2(20),
	PHONE_NUMBER VARCHAR2(20),
	OPEN_TIME VARCHAR2(20),
	CLOSE_TIME VARCHAR2(20),
	DESCRIPTION VARCHAR2(20),
	 PRIMARY KEY (STORE_ID)                                   
   );                                                  
                                                                                

                                                                                
                                                                                
  CREATE TABLE INVENTORY                                            
   (	STORE_ID CHAR(10),
	PRODUCT_ID CHAR(10),
	PRODUCT_NUMBER INT,
	 PRIMARY KEY (STORE_ID, PRODUCT_ID) ,
	 FOREIGN KEY (STORE_ID)                           
	  REFERENCES STORE (STORE_ID) ON DELETE CASCADE ,
	 FOREIGN KEY (PRODUCT_ID)                         
	  REFERENCES PRODUCT (PRODUCT_ID) ON DELETE CASCADE
   );                                                  
                                                                                
                                                                                
                                                                                
  CREATE TABLE VENDORS                                              
  (	STORE_ID CHAR(10),
   	VENDOR_NAME VARCHAR2(20),
	 PRIMARY KEY (STORE_ID) ,
	 FOREIGN KEY (STORE_ID)                            
	  REFERENCES STORE (STORE_ID)
   );                                                  


  CREATE TABLE PAYMENTMETHOD                                        
   (	METHOD_ID CHAR(10),
	HOLDER_NAME VARCHAR2(20),
	CARD_NUMBER VARCHAR2(20),
	EXPIRATION_DATE DATE,
	SVC VARCHAR2(20),
	USER_ID CHAR(10),
	 PRIMARY KEY (USER_ID) ,
	 FOREIGN KEY (USER_ID)                    
	  REFERENCES CUSTOMERS (USER_ID) ON DELETE CASCADE                                
   );                                                  
                                                                                

                                                                                
                                                                                
  CREATE TABLE ADDRESS                                              
   (	ADDRESS_ID CHAR(10),
	ADDRESS_LINE_1 VARCHAR2(20),
	ADDRESS_LINE_2 VARCHAR2(20),
	CITY VARCHAR2(20),
	ZIPCODE VARCHAR2(20),
	STATE VARCHAR2(20),
	USER_ID CHAR(10),
	 PRIMARY KEY (ADDRESS_ID) ,
	 FOREIGN KEY (USER_ID)                          
	  REFERENCES CUSTOMERS (USER_ID) ON DELETE CASCADE
   );                                                  
                                                                                
