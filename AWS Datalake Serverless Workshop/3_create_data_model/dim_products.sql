create view demo_serving_zone.vw_dim_products as
SELECT
p.productname, 
p.quantityperunit, 
p.unitsinstock, 
p.unitsonorder, 
p.reorderlevel, 
p.discontinued,
c.categoryname, 
c.description, 
c.picture, 
s.companyname, 
s.contactname, 
s.contacttitle, 
s.address, 
s.city, 
s.region, 
s.postalcode, 
s.country, 
s.phone, 
s.fax, 
s.homepage
From demo_raw_zone.products p 
Left Join demo_raw_zone.categories c on p.categoryid = c.categoryid
Left Join demo_raw_zone.suppliers s on p.supplierid = s.supplierid