import datafy.postgres as pg
import sqlalchemy

host, db, user, password = 'localhost', 'postgres', 'postgres', 'postgres'

class TestPostgresConnection():

    def connection_return_mock(self):
        return


    def test_connect(self):
        p = pg.PostgresConnection(host, db, user, password )
        assert isinstance(p, pg.PostgresConnection)

    def test_run_sql(self):
        p = pg.PostgresConnection(host, db, user, password)
        result = p.run_sql("select count(1) from test_table")
        assert result.fetchone()[0] == 1