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
-- Table structure for table `librarian`
--

DROP TABLE IF EXISTS `librarian`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `librarian` (
  `lib_id` int NOT NULL AUTO_INCREMENT,
  `lib_fname` varchar(30) NOT NULL,
  `lib_mname` varchar(30) NOT NULL,
  `lib_lname` varchar(30) NOT NULL,
  `lib_mail` varchar(50) NOT NULL,
  `lib_city` varchar(20) NOT NULL,
  `lib_village` varchar(20) DEFAULT NULL,
  `lib_street` varchar(20) DEFAULT NULL,
  `lib_phone` int NOT NULL,
  `lib_password` varchar(30) NOT NULL,
  `sup_id` int DEFAULT NULL,
  PRIMARY KEY (`lib_id`),
  UNIQUE KEY `lib_id` (`lib_id`),
  KEY `sup_fk` (`sup_id`),
  CONSTRAINT `sup_fk` FOREIGN KEY (`sup_id`) REFERENCES `librarian` (`lib_id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=9990010 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `librarian`
--

LOCK TABLES `librarian` WRITE;
/*!40000 ALTER TABLE `librarian` DISABLE KEYS */;
INSERT INTO `librarian` VALUES (9990003,'Abdullah','Sami','Naser','1201952@student.birzeit.edu','Ramallah','DeirQaddis','str2',598813310,'admin123123',NULL),(9990004,'majd','riyad','abdeddein','1202923@birzeit.edu','hebron','beit kahel','str2',593873434,'majd123123',9990003),(9990007,'ahmad','ismail','yacoub','ayacoub@birzeit.edu','ramallah','einyabroud','str3',222222,'ahmad11',9990003),(9990008,'yousef','ali','injas','yali@birzeit.edu','ramallah','kharbata','str1',59473632,'yousef123123',9990003),(9990009,'ahmad','wasel','ghannem','aghanem@gmail.com','ramallah','st','st',322332,'123123',9990003);
/*!40000 ALTER TABLE `librarian` ENABLE KEYS */;
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
