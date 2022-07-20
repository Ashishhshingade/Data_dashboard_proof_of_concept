# Data Dashboard (Proof Of Concept)

Data dashboard using chart js and django (backend), fetched data from remote sql server.

In Django Setting. py is supposed to be immutable and the data we got was on multiple databases i.e one database for one restaurant.
To counter this we used mysql connector to read the data in python files.
To display the data using chart js we dump the json data from python and pass it using context to the html file.
The user(Restaurant owners) have to login through the portal by entering the username and password which will be used to fetch the
respective database for the visualizations.

![image](https://user-images.githubusercontent.com/66113291/180042662-58136ac5-7399-4680-a4e8-f62f9318cd99.png)
![image](https://user-images.githubusercontent.com/66113291/180042712-58c814d2-146d-41fc-9a34-daf6dd33c91d.png)
