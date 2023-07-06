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
-- Table structure for table `librarian_permissions`
--

DROP TABLE IF EXISTS `librarian_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `librarian_permissions` (
  `perm_no` int NOT NULL AUTO_INCREMENT,
  `lib_id` int NOT NULL,
  `book_tab` int DEFAULT NULL,
  `mem_tab` int DEFAULT NULL,
  `lib_tab` int DEFAULT NULL,
  `det_tab` int DEFAULT NULL,
  `serv_tab` int DEFAULT NULL,
  `hist_tab` int DEFAULT NULL,
  `sett_tab` int DEFAULT NULL,
  PRIMARY KEY (`perm_no`),
  KEY `lib_per_fk` (`lib_id`),
  CONSTRAINT `lib_per_fk` FOREIGN KEY (`lib_id`) REFERENCES `librarian` (`lib_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `librarian_permissions`
--

LOCK TABLES `librarian_permissions` WRITE;
/*!40000 ALTER TABLE `librarian_permissions` DISABLE KEYS */;
INSERT INTO `librarian_permissions` VALUES (1,9990007,1,1,1,1,1,1,1),(2,9990003,1,1,1,1,1,1,1),(3,9990004,1,1,1,1,1,1,1),(4,9990008,1,1,0,0,1,0,1),(5,9990009,1,1,0,0,0,0,0);
/*!40000 ALTER TABLE `librarian_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-06  6:39:47
