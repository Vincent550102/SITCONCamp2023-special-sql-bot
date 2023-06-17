CREATE TABLE items (
  id INTEGER PRIMARY KEY,
  name TEXT,
  description TEXT,
  price REAL,
  quantity INTEGER
);

CREATE TABLE categories (
  id INTEGER PRIMARY KEY,
  name TEXT
);

CREATE TABLE item_category (
  item_id INTEGER,
  category_id INTEGER,
  FOREIGN KEY (item_id) REFERENCES items (id),
  FOREIGN KEY (category_id) REFERENCES categories (id)
);
