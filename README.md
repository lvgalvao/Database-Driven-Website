Database-Driven Website
=======================

This project aims to provide a comprehensive guide on developing dynamic database-driven web applications using Python, Flask, and MySQL. It serves as a showcase that is divided into two parts:

1. Development and deployment of a Flask-based site
2. Connecting the Flask application to a cloud-based MySQL database and deploying a production-ready database-driven web application.

Installation
------------

To get started with this project, make sure you have the following prerequisites:

* Python 3.11
* Flask 2.3.2

You can install the required dependencies by running the following command:

```shell
$ poetry install
```

Development Dependencies
------------------------

The development dependencies for this project are defined in the `pyproject.toml` file. These dependencies are used for testing, linting, documentation generation, and other development-related tasks.

To install the development dependencies, use the following command:

```shell
$ poetry install --dev
```

The key development dependencies include:

* `ipdb` - Debugger for Python
* `pytest` - Testing framework for Python
* `pytest-cov` - Plugin for pytest that measures code coverage
* `blue` - Code formatter for Python
* `isort` - Tool for sorting imports alphabetically
* `taskipy` - Task runner for Python projects

Usage
-----

The main functionality of this project revolves around developing dynamic database-driven web applications. It provides a solid foundation for building such applications using Python, Flask, and MySQL.

Throughout the course, you will learn various concepts and techniques for developing, deploying, and maintaining these applications. The project structure follows best practices to ensure a clean and organized codebase.

Documentation
-------------

The documentation for this project is generated using Mkdocstrings Python, which extracts docstrings from the source code and converts them into human-readable documentation.

To view the documentation locally, run the following command:

```shell
$ poetry run task docs
```

This will start a local server where you can access the documentation in your browser.

Testing
-------

Testing is an essential part of developing robust web applications. This project uses pytest as the testing framework. You can run the tests and generate a coverage report by executing the following command:

```shell
$ poetry run task test
```

This will run the tests and provide detailed information about the test results and code coverage.

License
-------

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute it according to your needs.

* * *

If you have any questions or need further assistance, please contact Luciano Filho at [lvgalvaofilho@gmail.com](mailto:lvgalvaofilho@gmail.com).