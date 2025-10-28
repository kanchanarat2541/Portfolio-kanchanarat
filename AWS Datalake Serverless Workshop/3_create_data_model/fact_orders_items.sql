  create view demo_serving_zone.vw_fact_orders_items as
  SELECT
  o.orderid, 
  customerid , 
  employeeid, 
  cast((YEAR(CAST(orderdate AS DATE)) + 543) as varchar) || substr(orderdate,5,10) as orderdate,
  cast((YEAR(CAST(requireddate AS DATE)) + 543) as varchar) || substr(requireddate,5,10) as requireddate,
  shippeddate,
  shipvia, 
  freight, 
  shipname , 
  shipaddress , 
  shipcity , 
  shipregion , 
  shippostalcode , 
  shipcountry, 
  od.productid, 
  od.unitprice, 
  od.quantity, 
  od.discount
  from  demo_raw_zone.orders o
  left join demo_raw_zone.orders_details od on o.orderid = od.orderid