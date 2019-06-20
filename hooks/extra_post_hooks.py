import os
import shutil

SUCCESS = "\x1b[1;32m [SUCCESS]: "
TERMINATOR = "\x1b[0m"

def run():
    shutil.rmtree("compose")
    shutil.rmtree("requirements")
    shutil.rmtree("docs")
    os.remove("requirements.txt")
    os.remove("merge_production_dotenvs_in_dotenv.py")
    os.remove("local.yml")
    os.remove("production.yml")

    print(SUCCESS + "1. Run `direnv allow` to activate your local env" + TERMINATOR)
    print(SUCCESS + "2. Install node and autofix the initial set of html files!" + TERMINATOR)
    print(SUCCESS + "3. pip install -r requirements.txt" + TERMINATOR)
    print(SUCCESS + "4. docker-compose up -d postgres" + TERMINATOR)
    print(SUCCESS + "5. ./manage.py migrate" + TERMINATOR)
    print(SUCCESS + "6. ./manage.py runserver_plus" + TERMINATOR)
