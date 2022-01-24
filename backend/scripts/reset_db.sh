touch schema/9999_delete_everything.sql

echo -e "DROP SCHEMA public CASCADE; CREATE SCHEMA public;" >> schema/9999_delete_everything.sql

python dummy_main.py > /dev/null

rm schema/9999_delete_everything.sql

python dummy_main.py
