-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 01, 2020 at 09:31 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `my_tarang`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `name` varchar(64) NOT NULL,
  `email` varchar(80) NOT NULL,
  `password` varchar(128) NOT NULL,
  `phone` int(11) NOT NULL,
  `remember_token` varchar(128) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `name`, `email`, `password`, `phone`, `remember_token`, `updated_at`, `created_at`) VALUES
(1, 'admin', 'admin@gmail.com', 'swapnil', 1234567890, NULL, '2020-05-20 09:43:30', '2020-05-20 09:43:30');

-- --------------------------------------------------------

--
-- Table structure for table `assignments`
--

CREATE TABLE `assignments` (
  `id` int(11) NOT NULL,
  `lecturer_id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL,
  `topic_name` varchar(255) NOT NULL,
  `path` varchar(128) NOT NULL,
  `topic_type` varchar(128) DEFAULT NULL,
  `topic_abstract` varchar(1024) DEFAULT NULL,
  `topic_subject` varchar(128) DEFAULT NULL,
  `topic_chapter` varchar(128) DEFAULT NULL,
  `updated_at` datetime DEFAULT current_timestamp(),
  `created_at` datetime DEFAULT current_timestamp(),
  `upvotes` longtext NOT NULL,
  `result` varchar(1024) DEFAULT NULL,
  `resource_center` varchar(128) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `assignments`
--

INSERT INTO `assignments` (`id`, `lecturer_id`, `author_id`, `topic_name`, `path`, `topic_type`, `topic_abstract`, `topic_subject`, `topic_chapter`, `updated_at`, `created_at`, `upvotes`, `result`, `resource_center`) VALUES
(12, 12, 12, 'Dipole Antenna Design and Simulation', 'uploads/6880991625', 'TaraNG 3D', 'This content block will provide a simulation of the dipole antenna using TaraNG simulation tool. Various 2D and 3D plots which includes port-parameters the farfield and the near field of dipole antennas. ', 'Antenna Design & Appliactions', 'Chapter 1', '2020-07-15 08:23:33', '2020-07-15 08:23:33', 'L13,L14,S18,L15,L12', '18,Not satisfactory,27,Satisfactory', 'False'),
(14, 12, 12, 'Tomorrow\'s lecture is cancelled', '', 'annoncement', 'Due to the condiotion of this this this ', '', '', '2020-07-15 08:35:55', '2020-07-15 08:35:55', 'L13,S18,L12', NULL, 'False'),
(17, 12, 12, 'Webinar Three', '', 'embbed_webinar', 'https://www.youtube.com/embed/81MMrkkdD2c', '', '', '2020-07-15 08:57:06', '2020-07-15 08:57:06', 'S18,L14', NULL, 'False'),
(19, 12, 12, 'Chapter-2', '', 'annoncement', 'hi how are you?', '', '', '2020-07-15 12:33:22', '2020-07-15 12:33:22', 'L13,S18,L15', NULL, 'False'),
(20, 13, 12, 'Chapter-2', '', 'annoncement', 'hi how are you?', '', '', '2020-07-15 12:39:05', '2020-07-15 12:39:05', 'S27,L13,S19', NULL, 'False'),
(22, 14, 12, 'Dipole Antenna Edited', 'uploads/6880991625', 'TaraNG 3D', 'This content block will provide a simulation of the dipole antenna using TaraNG simulation tool. Various 2D and 3D plots which includes port-parameters the farfield and the near field of dipole antennas. ', 'Antenna Design & Appliactions', 'Chapter 1', '2020-07-17 12:42:55', '2020-07-17 12:42:55', 'L13,L15', NULL, 'False'),
(23, 12, 12, 'Dipole Antenna Simulation', 'uploads/1041813949', 'TaraNG 3D', 'This content block will provide a simulation of the dipole antenna using TaraNG simulation tool. Various 2D and 3D plots which includes port-parameters the farfield and the near field of dipole antennas. ', 'Antenna Design & Appliactions', 'Chapter 1', '2020-07-17 18:55:40', '2020-07-17 18:55:40', 'L13,S27,S18', '27,Not satisfactory', 'False'),
(25, 18, 18, 'Dipole Antenna Simulation', 'uploads/2203687749', 'TaraNG 3D', 'This content block will provide a simulation of the dipole antenna using TaraNG simulation tool. Various 2D and 3D plots which includes port-parameters the farfield and the near field of dipole antennas. ', 'Antenna Design & Appliactions', 'Chapter 1', '2020-07-18 17:59:26', '2020-07-18 17:59:26', 'L15', NULL, 'False'),
(26, 15, 15, 'Dipole Antenna Simulation', 'uploads/4830368380', 'TaraNG 3D', 'This content block will provide a simulation of the dipole antenna using TaraNG simulation tool. Various 2D and 3D plots which includes port-parameters the farfield and the near field of dipole antennas. ', 'Antenna Design & Appliactions', 'Chapter 1', '2020-07-18 18:19:28', '2020-07-18 18:19:28', 'S27,S19,L15', NULL, 'False'),
(27, 15, 15, 'Dipole Antenna Simulation', 'uploads/4524080907', 'TaraNG 3D', 'This content block will provide a simulation of the dipole antenna using TaraNG simulation tool. Various 2D and 3D plots which includes port-parameters the farfield and the near field of dipole antennas. ', 'Antenna Design & Appliactions', 'Chapter 1', '2020-07-18 18:30:28', '2020-07-18 18:30:28', 'S27,S19,L15', NULL, 'False'),
(28, 13, 12, 'Dipole Antenna Simulation', 'uploads/1041813949', 'TaraNG 3D', 'This content block will provide a simulation of the dipole antenna using TaraNG simulation tool. Various 2D and 3D plots which includes port-parameters the farfield and the near field of dipole antennas. ', 'Antenna Design & Appliactions', 'Chapter 1', '2020-07-20 15:26:00', '2020-07-20 15:26:00', 'L13,S27', '37,Satisfactory', 'False'),
(30, 13, 12, 'Chapter-2', '', 'annoncement', 'hi how are you?', '', '', '2020-07-21 17:25:29', '2020-07-21 17:25:29', '', NULL, 'False'),
(31, 18, 18, 'Dipole Antenna Simulation', 'uploads/6693254564', 'TaraNG 3D', 'This content block will provide a simulation of the dipole antenna using TaraNG simulation tool. Various 2D and 3D plots which includes port-parameters the farfield and the near field of dipole antennas. ', 'Antenna Design & Appliactions', 'Chapter 1', '2020-07-21 17:35:52', '2020-07-21 17:35:52', '', NULL, 'False'),
(32, 21, 21, 'Dipole Antenna Simulation', 'uploads/7903458525', 'TaraNG 3D', 'This content block will provide a simulation of the dipole antenna using TaraNG simulation tool. Various 2D and 3D plots which includes port-parameters the farfield and the near field of dipole antennas. ', 'Antenna Design & Appliactions', 'Chapter 1', '2020-07-21 17:37:14', '2020-07-21 17:37:14', '', '27,Satisfactory', 'False'),
(33, 13, 12, 'Dipole Antenna Simulation', 'uploads/1041813949', 'TaraNG 3D', 'This content block will provide a simulation of the dipole antenna using TaraNG simulation tool. Various 2D and 3D plots which includes port-parameters the farfield and the near field of dipole antennas. ', 'Antenna Design & Appliactions', 'Chapter 1', '2020-08-01 09:29:12', '2020-08-01 09:29:12', '0', NULL, 'False');

-- --------------------------------------------------------

--
-- Table structure for table `lecturers`
--

CREATE TABLE `lecturers` (
  `id` int(11) NOT NULL,
  `name` varchar(64) NOT NULL,
  `email` varchar(80) NOT NULL,
  `password` varchar(128) CHARACTER SET utf8mb4 NOT NULL,
  `institute` varchar(128) DEFAULT NULL,
  `department` varchar(128) DEFAULT NULL,
  `membership` varchar(128) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `photo` varchar(128) DEFAULT NULL,
  `designation` varchar(128) DEFAULT NULL,
  `education` varchar(128) DEFAULT NULL,
  `skills` varchar(255) DEFAULT NULL,
  `about` varchar(1024) DEFAULT NULL,
  `experience` varchar(1024) DEFAULT NULL,
  `publications` varchar(1024) DEFAULT NULL,
  `projects` varchar(1024) DEFAULT NULL,
  `achievements` varchar(1024) DEFAULT NULL,
  `students_request` varchar(1024) DEFAULT NULL,
  `lecturers_request` varchar(1024) DEFAULT NULL,
  `teachers` varchar(1024) DEFAULT NULL,
  `linkedin` varchar(255) DEFAULT NULL,
  `github` varchar(255) DEFAULT NULL,
  `youtube` varchar(255) DEFAULT NULL,
  `email_verified` smallint(6) DEFAULT NULL,
  `google_provider_id` varchar(128) DEFAULT NULL,
  `facebook_provider_id` varchar(128) DEFAULT NULL,
  `batch_ids` varchar(128) DEFAULT NULL,
  `remember_token` varchar(128) DEFAULT NULL,
  `updated_at` datetime DEFAULT current_timestamp(),
  `created_at` datetime DEFAULT current_timestamp(),
  `lecturers_accepted` varchar(1024) DEFAULT NULL,
  `students_accepted` varchar(1024) DEFAULT NULL,
  `created_assignments` varchar(1024) DEFAULT NULL,
  `followed_assignments` varchar(1024) DEFAULT NULL,
  `subjects` varchar(128) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `lecturers`
--

INSERT INTO `lecturers` (`id`, `name`, `email`, `password`, `institute`, `department`, `membership`, `phone`, `photo`, `designation`, `education`, `skills`, `about`, `experience`, `publications`, `projects`, `achievements`, `students_request`, `lecturers_request`, `teachers`, `linkedin`, `github`, `youtube`, `email_verified`, `google_provider_id`, `facebook_provider_id`, `batch_ids`, `remember_token`, `updated_at`, `created_at`, `lecturers_accepted`, `students_accepted`, `created_assignments`, `followed_assignments`, `subjects`) VALUES
(12, 'Teacher One', 'teacher1@edu.in', '$5$rounds=535000$1qSTNp431j8TtVsf$C.9J2H6R0E24Ua5n3bKNGa2rypeUvHlLEReJhiGRs/5', 'Institute of Technology', 'Electrical Engineering', 'IEEE MTTS Fellow', '8390240904', 'img/12.jpeg', 'Assistant Professor', '', '', '', '', '', '', '', '34,19,37', NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, '2020-07-15 08:13:58', '2020-07-15 08:13:58', '13,14', '25,18,27,30', '12,13,14,15,16,17,19,21,23', NULL, 'Basic Electronics'),
(13, 'Teacher Two', 'teacher2@edu.in', '$5$rounds=535000$CH33H95kc067kgtB$.6vIjx0ASKuDBSRXmCEiGe09rp47.C.bs3RMPvodEV1', 'IIT Kharagpur', 'Electrical Engineering', 'None', '8390240903', 'img/13.jpg', 'Professor', 'None', 'None', 'None', 'None', 'None', 'None', 'None', NULL, NULL, '12,14', NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, '2020-07-15 12:24:48', '2020-07-15 12:24:48', NULL, '19,27,37', '18,20,28,29,30,33', '19,21,23', 'None'),
(14, 'Teacher Three', 'teacher3@edu.in', '$5$rounds=535000$mGVsP3WlqbugZelp$XYopWYMixRQYKwDfnSlc/O62QGnm0VmGjDdEHQgJ.Q2', 'ACEG', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '12', NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, '2020-07-17 12:40:21', '2020-07-17 12:40:21', '13', NULL, '22', '23', NULL),
(15, 'nagaraju', 'naga@gmail.com', '$5$rounds=535000$iDVuxUsr.GAEhfV0$ztQ1ctgdCb3YFp9erV/pXyHqrTsoXESV8D8A3xGBB4.', 'Microwave Devices ', 'Scientist', '8374407644', 'None', 'img/lecturers/15.jpg', 'IEEE Lifetime Member', 'None', 'Electromagnetics,TWT', 'None', 'Working as a Scientist at CSIR-CEERI, Pilani', 'None', 'None', 'None', NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, '2020-07-18 15:06:39', '2020-07-18 15:06:39', NULL, '25,34,27,30,19', '24,26,27', NULL, 'None'),
(17, 'ASHOK', 'ashok@gmail.com', '$5$rounds=535000$0zgVa6BVT1yX5wBf$JbvcEqlOpZdPihCmN2nEG7f3qECsH2Hiep/eLzx8Hx1', 'CEERI', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, '2020-07-18 17:52:20', '2020-07-18 17:52:20', NULL, NULL, NULL, NULL, NULL),
(18, 'Swati', 'sn@gmail.com', '$5$rounds=535000$6MEbGT9olKooq8yD$t/2pmKSfnJ/xmCPKIIiVX7/rxZb52YWrCDJQgZ9N159', 'SGI, Kolhapur', 'None', 'None', 'None', 'img/lecturers/18.jpg', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, '2020-07-18 17:52:21', '2020-07-18 17:52:21', NULL, NULL, '25,31', NULL, 'None'),
(19, 'teacher4', 'teacher4@edu.in', '$5$rounds=535000$OXErgzQPgzCMjKeZ$xFdILisUyBASWGVMfWvzBm/zf6MyqDVBN4.7PFzllA0', 'CEERI', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, '2020-07-21 02:52:49', '2020-07-21 02:52:49', NULL, '27', NULL, NULL, NULL),
(20, 'teacher5', 'teacher5@edu.in', '$5$rounds=535000$.2jRjEMZi1rYPyq7$YAdjtlGGso/q7ig5/hxe6hbmBqWmL0ex2hqlkB/ZeA2', 'CEERI', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, '2020-07-21 02:53:18', '2020-07-21 02:53:18', NULL, NULL, NULL, NULL, NULL),
(21, 'Eshwar', 'eshwar@gmail.com', '$5$rounds=535000$7oqTvB2m4AWcClGe$HORyHwD6hswOK44W5ZDJwI08yNgTylNo.ARpk9DJQe8', 'CEERI', 'None', 'None', 'None', NULL, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, '2020-07-21 13:33:12', '2020-07-21 13:33:12', NULL, NULL, '32', NULL, 'None'),
(22, 'ANUSHA', 'anu@gmail.com', '$5$rounds=535000$LX3ZNccQlajSX9ES$CzEkLOavr8XaE8Z6QMyAsMc6qZ/3tnPkW5tIl2ihrQ1', '<a href=\'https://www.gctcportal.in/p/new.html\'> Geethanjali Engineerring College </a>', 'ECE', 'IEEE', '1234567890', NULL, 'Assistant professor', 'M.tech', 'ESD, DBMS, WEB DEVELOPMENT', 'None', 'None', 'None', 'None', 'None', NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, '2020-07-30 23:19:48', '2020-07-30 23:19:48', NULL, NULL, NULL, NULL, 'Embedded Systems');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `name` varchar(64) NOT NULL,
  `email` varchar(80) NOT NULL,
  `password` varchar(128) CHARACTER SET utf8mb4 NOT NULL,
  `institute` varchar(128) DEFAULT NULL,
  `department` varchar(128) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `photo` varchar(128) DEFAULT NULL,
  `year` varchar(40) DEFAULT NULL,
  `skills` varchar(128) DEFAULT NULL,
  `publications` varchar(1024) DEFAULT NULL,
  `internship` varchar(1024) DEFAULT NULL,
  `projects` varchar(1024) DEFAULT NULL,
  `achievements` varchar(1024) DEFAULT NULL,
  `teachers` varchar(128) DEFAULT NULL,
  `email_verified` smallint(6) DEFAULT NULL,
  `admin_verified` smallint(6) DEFAULT NULL,
  `google_provider_id` varchar(128) DEFAULT NULL,
  `facebook_provider_id` varchar(128) DEFAULT NULL,
  `batch_ids` varchar(128) DEFAULT NULL,
  `remember_token` varchar(128) DEFAULT NULL,
  `updated_at` datetime DEFAULT current_timestamp(),
  `created_at` datetime DEFAULT current_timestamp(),
  `created_assignments` varchar(1024) DEFAULT NULL,
  `followed_assignments` varchar(1024) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `name`, `email`, `password`, `institute`, `department`, `phone`, `photo`, `year`, `skills`, `publications`, `internship`, `projects`, `achievements`, `teachers`, `email_verified`, `admin_verified`, `google_provider_id`, `facebook_provider_id`, `batch_ids`, `remember_token`, `updated_at`, `created_at`, `created_assignments`, `followed_assignments`) VALUES
(18, 'swati', 'swati@nagargoje.com', '$5$rounds=535000$LDHW5OYAjte12lch$6FjO1dMEN07fy3f0Cwa0BGiGXeQvCduimvv67O4ZUS7', 'Institute at Kolhapur', 'Elecronics Engineering', '8390240903', 'img/18.png', 'Third Year', 'Robotics, AI, ANN', '', 'Planted trees in nearby villages', 'Obstacle detector using IR Diode', 'Won first price in poetrty writing', '12', 0, 0, NULL, NULL, NULL, NULL, '2020-07-15 07:46:32', '2020-07-15 07:46:32', NULL, '19,23'),
(19, 'shiva', 'shivanarayanamurthy@gmail.com', '$5$rounds=535000$jSsMFtbBZBpWqxR4$h1EpBQeCNYWbBgUL0xqTig6tQxk0cV2c9qNs4/1KNL.', 'CEERI', 'None', 'None', 'img/students/19.jpg', 'None', 'None', 'None', 'None', 'None', 'None', '13,15', 0, 0, NULL, NULL, NULL, NULL, '2020-07-17 12:05:09', '2020-07-17 12:05:09', NULL, '28,29,30,33'),
(22, 'gtake', 'gttttake@gmail.com', '$5$rounds=535000$Ysryj1rHHTFCPdG9$.345QoGk/6jPAn1WYLHPwPVgf0YBVE6fz6r3pJxkpfA', 'IIT Kharagpur ', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, '2020-07-17 12:07:57', '2020-07-17 12:07:57', NULL, NULL),
(25, 'snm2', 'snm2@gou.com', '$5$rounds=535000$PwuyNKhKZgPa.mgo$OKldYRC3UA5cGhoRSiABJGXm6ZLsATtJY4JfmWVg/t/', 'CEERI', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '12,15', 0, 0, NULL, NULL, NULL, NULL, '2020-07-17 12:17:46', '2020-07-17 12:17:46', NULL, '23,26,27'),
(27, 'snm31', 'snm31@hi.com', '$5$rounds=535000$ot.8IThVEjHwWNch$Ah3QDVtQFs/0I9UWDMf/1skope1L7SHp2tx8nWwul06', '<a href=\'https://www.aceec.ac.in/\'> ACE Engineerring College </a>', 'Embedded Systems', '9949564680', 'img/27.jpg', '4th year', 'ESD, DBMS, WEB DEVELOPMENT', 'None', '<a href=\'https://www.aceec.ac.in/\'> ACE Engineerring College </a>', 'None', 'None', '12,13,15,19', 0, 0, NULL, NULL, NULL, NULL, '2020-07-17 12:24:16', '2020-07-17 12:24:16', NULL, '23,24,26,27,28,29,30,33'),
(28, 'shiva', 'shivanrayanamurthy@gmail.com', '$5$rounds=535000$x2ZMyCEols46VVXl$0bmTyUXUnD2ZZT.i0o3imJw8EcL9HHsJB3SyDYGcS60', 'ACEG', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, '2020-07-17 17:15:31', '2020-07-17 17:15:31', NULL, NULL),
(30, 'swati', 'swatinagargoje@gmail.com', '$5$rounds=535000$nllC0Np1NWoO2GGH$Pg3CC2WPJHyZBU3BKK72eml0eJNSFuIWReU92UCeSo5', 'SGI, Kolhapur', 'E&TC', 'None', 'img/students/30.jpg', '2017', 'None', 'None', 'None', 'None', 'None', '12,15', 0, 0, NULL, NULL, NULL, NULL, '2020-07-17 17:45:02', '2020-07-17 17:45:02', NULL, '23,26,27'),
(31, 'swatinagar', 'swati@gmail.com', '$5$rounds=535000$8rWphAgpc8opocpW$7Dj9.NOdx0BfTCOvRTaSU4BmqsAzKf8vuUZicY.E2ZA', 'SGI, Kolhapur', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, '2020-07-17 17:48:06', '2020-07-17 17:48:06', NULL, NULL),
(32, 'z', 'z@g.com', '$5$rounds=535000$GAsm8d07X3oFQFOD$/g7nZn9WletYABeUuDGN2ce/LPOWF9KLJIf7PGZSf91', 'z', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, '2020-07-18 12:48:04', '2020-07-18 12:48:04', NULL, NULL),
(33, 'nagaraju', 'naga@gmail.com', '$5$rounds=535000$u1P18fpYYQJEthnl$eSKiiHZXPzY27j5nWyVpoMJAmPFA7Sa.KEejrofInCA', 'CEERI', 'Microwave Devices', '8374407644', 'img/students/33.21', '4th year', 'None', 'None', 'None', 'None', 'None', NULL, 0, 0, NULL, NULL, NULL, NULL, '2020-07-18 15:30:54', '2020-07-18 15:30:54', NULL, NULL),
(34, 'veena', 'veena@gmail.com', '$5$rounds=535000$u5wIHqFuk3Ikhnkx$Na1dgDzJ7XcXu0XrCAvNYsd8Aq2ppQcgx4tlAu.C0o7', 'CEERI', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '15', 0, 0, NULL, NULL, NULL, NULL, '2020-07-18 18:28:08', '2020-07-18 18:28:08', NULL, '27'),
(35, 'veenatdz', 'veena1@gmail.com', '$5$rounds=535000$tz.RzkZ2BGHX.qb.$KnExFtn8giLMKplZt2KoS0TWz8wmBa6TrqA88JxPzp7', 'CEERI', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, '2020-07-20 02:04:10', '2020-07-20 02:04:10', NULL, NULL),
(36, 'rakesh', 'rakesh@gmail.com', '$5$rounds=535000$dGcWzqDO8K0cmTUC$sBa9gdWNw1fla.c4PazxGR0kJx5pSmN8KIlAhYSOl58', 'CEERI', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, '2020-07-21 13:22:01', '2020-07-21 13:22:01', NULL, NULL),
(37, 'studentone', 's1@gmail.com', '$5$rounds=535000$fwhwhu4REqw8Gwoh$vyw2c8br1s1csUidSEpCE9SR/4ehvhBk321fUcrR8I5', 'GCET', 'None', 'None', NULL, 'None', 'None', 'None', 'None', 'None', 'None', '13', 0, 0, NULL, NULL, NULL, NULL, '2020-07-21 17:46:42', '2020-07-21 17:46:42', NULL, '33'),
(38, 'Ashu', 'ashu@gmail.com', '$5$rounds=535000$qtTB29yHRarujp5i$l1QnU3cZEMbx0nWczge8U1UA74QEGl2x2LeGTeUNUdC', 'GCET', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, '2020-07-29 18:54:39', '2020-07-29 18:54:39', NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ix_admin_email` (`email`);

--
-- Indexes for table `assignments`
--
ALTER TABLE `assignments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `lecturers`
--
ALTER TABLE `lecturers`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ix_lecturers_email` (`email`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ix_users_email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `assignments`
--
ALTER TABLE `assignments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `lecturers`
--
ALTER TABLE `lecturers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
