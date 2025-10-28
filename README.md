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

## HTTP methods

- [https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods)
- GET - adatok lekérése
- POST - erőforrás létrehozása
- PUT - update (replace)
- PATCH - update (partial)
- DELETE - törlés

## HTTP Status codes
- [https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)
- Informational responses (100 – 199)
- Successful responses (200 – 299)
- Redirection messages (300 – 399)
- Client error responses (400 – 499)
- Server error responses (500 – 599)

## REST endpoints

- GET all: /items
- GET one by id: /items/:itemId
- POST: /items
- PUT: /items/:itemId
- PATCH: /items/:itemId
- DELETE: /items/:itemId

## CRUD 
- Create - POST
- Read - GET
- Update - PUT/PATCH
- Delete - DELETE

# Clean Arhitecture
- Controller: dummy, csak request reponse
- Service: Business Logic
- Repository: persistency (database)