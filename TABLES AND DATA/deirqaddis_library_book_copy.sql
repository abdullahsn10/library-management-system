-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: deirqaddis_library
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `book_copy`
--

DROP TABLE IF EXISTS `book_copy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_copy` (
  `copy_no` int NOT NULL AUTO_INCREMENT,
  `book_code` int NOT NULL,
  `loan_status` varchar(25) NOT NULL DEFAULT 'not_rented',
  `copy_status` varchar(20) NOT NULL DEFAULT 'new',
  `buy_status` varchar(20) DEFAULT 'yes',
  PRIMARY KEY (`copy_no`),
  KEY `on_del_cas` (`book_code`),
  CONSTRAINT `on_del_cas` FOREIGN KEY (`book_code`) REFERENCES `book` (`book_code`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_copy`
--

LOCK TABLES `book_copy` WRITE;
/*!40000 ALTER TABLE `book_copy` DISABLE KEYS */;
INSERT INTO `book_copy` VALUES (1,56560000,'not_rented','used','yes'),(2,56560000,'not_rented','used','yes'),(3,56560000,'not_rented','used','yes'),(4,56560000,'not_rented','new','yes'),(5,56560001,'not_rented','used','yes'),(6,56560001,'sold','new','yes'),(7,56560001,'sold','new','yes'),(8,56560001,'not_rented','used','yes'),(9,56560001,'not_rented','used','yes'),(10,56560001,'not_rented','used','no'),(11,56560001,'not_rented','new','no'),(12,56560002,'rented','used','no'),(13,56560002,'rented','used','no'),(14,56560002,'rented','used','no'),(20,56560004,'rented','used','yes'),(21,56560004,'rented','used','yes'),(22,56560004,'not_rented','new','yes'),(23,56560004,'not_rented','new','yes'),(24,56560004,'not_rented','new','yes'),(25,56560004,'not_rented','new','yes'),(26,56560005,'rented','used','yes'),(27,56560005,'rented','used','yes'),(28,56560005,'rented','used','yes'),(29,56560005,'rented','used','yes'),(30,56560005,'rented','used','yes'),(31,56560005,'sold','new','yes'),(32,56560005,'sold','new','yes'),(33,56560005,'rented','used','yes'),(34,56560006,'sold','used','yes'),(35,56560006,'sold','used','yes'),(36,56560006,'rented','used','no'),(37,56560007,'rented','used','no'),(38,56560007,'rented','used','no'),(39,56560007,'rented','used','no'),(40,56560007,'rented','used','no'),(41,56560008,'rented','used','yes'),(42,56560008,'rented','used','yes'),(43,56560008,'rented','used','yes'),(44,56560009,'sold','new','yes'),(45,56560009,'sold','new','yes'),(46,56560009,'not_rented','new','yes'),(47,56560009,'not_rented','new','yes'),(48,56560009,'not_rented','new','yes'),(49,56560008,'rented','used','no'),(50,56560004,'not_rented','used','no'),(51,56560010,'rented','used','yes'),(52,56560010,'rented','used','yes'),(53,56560010,'rented','used','yes'),(54,56560010,'rented','used','yes'),(55,56560010,'rented','used','no'),(56,56560010,'rented','used','yes'),(57,56560002,'sold','new','yes'),(58,56560002,'sold','new','yes'),(59,56560002,'sold','new','yes'),(60,56560002,'sold','new','yes'),(61,56560002,'sold','new','yes'),(62,56560010,'rented','used','yes'),(63,56560010,'rented','used','yes'),(64,56560006,'rented','used','yes'),(65,56560006,'rented','used','yes'),(66,56560006,'rented','used','yes'),(67,56560006,'rented','used','yes'),(68,56560011,'rented','used','yes'),(69,56560011,'sold','new','yes'),(70,56560011,'sold','new','yes'),(71,56560011,'not_rented','new','no'),(72,56560007,'rented','used','yes'),(73,56560007,'not_rented','new','yes'),(74,56560007,'not_rented','new','yes'),(75,56560007,'not_rented','new','yes'),(76,56560007,'not_rented','new','yes'),(77,56560007,'not_rented','new','yes'),(78,56560005,'rented','used','yes'),(79,56560005,'rented','used','yes');
/*!40000 ALTER TABLE `book_copy` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-06  6:39:48
