create_csv:
	python create_db.py

create_postgres:
	create_csv
	docker build -t ${POSTGRES_IMAGE} -f Dockerfile_postgres .
	docker run --rm --name ${POSTGRES_CONTAINER} -v ${HOME}/Sync/${POSTGRES_DB}/pgdata:/var/lib/postgresql/data -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} -e POSTGRES_DB=${POSTGRES_DB} -p 5432:5432 ${POSTGRES_IMAGE}
	mv raw_data/merged.csv ~/Sync/${POSTGRES_DB}/pgdata
	docker exec -it ${POSTGRES_CONTAINER} psql -U postgres -d ${POSTGRES_DB}
	@echo "copy below into shell \n copy airbnb FROM '/var/lib/postgresql/data/merged.csv' DELIMITER ',' CSV HEADER;"

