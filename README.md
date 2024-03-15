# ME Inventory Management

The ME Inventory Management monitors the items in Mintal Elementary School. With the app, the property custodian should be able to input:

- Serial Number of the items store
- Property ID (basically 1 for mouse, 2 for keyboard, and so on…)
- Room ID
- Item Specification (Ergonomic Keyboard, Ergonomic Mouse)
- Acquisition Date
- Custodian ID
- Description ID (1 - Item is ok, 2 - Item is broken, 3 item is missing)

Current Problem at Hand: Cannot connect to the database

# Techonologies Used

- Python
- MySQL
- XAMPP Control Panel

# Tables

<pre>
You may also refer to the Crow's Foot ERD.png

Table: Serialized_Items

PK serial_number *VARCHAR 16*

PK property_id *INT 3*

FK room_id *INT 3*

item_specification *VARCHAR 50* 

Table: Item_Type

PK item_type_id *INT 3*

PK item_type_name *VARCHAR 50*

Table: Acquisition

PK acquisition_id *INT 3*

FK company_id *INT 3*

FK custodian_id *INT 7*

acquisition_date *DATE*

Table: Acquisition Details

PK property_id *INT 3*

PK item_type_id *INT 3*

FK acquisition_id *INT 3*

Table: ICT Room

PK room_id *INT 3*

FK custodian_id *INT 7*

room_name *VARCHAR 50*

Table: Property_Custodian

PK custodian_id *INT 7*

name *VARCHAR 50*

gender *VARCHAR 20*

contact_information *VARCHAR 15*

start_date *DATE*

Table: Class

PK class_id *INT 3*

FK teacher_id *INT 7*

class_name *VARCHAR 50*

Table: Monitoring

FK attendance_id *INT 3*

FK serial_number *VARCHAR 16*

FK description_id *INT 3*

Table: Teacher

PK teacher_id *INT 7*

PK teacher_name *VARCHAR 50*

teacher_gender *VARCHAR 20*

teacher_contact_information *VARCHAR 15*

Table: Description

PK description_id *INT 3*

description_name *VARCHAR 50*

Table: Student

PK student_id *INT 12*

PK student_name *VARCHAR 50*

student_gender *VARCHAR 20*

student_contact_information *VARCHAR 15*

student_year_level *INT 2*

Table: Student_Attendance

PK attendance_id *INT 3*

FK student_id *INT 12*

Table: Company

PK company_id *INT 8*

company_name *VARCHAR 50*

company_address *VARCHAR 50*

company_contact_number *VARCHAR 15*

</pre>

# CLI Command

Commands for creating tables:

```
CREATE TABLE Serialized_Items (
    serial_number VARCHAR(16),
    property_id INT(3),
    room_id INT(3),
    item_specification VARCHAR(50),
    PRIMARY KEY (serial_number, property_id)
);

CREATE TABLE Item_Type (
    item_type_id INT(3),
    item_type_name VARCHAR(50),
    PRIMARY KEY (item_type_id)
);

CREATE TABLE Acquisition (
    acquisition_id INT(3),
    company_id INT(3),
    custodian_id INT(7),
    acquisition_date DATE,
    PRIMARY KEY (acquisition_id)
);

CREATE TABLE Acquisition_Details (
    property_id INT(3),
    item_type_id INT(3),
    acquisition_id INT(3),
    PRIMARY KEY (property_id, item_type_id)
);

CREATE TABLE ICT_Room (
    room_id INT(3),
    custodian_id INT(7),
    room_name VARCHAR(50),
    PRIMARY KEY (room_id)
);

CREATE TABLE Property_Custodian (
    custodian_id INT(7),
    name VARCHAR(50),
    gender VARCHAR(20),
    contact_information VARCHAR(15),
    start_date DATE,
    PRIMARY KEY (custodian_id)
);

CREATE TABLE Class (
    class_id INT(3),
    teacher_id INT(7),
    class_name VARCHAR(50),
    PRIMARY KEY (class_id)
);

CREATE TABLE Monitoring (
    attendance_id INT(3),
    serial_number VARCHAR(16),
    description_id INT(3)
);

CREATE TABLE Teacher (
    teacher_id INT(7),
    teacher_name VARCHAR(50),
    teacher_gender VARCHAR(20),
    teacher_contact_information VARCHAR(15),
    PRIMARY KEY (teacher_id)
);

CREATE TABLE Description (
    description_id INT(3),
    description_name VARCHAR(50),
    PRIMARY KEY (description_id)
);

CREATE TABLE Student (
    student_id INT(12),
    student_name VARCHAR(50),
    student_gender VARCHAR(20),
    student_contact_information VARCHAR(15),
    student_year_level INT(2),
    PRIMARY KEY (student_id)
);

CREATE TABLE Student_Attendance (
    attendance_id INT(3),
    student_id INT(12),
    PRIMARY KEY (attendance_id)
);

CREATE TABLE Company (
    company_id INT(8),
    company_name VARCHAR(50),
    company_address VARCHAR(50),
    company_contact_number VARCHAR(15),
    PRIMARY KEY (company_id)
);
```

Commands for creating foreign keys: