import sqlite3
import json
from flask import render_template

con = sqlite3.connect('laptop.db')
cur = con.cursor()
brand = 'Dell'
price = '5'
if brand == 'NoBrand':
                if price == '1':
                    cur.execute("SELECT IF.ID, IF.IMAGE, BR.PRICE,  BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE BR.PRICE < 5000000 ORDER BY PL.DESIGN DESC, PL.VGA DESC, IF.WEIGHT ASC, IF.SCREEN ASC LIMIT 5")
                elif price == '2':
                    cur.execute("SELECT IF.ID, IF.IMAGE, BR.PRICE,  BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE 5000000 <= BR.PRICE and BR.PRICE <= 10000000 ORDER BY PL.DESIGN DESC, PL.VGA DESC, IF.WEIGHT ASC, IF.SCREEN ASC LIMIT 5")
                elif price == '3':
                    cur.execute("SELECT IF.ID, IF.IMAGE, BR.PRICE,  BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE 10000000 <= BR.PRICE and BR.PRICE <= 15000000 ORDER BY PL.DESIGN DESC, PL.VGA DESC, IF.WEIGHT ASC, IF.SCREEN ASC LIMIT 5")
                elif price == '4':
                    cur.execute("SELECT IF.ID, IF.IMAGE, BR.PRICE,  BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE 15000000 <= BR.PRICE and BR.PRICE <= 20000000 ORDER BY PL.DESIGN DESC, PL.VGA DESC, IF.WEIGHT ASC, IF.SCREEN ASC LIMIT 5")
                elif price == '5':
                    cur.execute("SELECT IF.ID, IF.IMAGE, BR.PRICE,  BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE 20000000 <= BR.PRICE and BR.PRICE <= 25000000 ORDER BY PL.DESIGN DESC, PL.VGA DESC, IF.WEIGHT ASC, IF.SCREEN ASC LIMIT 5")
                elif price == '6':
                    cur.execute("SELECT IF.ID, IF.IMAGE, BR.PRICE,  BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE BR.PRICE > 25000000 ORDER BY PL.DESIGN DESC, PL.VGA DESC, IF.WEIGHT ASC, IF.SCREEN ASC LIMIT 5")
            else:
                if price == '1':
                    temp = "SELECT IF.ID, IF.IMAGE, BR.PRICE,  BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE BR.BRAND = '" + brand + "' AND BR.PRICE < 5000000 ORDER BY PL.DESIGN DESC, PL.VGA DESC, IF.WEIGHT ASC, IF.SCREEN ASC LIMIT 5"
                    cur.execute(temp)
                elif price == '2':
                    temp = "SELECT IF.ID, IF.IMAGE, BR.PRICE,  BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE BR.BRAND = '" + brand + "' AND 5000000 <= BR.PRICE and BR.PRICE <= 10000000 ORDER BY PL.DESIGN DESC, PL.VGA DESC, IF.WEIGHT ASC, IF.SCREEN ASC LIMIT 5"
                    cur.execute(temp)
                elif price == '3':
                    temp = "SELECT IF.ID, IF.IMAGE, BR.PRICE,  BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE BR.BRAND = '" + brand + "' AND 10000000 <= BR.PRICE and BR.PRICE <= 15000000 ORDER BY PL.DESIGN DESC, PL.VGA DESC, IF.WEIGHT ASC, IF.SCREEN ASC LIMIT 5"
                    cur.execute(temp)
                elif price == '4':
                    temp = "SELECT IF.ID, IF.IMAGE, BR.PRICE,  BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE BR.BRAND = '" + brand + "' AND 15000000 <= BR.PRICE and BR.PRICE <= 20000000 ORDER BY PL.DESIGN DESC, PL.VGA DESC, IF.WEIGHT ASC, IF.SCREEN ASC LIMIT 5"
                    cur.execute(temp)
                elif price == '5':
                    temp = "SELECT IF.ID, IF.IMAGE, BR.PRICE,  BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE BR.BRAND = '" + brand + "' AND 20000000 <= BR.PRICE and BR.PRICE <= 25000000 ORDER BY PL.DESIGN DESC, PL.VGA DESC, IF.WEIGHT ASC, IF.SCREEN ASC LIMIT 5"
                    cur.execute(temp)
                elif price == '6':
                    temp = "SELECT IF.ID, IF.IMAGE, BR.PRICE,  BR.PRICE,  IF.SCREEN, IF.CPU, IF.RAM, IF.VGA, IF.OS, IF.WEIGHT, IF.LINK FROM INFORMATION IF JOIN POINTLAPTOP PL ON IF.ID = PL.ID JOIN BRAND BR ON PL.ID = BR.ID WHERE BR.BRAND = '" + brand + "' AND BR.PRICE > 25000000 ORDER BY PL.DESIGN DESC, PL.VGA DESC, IF.WEIGHT ASC, IF.SCREEN ASC LIMIT 5"
                    cur.execute(temp)
# data = cur.fetchall()
columns = [column[0] for column in cur.description]
results = []
for row in cur.fetchall():
    results.append(dict(zip(columns, row)))
print (results)
# item = json.dumps(data)

# print (item)