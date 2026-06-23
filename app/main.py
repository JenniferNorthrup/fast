from fastapi import FastAPI
# from app.cache import redis_client
# from app.db import get_conn

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "prod fastapi on eks"}

# @app.get("/cache-test")
# def cache_test():
#     redis_client.set("ping", "pong")
#     return {"redis": redis_client.get("ping")}

# @app.get("/db-test")
# def db_test():
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute("SELECT 1;")
#     return {"db": cur.fetchone()[0]}