export FILE_PATH=/usr/src/schema/0000_delete_everything.sql

touch $FILE_PATH

echo -e "DROP SCHEMA public CASCADE; CREATE SCHEMA public;" >> $FILE_PATH

python /usr/src/init_db.py

rm $FILE_PATH
