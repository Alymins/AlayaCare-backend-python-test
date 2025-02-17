DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL
);

DROP TABLE IF EXISTS todos;
CREATE TABLE todos (
  id INTEGER PRIMARY KEY,
  user_id INT(11) NOT NULL,
  description VARCHAR(255),
  completed VARCHAR(100) DEFAULT 'unchecked',
  FOREIGN KEY (user_id) REFERENCES users(id)
);