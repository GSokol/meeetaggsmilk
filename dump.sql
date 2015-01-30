-- MySQL dump 10.15  Distrib 10.0.15-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: meateggsmilk
-- ------------------------------------------------------
-- Server version	10.0.15-MariaDB-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add категория рецептов',7,'add_recipecategory'),(20,'Can change категория рецептов',7,'change_recipecategory'),(21,'Can delete категория рецептов',7,'delete_recipecategory'),(22,'Can add рецепт',8,'add_recipe'),(23,'Can change рецепт',8,'change_recipe'),(24,'Can delete рецепт',8,'delete_recipe'),(25,'Can add ингридеенты',9,'add_recipeingridient'),(26,'Can change ингридеенты',9,'change_recipeingridient'),(27,'Can delete ингридеенты',9,'delete_recipeingridient'),(28,'Can add категория товаров',10,'add_goodcategory'),(29,'Can change категория товаров',10,'change_goodcategory'),(30,'Can delete категория товаров',10,'delete_goodcategory'),(31,'Can add товар',11,'add_good'),(32,'Can change товар',11,'change_good'),(33,'Can delete товар',11,'delete_good'),(34,'Can add заказ',12,'add_order'),(35,'Can change заказ',12,'change_order'),(36,'Can delete заказ',12,'delete_order'),(37,'Can add партнер',13,'add_partner'),(38,'Can change партнер',13,'change_partner'),(39,'Can delete партнер',13,'delete_partner'),(40,'Can add товар поставщика',14,'add_partnergood'),(41,'Can change товар поставщика',14,'change_partnergood'),(42,'Can delete товар поставщика',14,'delete_partnergood'),(43,'Can add поставщик/прилавок',15,'add_partnergoodtogood'),(44,'Can change поставщик/прилавок',15,'change_partnergoodtogood'),(45,'Can delete поставщик/прилавок',15,'delete_partnergoodtogood'),(46,'Can add поставка',16,'add_supply'),(47,'Can change поставка',16,'change_supply'),(48,'Can delete поставка',16,'delete_supply'),(49,'Can add пункт поставки',17,'add_supplyitem'),(50,'Can change пункт поставки',17,'change_supplyitem'),(51,'Can delete пункт поставки',17,'delete_supplyitem'),(52,'Can add пункт заказа',18,'add_supplyorderitem'),(53,'Can change пункт заказа',18,'change_supplyorderitem'),(54,'Can delete пункт заказа',18,'delete_supplyorderitem'),(55,'Can add заявка на звонок',19,'add_callorder'),(56,'Can change заявка на звонок',19,'change_callorder'),(57,'Can delete заявка на звонок',19,'delete_callorder'),(58,'Can add текст',20,'add_textmodel'),(59,'Can change текст',20,'change_textmodel'),(60,'Can delete текст',20,'delete_textmodel'),(61,'Can add картинка',21,'add_imagemodel'),(62,'Can change картинка',21,'change_imagemodel'),(63,'Can delete картинка',21,'delete_imagemodel'),(64,'Can add телефон',22,'add_phonemodel'),(65,'Can change телефон',22,'change_phonemodel'),(66,'Can delete телефон',22,'delete_phonemodel'),(67,'Can add переменная',23,'add_intmodel'),(68,'Can change переменная',23,'change_intmodel'),(69,'Can delete переменная',23,'delete_intmodel');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$7SIkuV23AevS$HErAbYko+iDDKfSmVmwTpZpbKkW/vTwZvwQNrhJTEzI=','2015-01-23 20:09:50',1,'sokol','','','g.sokol99@g-sokol.info',1,1,'2015-01-23 07:22:08');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-01-23 07:23:34','1','Иван: +7(982) 920-90-38',1,'',13,1),(2,'2015-01-23 07:24:25','1','Иван: +7(982) 920-90-38',2,'Добавлен товар поставщика \"Иван: Десяток яиц -- 100\".',13,1),(3,'2015-01-23 07:24:59','1','Говядина без кости',1,'',10,1),(4,'2015-01-23 07:26:59','2','Говядина без кости',1,'',10,1),(5,'2015-01-23 07:27:23','3','Баранина на кости',1,'',10,1),(6,'2015-01-23 07:27:46','4','Мелкий скот',1,'',10,1),(7,'2015-01-23 07:27:52','5','Молочные продукты',1,'',10,1),(8,'2015-01-23 07:28:03','6','Мед',1,'',10,1),(9,'2015-01-23 07:28:08','7','Сосиски',1,'',10,1),(10,'2015-01-23 07:28:17','8','Яйца',1,'',10,1),(11,'2015-01-23 07:30:30','1','Вырезка -- 600 (550) кг',1,'',11,1),(12,'2015-01-23 07:34:23','1','Говядина без кости',3,'',10,1),(13,'2015-01-23 07:38:45','3','Вырезка -- 600 (550) кг',1,'',11,1),(14,'2015-01-23 07:39:59','4','Филейный край -- 550 (500) кг',1,'',11,1),(15,'2015-01-23 07:40:59','5','Яйцо куриное -- 120 (110) дес',1,'',11,1),(16,'2015-01-23 07:41:21','3','Вырезка -- 600 (550) кг',2,'Изменен weekly.',11,1),(17,'2015-01-23 07:47:42','2','Иван: Десяток яиц -- 100',2,'Добавлен поставщик/прилавок \"Десяток яиц = Яйцо куриное * 0\".',14,1),(18,'2015-01-23 07:48:14','1','Иван: Полтуши -- 3000',2,'Добавлен поставщик/прилавок \"Полтуши = Вырезка * 4\". Добавлен поставщик/прилавок \"Полтуши = Филейный край * 5\".',14,1),(19,'2015-01-23 07:49:53','2','Иван: Десяток яиц -- 100',2,'Изменены value для поставщик/прилавок \"Десяток яиц = Яйцо куриное * 1\".',14,1),(20,'2015-01-23 07:59:19','1','логотип',1,'',21,1),(21,'2015-01-23 07:59:32','2','черно-белый логотип',1,'',21,1),(22,'2015-01-23 07:59:54','1','+7(985) 123-12-12',1,'',22,1),(23,'2015-01-23 08:00:18','1','текст главной страницы',1,'',20,1),(24,'2015-01-23 08:00:36','2','текст страницы доставки',1,'',20,1),(25,'2015-01-23 08:01:13','1','просто',1,'',7,1),(26,'2015-01-23 08:01:32','2','Сложно',1,'',7,1),(27,'2015-01-23 08:01:43','3','Смерть',1,'',7,1),(28,'2015-01-23 08:02:41','1','Яичница',1,'',8,1),(29,'2015-01-23 08:14:33','1','Иван: +7(982) 920-90-38',2,'Ни одно поле не изменено.',13,1),(30,'2015-01-23 08:20:26','1','Иван: +7(982) 920-90-38',2,'Ни одно поле не изменено.',13,1),(31,'2015-01-23 08:44:36','3','карта',1,'',21,1),(32,'2015-01-23 12:34:07','1','2015-01-27 заказаная',2,'Ни одно поле не изменено.',16,1),(33,'2015-01-23 12:44:18','1','2015-01-27 взвешенная',2,'Ни одно поле не изменено.',16,1),(34,'2015-01-23 13:51:19','1','max_delivery_interval: 4',1,'',23,1),(35,'2015-01-23 13:51:34','2','delivery_price: 300',1,'',23,1),(36,'2015-01-23 13:51:43','3','free_delivery_min_price: 3000',1,'',23,1),(37,'2015-01-23 14:16:21','4','Час закрытия доставки в тот же день: 19',1,'',23,1),(38,'2015-01-23 19:53:08','4','+7(915) 032-59-23 g.sokol99@gmail.com 2015-01-23 17:55:41+00:00 2400 руб. обработанный',2,'Ни одно поле не изменено.',12,1),(39,'2015-01-23 19:56:04','4','+7(915) 032-59-23 g.sokol99@gmail.com 2015-01-23 17:55:41+00:00 2400 руб. обработанный',2,'Ни одно поле не изменено.',12,1),(40,'2015-01-23 19:57:35','1','Андрей: +7(905) 751-95-97',2,'Изменен name и phone.',13,1),(41,'2015-01-23 20:00:00','1','Андрей: +7(905) 751-95-97',2,'Изменены maxOrder для товар поставщика \"Андрей: Десяток яиц -- 100\".',13,1),(42,'2015-01-23 20:08:43','6','Брарнья корейка -- 550 (520) кг',1,'',11,1),(43,'2015-01-23 20:09:08','5','Яйцо куриное -- 160 (160) дес',2,'Изменен priceFut и price.',11,1),(44,'2015-01-23 20:24:51','3','Андрей: Брарнья корейка -- 400',1,'',14,1),(45,'2015-01-23 20:29:17','2','2015-01-30 заказаная',2,'Ни одно поле не изменено.',16,1),(46,'2015-01-23 20:33:23','4','Птица',2,'Изменен name.',10,1),(47,'2015-01-30 06:04:54','2','2015-01-30 взвешенная',2,'Ни одно поле не изменено.',16,1),(48,'2015-01-30 06:06:31','6','+7(915) 032-59-23 g.sokol99@gmail.com 2015-01-23 17:56:53+00:00 1400 руб. обработанный',2,'Ни одно поле не изменено.',12,1),(49,'2015-01-30 06:07:14','5','+7(915) 032-59-23 g.sokol99@gmail.com 2015-01-23 17:56:18+00:00 1400 руб. обработанный',2,'Ни одно поле не изменено.',12,1),(50,'2015-01-30 06:16:07','6','+7(915) 032-59-23 g.sokol99@gmail.com 2015-01-23 17:56:53+00:00 1400 руб. взвешенный',2,'Ни одно поле не изменено.',12,1),(51,'2015-01-30 06:16:11','6','+7(915) 032-59-23 g.sokol99@gmail.com 2015-01-23 17:56:53+00:00 1400 руб. взвешенный',2,'Ни одно поле не изменено.',12,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'категория рецептов','main','recipecategory'),(8,'рецепт','main','recipe'),(9,'ингридеенты','main','recipeingridient'),(10,'категория товаров','main','goodcategory'),(11,'товар','main','good'),(12,'заказ','main','order'),(13,'партнер','main','partner'),(14,'товар поставщика','main','partnergood'),(15,'поставщик/прилавок','main','partnergoodtogood'),(16,'поставка','main','supply'),(17,'пункт поставки','main','supplyitem'),(18,'пункт заказа','main','supplyorderitem'),(19,'заявка на звонок','main','callorder'),(20,'текст','setts','textmodel'),(21,'картинка','setts','imagemodel'),(22,'телефон','setts','phonemodel'),(23,'переменная','setts','intmodel');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-01-23 07:21:33'),(2,'auth','0001_initial','2015-01-23 07:21:33'),(3,'admin','0001_initial','2015-01-23 07:21:34'),(4,'sessions','0001_initial','2015-01-23 07:21:34'),(5,'setts','0001_initial','2015-01-23 07:21:34'),(6,'setts','0002_auto_20141123_1218','2015-01-23 07:21:34'),(7,'setts','0003_auto_20150123_0632','2015-01-23 07:21:34'),(8,'setts','0004_intmodel','2015-01-23 13:47:23');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('29zrmlmepuihikdcjeogr127fv6ywawl','YzQwNWYwNjlhZmVkZDVhZjUyNmM3YjQyOTU4OWI1ZjBlMjA0NTAyNzp7Il9hdXRoX3VzZXJfaGFzaCI6IjYxOTViMjMxNTYxYjhhZTljMGJhZWEzM2RhZTQyNDgzOGZkMTU3MDQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-02-06 18:01:22'),('eb1eqjs3fagxgxd5bn5468k2637ucjya','YzQwNWYwNjlhZmVkZDVhZjUyNmM3YjQyOTU4OWI1ZjBlMjA0NTAyNzp7Il9hdXRoX3VzZXJfaGFzaCI6IjYxOTViMjMxNTYxYjhhZTljMGJhZWEzM2RhZTQyNDgzOGZkMTU3MDQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-02-06 07:22:16'),('ovqniet7w022lrr11fskitvtc06iaek8','YzQwNWYwNjlhZmVkZDVhZjUyNmM3YjQyOTU4OWI1ZjBlMjA0NTAyNzp7Il9hdXRoX3VzZXJfaGFzaCI6IjYxOTViMjMxNTYxYjhhZTljMGJhZWEzM2RhZTQyNDgzOGZkMTU3MDQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-02-06 13:51:09'),('wufrf4hvml8jry90am1gp01f1tkknmpi','YzQwNWYwNjlhZmVkZDVhZjUyNmM3YjQyOTU4OWI1ZjBlMjA0NTAyNzp7Il9hdXRoX3VzZXJfaGFzaCI6IjYxOTViMjMxNTYxYjhhZTljMGJhZWEzM2RhZTQyNDgzOGZkMTU3MDQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-02-06 20:09:50');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_callorder`
--

DROP TABLE IF EXISTS `main_callorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_callorder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `timestap` datetime NOT NULL,
  `phone` varchar(17) NOT NULL,
  `status` varchar(16) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_callorder`
--

LOCK TABLES `main_callorder` WRITE;
/*!40000 ALTER TABLE `main_callorder` DISABLE KEYS */;
/*!40000 ALTER TABLE `main_callorder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_good`
--

DROP TABLE IF EXISTS `main_good`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_good` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `category_id` int(11) NOT NULL,
  `description` longtext NOT NULL,
  `priceFut` decimal(6,2) NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `measureName` varchar(16) NOT NULL,
  `step` decimal(3,2) NOT NULL,
  `maxRequest` decimal(5,2) NOT NULL,
  `smallImage` varchar(100) NOT NULL,
  `bigImage` varchar(100) NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  `weekly` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_good_6f33f001` (`category_id`),
  CONSTRAINT `category_id_refs_id_55804b7f` FOREIGN KEY (`category_id`) REFERENCES `main_goodcategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_good`
--

LOCK TABLES `main_good` WRITE;
/*!40000 ALTER TABLE `main_good` DISABLE KEYS */;
INSERT INTO `main_good` VALUES (3,'Вырезка',2,'sdfsd',600.00,550.00,'кг',0.50,3.00,'./4389915_zYStX6z_vlAhOj4_1lMRMka_GznP7Vu.png','./4389915_zYStX6z_vlAhOj4_lcMBEAR.png',0,1),(4,'Филейный край',2,'sdfsd',550.00,500.00,'кг',0.25,3.00,'./4389915_Sl1J9fv_qLKgEcM.png','./4389915_Sl1J9fv_QoqJEai.png',0,0),(5,'Яйцо куриное',8,'adasd',160.00,160.00,'дес',1.00,5.00,'./eggs-new_pACaIcb.png','./eggs-new_UQzwMQL.png',0,0),(6,'Брарнья корейка',3,'Аsvfsdgsdadaf',550.00,520.00,'кг',1.00,10.00,'./4389915_ZJtW8vq_8Z9d4ou.png','./4389915_SXDZoMX_BNLOYVP.png',0,0);
/*!40000 ALTER TABLE `main_good` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_good_recipes`
--

DROP TABLE IF EXISTS `main_good_recipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_good_recipes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `good_id` int(11) NOT NULL,
  `recipe_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `good_id` (`good_id`,`recipe_id`),
  KEY `main_good_recipes_4a7ad2d3` (`good_id`),
  KEY `main_good_recipes_fba12377` (`recipe_id`),
  CONSTRAINT `good_id_refs_id_918868c8` FOREIGN KEY (`good_id`) REFERENCES `main_good` (`id`),
  CONSTRAINT `recipe_id_refs_id_8ef43c13` FOREIGN KEY (`recipe_id`) REFERENCES `main_recipe` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_good_recipes`
--

LOCK TABLES `main_good_recipes` WRITE;
/*!40000 ALTER TABLE `main_good_recipes` DISABLE KEYS */;
/*!40000 ALTER TABLE `main_good_recipes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_goodcategory`
--

DROP TABLE IF EXISTS `main_goodcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_goodcategory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_goodcategory`
--

LOCK TABLES `main_goodcategory` WRITE;
/*!40000 ALTER TABLE `main_goodcategory` DISABLE KEYS */;
INSERT INTO `main_goodcategory` VALUES (2,'Говядина без кости',0),(3,'Баранина на кости',0),(4,'Птица',0),(5,'Молочные продукты',0),(6,'Мед',0),(7,'Сосиски',0),(8,'Яйца',0);
/*!40000 ALTER TABLE `main_goodcategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_order`
--

DROP TABLE IF EXISTS `main_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` datetime NOT NULL,
  `phone` varchar(17) NOT NULL,
  `email` varchar(75) NOT NULL,
  `status` varchar(16) NOT NULL,
  `totalPrice` decimal(7,2) NOT NULL,
  `deliveryDate` date DEFAULT NULL,
  `freeDelivery` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_order`
--

LOCK TABLES `main_order` WRITE;
/*!40000 ALTER TABLE `main_order` DISABLE KEYS */;
INSERT INTO `main_order` VALUES (1,'2015-01-23 17:49:30','+7(915) 032-59-23','g.sokol99@gmail.com','new',300.00,'2015-01-27',0),(2,'2015-01-23 17:53:05','+7(915) 032-59-23','g.sokol99@gmail.com','new',300.00,'2015-01-27',0),(3,'2015-01-23 17:54:06','+7(915) 032-59-23','g.sokol99@gmail.com','new',300.00,'2015-01-27',0),(4,'2015-01-23 17:55:41','+7(915) 032-59-23','g.sokol99@gmail.com','processed',2400.00,'2015-01-27',0),(5,'2015-01-23 17:56:18','+7(915) 032-59-23','g.sokol99@gmail.com','processed',1400.00,'2015-01-27',0),(6,'2015-01-23 17:56:53','+7(915) 032-59-23','g.sokol99@gmail.com','weighted',1400.00,'2015-01-27',0);
/*!40000 ALTER TABLE `main_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_partner`
--

DROP TABLE IF EXISTS `main_partner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_partner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `phone` varchar(17) NOT NULL,
  `deliveryDay` varchar(32) NOT NULL,
  `invisiable` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_partner`
--

LOCK TABLES `main_partner` WRITE;
/*!40000 ALTER TABLE `main_partner` DISABLE KEYS */;
INSERT INTO `main_partner` VALUES (1,'Андрей','+7(905) 751-95-97','tue',0);
/*!40000 ALTER TABLE `main_partner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_partnergood`
--

DROP TABLE IF EXISTS `main_partnergood`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_partnergood` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `partner_id` int(11) NOT NULL,
  `name` varchar(32) NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `minOrder` decimal(5,2) NOT NULL,
  `step` decimal(3,2) NOT NULL,
  `maxOrder` decimal(5,2) DEFAULT NULL,
  `defaultOrder` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `main_partnergood_42b53b76` (`partner_id`),
  CONSTRAINT `partner_id_refs_id_3263eabb` FOREIGN KEY (`partner_id`) REFERENCES `main_partner` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_partnergood`
--

LOCK TABLES `main_partnergood` WRITE;
/*!40000 ALTER TABLE `main_partnergood` DISABLE KEYS */;
INSERT INTO `main_partnergood` VALUES (1,1,'Полтуши',3000.00,1.00,1.00,5.00,3.00),(2,1,'Десяток яиц',100.00,1.00,1.00,15.00,0.00),(3,1,'Брарнья корейка',400.00,1.00,0.50,10.00,1.50);
/*!40000 ALTER TABLE `main_partnergood` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_partnergoodtogood`
--

DROP TABLE IF EXISTS `main_partnergoodtogood`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_partnergoodtogood` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `partnerGood_id` int(11) NOT NULL,
  `good_id` int(11) NOT NULL,
  `value` decimal(5,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_partnergoodtogood_356d4ef4` (`partnerGood_id`),
  KEY `main_partnergoodtogood_4a7ad2d3` (`good_id`),
  CONSTRAINT `good_id_refs_id_0aeba978` FOREIGN KEY (`good_id`) REFERENCES `main_good` (`id`),
  CONSTRAINT `partnerGood_id_refs_id_e7b7589a` FOREIGN KEY (`partnerGood_id`) REFERENCES `main_partnergood` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_partnergoodtogood`
--

LOCK TABLES `main_partnergoodtogood` WRITE;
/*!40000 ALTER TABLE `main_partnergoodtogood` DISABLE KEYS */;
INSERT INTO `main_partnergoodtogood` VALUES (1,2,5,1.00),(2,1,3,4.00),(3,1,4,5.00),(4,3,6,1.00);
/*!40000 ALTER TABLE `main_partnergoodtogood` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_recipe`
--

DROP TABLE IF EXISTS `main_recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_recipe` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `smallImage` varchar(100) NOT NULL,
  `bigImage` varchar(100) NOT NULL,
  `coockingMethod` longtext NOT NULL,
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_recipe_6f33f001` (`category_id`),
  CONSTRAINT `category_id_refs_id_48d9369e` FOREIGN KEY (`category_id`) REFERENCES `main_recipecategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_recipe`
--

LOCK TABLES `main_recipe` WRITE;
/*!40000 ALTER TABLE `main_recipe` DISABLE KEYS */;
INSERT INTO `main_recipe` VALUES (1,'Яичница','./4389915_jZGlSRA.png','./4389915_98W2CXw.png','Делаем яичницу',1);
/*!40000 ALTER TABLE `main_recipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_recipecategory`
--

DROP TABLE IF EXISTS `main_recipecategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_recipecategory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_recipecategory`
--

LOCK TABLES `main_recipecategory` WRITE;
/*!40000 ALTER TABLE `main_recipecategory` DISABLE KEYS */;
INSERT INTO `main_recipecategory` VALUES (1,'просто','./fried-egg_KYeS6lq.png'),(2,'Сложно','./pasta_Oi9aMJP_hUWrieu.png'),(3,'Смерть','./risoto_Lr7uw3n.png');
/*!40000 ALTER TABLE `main_recipecategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_recipeingridient`
--

DROP TABLE IF EXISTS `main_recipeingridient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_recipeingridient` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `recipe_id` int(11) NOT NULL,
  `name` varchar(32) NOT NULL,
  `value` varchar(16) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_recipeingridient_fba12377` (`recipe_id`),
  CONSTRAINT `recipe_id_refs_id_c8a5c0c3` FOREIGN KEY (`recipe_id`) REFERENCES `main_recipe` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_recipeingridient`
--

LOCK TABLES `main_recipeingridient` WRITE;
/*!40000 ALTER TABLE `main_recipeingridient` DISABLE KEYS */;
INSERT INTO `main_recipeingridient` VALUES (1,1,'яйцо','2'),(2,1,'соль/перец','по вкусу');
/*!40000 ALTER TABLE `main_recipeingridient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_supply`
--

DROP TABLE IF EXISTS `main_supply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_supply` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `partner_id` int(11) NOT NULL,
  `supplyDate` date NOT NULL,
  `status` varchar(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_supply_42b53b76` (`partner_id`),
  CONSTRAINT `partner_id_refs_id_62d78467` FOREIGN KEY (`partner_id`) REFERENCES `main_partner` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_supply`
--

LOCK TABLES `main_supply` WRITE;
/*!40000 ALTER TABLE `main_supply` DISABLE KEYS */;
INSERT INTO `main_supply` VALUES (1,1,'2015-01-27','weighted'),(2,1,'2015-01-30','weighted');
/*!40000 ALTER TABLE `main_supply` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_supplyitem`
--

DROP TABLE IF EXISTS `main_supplyitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_supplyitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `supply_id` int(11) NOT NULL,
  `partnerGood_id` int(11) NOT NULL,
  `value` decimal(5,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_supplyitem_c527041e` (`supply_id`),
  KEY `main_supplyitem_356d4ef4` (`partnerGood_id`),
  CONSTRAINT `partnerGood_id_refs_id_7d68c842` FOREIGN KEY (`partnerGood_id`) REFERENCES `main_partnergood` (`id`),
  CONSTRAINT `supply_id_refs_id_b8ace8e5` FOREIGN KEY (`supply_id`) REFERENCES `main_supply` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_supplyitem`
--

LOCK TABLES `main_supplyitem` WRITE;
/*!40000 ALTER TABLE `main_supplyitem` DISABLE KEYS */;
INSERT INTO `main_supplyitem` VALUES (1,1,1,1.00),(2,1,2,0.00),(3,2,1,3.00),(4,2,2,0.00);
/*!40000 ALTER TABLE `main_supplyitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_supplyorderitem`
--

DROP TABLE IF EXISTS `main_supplyorderitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_supplyorderitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `good_id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `supply_id` int(11) NOT NULL,
  `value` decimal(5,2) NOT NULL,
  `cut` tinyint(1) NOT NULL,
  `isWheightable` tinyint(1) NOT NULL,
  `isFromResides` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_supplyorderitem_4a7ad2d3` (`good_id`),
  KEY `main_supplyorderitem_68d25c7a` (`order_id`),
  KEY `main_supplyorderitem_c527041e` (`supply_id`),
  CONSTRAINT `good_id_refs_id_ec68cc07` FOREIGN KEY (`good_id`) REFERENCES `main_good` (`id`),
  CONSTRAINT `order_id_refs_id_5221ff3c` FOREIGN KEY (`order_id`) REFERENCES `main_order` (`id`),
  CONSTRAINT `supply_id_refs_id_adae2815` FOREIGN KEY (`supply_id`) REFERENCES `main_supply` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_supplyorderitem`
--

LOCK TABLES `main_supplyorderitem` WRITE;
/*!40000 ALTER TABLE `main_supplyorderitem` DISABLE KEYS */;
INSERT INTO `main_supplyorderitem` VALUES (1,3,4,1,3.50,0,1,0),(2,4,5,1,2.00,0,1,0),(3,4,6,1,2.00,0,1,0);
/*!40000 ALTER TABLE `main_supplyorderitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `setts_imagemodel`
--

DROP TABLE IF EXISTS `setts_imagemodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `setts_imagemodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `imgType` varchar(32) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `setts_imagemodel`
--

LOCK TABLES `setts_imagemodel` WRITE;
/*!40000 ALTER TABLE `setts_imagemodel` DISABLE KEYS */;
INSERT INTO `setts_imagemodel` VALUES (1,'logo','./eggs_4pCr8C6.png'),(2,'logo_bw','./eggs_bw_Z2PgmgM.png'),(3,'map','./map_IQkfFjM.png');
/*!40000 ALTER TABLE `setts_imagemodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `setts_intmodel`
--

DROP TABLE IF EXISTS `setts_intmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `setts_intmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `intType` varchar(32) NOT NULL,
  `value` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `setts_intmodel`
--

LOCK TABLES `setts_intmodel` WRITE;
/*!40000 ALTER TABLE `setts_intmodel` DISABLE KEYS */;
INSERT INTO `setts_intmodel` VALUES (1,'max_delivery_interval',4),(2,'delivery_price',300),(3,'free_delivery_min_price',3000),(4,'hour_delivery_close',19);
/*!40000 ALTER TABLE `setts_intmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `setts_phonemodel`
--

DROP TABLE IF EXISTS `setts_phonemodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `setts_phonemodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phone` varchar(17) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `setts_phonemodel`
--

LOCK TABLES `setts_phonemodel` WRITE;
/*!40000 ALTER TABLE `setts_phonemodel` DISABLE KEYS */;
INSERT INTO `setts_phonemodel` VALUES (1,'+7(985) 123-12-12');
/*!40000 ALTER TABLE `setts_phonemodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `setts_textmodel`
--

DROP TABLE IF EXISTS `setts_textmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `setts_textmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `text` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `setts_textmodel`
--

LOCK TABLES `setts_textmodel` WRITE;
/*!40000 ALTER TABLE `setts_textmodel` DISABLE KEYS */;
INSERT INTO `setts_textmodel` VALUES (1,'main_page','Это текст на главной странице'),(2,'delivery_page','Это текст страницы доставки');
/*!40000 ALTER TABLE `setts_textmodel` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-01-30  9:47:42
