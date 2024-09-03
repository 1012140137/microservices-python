// use mongodb database "celery_backend"
db = db.getSiblingDB('celery_backend');
// create collection "tbl_user" and install first document if not existing else do nothing
if (!db.tbl_user.count()) {
    db.tbl_user.insertOne({
        "name": "admin",
        "display_name": "admin",
        "email": "xx@xx.com",
        "access_token": "token1-xx"
    });
}