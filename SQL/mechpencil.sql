CREATE TABLE store (
  productid INTEGER PRIMARY KEY,
  name TEXT,
  quantity INTEGER,
  price INTEGER
);

INSERT INTO store VALUES (1, "Pentel Graph 1000", 100, 30);
INSERT INTO store VALUES (2, "Pentel Graphgear 1000", 100, 35);
INSERT INTO store VALUES (3, "Pentel Kerry", 100, 35);
INSERT INTO store VALUES (4, "Pentel Orenz Nero", 100, 40);
INSERT INTO store VALUES (5, "Pilot S20", 100, 30);
INSERT INTO store VALUES (6, "Tombow Zoom C10", 100, 50);
INSERT INTO store VALUES (7, "Kurutoga Metal", 100, 50);
INSERT INTO store VALUES (8, "STAEDTLER 925 25", 100, 40);
INSERT INTO store VALUES (9, "STAEDTLER 925 25", 100, 40);
INSERT INTO store VALUES (10, "STAEDTLER 925 25", 100, 40);
INSERT INTO store VALUES (11, "STAEDTLER 925 35", 100, 45);
INSERT INTO store VALUES (12, "Kurutoga Dive", 100, 55);
INSERT INTO store VALUES (13, "Zebra DelGuard", 100, 20);
INSERT INTO store VALUES (14, "Pentel Graphgear 500", 100, 20);
INSERT INTO store VALUES (15, "Tombow Monograph", 100, 40);

SELECT * FROM store ORDER BY productid;
SELECT * FROM store ORDER BY price;
