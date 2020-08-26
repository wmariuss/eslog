# eslog

## Commands

* Help message.

    ```shell
    Usage: eslog [OPTIONS] COMMAND [ARGS]...

    Get and send logs

    Options:
    --version  Show the version and exit.
    --help     Show this message and exit.

    Commands:
    list  List all indexes.
    logs  Get and archive logs based on timestamp.
    ```

* List all indexes.

    ```shell
    --- eslog list
    loc-filebeat-7.6.0-2020.02.26
    security-auditlog-2020.02.25
    loc-filebeat-7.6.0-2020.02.24
    loc-filebeat-7.6.0-2020.03.03
    security-auditlog-2020.03.03
    loc-filebeat-7.6.0-2020.02.25
    security-auditlog-2020.02.24
    security-auditlog-2020.02.28
    ```

* Get last logs and archive them (last 5 min).

    ```shell
    --- eslog logs -i loc-filebeat -s now-5m
    Total 31 logs written in /tmp/loc-filebeat-2020-03-03T16:24:40.563510Z
    Archiving log file...
    ```

* Get last logs and archive them from a specific time.

    ```shell
    --- eslog logs -i loc-filebeat -s 2020-03-03T16:27:47.651Z
    Total 6 logs written in /tmp/loc-filebeat-2020-03-03T16:28:46.199276Z
    Archiving log file...
    ```

* Get logs from specific time and archive them (start and end time).

    ```shell
    --- eslog logs -i loc-filebeat -s 2020-03-03T16:27:47.651 -e 2020-03-03T16:50:47.651
    Total 35 logs written in /tmp/loc-filebeat-2020-03-03T16:33:09.705413Z
    Archiving log file...
    ```

* Get last logs and archive them by custom project name (last 5 min).

    ```shell
    --- eslog logs -i loc-filebeat -s now-5m -p project-name
    Total 31 logs written in /tmp/project-name-2020-03-03T16:35:38.944328Z
    Archiving log file...
    ```
