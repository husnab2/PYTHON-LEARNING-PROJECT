## build the project

poetry build


poetry install

On Terminal, navigate to repo and run following commands

    a. Create Virtual Env ```python3 -m venv behavex-env```

    b. Activate Virtual Env ```source behavex-env/bin/activate```

    c. Install Packages ```pip3 install -r requirements.txt```

    or

    d. Install Packages ```poetry install```

#### Running tests
* Run tests in Sequence: ```browser=chrome behavex```
* Run tests in Parallel: ```browser=chrome behavex --parallel-processes 5 --tags @test```

#### Report
* Report will be found here: ```/output/report.html```

## behavex
below environment variable need to be set before run tests 

BEHAVEX_PATH=src/python_learning_project, 

FEATURES_PATH= src/python_learning_project

browser=chrome behavex
https://behavex.readthedocs.io/
context.base_url = os.getenv('BASE_URL', <default_base_url>)

