-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: gotogym_bd
-- ------------------------------------------------------
-- Server version	8.3.0

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
-- Table structure for table `accounts_user`
--

DROP TABLE IF EXISTS `accounts_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `age` int unsigned DEFAULT NULL,
  `accepted_terms` tinyint(1) NOT NULL,
  `terms_accepted_at` datetime(6) DEFAULT NULL,
  `terms_hash` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `show_influencer_modal` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  CONSTRAINT `accounts_user_chk_1` CHECK ((`age` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_user`
--

LOCK TABLES `accounts_user` WRITE;
/*!40000 ALTER TABLE `accounts_user` DISABLE KEYS */;
INSERT INTO `accounts_user` VALUES (1,'pbkdf2_sha256$1000000$vsqxVAqBeXUbCrWKS2IKij$ByTdPufQybSaIJ2y/R4MUD0OsGVnAWamRQnW14hiik0=','2025-07-18 16:55:29.900335',1,'alex','alexandra','bedoya',1,1,'2025-07-01 14:25:10.967143','alexamunoz827@gmail.com',NULL,0,NULL,'',0),(2,'pbkdf2_sha256$1000000$Ttr9uH9z9YabOsT5BKRw7L$WAVERaygYmtFkJf7Rc3fdoPBnDuW/usGJuEtRU9EVSg=','2025-07-12 17:03:42.674975',0,'alexamunoz06@gmail.com','goto','gym',0,1,'2025-07-01 15:04:40.951174','alexamunoz06@gmail.com',34,1,'2025-07-01 15:04:40.948431','aa6b792d6a269edc729520e622a8436035c972a1e16adab080a02c623f231ed30342a986401842510326aa9a55f04a4ba151bc9ece1231eb3affe420be61f87c',0),(3,'pbkdf2_sha256$1000000$0Ycm9T8Uh30ETo99mstmcW$kmd768xH+OMuqn2RusgnQwGkM5Ue0YL/LB77Vg2hXqU=','2025-07-01 16:33:19.156204',0,'lhmunozc2014','Luis','Cortes',0,1,'2025-07-01 16:33:07.203781','lhmunozc2014@gmail.com',40,1,'2025-07-01 16:33:07.203129','aa6b792d6a269edc729520e622a8436035c972a1e16adab080a02c623f231ed30342a986401842510326aa9a55f04a4ba151bc9ece1231eb3affe420be61f87c',0),(4,'pbkdf2_sha256$1000000$SqIxbWpzvRrUWf3WCXCP5J$DIW+J5VkPvvIQ6/7CcMD5S2ITu+tD58BWrRtqLSxbJQ=','2025-07-12 15:11:44.599428',0,'ppruebaa','prueba','p',0,1,'2025-07-12 15:04:06.555890','ppruebaa@gmail.com',23,1,'2025-07-12 15:04:06.555244','aa6b792d6a269edc729520e622a8436035c972a1e16adab080a02c623f231ed30342a986401842510326aa9a55f04a4ba151bc9ece1231eb3affe420be61f87c',0),(5,'pbkdf2_sha256$1000000$koDNCLDy20PltU8TcSLp5R$J0JJpi6xeBaOKzftS12Gmjbcupznw7F2QtCUkmRihVA=','2025-07-12 16:10:00.765566',0,'wilson.parrado1993','Wilson','Parrado',0,1,'2025-07-12 16:08:58.616591','wilson.parrado1993@gmail.com',30,1,'2025-07-12 16:08:58.616285','aa6b792d6a269edc729520e622a8436035c972a1e16adab080a02c623f231ed30342a986401842510326aa9a55f04a4ba151bc9ece1231eb3affe420be61f87c',0),(6,'pbkdf2_sha256$1000000$xNtJoISNA1duStbeGG8VYG$S/IIro4/ymJ7xVi0o1onI22Fdj/5VWa/lj7C/9qB+Yc=','2025-07-12 16:52:06.178772',1,'abm','Alexandra1','Beodya1',1,1,'2025-07-12 16:35:10.138968','abmunoz06@gmail.com',NULL,0,NULL,'',0);
/*!40000 ALTER TABLE `accounts_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_user_groups`
--

DROP TABLE IF EXISTS `accounts_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_user_groups_user_id_group_id_59c0b32f_uniq` (`user_id`,`group_id`),
  KEY `accounts_user_groups_group_id_bd11a704_fk_auth_group_id` (`group_id`),
  CONSTRAINT `accounts_user_groups_group_id_bd11a704_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `accounts_user_groups_user_id_52b62117_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_user_groups`
--

LOCK TABLES `accounts_user_groups` WRITE;
/*!40000 ALTER TABLE `accounts_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_user_user_permissions`
--

DROP TABLE IF EXISTS `accounts_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_user_user_permi_user_id_permission_id_2ab516c2_uniq` (`user_id`,`permission_id`),
  KEY `accounts_user_user_p_permission_id_113bb443_fk_auth_perm` (`permission_id`),
  CONSTRAINT `accounts_user_user_p_permission_id_113bb443_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `accounts_user_user_p_user_id_e4f0a161_fk_accounts_` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_user_user_permissions`
--

LOCK TABLES `accounts_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `accounts_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can view permission',1,'view_permission'),(5,'Can add group',2,'add_group'),(6,'Can change group',2,'change_group'),(7,'Can delete group',2,'delete_group'),(8,'Can view group',2,'view_group'),(9,'Can add content type',3,'add_contenttype'),(10,'Can change content type',3,'change_contenttype'),(11,'Can delete content type',3,'delete_contenttype'),(12,'Can view content type',3,'view_contenttype'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add log entry',5,'add_logentry'),(18,'Can change log entry',5,'change_logentry'),(19,'Can delete log entry',5,'delete_logentry'),(20,'Can view log entry',5,'view_logentry'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add category',7,'add_category'),(26,'Can change category',7,'change_category'),(27,'Can delete category',7,'delete_category'),(28,'Can view category',7,'view_category'),(29,'Can add post',8,'add_post'),(30,'Can change post',8,'change_post'),(31,'Can delete post',8,'delete_post'),(32,'Can view post',8,'view_post'),(33,'Can add product category',9,'add_productcategory'),(34,'Can change product category',9,'change_productcategory'),(35,'Can delete product category',9,'delete_productcategory'),(36,'Can view product category',9,'view_productcategory'),(37,'Can add product',10,'add_product'),(38,'Can change product',10,'change_product'),(39,'Can delete product',10,'delete_product'),(40,'Can view product',10,'view_product'),(41,'Can add brand',11,'add_brand'),(42,'Can change brand',11,'change_brand'),(43,'Can delete brand',11,'delete_brand'),(44,'Can view brand',11,'view_brand'),(45,'Can add color marca',12,'add_colormarca'),(46,'Can change color marca',12,'change_colormarca'),(47,'Can delete color marca',12,'delete_colormarca'),(48,'Can view color marca',12,'view_colormarca'),(49,'Can add influencer profile',13,'add_influencerprofile'),(50,'Can change influencer profile',13,'change_influencerprofile'),(51,'Can delete influencer profile',13,'delete_influencerprofile'),(52,'Can view influencer profile',13,'view_influencerprofile'),(53,'Can add template config',14,'add_templateconfig'),(54,'Can change template config',14,'change_templateconfig'),(55,'Can delete template config',14,'delete_templateconfig'),(56,'Can view template config',14,'view_templateconfig');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_category`
--

DROP TABLE IF EXISTS `blog_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blog_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug` varchar(120) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_category`
--

LOCK TABLES `blog_category` WRITE;
/*!40000 ALTER TABLE `blog_category` DISABLE KEYS */;
INSERT INTO `blog_category` VALUES (36,'Bienestar Corporativo','bienestar-corporativo'),(37,'Historias de Atletas & Embajadores','historias-de-atletas-embajadores'),(38,'Salud Mental & Motivación','salud-mental-motivacion'),(39,'Entrenamiento Consciente','entrenamiento-consciente'),(40,'	Nutrición & Rendimiento','nutricion-rendimiento'),(41,'	Outfits & Estilismo Deportivo','outfits-estilismo-deportivo'),(42,'Tendencias de Activewear','tendencias-de-activewear'),(44,'ejemplo','ejemplo');
/*!40000 ALTER TABLE `blog_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_post`
--

DROP TABLE IF EXISTS `blog_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blog_post` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug` varchar(220) COLLATE utf8mb4_unicode_ci NOT NULL,
  `excerpt` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `featured` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `published` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `reading_time` int unsigned NOT NULL,
  `is_published` tinyint(1) NOT NULL,
  `author_id` bigint NOT NULL,
  `category_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `blog_post_author_id_dd7a8485_fk_accounts_user_id` (`author_id`),
  KEY `blog_post_category_id_c326dbf8_fk_blog_category_id` (`category_id`),
  CONSTRAINT `blog_post_author_id_dd7a8485_fk_accounts_user_id` FOREIGN KEY (`author_id`) REFERENCES `accounts_user` (`id`),
  CONSTRAINT `blog_post_category_id_c326dbf8_fk_blog_category_id` FOREIGN KEY (`category_id`) REFERENCES `blog_category` (`id`),
  CONSTRAINT `blog_post_chk_1` CHECK ((`reading_time` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_post`
--

LOCK TABLES `blog_post` WRITE;
/*!40000 ALTER TABLE `blog_post` DISABLE KEYS */;
INSERT INTO `blog_post` VALUES (1,'Alimentación periodizada: cómo ajustar tus macros a tu ciclo de entrenamiento','alimentacion-periodizada-como-ajustar-tus-macros-a-tu-ciclo-de-entrenamiento','Planificar la nutrición según el micro-ciclo de carga permite maximizar la síntesis proteica, mantener la disponibilidad de glucógeno y optimizar la recuperación. No se trata solo de “comer sano”, sino de sincronizar el tipo y la cantidad de macronutrientes con los estímulos fisiológicos de cada sesión. La periodización nutricional convierte la mesa en una extensión del gimnasio y reduce el riesgo de sobre-entrenamiento.\r\n\r\nAl calibre personal de las cargas se añaden variables contextuales: clima, altitud, horarios de sueño y niveles de estrés. Cuando el deportista entiende esta interacción, transforma su relación con la comida; deja de contar calorías para comenzar a “programar combustible”. El resultado es mayor bio-disponibilidad energética, mejor inmunocompetencia y un rendimiento consistente durante toda la temporada.','La periodización nutricional surgió de la práctica del “train low, compete high” en el ciclismo de élite. Su premisa es simple: la señal adaptativa del músculo depende tanto del esfuerzo como de la disponibilidad de sustratos.\r\n\r\nDías de alta intensidad – Prioriza 6–8 g CHO/kg para saturar glucógeno; reparte proteínas magras (2–2,2 g/kg) y un 25 % de lípidos con alta densidad de omega-3.\r\n\r\nDías de volumen moderado – Reduce hidratos a 4–5 g/kg y eleva grasas “slow fuel” a 35 %; mantén proteína estable.\r\n\r\nSesiones técnicas o descanso activo – 3 g CHO/kg bastan; el objetivo es apoyar procesos anabólicos y recuperación neuronal con 30 % de calorías en grasas saludables.\r\n\r\nAñade ventanas de “sleep low”: cena baja en carbohidratos tras un estímulo aeróbico para favorecer la biogénesis mitocondrial nocturna. Monitoriza HRV y glucosa capilar para ajustar. La consistencia se mide en semanas, no en días; usa diarios alimentarios digitales y métricas de percepción de esfuerzo (RPE). Esta estrategia modular convierte cada comida en un eslabón estratégico entre la sesión que termina y la que viene.','blog/featured/ChatGPT_Image_2_jul_2025_22_14_12.png','2025-07-03 03:03:13.064655','2025-07-03 03:15:27.459389',3,1,1,40),(2,'Superalimentos colombianos para corredores de fondo','superalimentos-colombianos-para-corredores-de-fondo','Los maratones a 2 600 m de Bogotá inspiran a buscar combustibles nativos que aporten densidad nutricional sin inflamar. Alimentos andinos como la quinua, la chía y la papa criolla ofrecen matrices de carbohidratos de liberación sostenida, proteínas completas y electrolitos naturales. Más allá del marketing, la evidencia científica confirma su rol en la reducción de marcadores de daño oxidativo y en la mejora de la eficiencia metabólica.\r\n\r\nIncluir ingredientes de kilómetro cero disminuye la huella de carbono y favorece economías rurales. La biodiversidad colombiana agrega fitoquímicos únicos —antocianinas, betacianinas y alcaloides suaves— que potencian la hematopoyesis y la recuperación tisular. Comer local deja de ser una moda para convertirse en un arma competitiva que armoniza rendimiento, sostenibilidad y orgullo gastronómico.','Quinua tolimense: 13 % proteína con perfil de aminoácidos equiparable a la caseína; su índice glucémico (IG = 53) estabiliza la glicemia en tiradas > 25 km. Receta: bowl de quinua cocida en caldo de hueso, aguacate y limón mandarino.\r\n\r\nPapa criolla: alta en almidón resistente y vitamina C; pruebas in vitro muestran 20 % menos producción de IL-6 post-ejercicio respecto a papas blancas. Ideal en puré con sal rosada y aceite de achiote.\r\n\r\nChía boyacense: 34 % fibra soluble; forma un gel que prolonga la hidratación. Combina 2 cucharadas en bebida isotónica casera (agua + panela + limón).\r\n\r\nGuayaba agria: 8 mg de licopeno/100 g; mejora la disponibilidad de carnitina. Úsala en smoothies post-run con kefir.\r\n\r\nIntegra estos superalimentos en bloques: pre-run (carb-loading), durante (geles caseros de papa criolla), y post-run (recovery bowls). El resultado: menor percepción de fatiga, mejor VO₂max y una economía de carrera que celebra el sabor colombiano.','blog/featured/ChatGPT_Image_2_jul_2025_22_28_20.png','2025-07-03 03:28:38.898037','2025-07-03 03:28:38.898115',3,1,1,40),(3,'El Poder de la Ropa Deportiva en Tu Salud Mental y Motivación Diaria','el-poder-de-la-ropa-deportiva-en-tu-salud-mental-y-motivacion-diaria','Descubre cómo la ropa deportiva no solo viste tu cuerpo, sino que también puede transformar tu estado de ánimo y potenciar tu motivación para alcanzar tus metas. En este artículo, exploramos la conexión entre lo que llevas puesto y tu bienestar mental.','¿Alguna vez te has puesto tu conjunto deportivo favorito y has sentido una oleada de energía y ganas de moverte? No es casualidad. La ropa deportiva va más allá de su función práctica; es una herramienta poderosa para tu salud mental y motivación.\r\n\r\nLa Psicología Detrás de la Ropa Deportiva\r\nLos psicólogos sostienen que la ropa que llevamos afecta a nuestro estado de ánimo y comportamiento. Este fenómeno se conoce como cognición vestimentaria. Cuando te pones ropa deportiva, tu mente recibe el mensaje de que es hora de la actividad. Es un recordatorio visual y táctil de tus objetivos de salud y bienestar.\r\n\r\nComodidad y Confianza: Un Binomio Invencible\r\nSentirte cómodo es fundamental para rendir al máximo, tanto física como mentalmente. La ropa deportiva de calidad, diseñada con tejidos transpirables y que se adaptan a tu cuerpo, te permite moverte con libertad. Además, cuando te ves bien en el espejo, tu autoestima se eleva. Esa confianza se traslada a otros aspectos de tu vida.\r\n\r\n\r\n La Motivación en Cada Prenda\r\nElegir prendas que te gustan y que reflejan tu personalidad puede ser un gran motivador. ¿Quién no ha comprado unas nuevas zapatillas o un top con un diseño inspirador para animarse a ir al gimnasio? La ilusión por estrenar ropa deportiva puede ser el empujón que necesitas para mantener la constancia.\r\n\r\nInversión en Calidad, Inversión en Ti\r\nOptar por ropa deportiva de calidad no solo es una cuestión de durabilidad, sino también de rendimiento y comodidad. Las prendas técnicas, con propiedades como el control de la humedad o el soporte muscular, te ayudan a rendir mejor y a evitar lesiones. Y cuando inviertes en ti, refuerzas el compromiso con tus metas.\r\n\r\n\r\nTips para Elegir tu Ropa Deportiva Motivacional\r\n   1. Color y Diseño: Elige colores que te alegren el día. Los tonos vivos pueden mejorar tu estado de ánimo.\r\n   2. Ajuste Perfecto:Que no apriete ni quede suelto. La ropa debe permitirte moverte sin restricciones.\r\n   3. Tecnología: Busca tejidos que se adapten a tu actividad (transpirables, con compresión, etc.).\r\n   4. Sostenibilidad:Cada vez más marcas apuestan por materiales ecológicos. Contribuir al planeta también mejora tu bienestar emocional.','blog/featured/Salud_mental.jpg','2025-07-07 22:21:47.050507','2025-07-07 22:21:47.050559',3,1,2,38),(4,'De la Oficina al Parque: El Athleisure Chic que Deslumbra en la Ciudad','de-la-oficina-al-parque-el-athleisure-chic-que-deslumbra-en-la-ciudad','Transforma tu look deportivo en un statement de moda urbana con este outfit multifuncional. Ideado para transiciones fluidas entre reuniones, cafés y sesiones de entrenamiento express.','1. Prenda Estrella: Overshirt Térmico\r\n\r\nMaterial: Jersey técnico con tratamiento antiarrugas + repelente al agua.\r\n\r\nVersatilidad: Cremallera completa para convertir en chaqueta o chaleco.\r\n\r\nTono: Beige terroso (neutraliza sudor y combina con todo).\r\n\r\n2. Base Adaptable:\r\n\r\nOpción 1: Monocromo total (leggings borgoña + top cortaviento en mismo tono).\r\n\r\nOpción 2: Contraste vibrante (leggings negros + top coral para energía instantánea).\r\n\r\n3. Calzado Híbrido:\r\n\r\nModelo: Zapatillas estilo \"trail-running\" con suela de tacos bajos.\r\n\r\nEstilismo: Usar con medias tobilleras de tejido merino (regula temperatura sin volumen).\r\n\r\n4. Accesorios Clave:\r\n\r\nRiñonera ampliable: De neopreno (cabeza tablet + botella de agua).\r\n\r\nGafas de sol deportivas: Montura ultraligera con lentes fotocromáticas.\r\n\r\nTurbante absorbente: Reemplaza gorras; controla sudor sin aplastar cabello.\r\n\r\nTips de Composición:\r\n\r\n\"La regla 70/30:\r\n\r\n70% prendas técnicas (rendimiento).\r\n\r\n30% piezas de diseño (estilo personal).\r\nEjemplo: Combina overshirt minimalista con leggings estampados geométricos\".','blog/featured/post56.jpg','2025-07-07 22:30:49.710060','2025-07-07 22:30:49.710121',3,1,3,41),(6,'Cambio generado por gotogym456','1212','1233','333','blog/featured/dd48c2ac-8fa2-47ae-93c5-7acb2965b676.png','2025-07-07 22:31:43.307123','2025-07-08 02:15:59.166472',3,1,2,40),(7,'2121','2121','3312','121212','blog/featured/Imagen_Home_3.jpg','2025-07-07 22:32:00.330048','2025-07-08 00:04:32.992223',3,1,3,42),(10,'prueba','dfdf','dfdf','dfdf','blog/featured/VERBAL.png','2025-07-08 13:06:30.822730','2025-07-08 14:21:56.609881',3,1,2,39),(11,'hhh','hhh','hh','dfdfdff','blog/featured/sss.png','2025-07-08 14:18:36.633745','2025-07-08 14:18:36.633800',3,1,1,NULL),(14,'ejemplo','ejemplo','ejemplo','ejemplo','blog/featured/Foto_1-06-25_2_25_28_pm.jpg','2025-07-12 15:49:12.862315','2025-07-12 15:49:12.862396',3,1,1,37);
/*!40000 ALTER TABLE `blog_post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `configuracion_marca_colormarca`
--

DROP TABLE IF EXISTS `configuracion_marca_colormarca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `configuracion_marca_colormarca` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `codigo_hex` varchar(7) COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `codigo_hex` (`codigo_hex`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `configuracion_marca_colormarca`
--

LOCK TABLES `configuracion_marca_colormarca` WRITE;
/*!40000 ALTER TABLE `configuracion_marca_colormarca` DISABLE KEYS */;
/*!40000 ALTER TABLE `configuracion_marca_colormarca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_accounts_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (4,'accounts','user'),(5,'admin','logentry'),(2,'auth','group'),(1,'auth','permission'),(7,'blog','category'),(8,'blog','post'),(12,'configuracion_marca','colormarca'),(3,'contenttypes','contenttype'),(13,'influencer','influencerprofile'),(11,'products','brand'),(10,'products','product'),(9,'products','productcategory'),(6,'sessions','session'),(14,'web','templateconfig');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-07-01 14:19:17.775897'),(2,'contenttypes','0002_remove_content_type_name','2025-07-01 14:19:18.296416'),(3,'auth','0001_initial','2025-07-01 14:19:19.574000'),(4,'auth','0002_alter_permission_name_max_length','2025-07-01 14:19:19.746885'),(5,'auth','0003_alter_user_email_max_length','2025-07-01 14:19:19.754382'),(6,'auth','0004_alter_user_username_opts','2025-07-01 14:19:19.762677'),(7,'auth','0005_alter_user_last_login_null','2025-07-01 14:19:19.770645'),(8,'auth','0006_require_contenttypes_0002','2025-07-01 14:19:19.774021'),(9,'auth','0007_alter_validators_add_error_messages','2025-07-01 14:19:19.790445'),(10,'auth','0008_alter_user_username_max_length','2025-07-01 14:19:19.799805'),(11,'auth','0009_alter_user_last_name_max_length','2025-07-01 14:19:19.810272'),(12,'auth','0010_alter_group_name_max_length','2025-07-01 14:19:19.849471'),(13,'auth','0011_update_proxy_permissions','2025-07-01 14:19:19.862231'),(14,'auth','0012_alter_user_first_name_max_length','2025-07-01 14:19:19.873333'),(15,'accounts','0001_initial','2025-07-01 14:19:20.416733'),(16,'accounts','0002_user_show_influencer_modal','2025-07-01 14:21:42.304669'),(17,'admin','0001_initial','2025-07-01 14:22:20.957262'),(18,'admin','0002_logentry_remove_auto_add','2025-07-01 14:22:20.966587'),(19,'admin','0003_logentry_add_action_flag_choices','2025-07-01 14:22:20.988098'),(20,'blog','0001_initial','2025-07-01 14:22:21.510345'),(21,'configuracion_marca','0001_initial','2025-07-01 14:22:21.554720'),(22,'influencer','0001_initial','2025-07-01 14:22:21.726849'),(23,'products','0001_initial','2025-07-01 14:22:21.957960'),(24,'products','0002_brand_product_discount_product_featured_and_more','2025-07-01 14:22:22.587155'),(25,'sessions','0001_initial','2025-07-01 14:22:22.746558'),(26,'tienda','0001_initial','2025-07-01 14:22:23.226618'),(27,'tienda','0002_remove_producto_categoria_remove_producto_marca_and_more','2025-07-01 14:22:24.366545'),(28,'accounts','0003_alter_user_first_name_alter_user_last_name','2025-07-01 14:24:41.562467'),(29,'products','0003_alter_product_price','2025-07-01 14:35:34.811907'),(30,'web','0001_initial','2025-07-01 16:58:12.147891'),(31,'accounts','0004_user_happiness_index_user_height_user_profession_and_more','2025-07-08 13:54:01.081003'),(32,'accounts','0005_remove_user_happiness_index_remove_user_height_and_more','2025-07-16 02:16:46.127063');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('6y3gapxk8dvddxd2h5i2182frtipzsgs','.eJxVjDsOwjAQBe_iGlnZrG1iSnrOYO3HwgHkSHFSIe5OIqWA9s3Me5tE61LS2vKcRjUXA-b0uzHJM9cd6IPqfbIy1WUe2e6KPWizt0nz63q4fweFWtlqzwiCrMHFjmEAJSEIlNVJzyFEJ1k19l0mQFE_eD0Tw1Z5RMbozOcL-ak4RQ:1ucoMs:zLq4flI13dyFC2wvlvp9XCG_WhddTfDIBRWwsbyas9U','2025-08-01 16:55:30.403051'),('8af1qbakruqfrx1g0cc0i7zw5qrd1pz6','.eJxVjDsOwjAQBe_iGlnZrG1iSnrOYO3HwgHkSHFSIe5OIqWA9s3Me5tE61LS2vKcRjUXA-b0uzHJM9cd6IPqfbIy1WUe2e6KPWizt0nz63q4fweFWtlqzwiCrMHFjmEAJSEIlNVJzyFEJ1k19l0mQFE_eD0Tw1Z5RMbozOcL-ak4RQ:1uYy88:5xE9mzM6irihczYnOl7-aYREpvoaq_aeUpniqq-hUzQ','2025-07-22 02:32:24.880185'),('boi86rdstqwpjs3ebfntc8dtw9ddn5kr','.eJxVjMsOwiAQRf-FtSEOjwFcuvcbCI9BqoYmpV0Z_92SdKHbe865b-bDtla_dVr8lNmFCXb63WJIT2oD5Edo95mnua3LFPlQ-EE7v82ZXtfD_TuooddRSxFBOQStizwDBmesTQUcJekiJFfQKENFo8oKsswJd0BoKYpdkezzBcyFN70:1uZ7w8:p79zbgaaAeSqEvq-dsjhWSouLnkpdpXJL82TKEERpR0','2025-07-22 13:00:40.470122'),('lkkqhdguxjht1jn4husggcac9y69txc1','.eJxVjjkOgzAURO_iOrL43oIp03MG9BcrJolAAlMh7h4jUSTtzJun2dWAW8nDtqZlGEV1CtTtNyPkd5rOQl44PWfN81SWkfSJ6KtddT9L-jwu9k-Qcc117ckCW5LgYkPQgiAjBEzi2FAI0XESiaZJCJbFt17uSFBX3lqy0VUp41JUt9eHnTmOL2RyPHI:1ubrkc:cFP18uWCfR5bMzAMpGC0yFaVeyJfGNRLA0waho5kaww','2025-07-30 02:20:06.624800'),('ny97vgjcgn2nbequ23d4vu3pw6qb3z5g','.eJxVjMsOwiAQRf-FtSEOjwFcuvcbCI9BqoYmpV0Z_92SdKHbe865b-bDtla_dVr8lNmFCXb63WJIT2oD5Edo95mnua3LFPlQ-EE7v82ZXtfD_TuooddRSxFBOQStizwDBmesTQUcJekiJFfQKENFo8oKsswJd0BoKYpdkezzBcyFN70:1uZ9BE:g8J6PJuxphuUIwmeYc2YZ0Xjj4HmIpYJ7x2-EU-8tuc','2025-07-22 14:20:20.021531'),('u28i3z3eyaycydkcf8lofr51iqyo9a4o','.eJxVjMsOwiAQRf-FtSEOjwFcuvcbCI9BqoYmpV0Z_92SdKHbe865b-bDtla_dVr8lNmFCXb63WJIT2oD5Edo95mnua3LFPlQ-EE7v82ZXtfD_TuooddRSxFBOQStizwDBmesTQUcJekiJFfQKENFo8oKsswJd0BoKYpdkezzBcyFN70:1uZ7vV:jBBdfLif_-zm6bprePx9w1W-RHbkalbwZwkS9jbo7Rw','2025-07-22 13:00:01.898993');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `influencer_influencerprofile`
--

DROP TABLE IF EXISTS `influencer_influencerprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `influencer_influencerprofile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `referral_code` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `commission_balance` decimal(10,2) NOT NULL,
  `total_referred` int unsigned NOT NULL,
  `total_sales` decimal(10,2) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `referral_code` (`referral_code`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `influencer_influence_user_id_f065b334_fk_accounts_` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`),
  CONSTRAINT `influencer_influencerprofile_chk_1` CHECK ((`total_referred` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `influencer_influencerprofile`
--

LOCK TABLES `influencer_influencerprofile` WRITE;
/*!40000 ALTER TABLE `influencer_influencerprofile` DISABLE KEYS */;
INSERT INTO `influencer_influencerprofile` VALUES (1,'15cbc02d-3131-4cd9-8dea-41adea211d9b',0.00,0,0.00,'2025-07-01 15:06:01.228142',1,2),(2,'27f616d1-29f9-432d-923a-2b555df6a3c0',0.00,0,0.00,'2025-07-01 16:33:45.607302',1,3),(3,'b58841ea-6a64-49fb-8aba-12e161cb21fc',0.00,0,0.00,'2025-07-06 02:27:52.607704',1,1),(4,'7798847d-9338-4521-a20f-d29fd91fd269',0.00,0,0.00,'2025-07-12 15:05:19.909154',1,4);
/*!40000 ALTER TABLE `influencer_influencerprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_brand`
--

DROP TABLE IF EXISTS `products_brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_brand` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_brand`
--

LOCK TABLES `products_brand` WRITE;
/*!40000 ALTER TABLE `products_brand` DISABLE KEYS */;
INSERT INTO `products_brand` VALUES (6,'GoToGym'),(4,'John Frank Alza'),(5,'Kosta Azul');
/*!40000 ALTER TABLE `products_brand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_product`
--

DROP TABLE IF EXISTS `products_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `price` decimal(12,4) NOT NULL,
  `stock` int unsigned NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `category_id` bigint NOT NULL,
  `discount` int unsigned NOT NULL,
  `featured` tinyint(1) NOT NULL,
  `brand_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `products_product_category_id_9b594869_fk_products_` (`category_id`),
  KEY `products_product_brand_id_3e2e8fd1_fk_products_brand_id` (`brand_id`),
  CONSTRAINT `products_product_brand_id_3e2e8fd1_fk_products_brand_id` FOREIGN KEY (`brand_id`) REFERENCES `products_brand` (`id`),
  CONSTRAINT `products_product_category_id_9b594869_fk_products_` FOREIGN KEY (`category_id`) REFERENCES `products_productcategory` (`id`),
  CONSTRAINT `products_product_chk_1` CHECK ((`stock` >= 0)),
  CONSTRAINT `products_product_chk_2` CHECK ((`discount` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_product`
--

LOCK TABLES `products_product` WRITE;
/*!40000 ALTER TABLE `products_product` DISABLE KEYS */;
INSERT INTO `products_product` VALUES (1,'Conjunto Fit leggins y top flex','Disfruta de este conjunto de alta costura y tecnología, diseño exclusivo de John Frank Alza.\r\n\r\nTop color naranja impreso en acabados hexagonales en grafeno de alta tectecnología.\r\n\r\nBiker color azul oscuro impreso en hexagonales en grafeno, que te permite generar un mejor rendimiento deportivo.\r\n\r\nDisfruta de estas predas del gimnasio a la casa.',450.0000,1,'products/Foto_1-06-25_2_19_49_pm.png',1,0,0,4),(2,'Short FlexLite','Short negro ligero, cintura elástica y logo reflectivo.',99.9000,95,'products/Short_FlexLite_Ej7edq1.png',1,0,1,NULL),(3,'Leggings PowerStretch','Legigns azul',990.0000,23,'products/Leggings_PowerStretch_x0EgZyB.png',1,0,1,NULL),(4,'Sudadera Core Performance','',129.0000,120,'products/Sudadera_Core_Performance_4SpJQWZ.png',3,0,1,NULL),(5,'Rompevientos SpeedWind','',12.7000,200,'products/Rompevientos_SpeedWind_O4BH5HX.png',1,0,1,NULL),(6,'Short FlexLite','',230.0000,124,'products/Short_TrailGrip_1h95hqZ.png',3,0,1,NULL),(7,'Mallas FastTrack','Mallas FastTrack',34.0000,5,'products/Mallas_FastTrack_qzmLXDf.png',3,0,1,NULL);
/*!40000 ALTER TABLE `products_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_productcategory`
--

DROP TABLE IF EXISTS `products_productcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_productcategory` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_productcategory`
--

LOCK TABLES `products_productcategory` WRITE;
/*!40000 ALTER TABLE `products_productcategory` DISABLE KEYS */;
INSERT INTO `products_productcategory` VALUES (1,'John Frank Alza','Bienvenidos a nuestra colecciòn GoToGym by John Frank Alza, donde descubriras lo mejor de la ropa deportiva y la alta costura, encuentra ropa para hombre y para mujer y disfruta de nuestras piezas únicas.'),(2,'Correr y Trail','Prendas ultraligeras y reflectivas para running urbano o de montaña, con paneles de ventilación y protección UV.'),(3,'Yoga y Pilates','Conjuntos de tejido suave y elástico que se adaptan al cuerpo, brindando libertad de movimiento y soporte en posturas estáticas o dinámicas.'),(4,'Ciclismo de Alto Rendimiento','Jerseys aerodinámicos, culottes con badana anatómica y chaquetas cortaviento con bolsillos estratégicos para carretera y MTB.'),(5,'Kosta Azul','Bienevenidos a nuestra colección GoToGym Kosta Azul, encuentra ropa para hombre casual de alta tecnología y performance, disfrutas camisas, camisetas y más.');
/*!40000 ALTER TABLE `products_productcategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `web_templateconfig`
--

DROP TABLE IF EXISTS `web_templateconfig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `web_templateconfig` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `template_name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `color` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `font` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `template_name` (`template_name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `web_templateconfig`
--

LOCK TABLES `web_templateconfig` WRITE;
/*!40000 ALTER TABLE `web_templateconfig` DISABLE KEYS */;
INSERT INTO `web_templateconfig` VALUES (1,'home','#ff0000','','');
/*!40000 ALTER TABLE `web_templateconfig` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-20 22:20:41
