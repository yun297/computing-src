-- Task 4.1

CREATE TABLE Kisok (
    KisokID INTEGER PRIMARY KEY AUTOINCREMENT,
    Location TEXT,
    Rating REAL,
);

CREATE TABLE BentoBox (
    BentoxName TEXT PRIMARY KEY,
    ProductionCost REAL,
    ContainEgg INTEGER,
    ContainNut INTEGER,
    ContainSeafood INTEGER,
);

CREATE TABLE KisokBento (
    FOREIGN KEY KisokID INTEGER REFERENCES Kisok(KisokID),
    FOREIGN KEY BentoName TEXT REFERENCES BentoBox(BentoName),
    SellPrice REAL,
);