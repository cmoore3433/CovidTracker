import COVID19Py
import os

covid19 = COVID19Py.COVID19(data_source="csbs")
try:
    data=covid19.getLocations()
except:
    print("Failure to connect, retrying...")
    data=covid19.getLocations()

states=["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
output={}
for i in states:
    output[i]=0

for i in data:
    try:
        output[i['province']]+=i['latest']['confirmed']
    except KeyError:
        continue

with open('results.html', 'w') as file:
    file.write("""<!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>Covid-19 Case Tracker</title>
        <link rel="stylesheet" href="stylish.css">
      </head>
      <body>
        <table>
            <tr>
                <th>State:</th>
                <th>Number of cases:</th>
            </tr>""")
    for state in states:
        file.write("""
        <tr>
            <td>"""+state+"""</td>
            <td>"""+str(output[state])+"""</td>
        </tr>""")
    file.write("""
        </table>
      </body>
    </html>""")

os.startfile(r"results.html")
