SELECT Model, COUNT(*) AS Total

FROM  dbo.CarSaless

GROUP BY Model

ORDER BY Total DESC;


SELECT Model, AVG(Price_USD) AS AvgPrice

FROM dbo.CarSaless

GROUP BY Model

ORDER BY AvgPrice DESC;





SELECT Transmission, COUNT(*) AS Nombre

FROM dbo.CarSaless

GROUP BY Transmission;



SELECT Body_Style, COUNT(*) AS NombreVoitures, AVG(Price_USD) AS PrixMoyen

FROM dbo.CarSaless

GROUP BY Body_Style

ORDER BY NombreVoitures DESC;



SELECT Dealer_Region, COUNT(*) AS TotalVentes, AVG(Price_USD) AS PrixMoyen

FROM dbo.CarSaless

GROUP BY Dealer_Region

ORDER BY TotalVentes DESC;







SELECT Annual_Income, AVG(Price_USD) AS PrixMoyen

FROM dbo.CarSaless

GROUP BY Annual_Income

ORDER BY Annual_Income;







SELECT Dealer_Name, COUNT(*) AS NombreVentes, AVG(Price_USD) AS PrixMoyen

FROM dbo.CarSaless

GROUP BY Dealer_Name

ORDER BY NombreVentes DESC;







SELECT FORMAT(Date, 'yyyy-MM') AS Mois, COUNT(*) AS NombreVentes, AVG(Price_USD) AS PrixMoyen

FROM dbo.CarSaless

GROUP BY FORMAT(Date, 'yyyy-MM')

ORDER BY Mois;



SELECT

    Gender,

    COUNT(*) AS NombreClients,

    AVG(CAST(Annual_Income AS BIGINT)) AS RevenuMoyen,

    AVG(CAST(Price_USD AS DECIMAL(18,2))) AS PrixMoyen

FROM dbo.CarSaless

GROUP BY Gender;




 

