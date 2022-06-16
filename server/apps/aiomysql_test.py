import asyncio
import aiomysql


@asyncio.coroutine
def go():
    pool = yield from aiomysql.create_pool(host='3.140.174.58', port=3306,
                                           user='root', password='Yy141025',
                                           db='blog', loop=loop, autocommit=False, charset="utf8")

    with (yield from pool) as conn:
        cur = yield from conn.cursor()
        yield from cur.execute("SELECT * from article")
        r = yield from cur.fetchone()
        print(r)
    pool.close()
    yield from pool.wait_closed()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(go())
