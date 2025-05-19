from sqlalchemy import create_engine, text, update
from sqlalchemy.orm import Session

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# The 'Connection' object
with engine.connect() as conn:
    result = conn.execute(text("SELECT 'Hello, World'"))
    # `result` is an object of type 'Result'
    print(result.all())
    conn.commit()  # 'Commit-as-you-go' style

# 'Begin-once' style
with engine.begin() as conn:
    # this is an implicit transaction block
    createResult = conn.execute(text("CREATE TABLE IF NOT EXISTS table_1 (x int, y int)"))
    print(createResult)
    insertResult = conn.execute(
            text("INSERT INTO table_1 (x, y) VALUES (:x_val, :y_val)"),
            [{"x_val": 1, "y_val": 2}, {"x_val": 3, "y_val": 4}]
        )
    print(insertResult)
    selectResult = conn.execute(text("SELECT * FROM table_1"))
    print(selectResult.all())

# The 'Session' object (ORM-style)
with Session(engine) as session:
    updateResult = session.execute(
            text("UPDATE table_1 SET y=10*x where x=:x_val"),
            [{"x_val": 1}, {"x_val": 3}]
        )
    selectResult = session.execute(text("SELECT * FROM table_1"))
    print(selectResult.all())
    session.commit()

"""
CORE
Metadata: table-name to 'Table' object mapping

ORM
(All tables are declared as classes)
Declarative base
- Base class for all table-classes
- Contains registry and metadata attributes as well
"""
