# Protected Routes - Authentication Middleware

## Használat

### 1. Regisztráció

```bash
POST /api/auth/registration
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "secret123",
  "first_name": "John",
  "last_name": "Doe"
}
```

### 2. Bejelentkezés

```bash
POST /api/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "secret123"
}
```

Ez visszaad egy cookie-t `access_token` néven, ami tartalmazza a JWT tokent.

### 3. Védett endpoint használata

A védett endpoint-ok automatikusan ellenőrzik a cookie-ban lévő JWT tokent.

**Példa: Jelenlegi felhasználó lekérdezése**

```bash
GET /api/auth/me
Cookie: access_token=<your_jwt_token>
```

**Válasz ha be vagy jelentkezve:**
```json
{
  "user_id": 1,
  "message": "You are authenticated!"
}
```

**Válasz ha nincs token vagy lejárt:**
```json
{
  "detail": "Not authenticated - no token found"
}
```

### 4. User frissítése (védett)

```bash
PATCH /api/users/1
Cookie: access_token=<your_jwt_token>
Content-Type: application/json

{
  "first_name": "Jane"
}
```

### 5. User törlése (védett)

```bash
DELETE /api/users/1
Cookie: access_token=<your_jwt_token>
```

### 6. Kijelentkezés (védett)

```bash
POST /api/auth/logout
Cookie: access_token=<your_jwt_token>
```

Ez törli a cookie-t.

## Védett route-ok listája

- ✅ `GET /api/auth/me` - Jelenlegi user ID lekérdezése
- ✅ `POST /api/auth/logout` - Kijelentkezés
- ✅ `PATCH /api/users/{user_id}` - User frissítése
- ✅ `DELETE /api/users/{user_id}` - User törlése

## Nem védett route-ok

- `POST /api/auth/registration` - Regisztráció
- `POST /api/auth/login` - Bejelentkezés
- `GET /api/users/` - Összes user listázása
- `GET /api/users/{user_id}` - Egy user lekérdezése

## Middleware működése

A `get_current_user_id` dependency:
1. Kiolvassa az `access_token` cookie-t
2. Dekódolja a JWT tokent
3. Ellenőrzi a token érvényességét
4. Visszaadja a `user_id`-t

Ha bármelyik lépés sikertelen → **401 Unauthorized** hiba

## Postman használat

1. **Login request**
   - POST `http://localhost:8000/api/auth/login`
   - Body: JSON with email + password
   - Postman automatikusan elmenti a cookie-t

2. **Protected request**
   - GET `http://localhost:8000/api/auth/me`
   - Postman automatikusan elküldi a cookie-t
   - Ha nem működik, ellenőrizd a Cookies kezelését Postman-ben

## Opcionális védelem

Ha olyan route-ot akarsz, ami működik token nélkül is, de használja ha van:

```python
from ..auth.middleware import get_current_user_id_optional

@user_router.get("/optional")
async def optional_route(
    current_user_id: Optional[int] = Depends(get_current_user_id_optional)
):
    if current_user_id:
        return {"message": "Authenticated", "user_id": current_user_id}
    return {"message": "Not authenticated"}
```

## Token a Header-ben (alternatív)

Ha nem cookie-t akarsz használni, hanem Authorization header-t:

```python
from ..auth.middleware import get_current_user_id_from_header

@user_router.get("/protected")
async def protected(
    current_user_id: int = Depends(get_current_user_id_from_header)
):
    return {"user_id": current_user_id}
```

Ekkor a request:
```bash
GET /api/users/protected
Authorization: Bearer <your_jwt_token>
```
