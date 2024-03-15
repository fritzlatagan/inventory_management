-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 15, 2024 at 08:50 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `inventory_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `acquisition`
--

CREATE TABLE `acquisition` (
  `acquisition_id` int(11) NOT NULL,
  `company_id` int(11) DEFAULT NULL,
  `custodian_id` int(11) DEFAULT NULL,
  `acquisition_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `acquisition_details`
--

CREATE TABLE `acquisition_details` (
  `property_id` int(11) NOT NULL,
  `item_type_id` int(11) NOT NULL,
  `acquisition_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `class`
--

CREATE TABLE `class` (
  `class_id` int(11) NOT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  `class_name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `company`
--

CREATE TABLE `company` (
  `company_id` int(11) NOT NULL,
  `company_name` varchar(50) DEFAULT NULL,
  `company_address` varchar(50) DEFAULT NULL,
  `company_contact_number` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `description`
--

CREATE TABLE `description` (
  `description_id` int(11) NOT NULL,
  `description_name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ict_room`
--

CREATE TABLE `ict_room` (
  `room_id` int(11) NOT NULL,
  `custodian_id` int(11) DEFAULT NULL,
  `room_name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `item_type`
--

CREATE TABLE `item_type` (
  `item_type_id` int(11) NOT NULL,
  `item_type_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `monitoring`
--

CREATE TABLE `monitoring` (
  `attendance_id` int(11) NOT NULL,
  `serial_number` varchar(16) DEFAULT NULL,
  `description_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `property_custodian`
--

CREATE TABLE `property_custodian` (
  `custodian_id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `contact_information` varchar(15) DEFAULT NULL,
  `start_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `serialized_items`
--

CREATE TABLE `serialized_items` (
  `serial_number` varchar(16) NOT NULL,
  `property_id` int(11) NOT NULL,
  `room_id` int(11) DEFAULT NULL,
  `item_specification` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `student_id` int(11) NOT NULL,
  `student_name` varchar(50) NOT NULL,
  `student_gender` varchar(20) DEFAULT NULL,
  `student_contact_information` varchar(15) DEFAULT NULL,
  `student_year_level` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `student_attendance`
--

CREATE TABLE `student_attendance` (
  `attendance_id` int(11) NOT NULL,
  `student_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

CREATE TABLE `teacher` (
  `teacher_id` int(11) NOT NULL,
  `teacher_name` varchar(50) NOT NULL,
  `teacher_gender` varchar(20) DEFAULT NULL,
  `teacher_contact_information` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `acquisition`
--
ALTER TABLE `acquisition`
  ADD PRIMARY KEY (`acquisition_id`),
  ADD KEY `company_id` (`company_id`),
  ADD KEY `custodian_id` (`custodian_id`);

--
-- Indexes for table `acquisition_details`
--
ALTER TABLE `acquisition_details`
  ADD PRIMARY KEY (`property_id`,`item_type_id`),
  ADD KEY `acquisition_id` (`acquisition_id`);

--
-- Indexes for table `class`
--
ALTER TABLE `class`
  ADD PRIMARY KEY (`class_id`),
  ADD KEY `teacher_id` (`teacher_id`);

--
-- Indexes for table `company`
--
ALTER TABLE `company`
  ADD PRIMARY KEY (`company_id`);

--
-- Indexes for table `description`
--
ALTER TABLE `description`
  ADD PRIMARY KEY (`description_id`);

--
-- Indexes for table `ict_room`
--
ALTER TABLE `ict_room`
  ADD PRIMARY KEY (`room_id`),
  ADD KEY `custodian_id` (`custodian_id`);

--
-- Indexes for table `item_type`
--
ALTER TABLE `item_type`
  ADD PRIMARY KEY (`item_type_id`,`item_type_name`);

--
-- Indexes for table `monitoring`
--
ALTER TABLE `monitoring`
  ADD PRIMARY KEY (`attendance_id`),
  ADD KEY `serial_number` (`serial_number`),
  ADD KEY `description_id` (`description_id`);

--
-- Indexes for table `property_custodian`
--
ALTER TABLE `property_custodian`
  ADD PRIMARY KEY (`custodian_id`);

--
-- Indexes for table `serialized_items`
--
ALTER TABLE `serialized_items`
  ADD PRIMARY KEY (`serial_number`,`property_id`),
  ADD KEY `room_id` (`room_id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`student_id`,`student_name`);

--
-- Indexes for table `student_attendance`
--
ALTER TABLE `student_attendance`
  ADD PRIMARY KEY (`attendance_id`),
  ADD KEY `student_id` (`student_id`);

--
-- Indexes for table `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`teacher_id`,`teacher_name`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `acquisition`
--
ALTER TABLE `acquisition`
  ADD CONSTRAINT `acquisition_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `company` (`company_id`),
  ADD CONSTRAINT `acquisition_ibfk_2` FOREIGN KEY (`custodian_id`) REFERENCES `property_custodian` (`custodian_id`);

--
-- Constraints for table `acquisition_details`
--
ALTER TABLE `acquisition_details`
  ADD CONSTRAINT `acquisition_details_ibfk_1` FOREIGN KEY (`acquisition_id`) REFERENCES `acquisition` (`acquisition_id`);

--
-- Constraints for table `class`
--
ALTER TABLE `class`
  ADD CONSTRAINT `class_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`teacher_id`);

--
-- Constraints for table `ict_room`
--
ALTER TABLE `ict_room`
  ADD CONSTRAINT `ict_room_ibfk_1` FOREIGN KEY (`custodian_id`) REFERENCES `property_custodian` (`custodian_id`);

--
-- Constraints for table `monitoring`
--
ALTER TABLE `monitoring`
  ADD CONSTRAINT `monitoring_ibfk_1` FOREIGN KEY (`serial_number`) REFERENCES `serialized_items` (`serial_number`),
  ADD CONSTRAINT `monitoring_ibfk_2` FOREIGN KEY (`description_id`) REFERENCES `description` (`description_id`),
  ADD CONSTRAINT `monitoring_ibfk_3` FOREIGN KEY (`serial_number`) REFERENCES `serialized_items` (`serial_number`),
  ADD CONSTRAINT `monitoring_ibfk_4` FOREIGN KEY (`description_id`) REFERENCES `description` (`description_id`);

--
-- Constraints for table `serialized_items`
--
ALTER TABLE `serialized_items`
  ADD CONSTRAINT `serialized_items_ibfk_1` FOREIGN KEY (`room_id`) REFERENCES `ict_room` (`room_id`);

--
-- Constraints for table `student_attendance`
--
ALTER TABLE `student_attendance`
  ADD CONSTRAINT `student_attendance_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
