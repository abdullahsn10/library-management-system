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
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `book_code` int NOT NULL AUTO_INCREMENT,
  `book_title` varchar(90) NOT NULL,
  `book_price` int DEFAULT NULL,
  `book_pages` int DEFAULT NULL,
  `book_cat` int NOT NULL,
  `book_pub` int NOT NULL,
  `book_auth` int NOT NULL,
  `book_desc` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`book_code`),
  UNIQUE KEY `book_code` (`book_code`),
  KEY `book_cat` (`book_cat`),
  KEY `book_pub` (`book_pub`),
  KEY `book_auth` (`book_auth`),
  CONSTRAINT `book_ibfk_1` FOREIGN KEY (`book_cat`) REFERENCES `category` (`cat_no`),
  CONSTRAINT `book_ibfk_2` FOREIGN KEY (`book_pub`) REFERENCES `publisher` (`pub_id`),
  CONSTRAINT `book_ibfk_3` FOREIGN KEY (`book_auth`) REFERENCES `author` (`auth_id`)
) ENGINE=InnoDB AUTO_INCREMENT=56560012 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (56560000,'the phoenix project: a novel about it, devops, and helping your business win',24,376,8800,2200,1100,'it book'),(56560001,'a brief history of time',20,256,8801,2201,1101,'science book'),(56560002,'hamlet',10,320,8802,2202,1102,'drama book'),(56560004,'arabian nights: the complete and unexpurgated edition',22,992,8804,2203,1104,'arabic book'),(56560005,'the body keeps the score: brain, mind, and body in the healing of trauma',18,464,8801,2202,1105,'scientific book'),(56560006,'the crucible',11,144,8802,2202,1106,'drama book classic'),(56560007,'1984',10,328,8803,2206,1107,'english book , overrated'),(56560008,'the yacoubian building',17,272,8804,2204,1107,'arabic event'),(56560009,'homicide: a year on the killing streets',17,672,8805,2205,1110,'poilice book , overrated'),(56560010,'learning python',80,1643,8800,2207,1111,'one of the best books for learning python'),(56560011,'effective java',30,412,8800,2208,1112,'introduction to java');
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
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
