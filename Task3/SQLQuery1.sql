SELECT * FROM orders;

SELECT Product, TotalPrice
FROM orders;

SELECT *
FROM orders
WHERE TotalPrice > 500;

SELECT *
FROM orders
ORDER BY TotalPrice DESC;

SELECT Product,
       SUM(TotalPrice) AS TotalSales
FROM orders
GROUP BY Product;

SELECT COUNT(*) AS TotalOrders
FROM orders;


SELECT SUM(TotalPrice) AS TotalSales
FROM orders;

SELECT AVG(TotalPrice) AS AverageSales
FROM orders;