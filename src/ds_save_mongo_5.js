use myDB
show dbs
show tables
db.myCol.insert({"Persons":[{"id":"201511079", "이름":"KangEunda"},{"id":"201511095","이름":"김지영"}]})
db.myCol.find({"Persons.이름":"김지영"})