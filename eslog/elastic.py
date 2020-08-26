import re
from elasticsearch import Elasticsearch


class EsLog(object):
    def __init__(
        self,
        hosts=[],
        auth={},
        scheme="https",
        port=9200,
        verify_certs=False,
        ssl_show_warn=False,
    ):
        self.hosts = hosts
        self.username = auth.get("username")
        self.passwd = auth.get("password")
        self.scheme = scheme
        self.port = port
        self.verify_certs = verify_certs
        self.ssl_show_warn = ssl_show_warn

    @property
    def _conn(self):
        """
        Create a connection to ES
        """
        elastic = Elasticsearch(
            hosts=self.hosts,
            http_auth=(self.username, self.passwd),
            scheme=self.scheme,
            port=self.port,
            verify_certs=self.verify_certs,
            ssl_show_warn=self.ssl_show_warn,
        )
        health = elastic.cluster.health()

        if health:
            return elastic
        return

    @property
    def ping(self):
        """Check if ES server respond"""
        return self._conn.ping()

    @property
    def indexes(self):
        """Get all indexes"""
        return [index for index in self._conn.indices.get_alias("*")]

    def match_index(self, index_name):
        """Match index"""
        index_list = []

        for index in self.indexes:
            match_index = re.search("{}.+$".format(index_name), index)
            if match_index:
                index_list.append(index)
        return index_list

    def search(
        self,
        start_time,
        end_time,
        index=[],
        fields=["host", "message"],
        size=10000,
        scroll="5s",
    ):
        """
        Get logs based on time range. Example time:
        start (2020-02-19T23:59:59 or now-5m) and end (2020-02-21T00:00:00 or now)
        """
        return self._conn.search(
            body={
                "_source": fields,
                "query": {
                    "range": {
                        "@timestamp": {
                            "gte": "{}".format(start_time),
                            "lte": "{}".format(end_time),
                        }
                    },
                },
            },
            index=index,
            size=size,
            scroll=scroll,
        )

    def scroll(self, id, scroll="5s"):
        """
        Scroll for large result.
        """
        return self._conn.search(scroll_id=id, scroll=scroll)

    def get_logs(self, data):
        """
        Get all logs.
        """
        return data["hits"]["hits"]

    def prepare_logs(self, data, path):
        count = 0

        with open(path, "w") as content:
            for d in data:
                count += 1
                source = d["_source"]
                host = source["host"]["hostname"]
                message = source.get("message")

                content.write("{}: {}\n".format(host, message))
        return count
