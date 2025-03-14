CREATE TABLE patients(
patient_id INT PRIMARY KEY,
first_name TEXT,
last_name TEXT,
age INT,
gender TEXT,
contact TEXT);

CREATE TABLE doctors (
doctor_id INT PRIMARY KEY,
first_name TEXT,
last_name TEXT,
speciality Text,
contact TEXT);

CREATE TABLE appointments (
appointment_id INT PRIMARY KEY,
patient_id INT,
doctor_id INT,
appointment_date DATE,
appointment_time TIME,
FOREIGN KEY(patient_id) REFERENCES patients(patient_id),
FOREIGN KEY(doctor_id) REFERENCES doctors(doctor_id)
);

CREATE TABLE bills (
bill_id INT PRIMARY KEY,
patient_id INT,
service TEXT,
total_amount DECIMAL(10,2),
bill_date DATE,
FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
);

CREATE TABLE medicalrecords(
record_id INT PRIMARY KEY,
patient_id INT,
doctor_id INT,
diagnosis TEXT,
prescription TEXT,
date DATE,
FOREIGN KEY(patient_id) REFERENCES patients(patient_id),
FOREIGN KEY(doctor_id) REFERENCES doctors(doctor_id)
);
