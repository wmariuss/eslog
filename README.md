# eslog

[![pipeline status]()](https://github.com/wmariuss/eslog/commits/master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/wmariuss/eslog/commits/master)
[![License](https://img.shields.io/badge/License-BSD-brightgreen.svg)](https://github.com/wmariuss/eslog/blob/master/LICENSE)

Get and send logs.

## Requirements

* `Python >= 3.7`
* `Elastic Stack >= 7.x`

## Install

Production:

* Export environment variables. Example:

    ```shell
    export ELASTICSEARCH_HOSTS=localhost # Default: localhost
    export ELASTICSEARCH_USER=user # Default: eslog
    export ELASTICSEARCH_PASS=pass # Default: eslog
    export FILE_LOG_PATH=/tmp # Default: /tmp
    ```

* For easy deployment this is built as executable. You can download it from [release](https://github.com/wmariuss/eslog/releases) section.

Development:

* `cp env .env` and change the values with yours
* `pip install pipenv`
* `pipenv install --dev`

Build executable:

* `pipenv run tox -e package`

## Usage

List all indexes

`eslog list`

Get and archive log file generated

`eslog logs --index loc-filebeat --start 2020-02-19T23:59:59 --end 2020-02-20T23:59:59 (--end command is optional)`

Help

`eslog --help`

More info, [here](docs/).

## Tests

`pytest -s -v`

## Contribute

Contributions are always welcome.

* Fork the repo
* Create a pull request against master
* Be sure tests pass (if exists)

Check [GitHub Flow](https://guides.github.com/introduction/flow/) for details.

## Authors

* [Marius Stanca](mailto:me@marius.xyz)
