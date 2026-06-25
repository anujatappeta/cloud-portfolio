CREATE TABLE contacts (
  id int NOT NULL AUTO_INCREMENT,
  name varchar(100) DEFAULT NULL,
  email varchar(100) DEFAULT NULL,
  message text,
  PRIMARY KEY (id)
);
