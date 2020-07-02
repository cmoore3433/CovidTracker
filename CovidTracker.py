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
        <button onclick="swapTables()">Order by Name/# of cases</button>
        <div id="nameTable" style="display:block;">
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
        </div>
        <div id="caseTable" style="display:none;">
        <table>
            <tr>
                <th>#</th>
                <th>State:</th>
                <th>Number of cases:</th>
            </tr>""")
    output=list(output.items())
    output.sort(key=lambda state: state[1], reverse=True)
    rank=1 # I didn't want to make a nested for loop just to number the states' ranks
    for stateTup in output:
        file.write("""
            <tr>
                <td>"""+str(rank)+"""</td>
                <td>"""+stateTup[0]+"""</td>
                <td>"""+str(stateTup[1])+"""</td>
            </tr>""")
        rank+=1
    file.write("""
        </table>
        </div>
        <script>
        function swapTables() {
            if(document.getElementById("nameTable").style.display=="block") {
                document.getElementById("nameTable").style.display = "none";
                document.getElementById("caseTable").style.display = "block";
            } else {
                document.getElementById("nameTable").style.display = "block";
                document.getElementById("caseTable").style.display = "none";
            }
        }
        </script>
      </body>
    </html>""")
# From what I read, this will only work on Windows but honestly that's okay because it's just being helpful
# That and all the people I'm giving this to have Windows machines
os.startfile(r"results.html")
