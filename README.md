# FastAPI

## Non sync excution
- threading
  - nem valódi párhuzamos
  - a GIL (Global Interpreter Lock) egyszerre egy szál futását engedi
  - I/O műveletek gyorstására használunk szálakat
  - bár nem valódi párhuzamos, nagyon hatékony
- multiprocessing
  - valódi párhuzamos végrehajtás
  - proc heavy műveleteknél használjuk
- async
  - nem valódi párhuzamos végrehajtás
  - egy szál van
  - event loop