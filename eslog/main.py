import os
import click
from datetime import datetime

from eslog.elastic import EsLog
from eslog.utils import pretty, archive

HOSTS = os.getenv("ELASTICSEARCH_HOSTS", "localhost")
ES = EsLog(
    hosts=[host for host in HOSTS.split(";")],
    auth={
        "username": os.getenv("ELASTICSEARCH_USER", "eslog"),
        "password": os.getenv("ELASTICSEARCH_PASS", "eslog"),
    },
)
TEMP_PATH = os.getenv("FILE_LOG_PATH", "/tmp")


@click.group()
@click.version_option()
def cli():
    """Get and send logs"""


@cli.command(help="List all indexes.")
def list():
    """
    List all indexes.
    """
    if ES.ping:
        for index in ES.indexes:
            click.echo(index)
    else:
        click.echo("There is not connection to Elasticsearch server")


@cli.command()
@click.option("--index", "-i", help="Get logs.", required=True)
@click.option("--start", "-s", help="Give a start time.", required=True)
@click.option("--end", "-e", help="Give an end time.")
@click.option(
    "--project",
    "-p",
    help="Give a name of the project. This will help to identify the log file",
)
def logs(index, start, end, project):
    """
    Get and archive logs based on timestamp.
    """
    if index and start:
        if ES.ping:
            index_list = ES.match_index(index)
            current_time = datetime.now()
            format_time = current_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            log_file = "{}/{}-{}".format(TEMP_PATH, project, format_time)

            if not project:
                log_file = "{}/{}-{}".format(TEMP_PATH, index, format_time)

            if not end:
                end = format_time

            if len(index_list) >= 1:
                logs = ES.search(index=index_list, start_time=start, end_time=end)
                get_logs = ES.get_logs(logs)
                prepare = ES.prepare_logs(get_logs, path=log_file)
                click.echo("Total {} logs written in {}".format(prepare, log_file))
                click.echo("Archiving log file...")
                archive(log_file)
            else:
                click.echo("There is not any index with the {} name".format(index))
        else:
            click.echo("There is not connection to Elasticsearch server")
    else:
        click.echo("Specify --index/-i and --start/-s commands")
