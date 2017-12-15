"""datafy.postgres
~~~~~~~~~~~~~~~~~~

This module provides a PostgresConnection object to manage access to a postgres instance with some ready to use methods
for doing common tasks.
"""
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import logging
log = logging.getLogger(__name__)


class PostgresConnection():
    def __init__(self, host, database, user, password):
        self.engine = create_engine("postgres://{0}:{1}@{2}/{3}".format(user, password, host, database))
        self.connection = self._connect()

    def _connect(self):
        """Establish connection to Postgres database

        :return: Connection to Postgres
        :rtype sqlalchemy.engine.Connection
        """
        return self.engine.connect()

    def run_sql(self, query):  # courseTagDict
        """Runs SQL statement and commits changes to database.
        Returns :class:`result <sqlalchemy.engine.result>` object with results of the execute call

        :param query: Valid query string
        :type query: string

        :return: ResultProxy from executing statement, acts similar to a cursor
        :rtype sqlalchemy.engine.result.ResultProxy
        """
        log.debug("Run postgres query: %s", query)
        result = self.connection.execute(query)

        return result



