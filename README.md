# Ntshoekhe
Ntshoekhe

Ntsoekhe is a distributed database management system (DDBMS) designed for the digital health sector. It facilitates secure, efficient storage and management of health-related data across multiple nodes, ensuring data integrity, availability, and confidentiality.

**Prerequisites:**

    Python 3.9 or later
    Django framework
    Docker Desktop 
    
**Installation and Setup(all commands are linux based)**
      these commands must be run on the vscode terminal
-Create Virtual Environment using this "python -m venv env" 
-Install Dependencies using pip install -r requirements.txt

**Building Docker Images**
Assuming we are already in the directory that contains docker-compose.yml we run:
  we run the command to build an image "docker-compose build"

**Running the system:**

-Start Docker Services(if using docker desktop) using the command "docker-compose up -d


**lastly run the django server**
-using this "python manage.py runserver" command we run the server

Currently the CRUD opertions on the health data can be done on django admin interfacebut we are working on a custom django views that will handle user for CRUD operations on health data models. 










