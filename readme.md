# azure-producrement-demo

Demo how to use Azure hosted Search and AI to answer questions based on documents

## Project setup

```sh
python3 -m venv venv
source venv/bin/activate        # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Run the project

### (Re-)Create the database tables

```sh
source venv/bin/activate        # On Windows use `venv\Scripts\activate`
python rebuild_database.py
```

### Add questions for the tender

The questions are stored in `questions.csv` update that file, but keep the
header line.

```sh
source venv/bin/activate        # On Windows use `venv\Scripts\activate`
python add_questions.py
```

### Process the data, this will provide some output to the console

```sh
source venv/bin/activate        # On Windows use `venv\Scripts\activate`
python process.py
```

### Show the result on the console

```sh
source venv/bin/activate        # On Windows use `venv\Scripts\activate`
python show_results.py
```

## Environment variables

The code depends on the following environment variables to be set.
Either via export commands in the current shell, or stored in a .env file.
(Don't commit the .env)

- DB_USER
- DB_PASS
- DEBUG (optionally)
- AISEARCH_API_KEY
- OPENAI_API_KEY
- LOCAL (optionally, use sqlite database)
