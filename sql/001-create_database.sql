CREATE TABLE IF NOT EXISTS t_app_status (
  id BIGSERIAL,
  "date" TIMESTAMP,
  app_name varchar(255),
  status varchar(50),
  response_time float
);