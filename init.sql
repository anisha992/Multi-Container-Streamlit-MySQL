CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(100)
);

INSERT INTO users (name, email)
VALUES 
  ('Anisha', 'a@example.com'),
  ('Asha', 'b@example.com');
