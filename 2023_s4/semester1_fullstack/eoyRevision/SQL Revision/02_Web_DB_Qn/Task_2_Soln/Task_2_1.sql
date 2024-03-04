CREATE TABLE "Student" (
	"MatricNo"	TEXT,
	"Name"	TEXT NOT NULL,
	"Class"	TEXT NOT NULL,
	"IndexNo"	INTEGER NOT NULL,
	"Gender"	TEXT NOT NULL CHECK("Gender" = 'M' OR "Gender" = 'F'),
	PRIMARY KEY("MatricNo")
);

CREATE TABLE "ClassGroup" (
	"ClassGroupID"	INTEGER,
	"ClassGroupName"	TEXT NOT NULL,
	"Venue"	TEXT NOT NULL,
	PRIMARY KEY("ClassGroupID" AUTOINCREMENT)
);

CREATE TABLE "SCR" (
	"MatricNo"	TEXT,
	"ClassGroupID"	INTEGER,
	PRIMARY KEY("MatricNo","ClassGroupID"),
	FOREIGN KEY("MatricNo") REFERENCES "Student"("MatricNo"),
	FOREIGN KEY("ClassGroupID") REFERENCES "ClassGroup"("ClassGroupID")
);