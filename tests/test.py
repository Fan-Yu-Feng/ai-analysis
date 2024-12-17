from backend.sql_app.database import SessionLocal
import backend.sql_app.social_media_comment_list_curd as social_media_comment_list_crud


def test_something():
	db = SessionLocal()
	db_user = social_media_comment_list_crud.get_social_media_info(db, 1822126883)
	print(db_user)
	try:
		yield db
	finally:
		db.close()


test_something()
