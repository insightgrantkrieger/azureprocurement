# Azure OpenAI Procurement accelerator
-  Azure OpenAI Procurement accelerator is a powerful tool that streamlines the procurement process for businesses by leveraging the capabilities of Microsoft Azure and OpenAI. This accelerator uses advanced AI to automate and optimize procurement work work by assessing and validating documents, allowing businesses to make more informed decisions and reduce costs. With its intuitive interface and powerful features, the Azure OpenAI Procurement accelerator is a game-changer for businesses looking to improve their procurement processes.

## Azure portal setup
-  Login into Azure portal
-  Create a resource group
-  Create the following resources
    -  Azure Storage account (Create 1 container)
    -  Azure AI Search 
    -  Azure OpenAI (1 Model deployment GPT 3.5 Turbo 16K)
    -  Azure sql server and database (1 database. Ensure SQL Auth and remember username and pwd)
        - Connect to the database and copy contents of SQLObjects\CreateTables.sql and then execute (Creates tables)
        - Connect to the database and copy contents of SQLObjects\InsertIntoTables.sql and then execute (Loads dummy data)

## Developer Installation

-   Install vscode and clone this repo to your desktop (Require git bash and Python 3)
-   Launch vscode and open cloned project then open Git Bash terminal and run the following:

### VSCODE gitbash environment setup
-   python -m venv procure-env
-   source procure-env/Scripts/activate
-   source procure-env/Scripts/activate
-   python.exe -m pip install --upgrade pip
-   pip install -r requirements.txt

### Configure azure resources
-   Add OpenAI, AISearch, SQL database details into confighelper.py

### Configure python app document source
-   create folder C:\\azureprocurement\\source\\ on your computer and paste PDF text documents into this folder

## Generate data with Python application
-   Place text searchable PDF's in C:\\azureprocurement\\source\\
-   In terminal run "python maincsv.py"   This will generate and load a new folder C:\\azureprocurement\\output\\  with chunked CSV's
