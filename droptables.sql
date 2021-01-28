use wisp;
drop table pm10;
drop table pm25;
drop table iaq_accuracy;
drop table iaq;
drop table temperature;
drop table humidity;
drop table pressure;
drop table gas;
drop table iaq_static;
drop table CO2e;
drop table VOCe;
drop table formaldehyde;
drop table temperature_;
drop table humidity_;
drop table pressure_;
drop table gas_;
drop table altitude_;

create table pm10 (
        currBox int,
	currTime timestamp,
	currValue float NOT NULL,
	PRIMARY KEY(currBox, currTime)
);

create table pm25 (
	currBox int,
	currTime timestamp,
	currValue float NOT NULL,
	PRIMARY KEY(currBox, currTime)
);

create table iaq_accuracy (
	currBox int,
	currTime timestamp,
	currValue varchar(12) NOT NULL,
	PRIMARY KEY(currBox, currTime)
);

create table iaq (
	currBox int,
	currTime timestamp,
	currValue float NOT NULL,
	PRIMARY KEY(currBox, currTime)
);

create table temperature (
	currBox int,
	currTime timestamp,
	currValue float NOT NULL,
	PRIMARY KEY(currBox, currTime)
);

create table humidity (
	currBox int,
	currTime timestamp,
	currValue float NOT NULL,
	PRIMARY KEY(currBox, currTime)
);

create table pressure (
	currBox int,
	currTime timestamp,
	currValue float NOT NULL,
	PRIMARY KEY(currBox, currTime)
);

create table gas (
	currBox int,
	currTime timestamp,
	currValue float NOT NULL,
	PRIMARY KEY(currBox, currTime)
);

create table iaq_static (
	currBox int,
	currTime timestamp,
	currValue float NOT NULL,
	PRIMARY KEY(currBox, currTime)
);

create table CO2e (
	currBox int,
	currTime timestamp,
	currValue float NOT NULL,
	PRIMARY KEY(currBox, currTime)
);

create table VOCe (
	currBox int,
	currTime timestamp,
	currValue float NOT NULL,
	PRIMARY KEY(currBox, currTime)
);

create table temperature_ (
	currBox int,
	currTime timestamp,
	currValue float NOT NULL,
	PRIMARY KEY(currBox, currTime)
);

create table altitude_ (
	currBox int,
	currTime timestamp,
	currValue float NOT NULL,
	PRIMARY KEY(currBox, currTime)
);

create table humidity_ (
	currBox int,
	currTime timestamp,
	currValue float NOT NULL,
	PRIMARY KEY(currBox, currTime)
);

create table pressure_ (
	currBox int,
	currTime timestamp,
	currValue float NOT NULL,
	PRIMARY KEY(currBox, currTime)
);

create table gas_ (
	currBox int,
	currTime timestamp,
	currValue float NOT NULL,
	PRIMARY KEY(currBox, currTime)
);

create table formaldehyde (
	currBox int,
	currTime timestamp,
	currValue float NOT NULL,
	PRIMARY KEY(currBox, currTime)
);

