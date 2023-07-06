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
-- Table structure for table `members`
--

DROP TABLE IF EXISTS `members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `members` (
  `mem_id` int NOT NULL AUTO_INCREMENT,
  `mem_fname` varchar(30) NOT NULL,
  `mem_mname` varchar(30) NOT NULL,
  `mem_lname` varchar(30) NOT NULL,
  `mem_addr` varchar(30) NOT NULL,
  `mem_phone_one` varchar(35) NOT NULL,
  `mem_phone_two` varchar(35) DEFAULT NULL,
  `mem_mail` varchar(50) NOT NULL,
  PRIMARY KEY (`mem_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1200008 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members`
--

LOCK TABLES `members` WRITE;
/*!40000 ALTER TABLE `members` DISABLE KEYS */;
INSERT INTO `members` VALUES (1200000,'Omar','Ahmed','Khalid','Ramallah','971 234567890','971 876543210','omar.ahmed@example.com'),(1200001,'ali','mahmoud','ibrahim','jenin','971 456789012','971 654321098','alimm@example.com'),(1200002,'Sarah','Khalid','Ibrahim','Ramallah','971 567890123','971 543210987','sarah.khalid@example.com'),(1200003,'Emily','R.','Roberts','USA','1 555-123-4567','1 555-987-6543','emily.roberts@example.com'),(1200004,'Benjamin','A.','Rodriguez','USA','1 777-999-1111','1 222-333-4444','benjamin.rodriguez@example.com'),(1200005,'Noah','A.','Robinson','UK','1 444-333-2222','1 444-323-2222','noah.robinson@example.com'),(1200006,'Mohammad','Sami','Naser','Ramallah','0598888221','0585738822','moha@gmail.com'),(1200007,'Julian','Armando','Alvarez','Espain','9547473','3883838','jAlvarez@yahoo.com');
/*!40000 ALTER TABLE `members` ENABLE KEYS */;
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
