# Importing the required libraries
import xml.etree.ElementTree as Xet
import pandas as pd
  
cols = ["orden","segd", "segi","color"]
rows = []
  
# Parsing the XML file
xmlparse = Xet.parse('C:/Users/54112/Documents/indec/plugin/salidagrafica-atlas-master/salidagrafica-atlas-master/estilo_radio/segmentos.qml')
root = xmlparse.getroot()
for i in root:
    segd = i.find(str("segd&quot"))
    segi = i.find("segi")
    color = i.find("color")

  
  
  
    rows.append({"segd": segd,
                 "segi": segi,
                 "color":color
                })

   
  
df = pd.DataFrame(rows, columns=cols)
print(df)
  
# Writing dataframe to csv
df.to_csv('output.csv')
