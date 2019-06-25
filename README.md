# Nse_Report
Using the mongo and its concepts for storing and modelling the data for the purpose of Analysis.


Goal: To get the data(.csv) from the URL or from the machine and convert to the json for loading it to Mongo. Now use this data to for analysis, it may need some modelling techniques(Embedding(UnNormalized) or Reference(Normalized)) which will offer the query optimizations.

Library Stack:<br/>
1 Requests(for data from the url) <br/> 
2 Tkinter(for the Gui in python) <br/> 
3 CSV(for operations on csv) <br/> 
4 JSON(for operaton on JSON) <br/>
5 Pymongo(Bridge librarie for python and mongo)<br/>
6 <br/>   

Program Flow:<br/>
1 Collecting the Files from the Local Machine(Tkinter) or can be done by URL(Requests)<br/>
2 Now read these collected files (.csv) and convert them to the (.json)<br/>
3 By connecting the Python program to mongo using the Pymongo now load the Files to the Mongo DB<br/>
4 Writing some rudimentry Queries on the Schema<br/>
5 Showing the Results using Matplot.lib<br/>

