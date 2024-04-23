-- MySQL dump 10.13  Distrib 8.0.36, for macos14.2 (x86_64)
--
-- Host: localhost    Database: RideShare
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Driver`
--

DROP TABLE IF EXISTS `Driver`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Driver` (
  `driverID` int NOT NULL,
  `name` varchar(40) DEFAULT NULL,
  `driverMode` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`driverID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Driver`
--

LOCK TABLES `Driver` WRITE;
/*!40000 ALTER TABLE `Driver` DISABLE KEYS */;
INSERT INTO `Driver` VALUES (1,'Vivian','true'),(80,'Lindsey','false'),(91,'Penelope','true'),(302,'Ian','true');
/*!40000 ALTER TABLE `Driver` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Ride`
--

DROP TABLE IF EXISTS `Ride`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Ride` (
  `rideID` int NOT NULL,
  `riderID` int NOT NULL,
  `driverID` int NOT NULL,
  `date` datetime DEFAULT NULL,
  `pickupLocation` varchar(50) DEFAULT NULL,
  `dropoffLocation` varchar(50) DEFAULT NULL,
  `rating` int DEFAULT NULL,
  PRIMARY KEY (`rideID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ride`
--

LOCK TABLES `Ride` WRITE;
/*!40000 ALTER TABLE `Ride` DISABLE KEYS */;
INSERT INTO `Ride` VALUES (1,1,1,'2024-01-12 00:00:00','418 Almond St','491 Cypress Ave',3),(2,5,1,'2024-02-08 00:00:00','222 Elm Ave','587 Tustin Ln',4),(3,4,2,'2024-04-09 00:00:00','921','Starry Way',1),(4,3,4,'2024-03-21 00:00:00','342 Yummy Rd','900 Lake St',4),(5,2,4,'2024-02-15 00:00:00','758 Tulip Ln','878 Widow Rd',2),(6,2,1,'2024-02-25 00:00:00','2659 Cedar Ave','8945 Oakley',0),(7,2,2,'2024-02-14 00:00:00','9347 Jonston','3484 Lion Ln',4),(8,2,1,'2024-02-01 00:00:00','7643 Mellow Ln','773 Jam Way',3),(9,1,91,'2024-04-08 15:25:57','904 Grand Avenue','105 Olive Street',4),(10,700,91,'2024-04-08 15:58:33','666 Falcon Lane','707 Chapman Avenue',0);
/*!40000 ALTER TABLE `Ride` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Rider`
--

DROP TABLE IF EXISTS `Rider`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Rider` (
  `riderID` int NOT NULL,
  `name` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`riderID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Rider`
--

LOCK TABLES `Rider` WRITE;
/*!40000 ALTER TABLE `Rider` DISABLE KEYS */;
INSERT INTO `Rider` VALUES (1,'Ally'),(2,'Betty'),(3,'Carina'),(4,'Derek'),(5,'Ethan'),(6,'Nila'),(700,'Liam');
/*!40000 ALTER TABLE `Rider` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-08 16:46:09
