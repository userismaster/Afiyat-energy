-- MySQL dump generated from SQLite
-- Generated at: 2024-12-28 19:25:35

SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE = 'NO_AUTO_VALUE_ON_ZERO';
SET time_zone = '+00:00';

USE `salox289_afiyat`;


-- Table structure for table `django_migrations`
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `app` VARCHAR(255) NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `applied` DATETIME NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table `django_migrations`
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (1, 'contenttypes', '0001_initial', '2024-12-27 10:18:34');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (2, 'auth', '0001_initial', '2024-12-27 10:18:34');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (3, 'admin', '0001_initial', '2024-12-27 10:18:34');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2024-12-27 10:18:34');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2024-12-27 10:18:34');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2024-12-27 10:18:34');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2024-12-27 10:18:34');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (8, 'auth', '0003_alter_user_email_max_length', '2024-12-27 10:18:34');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (9, 'auth', '0004_alter_user_username_opts', '2024-12-27 10:18:34');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (10, 'auth', '0005_alter_user_last_login_null', '2024-12-27 10:18:34');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (11, 'auth', '0006_require_contenttypes_0002', '2024-12-27 10:18:34');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2024-12-27 10:18:34');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (13, 'auth', '0008_alter_user_username_max_length', '2024-12-27 10:18:34');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2024-12-27 10:18:34');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (15, 'auth', '0010_alter_group_name_max_length', '2024-12-27 10:18:34');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (16, 'auth', '0011_update_proxy_permissions', '2024-12-27 10:18:34');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (17, 'auth', '0012_alter_user_first_name_max_length', '2024-12-27 10:18:34');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (19, 'sessions', '0001_initial', '2024-12-27 10:18:34');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (31, 'telegram_bot', '0001_initial', '2024-12-28 07:58:42');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (32, 'contacts', '0001_initial', '2024-12-28 08:43:17');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (36, 'contacts', '0002_contactmessage_is_processed_contactmessage_read_at', '2024-12-28 10:54:56');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (37, 'notifications', '0001_initial', '2024-12-28 11:50:20');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (38, 'catalog', '0001_initial', '2024-12-28 12:10:06');


-- Table structure for table `auth_group_permissions`
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `group_id` INT NOT NULL,
  `permission_id` INT NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- Table structure for table `auth_user_groups`
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `group_id` INT NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- Table structure for table `auth_user_user_permissions`
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `permission_id` INT NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- Table structure for table `django_admin_log`
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `object_id` TEXT,
  `object_repr` VARCHAR(200) NOT NULL,
  `action_flag` TEXT NOT NULL,
  `change_message` TEXT NOT NULL,
  `content_type_id` INT,
  `user_id` INT NOT NULL,
  `action_time` DATETIME NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table `django_admin_log`
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (1, '1', 'ss', 1, '[{"added": {}}]', 8, 1, '2024-12-27 10:21:13');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (2, '1', 'asdasdasd', 1, '[{"added": {}}]', 9, 1, '2024-12-27 10:22:06');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (3, '1', 'asdasd', 1, '[{"added": {}}]', 7, 1, '2024-12-27 10:34:22');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (4, '2', 'asdasdasd', 1, '[{"added": {}}]', 8, 1, '2024-12-27 10:34:31');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (5, '1', 'фывфывфыв', 1, '[{"added": {}}]', 10, 1, '2024-12-27 12:27:51');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (6, '1', 'ProductImage object (1)', 1, '[{"added": {}}]', 19, 1, '2024-12-27 13:07:23');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (7, '1', 'Muhammad Qodir: asdasdasd', 1, '[{"added": {}}]', 20, 1, '2024-12-27 13:33:07');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (8, '1', 'ProductImage object (1)', 3, '', 19, 1, '2024-12-27 13:43:36');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (9, '2', 'Muhammad Qodir', 1, '[{"added": {}}, {"added": {"name": "\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0430 \u0442\u043e\u0432\u0430\u0440\u0430", "object": "asdasd: adsadsasddaasd"}}, {"added": {"name": "\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442 \u0442\u043e\u0432\u0430\u0440\u0430", "object": "asdasd"}}, {"added": {"name": "\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430", "object": "ProductImage object (2)"}}]', 9, 1, '2024-12-27 13:47:49');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (10, '2', 'Muhammad Qodir', 2, '[{"changed": {"fields": ["\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)", "\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438", "\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 (EN)", "\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 (UZ)"]}}]', 9, 1, '2024-12-27 16:31:49');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (11, '6', 'Заказ 6 от вфывфыв фывфвы', 3, '', 17, 1, '2024-12-28 06:49:42');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (12, '5', 'Заказ 5 от вфывфыв фывфвы', 3, '', 17, 1, '2024-12-28 06:49:42');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (13, '4', 'Заказ 4 от вфывфыв фывфвы', 3, '', 17, 1, '2024-12-28 06:49:42');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (14, '3', 'Заказ 3 от вфывфыв фывфвы', 3, '', 17, 1, '2024-12-28 06:49:42');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (15, '2', 'Заказ 2 от вфывфыв фывфвы', 3, '', 17, 1, '2024-12-28 06:49:42');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (16, '1', 'Заказ 1 от вфывфыв фывфвы', 3, '', 17, 1, '2024-12-28 06:49:42');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (17, '2', 'Русский', 2, '[{"changed": {"fields": ["\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 (EN)", "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 06:55:08');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (18, '1', 'Русский язык', 2, '[{"changed": {"fields": ["\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a", "\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a (EN)", "\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a (UZ)"]}}]', 10, 1, '2024-12-28 07:05:18');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (19, '1', 'Русский язык', 2, '[{"changed": {"fields": ["\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435", "\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435 (EN)", "\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435 (UZ)"]}}]', 10, 1, '2024-12-28 07:05:34');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (20, '1', 'Русский', 2, '[{"changed": {"fields": ["\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 (UZ)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 7, 1, '2024-12-28 07:20:30');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (21, '1', 'Русский', 2, '[{"changed": {"fields": ["\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 (UZ)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 8, 1, '2024-12-28 07:21:06');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (22, '2', 'Русский', 2, '[{"changed": {"fields": ["\u041f\u043e\u043f\u0443\u043b\u044f\u0440\u043d\u044b\u0439 \u0442\u043e\u0432\u0430\u0440"]}}]', 9, 1, '2024-12-28 10:27:55');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (23, '30', 'Ammonium Chloride N:26%', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 11:25:27');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (24, '29', 'OLTIN SOP Sulphate of Potash K:50%', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 11:25:36');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (25, '28', 'OLTIN NPK Supra Red 10:10:40+TE', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 11:25:44');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (26, '27', 'OLTIN NPK Supra Yellow 13:40:13+TE', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 11:25:50');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (27, '26', 'OLTIN NPK Supra Green 18:18:18+TE', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 11:25:56');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (28, '25', 'OLTIN NPK Supra Blue 12:11:18(14)', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 11:26:06');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (29, '24', 'Ammoniated Single Superphosphate (ASSP)', 2, '[{"changed": {"fields": ["\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 11:26:11');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (30, '24', 'Ammoniated Single Superphosphate (ASSP)', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435"]}}]', 9, 1, '2024-12-28 11:26:20');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (31, '23', 'OLTIN CarboPhos Tez 42:5', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 11:26:42');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (32, '22', 'OLTIN Mini Amophos', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 11:26:49');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (33, '21', 'OLTIN NPK(S) 16:16:16(7)', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 11:26:57');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (34, '20', 'OLTIN NPK(S) 15:15:15(7)', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 11:27:09');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (35, '19', 'OLTIN NPK 20:10:10(10)', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 11:27:16');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (36, '18', 'OLTIN NPK(S) 10:20:20(5)', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 11:27:26');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (37, '17', 'OLTIN NPK 8:24:24', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 11:27:46');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (38, '16', 'OLTIN NPK 8:20:30', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 11:27:55');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (39, '15', 'OLTIN NPK(S) 12:24(8)', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 11:28:04');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (40, '14', 'OLTIN NPK(S) 7:22:14(5)', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 11:28:14');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (41, '13', 'OLTIN NPK(S) 5:17:10(7)', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 11:28:27');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (42, '13', 'OLTIN NPK(S) 5:17:10(7)', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435"]}}]', 9, 1, '2024-12-28 11:28:27');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (43, '18', 'Ammonium Chloride N:26%', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 12:25:36');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (44, '17', 'OLTIN SOP Sulphate of Potash K:50%', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 12:25:43');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (45, '16', 'OLTIN NPK Supra Red 10:10:40+TE', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 12:29:34');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (46, '15', 'OLTIN NPK Supra Yellow 13:40:13+TE', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 12:29:40');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (47, '14', 'OLTIN NPK Supra Green 18:18:18+TE', 2, '[{"changed": {"fields": ["\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}, {"added": {"name": "\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430", "object": "ProductImage object (1)"}}]', 9, 1, '2024-12-28 12:29:54');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (48, '14', 'OLTIN NPK Supra Green 18:18:18+TE', 2, '[{"added": {"name": "\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430", "object": "ProductImage object (2)"}}]', 9, 1, '2024-12-28 12:29:54');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (49, '14', 'OLTIN NPK Supra Green 18:18:18+TE', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435"]}}]', 9, 1, '2024-12-28 12:30:05');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (50, '13', 'OLTIN NPK Supra Blue 12:11:18(14)', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 12:30:12');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (51, '12', 'Ammoniated Single Superphosphate (ASSP)', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 12:30:19');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (52, '11', 'OLTIN CarboPhos Tez 42:5', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 12:30:26');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (53, '10', 'OLTIN Mini Amophos', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 12:30:32');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (54, '9', 'OLTIN NPK(S) 16:16:16(7)', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 12:31:46');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (55, '8', 'OLTIN NPK(S) 15:15:15(7)', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 12:31:56');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (56, '7', 'OLTIN NPK 20:10:10(10)', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 12:32:03');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (57, '6', 'OLTIN NPK(S) 10:20:20(5)', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 12:32:10');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (58, '5', 'OLTIN NPK 8:24:24', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 12:32:21');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (59, '4', 'OLTIN NPK 8:20:30', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 12:32:32');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (60, '3', 'OLTIN NPK(S) 12:24(8)', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 12:32:43');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (61, '2', 'OLTIN NPK(S) 7:22:14(5)', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 12:32:51');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (62, '1', 'OLTIN NPK(S) 5:17:10(7)', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (EN)", "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (UZ)"]}}]', 9, 1, '2024-12-28 12:33:00');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (63, '1', 'Удобрения', 2, '[{"changed": {"fields": ["\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435"]}}]', 8, 1, '2024-12-28 13:04:50');


-- Table structure for table `django_content_type`
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `app_label` VARCHAR(100) NOT NULL,
  `model` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table `django_content_type`
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (6, 'sessions', 'session');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (7, 'catalog', 'articlecategory');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (8, 'catalog', 'productcategory');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (9, 'catalog', 'product');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (10, 'catalog', 'article');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (11, 'catalog', 'contactmessage');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (12, 'catalog', 'productrequestitem');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (13, 'catalog', 'productrequest');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (14, 'catalog', 'cartitem');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (15, 'catalog', 'cart');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (16, 'catalog', 'orderitem');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (17, 'catalog', 'order');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (18, 'catalog', 'productdocument');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (19, 'catalog', 'productimage');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (20, 'catalog', 'productspecification');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (21, 'telegram_bot', 'telegramnotification');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (22, 'telegram_bot', 'telegramsettings');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (23, 'contacts', 'contactmessage');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (24, 'notifications', 'notification');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (25, 'notifications', 'telegramsettings');


-- Table structure for table `auth_permission`
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `content_type_id` INT NOT NULL,
  `codename` VARCHAR(100) NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table `auth_permission`
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (1, 1, 'add_logentry', 'Can add log entry');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (2, 1, 'change_logentry', 'Can change log entry');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (3, 1, 'delete_logentry', 'Can delete log entry');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (4, 1, 'view_logentry', 'Can view log entry');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (5, 2, 'add_permission', 'Can add permission');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (6, 2, 'change_permission', 'Can change permission');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (7, 2, 'delete_permission', 'Can delete permission');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (8, 2, 'view_permission', 'Can view permission');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (9, 3, 'add_group', 'Can add group');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (10, 3, 'change_group', 'Can change group');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (11, 3, 'delete_group', 'Can delete group');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (12, 3, 'view_group', 'Can view group');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (13, 4, 'add_user', 'Can add user');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (14, 4, 'change_user', 'Can change user');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (15, 4, 'delete_user', 'Can delete user');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (16, 4, 'view_user', 'Can view user');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (17, 5, 'add_contenttype', 'Can add content type');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (18, 5, 'change_contenttype', 'Can change content type');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (19, 5, 'delete_contenttype', 'Can delete content type');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (20, 5, 'view_contenttype', 'Can view content type');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (21, 6, 'add_session', 'Can add session');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (22, 6, 'change_session', 'Can change session');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (23, 6, 'delete_session', 'Can delete session');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (24, 6, 'view_session', 'Can view session');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (25, 7, 'add_articlecategory', 'Can add Категория статей');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (26, 7, 'change_articlecategory', 'Can change Категория статей');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (27, 7, 'delete_articlecategory', 'Can delete Категория статей');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (28, 7, 'view_articlecategory', 'Can view Категория статей');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (29, 8, 'add_productcategory', 'Can add Категория товаров');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (30, 8, 'change_productcategory', 'Can change Категория товаров');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (31, 8, 'delete_productcategory', 'Can delete Категория товаров');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (32, 8, 'view_productcategory', 'Can view Категория товаров');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (33, 9, 'add_product', 'Can add Товар');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (34, 9, 'change_product', 'Can change Товар');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (35, 9, 'delete_product', 'Can delete Товар');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (36, 9, 'view_product', 'Can view Товар');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (37, 10, 'add_article', 'Can add Статья');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (38, 10, 'change_article', 'Can change Статья');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (39, 10, 'delete_article', 'Can delete Статья');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (40, 10, 'view_article', 'Can view Статья');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (41, 11, 'add_contactmessage', 'Can add Сообщение');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (42, 11, 'change_contactmessage', 'Can change Сообщение');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (43, 11, 'delete_contactmessage', 'Can delete Сообщение');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (44, 11, 'view_contactmessage', 'Can view Сообщение');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (45, 12, 'add_productrequestitem', 'Can add Товар в заявке');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (46, 12, 'change_productrequestitem', 'Can change Товар в заявке');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (47, 12, 'delete_productrequestitem', 'Can delete Товар в заявке');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (48, 12, 'view_productrequestitem', 'Can view Товар в заявке');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (49, 13, 'add_productrequest', 'Can add Заявка');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (50, 13, 'change_productrequest', 'Can change Заявка');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (51, 13, 'delete_productrequest', 'Can delete Заявка');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (52, 13, 'view_productrequest', 'Can view Заявка');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (53, 14, 'add_cartitem', 'Can add Товар в корзине');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (54, 14, 'change_cartitem', 'Can change Товар в корзине');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (55, 14, 'delete_cartitem', 'Can delete Товар в корзине');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (56, 14, 'view_cartitem', 'Can view Товар в корзине');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (57, 15, 'add_cart', 'Can add Корзина');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (58, 15, 'change_cart', 'Can change Корзина');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (59, 15, 'delete_cart', 'Can delete Корзина');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (60, 15, 'view_cart', 'Can view Корзина');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (61, 16, 'add_orderitem', 'Can add Товар в заказе');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (62, 16, 'change_orderitem', 'Can change Товар в заказе');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (63, 16, 'delete_orderitem', 'Can delete Товар в заказе');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (64, 16, 'view_orderitem', 'Can view Товар в заказе');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (65, 17, 'add_order', 'Can add Заказ');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (66, 17, 'change_order', 'Can change Заказ');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (67, 17, 'delete_order', 'Can delete Заказ');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (68, 17, 'view_order', 'Can view Заказ');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (69, 18, 'add_productdocument', 'Can add Документ товара');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (70, 18, 'change_productdocument', 'Can change Документ товара');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (71, 18, 'delete_productdocument', 'Can delete Документ товара');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (72, 18, 'view_productdocument', 'Can view Документ товара');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (73, 19, 'add_productimage', 'Can add Изображение товара');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (74, 19, 'change_productimage', 'Can change Изображение товара');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (75, 19, 'delete_productimage', 'Can delete Изображение товара');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (76, 19, 'view_productimage', 'Can view Изображение товара');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (77, 20, 'add_productspecification', 'Can add Характеристика товара');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (78, 20, 'change_productspecification', 'Can change Характеристика товара');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (79, 20, 'delete_productspecification', 'Can delete Характеристика товара');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (80, 20, 'view_productspecification', 'Can view Характеристика товара');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (81, 21, 'add_telegramnotification', 'Can add Telegram Notification');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (82, 21, 'change_telegramnotification', 'Can change Telegram Notification');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (83, 21, 'delete_telegramnotification', 'Can delete Telegram Notification');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (84, 21, 'view_telegramnotification', 'Can view Telegram Notification');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (85, 22, 'add_telegramsettings', 'Can add Telegram Settings');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (86, 22, 'change_telegramsettings', 'Can change Telegram Settings');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (87, 22, 'delete_telegramsettings', 'Can delete Telegram Settings');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (88, 22, 'view_telegramsettings', 'Can view Telegram Settings');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (89, 23, 'add_contactmessage', 'Can add Contact Message');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (90, 23, 'change_contactmessage', 'Can change Contact Message');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (91, 23, 'delete_contactmessage', 'Can delete Contact Message');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (92, 23, 'view_contactmessage', 'Can view Contact Message');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (93, 24, 'add_notification', 'Can add Уведомление');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (94, 24, 'change_notification', 'Can change Уведомление');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (95, 24, 'delete_notification', 'Can delete Уведомление');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (96, 24, 'view_notification', 'Can view Уведомление');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (97, 25, 'add_telegramsettings', 'Can add Настройки Telegram');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (98, 25, 'change_telegramsettings', 'Can change Настройки Telegram');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (99, 25, 'delete_telegramsettings', 'Can delete Настройки Telegram');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (100, 25, 'view_telegramsettings', 'Can view Настройки Telegram');


-- Table structure for table `auth_group`
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- Table structure for table `auth_user`
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `password` VARCHAR(128) NOT NULL,
  `last_login` DATETIME,
  `is_superuser` TEXT NOT NULL,
  `username` VARCHAR(150) NOT NULL,
  `last_name` VARCHAR(150) NOT NULL,
  `email` VARCHAR(254) NOT NULL,
  `is_staff` TEXT NOT NULL,
  `is_active` TEXT NOT NULL,
  `date_joined` DATETIME NOT NULL,
  `first_name` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table `auth_user`
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `first_name`) VALUES (1, 'pbkdf2_sha256$600000$aA49BiUj7GQu3OCJU0BtNk$WGnc3yCuUQmX5yG99ImG9UQum20jBvVWWS8T9lQ/k/0=', '2024-12-27 10:20:52', 1, 'admin', '', 'admin@example.com', 1, 1, '2024-12-27 10:20:39', '');


-- Table structure for table `django_session`
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` VARCHAR(40) NOT NULL,
  `session_data` TEXT NOT NULL,
  `expire_date` DATETIME NOT NULL,
  PRIMARY KEY (`session_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table `django_session`
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES ('qhixoowxre18bo8b6uz792dpu9c4oi2u', '.eJxVjssOgyAQRf-FtSGAKOCy-36DGV5Ka7RFWDTGfy8aF-0sZjH3zMndUA85jX1eXeyDRR2iqPq9aTBPNx-BfcA8LNgsc4pB4wPBV7ri-2LddLvYP8EI61i-Gy6sllxJ1pBWauEBKDek8R6s8oIIMBpqrgmTyltGW82Ml6ZuHBGu9rpIDcR0dqQVmkqXDIMr5pivDHUbYurY7wxzCulzoq8YzMFRScpgQtC-719oCE9A:1tRWs5:ZXEwOx4LerqIoeBL-IkRpxc5l7tbzuNW7WW_dgNjQME', '2025-01-11 13:28:49');


-- Table structure for table `telegram_bot_telegramnotification`
DROP TABLE IF EXISTS `telegram_bot_telegramnotification`;
CREATE TABLE `telegram_bot_telegramnotification` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `type` VARCHAR(20) NOT NULL,
  `object_id` INT NOT NULL,
  `is_read` TEXT NOT NULL,
  `sent_at` DATETIME NOT NULL,
  `read_at` DATETIME,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table `telegram_bot_telegramnotification`
INSERT INTO `telegram_bot_telegramnotification` (`id`, `type`, `object_id`, `is_read`, `sent_at`, `read_at`) VALUES (1, 'message', 2, 1, '2024-12-28 10:55:53', NULL);
INSERT INTO `telegram_bot_telegramnotification` (`id`, `type`, `object_id`, `is_read`, `sent_at`, `read_at`) VALUES (2, 'order', 7, 1, '2024-12-28 10:55:58', NULL);
INSERT INTO `telegram_bot_telegramnotification` (`id`, `type`, `object_id`, `is_read`, `sent_at`, `read_at`) VALUES (3, 'order', 8, 1, '2024-12-28 11:53:26', NULL);


-- Table structure for table `telegram_bot_telegramsettings`
DROP TABLE IF EXISTS `telegram_bot_telegramsettings`;
CREATE TABLE `telegram_bot_telegramsettings` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `bot_token` VARCHAR(255) NOT NULL,
  `admin_chat_id` VARCHAR(255) NOT NULL,
  `is_active` TEXT NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table `telegram_bot_telegramsettings`
INSERT INTO `telegram_bot_telegramsettings` (`id`, `bot_token`, `admin_chat_id`, `is_active`, `created_at`, `updated_at`) VALUES (1, '7698230012:AAGudGNHAwyxeGhIRbLewF-zPf36DqowFJ0', '1516663193', 1, '2024-12-28 08:46:36', '2024-12-28 08:46:36');


-- Table structure for table `contacts_contactmessage`
DROP TABLE IF EXISTS `contacts_contactmessage`;
CREATE TABLE `contacts_contactmessage` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `email` VARCHAR(254) NOT NULL,
  `phone` VARCHAR(20) NOT NULL,
  `subject` VARCHAR(200) NOT NULL,
  `message` TEXT NOT NULL,
  `created_at` DATETIME NOT NULL,
  `is_read` TEXT NOT NULL,
  `is_processed` TEXT NOT NULL,
  `read_at` DATETIME,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table `contacts_contactmessage`
INSERT INTO `contacts_contactmessage` (`id`, `name`, `email`, `phone`, `subject`, `message`, `created_at`, `is_read`, `is_processed`, `read_at`) VALUES (1, 'Test User', 'test@example.com', '', 'Test Message', 'This is a test message', '2024-12-28 09:02:27', 0, 0, NULL);
INSERT INTO `contacts_contactmessage` (`id`, `name`, `email`, `phone`, `subject`, `message`, `created_at`, `is_read`, `is_processed`, `read_at`) VALUES (2, 'Kader Ahmadjonov', 'mukhammadqodir4047@gmail.com', '8999963629', 'Codeium: Your Windsurf version is too old. Install the latest version then restart. For help, contact us at https://codeium.com/support.', 'фывфыввфыфвы', '2024-12-28 10:34:41', 1, 0, '2024-12-28 10:55:53');
INSERT INTO `contacts_contactmessage` (`id`, `name`, `email`, `phone`, `subject`, `message`, `created_at`, `is_read`, `is_processed`, `read_at`) VALUES (3, 'Kader Ahmadjonov', 'mukhammadqodir4047@gmail.com', '8999963629', 'Codeium: Your Windsurf version is too old. Install the latest version then restart. For help, contact us at https://codeium.com/support.', 'asdasd', '2024-12-28 11:53:59', 0, 0, NULL);
INSERT INTO `contacts_contactmessage` (`id`, `name`, `email`, `phone`, `subject`, `message`, `created_at`, `is_read`, `is_processed`, `read_at`) VALUES (4, 'Kader Ahmadjonov', 'mukhammadqodir4047@gmail.com', '8999963629', 'Sign in failed: invalid auth token', 'фывфвыфыв', '2024-12-28 13:21:17', 0, 0, NULL);


-- Table structure for table `notifications_notification`
DROP TABLE IF EXISTS `notifications_notification`;
CREATE TABLE `notifications_notification` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `type` VARCHAR(20) NOT NULL,
  `title` VARCHAR(255) NOT NULL,
  `message` TEXT NOT NULL,
  `sent` TEXT NOT NULL,
  `error` TEXT,
  `created_at` DATETIME NOT NULL,
  `sent_at` DATETIME,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table `notifications_notification`
INSERT INTO `notifications_notification` (`id`, `type`, `title`, `message`, `sent`, `error`, `created_at`, `sent_at`) VALUES (1, 'message', 'Новое сообщение от Kader Ahmadjonov', '
📨 <b>Новое сообщение</b>

👤 <b>От:</b>
Имя: Kader Ahmadjonov
Email: mukhammadqodir4047@gmail.com
Телефон: 8999963629

📝 <b>Тема:</b> Codeium: Your Windsurf version is too old. Install the latest version then restart. For help, contact us at https://codeium.com/support.

💬 <b>Сообщение:</b>
asdasd
', 1, NULL, '2024-12-28 11:53:59', '2024-12-28 11:54:00');
INSERT INTO `notifications_notification` (`id`, `type`, `title`, `message`, `sent`, `error`, `created_at`, `sent_at`) VALUES (2, 'order', 'Новый заказ #13', '
🛍️ <b>Новый заказ #13</b>

👤 <b>Клиент:</b>
Имя: Kader Ahmadjonov
Телефон: 8999963629
Email: mukhammadqodir4047@gmail.com

📦 <b>Товары:</b>
- OLTIN CarboPhos Tez 42:5 x 1 = 140,000.00 UZS

💰 <b>Итого:</b> 140,000.00 UZS

💬 <b>Комментарий:</b>
asdasdasd', 1, NULL, '2024-12-28 11:54:09', '2024-12-28 11:54:10');
INSERT INTO `notifications_notification` (`id`, `type`, `title`, `message`, `sent`, `error`, `created_at`, `sent_at`) VALUES (3, 'order', 'Новый заказ #1', '
🛍️ <b>Новый заказ #1</b>

👤 <b>Клиент:</b>
Имя: фывфыв фвыфывфвы
Телефон: 8999963629
Email: mukhammadqodir4047@gmail.com

📦 <b>Товары:</b>
- OLTIN NPK(S) 15:15:15(7) x 1 = 116,000.00 UZS
- OLTIN NPK(S) 16:16:16(7) x 1 = 117,000.00 UZS
- OLTIN SOP Sulphate of Potash K:50% x 1 = 180,000.00 UZS
- Ammonium Chloride N:26% x 2 = 290,000.00 UZS

💰 <b>Итого:</b> 703,000.00 UZS

💬 <b>Комментарий:</b>
фывфвыфывыв', 1, NULL, '2024-12-28 12:56:41', '2024-12-28 12:56:42');
INSERT INTO `notifications_notification` (`id`, `type`, `title`, `message`, `sent`, `error`, `created_at`, `sent_at`) VALUES (4, 'order', 'Новый заказ #2', '
🛍️ <b>Новый заказ #2</b>

👤 <b>Клиент:</b>
Имя: фывфывфыв Ahmadjonov
Телефон: фывфывфыв
Email: mukhammadqodir4047@gmail.com

📦 <b>Товары:</b>
- OLTIN NPK Supra Red 10:10:40+TE x 6 = 1,050,000.00 UZS
- OLTIN SOP Sulphate of Potash K:50% x 4 = 720,000.00 UZS

💰 <b>Итого:</b> 1,770,000.00 UZS

💬 <b>Комментарий:</b>
фывфывфыв', 1, NULL, '2024-12-28 13:21:04', '2024-12-28 13:21:05');
INSERT INTO `notifications_notification` (`id`, `type`, `title`, `message`, `sent`, `error`, `created_at`, `sent_at`) VALUES (5, 'message', 'Новое сообщение от Kader Ahmadjonov', '
📨 <b>Новое сообщение</b>

👤 <b>От:</b>
Имя: Kader Ahmadjonov
Email: mukhammadqodir4047@gmail.com
Телефон: 8999963629

📝 <b>Тема:</b> Sign in failed: invalid auth token

💬 <b>Сообщение:</b>
фывфвыфыв
', 1, NULL, '2024-12-28 13:21:17', '2024-12-28 13:21:18');


-- Table structure for table `notifications_telegramsettings`
DROP TABLE IF EXISTS `notifications_telegramsettings`;
CREATE TABLE `notifications_telegramsettings` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `bot_token` VARCHAR(255) NOT NULL,
  `chat_id` VARCHAR(255) NOT NULL,
  `enabled` TEXT NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table `notifications_telegramsettings`
INSERT INTO `notifications_telegramsettings` (`id`, `bot_token`, `chat_id`, `enabled`, `created_at`, `updated_at`) VALUES (1, '7698230012:AAGudGNHAwyxeGhIRbLewF-zPf36DqowFJ0', '1516663193', 1, '2024-12-28 11:51:21', '2024-12-28 11:51:21');


-- Table structure for table `catalog_articlecategory`
DROP TABLE IF EXISTS `catalog_articlecategory`;
CREATE TABLE `catalog_articlecategory` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(200) NOT NULL,
  `name_en` VARCHAR(200) NOT NULL,
  `name_uz` VARCHAR(200) NOT NULL,
  `slug` VARCHAR(200) NOT NULL,
  `description` TEXT NOT NULL,
  `description_en` TEXT NOT NULL,
  `description_uz` TEXT NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table `catalog_articlecategory`
INSERT INTO `catalog_articlecategory` (`id`, `name`, `name_en`, `name_uz`, `slug`, `description`, `description_en`, `description_uz`, `created_at`, `updated_at`) VALUES (7, 'Новости компании', 'Company News', 'Kompaniya yangiliklari', 'news', '', '', '', '2024-12-28 12:16:41', '2024-12-28 12:16:41');
INSERT INTO `catalog_articlecategory` (`id`, `name`, `name_en`, `name_uz`, `slug`, `description`, `description_en`, `description_uz`, `created_at`, `updated_at`) VALUES (8, 'Статьи', 'Articles', 'Maqolalar', 'articles', '', '', '', '2024-12-28 12:16:41', '2024-12-28 12:16:41');
INSERT INTO `catalog_articlecategory` (`id`, `name`, `name_en`, `name_uz`, `slug`, `description`, `description_en`, `description_uz`, `created_at`, `updated_at`) VALUES (9, 'Советы по применению', 'Usage Tips', 'Foydalanish bo''yicha maslahatlar', 'tips', '', '', '', '2024-12-28 12:16:41', '2024-12-28 12:16:41');


-- Table structure for table `catalog_cart`
DROP TABLE IF EXISTS `catalog_cart`;
CREATE TABLE `catalog_cart` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `session_key` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table `catalog_cart`
INSERT INTO `catalog_cart` (`id`, `session_key`, `created_at`, `updated_at`) VALUES (1, 'qhixoowxre18bo8b6uz792dpu9c4oi2u', '2024-12-28 12:10:13', '2024-12-28 12:10:13');


-- Table structure for table `catalog_order`
DROP TABLE IF EXISTS `catalog_order`;
CREATE TABLE `catalog_order` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `email` VARCHAR(254) NOT NULL,
  `phone` VARCHAR(20) NOT NULL,
  `address` TEXT NOT NULL,
  `status` VARCHAR(20) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `comment` TEXT NOT NULL,
  `user_id` INT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table `catalog_order`
INSERT INTO `catalog_order` (`id`, `first_name`, `last_name`, `email`, `phone`, `address`, `status`, `created_at`, `updated_at`, `comment`, `user_id`) VALUES (1, 'фывфыв', 'фвыфывфвы', 'mukhammadqodir4047@gmail.com', '8999963629', 'Uvaysiy MFY, Nurli oy ko''chasi
33', 'new', '2024-12-28 12:56:41', '2024-12-28 12:56:41', 'фывфвыфывыв', 1);
INSERT INTO `catalog_order` (`id`, `first_name`, `last_name`, `email`, `phone`, `address`, `status`, `created_at`, `updated_at`, `comment`, `user_id`) VALUES (2, 'фывфывфыв', 'Ahmadjonov', 'mukhammadqodir4047@gmail.com', 'фывфывфыв', 'Nurli oy 303', 'new', '2024-12-28 13:21:04', '2024-12-28 13:21:04', 'фывфывфыв', 1);


-- Table structure for table `catalog_productspecification`
DROP TABLE IF EXISTS `catalog_productspecification`;
CREATE TABLE `catalog_productspecification` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `value` VARCHAR(255) NOT NULL,
  `product_id` TEXT NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- Table structure for table `catalog_productimage`
DROP TABLE IF EXISTS `catalog_productimage`;
CREATE TABLE `catalog_productimage` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `image` VARCHAR(100) NOT NULL,
  `product_id` TEXT NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table `catalog_productimage`
INSERT INTO `catalog_productimage` (`id`, `image`, `product_id`) VALUES (1, 'products/images/SUPRA_GREEN_Kddb374.png', 14);
INSERT INTO `catalog_productimage` (`id`, `image`, `product_id`) VALUES (2, 'products/images/SUPRA_GREEN_3JXQjGN.png', 14);


-- Table structure for table `catalog_productdocument`
DROP TABLE IF EXISTS `catalog_productdocument`;
CREATE TABLE `catalog_productdocument` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(100) NOT NULL,
  `file` VARCHAR(100) NOT NULL,
  `product_id` TEXT NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- Table structure for table `catalog_productcategory`
DROP TABLE IF EXISTS `catalog_productcategory`;
CREATE TABLE `catalog_productcategory` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(200) NOT NULL,
  `name_en` VARCHAR(200) NOT NULL,
  `name_uz` VARCHAR(200) NOT NULL,
  `slug` VARCHAR(200) NOT NULL,
  `description` TEXT NOT NULL,
  `description_en` TEXT NOT NULL,
  `description_uz` TEXT NOT NULL,
  `image` VARCHAR(100) NOT NULL,
  `icon_class` VARCHAR(50) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `parent_id` TEXT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table `catalog_productcategory`
INSERT INTO `catalog_productcategory` (`id`, `name`, `name_en`, `name_uz`, `slug`, `description`, `description_en`, `description_uz`, `image`, `icon_class`, `created_at`, `updated_at`, `parent_id`) VALUES (1, 'Удобрения', 'Fertilizers', 'O''g''itlar', 'fertilizers', 'Широкий ассортимент высококачественных удобрений для различных культур', 'Wide range of high-quality fertilizers for various crops', 'Turli ekinlar uchun yuqori sifatli o''g''itlarning keng assortimenti', 'categories/SUPRA_GREEN.png', '', '2024-12-28 12:14:12', '2024-12-28 13:04:50', NULL);
INSERT INTO `catalog_productcategory` (`id`, `name`, `name_en`, `name_uz`, `slug`, `description`, `description_en`, `description_uz`, `image`, `icon_class`, `created_at`, `updated_at`, `parent_id`) VALUES (2, 'Удобрения с макроэлементами (NPK и S)', 'Macronutrient Fertilizers (NPK and S)', 'Makroelementli o''g''itlar (NPK va S)', 'macro', 'Удобрения, содержащие основные питательные элементы: азот, фосфор, калий и серу', 'Fertilizers containing essential nutrients: nitrogen, phosphorus, potassium, and sulfur', 'Asosiy ozuqa elementlarini o''z ichiga olgan o''g''itlar: azot, fosfor, kaliy va oltingugurt', '', '', '2024-12-28 12:14:12', '2024-12-28 12:14:12', 1);
INSERT INTO `catalog_productcategory` (`id`, `name`, `name_en`, `name_uz`, `slug`, `description`, `description_en`, `description_uz`, `image`, `icon_class`, `created_at`, `updated_at`, `parent_id`) VALUES (3, 'Комплексные минеральные удобрения', 'Complex Mineral Fertilizers', 'Kompleks mineral o''g''itlar', 'complex', 'Сбалансированные комплексные удобрения для различных типов почв и культур', 'Balanced complex fertilizers for various soil types and crops', 'Turli tuproq va ekinlar uchun muvozanatlashtirilgan kompleks o''g''itlar', '', '', '2024-12-28 12:14:12', '2024-12-28 12:14:12', 1);
INSERT INTO `catalog_productcategory` (`id`, `name`, `name_en`, `name_uz`, `slug`, `description`, `description_en`, `description_uz`, `image`, `icon_class`, `created_at`, `updated_at`, `parent_id`) VALUES (4, 'Водорастворимые удобрения', 'Water-Soluble Fertilizers', 'Suvda eruvchan o''g''itlar', 'water', 'Полностью растворимые удобрения для капельного полива и листовых подкормок', 'Fully soluble fertilizers for drip irrigation and foliar feeding', 'Tomchilab sug''orish va bargdan oziqlantirish uchun to''liq eruvchan o''g''itlar', '', '', '2024-12-28 12:14:12', '2024-12-28 12:14:12', 1);
INSERT INTO `catalog_productcategory` (`id`, `name`, `name_en`, `name_uz`, `slug`, `description`, `description_en`, `description_uz`, `image`, `icon_class`, `created_at`, `updated_at`, `parent_id`) VALUES (5, 'Специальные удобрения', 'Special Fertilizers', 'Maxsus o''g''itlar', 'special', 'Специализированные удобрения для особых потребностей растений', 'Specialized fertilizers for specific plant needs', 'O''simliklarning maxsus ehtiyojlari uchun ixtisoslashtirilgan o''g''itlar', '', '', '2024-12-28 12:14:12', '2024-12-28 12:14:12', 1);


-- Table structure for table `catalog_product`
DROP TABLE IF EXISTS `catalog_product`;
CREATE TABLE `catalog_product` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(200) NOT NULL,
  `name_en` VARCHAR(200) NOT NULL,
  `name_uz` VARCHAR(200) NOT NULL,
  `description` TEXT NOT NULL,
  `description_en` TEXT NOT NULL,
  `description_uz` TEXT NOT NULL,
  `specifications` TEXT,
  `specifications_en` TEXT,
  `specifications_uz` TEXT,
  `slug` VARCHAR(200) NOT NULL,
  `price` TEXT NOT NULL,
  `stock` INT NOT NULL,
  `available` TEXT NOT NULL,
  `is_popular` TEXT NOT NULL,
  `image` VARCHAR(100),
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `category_id` TEXT NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table `catalog_product`
INSERT INTO `catalog_product` (`id`, `name`, `name_en`, `name_uz`, `description`, `description_en`, `description_uz`, `specifications`, `specifications_en`, `specifications_uz`, `slug`, `price`, `stock`, `available`, `is_popular`, `image`, `created_at`, `updated_at`, `category_id`) VALUES (1, 'OLTIN NPK(S) 5:17:10(7)', 'OLTIN NPK(S) 5:17:10(7)', 'OLTIN NPK(S) 5:17:10(7)', '<p>Комплексное удобрение с оптимальным балансом макроэлементов. Состав: - Азот (N): 5% - Фосфор (P): 17% - Калий (K): 10% - Сера (S): 7% Особенности: - Все элементы представлены в форме, доступной для быстрого усвоения растениями - Высокая водорастворимость фосфора обеспечивает быстрое развитие корневой системы - Сбалансированное содержание калия улучшает вкус и качество продукции - Сера способствует синтезу аминокислот, улучшая здоровье растений Рекомендуемое использование: - Подходит для картофеля, лука, чеснока, кукурузы и хлопка - Идеально для весеннего и осеннего внесения в грунт</p>', '<p>Complex fertilizer with optimal balance of macronutrients. Composition: - Nitrogen (N): 5% - Phosphorus (P): 17% - Potassium (K): 10% - Sulfur (S): 7% Features: - All elements are in a form readily available for plant uptake - High water solubility of phosphorus ensures rapid root system development - Balanced potassium content improves taste and product quality - Sulfur promotes amino acid synthesis, improving plant health Recommended use: - Suitable for potatoes, onions, garlic, corn and cotton - Perfect for spring and autumn soil application</p>', '<p>Makroelementlarning optimal muvozanatiga ega kompleks o&#39;g&#39;it. Tarkibi: - Azot (N): 5% - Fosfor (P): 17% - Kaliy (K): 10% - Oltingugurt (S): 7% Xususiyatlari: - Barcha elementlar o&#39;simliklar tomonidan tez o&#39;zlashtirilishi mumkin bo&#39;lgan shaklda - Fosforning yuqori suvda eruvchanligi ildiz tizimining tez rivojlanishini ta&#39;minlaydi - Kaliyning muvozanatlashgan tarkibi mahsulot ta&#39;mi va sifatini yaxshilaydi - Oltingugurt aminokislotalar sinteziga yordam beradi, o&#39;simliklar salomatligini yaxshilaydi Tavsiya etilgan foydalanish: - Kartoshka, piyoz, sarimsoq, makkajo&#39;xori va g&#39;o&#39;za uchun mos keladi - Bahorda va kuzda tuproqqa kiritish uchun ideal</p>', '', '', '', 'oltin-npk-s-5-17-10-7', 100000, 100, 1, 0, 'products/images/NP_5_17_10_auZjdZp.png', '2024-12-28 12:14:12', '2024-12-28 12:33:00', 2);
INSERT INTO `catalog_product` (`id`, `name`, `name_en`, `name_uz`, `description`, `description_en`, `description_uz`, `specifications`, `specifications_en`, `specifications_uz`, `slug`, `price`, `stock`, `available`, `is_popular`, `image`, `created_at`, `updated_at`, `category_id`) VALUES (2, 'OLTIN NPK(S) 7:22:14(5)', 'OLTIN NPK(S) 7:22:14(5)', 'OLTIN NPK(S) 7:22:14(5)', '<p>Комплексное удобрение для улучшения корневой системы. Состав: - Азот (N): 7% - Фосфор (P): 22% - Калий (K): 14% - Сера (S): 5% Особенности: - Низкое содержание азота помогает избежать избытка зелёной массы в ущерб плодоношению - Высокий уровень фосфора способствует росту корневой системы, особенно в ранних стадиях развития - Сбалансированное содержание серы и калия улучшает устойчивость растений к болезням Рекомендуемое использование: - Подходит для многолетних трав, сахарной свеклы и картофеля - Эффективно для осеннего внесения на корнеплоды</p>', '<p>Complex fertilizer for root system improvement. Composition: - Nitrogen (N): 7% - Phosphorus (P): 22% - Potassium (K): 14% - Sulfur (S): 5% Features: - Low nitrogen content helps avoid excess green mass without compromising fruiting - High phosphorus level promotes root system growth, especially in early development stages - Balanced sulfur and potassium content improves plant disease resistance Recommended use: - Suitable for perennial grasses, sugar beets and potatoes - Effective for autumn application on root crops</p>', '<p>Ildiz tizimini yaxshilash uchun kompleks o&#39;g&#39;it. Tarkibi: - Azot (N): 7% - Fosfor (P): 22% - Kaliy (K): 14% - Oltingugurt (S): 5% Xususiyatlari: - Azotning past miqdori meva tugishiga zarar yetkazmagan holda yashil massaning ortiqcha bo&#39;lishini oldini oladi - Fosforning yuqori darajasi, ayniqsa rivojlanishning dastlabki bosqichlarida ildiz tizimining o&#39;sishiga yordam beradi - Oltingugurt va kaliyning muvozanatlashgan tarkibi o&#39;simliklarning kasalliklarga chidamliligini oshiradi Tavsiya etilgan foydalanish: - Ko&#39;p yillik o&#39;tlar, qand lavlagi va kartoshka uchun mos keladi - Ildizmevalilar uchun kuzgi kiritish uchun samarali</p>', '', '', '', 'oltin-npk-s-7-22-14-5', 110000, 150, 1, 0, 'products/images/NPKS_7_22_145_nfhkjQ0.png', '2024-12-28 12:14:12', '2024-12-28 12:32:51', 2);
INSERT INTO `catalog_product` (`id`, `name`, `name_en`, `name_uz`, `description`, `description_en`, `description_uz`, `specifications`, `specifications_en`, `specifications_uz`, `slug`, `price`, `stock`, `available`, `is_popular`, `image`, `created_at`, `updated_at`, `category_id`) VALUES (3, 'OLTIN NPK(S) 12:24(8)', 'OLTIN NPK(S) 12:24(8)', 'OLTIN NPK(S) 12:24(8)', '<p>Комплексное удобрение с высоким содержанием фосфора. Состав: - Азот (N): 12% - Фосфор (P): 24% - Сера (S): 8% Особенности: - Богатый источник фосфора для улучшенного роста корней и повышения урожайности - Высокое содержание азота способствует быстрому росту вегетативной массы - Сера улучшает фотосинтез и образование хлорофилла Рекомендуемое использование: - Для пшеницы, овощей и фруктов - Применяется как основное удобрение при подготовке почвы</p>', '<p>Complex fertilizer with high phosphorus content. Composition: - Nitrogen (N): 12% - Phosphorus (P): 24% - Sulfur (S): 8% Features: - Rich source of phosphorus for improved root growth and increased yield - High nitrogen content promotes rapid vegetative growth - Sulfur improves photosynthesis and chlorophyll formation Recommended use: - For wheat, vegetables and fruits - Applied as a base fertilizer in soil preparation</p>', '<p>Fosfor miqdori yuqori bo&#39;lgan kompleks o&#39;g&#39;it. Tarkibi: - Azot (N): 12% - Fosfor (P): 24% - Oltingugurt (S): 8% Xususiyatlari: - Ildizlarning yaxshilangan o&#39;sishi va hosildorlikni oshirish uchun fosforning boy manbai - Azotning yuqori miqdori vegetativ massaning tez o&#39;sishiga yordam beradi - Oltingugurt fotosintez va xlorofill hosil bo&#39;lishini yaxshilaydi Tavsiya etilgan foydalanish: - Bug&#39;doy, sabzavotlar va mevalar uchun - Tuproqni tayyorlashda asosiy o&#39;g&#39;it sifatida qo&#39;llaniladi</p>', '', '', '', 'oltin-npk-s-12-24-8', 115000, 130, 1, 0, 'products/images/NPS_12_248_PnA67he.png', '2024-12-28 12:14:12', '2024-12-28 12:32:43', 2);
INSERT INTO `catalog_product` (`id`, `name`, `name_en`, `name_uz`, `description`, `description_en`, `description_uz`, `specifications`, `specifications_en`, `specifications_uz`, `slug`, `price`, `stock`, `available`, `is_popular`, `image`, `created_at`, `updated_at`, `category_id`) VALUES (4, 'OLTIN NPK 8:20:30', 'OLTIN NPK 8:20:30', 'OLTIN NPK 8:20:30', '<p>Комплексное удобрение с повышенным содержанием калия. Состав: - Азот (N): 8% - Фосфор (P): 20% - Калий (K): 30% Особенности: - Высокое содержание калия улучшает устойчивость растений к засухе и болезням - Подходит для всех видов культур, особенно для корнеплодов и овощей - Эффективно поддерживает рост и развитие растений в любых климатических условиях Рекомендуемое использование: - Применяется перед посевом или в начале вегетации - Идеально для культур с высокой потребностью в калии</p>', '<p>Complex fertilizer with increased potassium content. Composition: - Nitrogen (N): 8% - Phosphorus (P): 20% - Potassium (K): 30% Features: - High potassium content improves plant resistance to drought and diseases - Suitable for all types of crops, especially root vegetables - Effectively supports plant growth and development in any climatic conditions Recommended use: - Applied before sowing or at the beginning of vegetation - Perfect for crops with high potassium demand</p>', '<p>Kaliy miqdori yuqori bo&#39;lgan kompleks o&#39;g&#39;it. Tarkibi: - Azot (N): 8% - Fosfor (P): 20% - Kaliy (K): 30% Xususiyatlari: - Kaliyning yuqori miqdori o&#39;simliklarning qurg&#39;oqchilik va kasalliklarga chidamliligini oshiradi - Barcha turdagi ekinlar, ayniqsa ildizmevalar va sabzavotlar uchun mos keladi - Har qanday iqlim sharoitida o&#39;simliklarning o&#39;sishi va rivojlanishini samarali qo&#39;llab-quvvatlaydi Tavsiya etilgan foydalanish: - Ekishdan oldin yoki vegetatsiya boshida qo&#39;llaniladi - Kaliyga bo&#39;lgan ehtiyoji yuqori bo&#39;lgan ekinlar uchun ideal</p>', '', '', '', 'oltin-npk-8-20-30', 120000, 140, 1, 0, 'products/images/NPK_8_20_30_idINNfU.png', '2024-12-28 12:14:12', '2024-12-28 12:32:32', 2);
INSERT INTO `catalog_product` (`id`, `name`, `name_en`, `name_uz`, `description`, `description_en`, `description_uz`, `specifications`, `specifications_en`, `specifications_uz`, `slug`, `price`, `stock`, `available`, `is_popular`, `image`, `created_at`, `updated_at`, `category_id`) VALUES (5, 'OLTIN NPK 8:24:24', 'OLTIN NPK 8:24:24', 'OLTIN NPK 8:24:24', '<p>Комплексное удобрение с повышенным содержанием фосфора и калия. Состав: - Азот (N): 8% - Фосфор (P): 24% - Калий (K): 24% Особенности: - Сбалансированное содержание фосфора и калия для оптимального развития растений - Улучшает корневую систему и повышает устойчивость к стрессам - Способствует лучшему цветению и формированию плодов Рекомендуемое использование: - Идеально для овощных культур и фруктовых деревьев - Применяется в период активного роста и плодоношения</p>', '<p>Complex fertilizer with increased phosphorus and potassium content. Composition: - Nitrogen (N): 8% - Phosphorus (P): 24% - Potassium (K): 24% Features: - Balanced phosphorus and potassium content for optimal plant development - Improves root system and increases stress resistance - Promotes better flowering and fruit formation Recommended use: - Perfect for vegetable crops and fruit trees - Applied during active growth and fruiting period</p>', '<p>Fosfor va kaliy miqdori yuqori bo&#39;lgan kompleks o&#39;g&#39;it. Tarkibi: - Azot (N): 8% - Fosfor (P): 24% - Kaliy (K): 24% Xususiyatlari: - O&#39;simliklarning optimal rivojlanishi uchun fosfor va kaliyning muvozanatlashgan tarkibi - Ildiz tizimini yaxshilaydi va stresslarga chidamlilikni oshiradi - Yaxshi gullash va meva shakllanishiga yordam beradi Tavsiya etilgan foydalanish: - Sabzavot ekinlari va mevali daraxtlar uchun ideal - Faol o&#39;sish va meva tugish davrida qo&#39;llaniladi</p>', '', '', '', 'oltin-npk-8-24-24', 125000, 160, 1, 0, 'products/images/NKP_8_24_24_KoW7GTX.png', '2024-12-28 12:14:12', '2024-12-28 12:32:21', 2);
INSERT INTO `catalog_product` (`id`, `name`, `name_en`, `name_uz`, `description`, `description_en`, `description_uz`, `specifications`, `specifications_en`, `specifications_uz`, `slug`, `price`, `stock`, `available`, `is_popular`, `image`, `created_at`, `updated_at`, `category_id`) VALUES (6, 'OLTIN NPK(S) 10:20:20(5)', 'OLTIN NPK(S) 10:20:20(5)', 'OLTIN NPK(S) 10:20:20(5)', '<p>Комплексное удобрение с серой. Состав: - Азот (N): 10% - Фосфор (P): 20% - Калий (K): 20% - Сера (S): 5% Особенности: - Способствует развитию мощной корневой системы - Улучшает засухоустойчивость и холодостойкость растений - Сбалансированное содержание макроэлементов повышает урожайность Рекомендуемое использование: - Для всех видов культур, включая овощи, фрукты и зерновые - Подходит для основного внесения и подкормок</p>', '<p>Complex fertilizer with sulfur. Composition: - Nitrogen (N): 10% - Phosphorus (P): 20% - Potassium (K): 20% - Sulfur (S): 5% Features: - Promotes development of powerful root system - Improves drought resistance and cold tolerance of plants - Balanced content of macronutrients increases yield Recommended use: - For all types of crops, including vegetables, fruits and cereals - Suitable for basic application and top dressing</p>', '<p>Oltingugurtli kompleks o&#39;g&#39;it. Tarkibi: - Azot (N): 10% - Fosfor (P): 20% - Kaliy (K): 20% - Oltingugurt (S): 5% Xususiyatlari: - Kuchli ildiz tizimining rivojlanishiga yordam beradi - O&#39;simliklarning qurg&#39;oqchilik va sovuqqa chidamliligini oshiradi - Makroelementlarning muvozanatlashgan tarkibi hosildorlikni oshiradi Tavsiya etilgan foydalanish: - Sabzavotlar, mevalar va don ekinlari kabi barcha turdagi ekinlar uchun - Asosiy kiritish va oziqlantirish uchun mos keladi</p>', '', '', '', 'oltin-npk-s-10-20-20-5', 118000, 170, 1, 0, 'products/images/NPKS_10_20_205_f5FYDkL.png', '2024-12-28 12:14:12', '2024-12-28 12:32:10', 2);
INSERT INTO `catalog_product` (`id`, `name`, `name_en`, `name_uz`, `description`, `description_en`, `description_uz`, `specifications`, `specifications_en`, `specifications_uz`, `slug`, `price`, `stock`, `available`, `is_popular`, `image`, `created_at`, `updated_at`, `category_id`) VALUES (7, 'OLTIN NPK 20:10:10(10)', 'OLTIN NPK 20:10:10(10)', 'OLTIN NPK 20:10:10(10)', '<p>Комплексное удобрение с повышенным содержанием азота. Состав: - Азот (N): 20% - Фосфор (P): 10% - Калий (K): 10% - Сера (S): 10% Особенности: - Идеальное удобрение для азотных культур - Помогает растениям справляться с неблагоприятными условиями - Увеличивает урожайность за счёт улучшенного фотосинтеза Рекомендуемое использование: - Рекомендуется для использования в овощеводстве и садоводстве - Эффективно для культур, требующих азотного питания</p>', '<p>Complex fertilizer with increased nitrogen content. Composition: - Nitrogen (N): 20% - Phosphorus (P): 10% - Potassium (K): 10% - Sulfur (S): 10% Features: - Perfect fertilizer for nitrogen-loving crops - Helps plants cope with adverse conditions - Increases yield through improved photosynthesis Recommended use: - Recommended for use in vegetable growing and horticulture - Effective for crops requiring nitrogen nutrition</p>', '<p>Azot miqdori yuqori bo&#39;lgan kompleks o&#39;g&#39;it. Tarkibi: - Azot (N): 20% - Fosfor (P): 10% - Kaliy (K): 10% - Oltingugurt (S): 10% Xususiyatlari: - Azotli ekinlar uchun ideal o&#39;g&#39;it - O&#39;simliklarga noqulay sharoitlarga bardosh berishga yordam beradi - Yaxshilangan fotosintez hisobiga hosildorlikni oshiradi Tavsiya etilgan foydalanish: - Sabzavotchilik va bog&#39;dorchilikda foydalanish uchun tavsiya etiladi - Azotli oziqlanishni talab qiladigan ekinlar uchun samarali</p>', '', '', '', 'oltin-npk-20-10-10-10', 122000, 145, 1, 0, 'products/images/NPKS_20_10_1010_VWYiebL.png', '2024-12-28 12:14:12', '2024-12-28 12:32:03', 2);
INSERT INTO `catalog_product` (`id`, `name`, `name_en`, `name_uz`, `description`, `description_en`, `description_uz`, `specifications`, `specifications_en`, `specifications_uz`, `slug`, `price`, `stock`, `available`, `is_popular`, `image`, `created_at`, `updated_at`, `category_id`) VALUES (8, 'OLTIN NPK(S) 15:15:15(7)', 'OLTIN NPK(S) 15:15:15(7)', 'OLTIN NPK(S) 15:15:15(7)', '<p>Универсальное комплексное удобрение с серой. Состав: - Азот (N): 15% - Фосфор (P): 15% - Калий (K): 15% - Сера (S): 7% Особенности: - Универсальное сбалансированное удобрение для всех культур - Сера способствует образованию белков и укреплению растений - Улучшает качество продукции и повышает урожайность Рекомендуемое использование: - Для улучшения структуры почвы и плодородия - Подходит для всех сельскохозяйственных культур</p>', '<p>Universal complex fertilizer with sulfur. Composition: - Nitrogen (N): 15% - Phosphorus (P): 15% - Potassium (K): 15% - Sulfur (S): 7% Features: - Universal balanced fertilizer for all crops - Sulfur promotes protein formation and plant strengthening - Improves product quality and increases yield Recommended use: - For improving soil structure and fertility - Suitable for all agricultural crops</p>', '<p>Oltingugurtli universal kompleks o&#39;g&#39;it. Tarkibi: - Azot (N): 15% - Fosfor (P): 15% - Kaliy (K): 15% - Oltingugurt (S): 7% Xususiyatlari: - Barcha ekinlar uchun universal muvozanatlashtirilgan o&#39;g&#39;it - Oltingugurt oqsillar hosil bo&#39;lishiga va o&#39;simliklarni mustahkamlashga yordam beradi - Mahsulot sifatini yaxshilaydi va hosildorlikni oshiradi Tavsiya etilgan foydalanish: - Tuproq tuzilishi va unumdorligini yaxshilash uchun - Barcha qishloq xo&#39;jaligi ekinlari uchun mos keladi</p>', '', '', '', 'oltin-npk-s-15-15-15-7', 116000, 155, 1, 0, 'products/images/NPKS_15_15_157_sjV9YeS.png', '2024-12-28 12:14:12', '2024-12-28 12:31:56', 2);
INSERT INTO `catalog_product` (`id`, `name`, `name_en`, `name_uz`, `description`, `description_en`, `description_uz`, `specifications`, `specifications_en`, `specifications_uz`, `slug`, `price`, `stock`, `available`, `is_popular`, `image`, `created_at`, `updated_at`, `category_id`) VALUES (9, 'OLTIN NPK(S) 16:16:16(7)', 'OLTIN NPK(S) 16:16:16(7)', 'OLTIN NPK(S) 16:16:16(7)', '<p>Универсальное комплексное удобрение с повышенным содержанием NPK. Состав: - Азот (N): 16% - Фосфор (P): 16% - Калий (K): 16% - Сера (S): 7% Особенности: - Оптимальное соотношение питательных веществ для повышения урожайности - Сбалансированное содержание азота, фосфора и калия улучшает общий рост растений - Способствует улучшению структуры почвы, её водопроницаемости и аэрации Рекомендуемое использование: - Подходит для овощей, зерновых, фруктов и других культур - Рекомендуется для применения в качестве основного или дополнительного удобрения</p>', '<p>Universal complex fertilizer with increased NPK content. Composition: - Nitrogen (N): 16% - Phosphorus (P): 16% - Potassium (K): 16% - Sulfur (S): 7% Features: - Optimal nutrient ratio for increased yield - Balanced content of nitrogen, phosphorus and potassium improves overall plant growth - Helps improve soil structure, water permeability and aeration Recommended use: - Suitable for vegetables, cereals, fruits and other crops - Recommended for use as main or supplementary fertilizer</p>', '<p>NPK miqdori yuqori bo&#39;lgan universal kompleks o&#39;g&#39;it. Tarkibi: - Azot (N): 16% - Fosfor (P): 16% - Kaliy (K): 16% - Oltingugurt (S): 7% Xususiyatlari: - Hosildorlikni oshirish uchun ozuqa moddalarining optimal nisbati - Azot, fosfor va kaliyning muvozanatlashgan tarkibi o&#39;simliklarning umumiy o&#39;sishini yaxshilaydi - Tuproq tuzilishi, suv o&#39;tkazuvchanligi va aeratsiyasini yaxshilashga yordam beradi Tavsiya etilgan foydalanish: - Sabzavotlar, don ekinlari, mevalar va boshqa ekinlar uchun mos keladi - Asosiy yoki qo&#39;shimcha o&#39;g&#39;it sifatida qo&#39;llash uchun tavsiya etiladi</p>', '', '', '', 'oltin-npk-s-16-16-16-7', 117000, 165, 1, 0, 'products/images/NPKS_16_16_167_PpIkImt.png', '2024-12-28 12:14:12', '2024-12-28 12:31:46', 2);
INSERT INTO `catalog_product` (`id`, `name`, `name_en`, `name_uz`, `description`, `description_en`, `description_uz`, `specifications`, `specifications_en`, `specifications_uz`, `slug`, `price`, `stock`, `available`, `is_popular`, `image`, `created_at`, `updated_at`, `category_id`) VALUES (10, 'OLTIN Mini Amophos', 'OLTIN Mini Amophos', 'OLTIN Mini Amofos', '<p>Комплексное фосфорное удобрение с добавлением азота. Состав: - Азот (N): 5% - Фосфор (P): 23% - Сера (S): 4% - Кальций (Ca): 12% Особенности: - Способствует улучшению почвенного плодородия и усвоению питательных веществ - Высокая концентрация фосфора стимулирует развитие корневой системы - Кальций улучшает структуру почвы и pH баланс Рекомендуемое использование: - Идеально подходит для применения на бедных фосфором почвах - Эффективно для предпосевной обработки и основного внесения</p>', '<p>Complex phosphorus fertilizer with added nitrogen. Composition: - Nitrogen (N): 5% - Phosphorus (P): 23% - Sulfur (S): 4% - Calcium (Ca): 12% Features: - Promotes improvement of soil fertility and nutrient absorption - High phosphorus concentration stimulates root system development - Calcium improves soil structure and pH balance Recommended use: - Ideal for use on phosphorus-poor soils - Effective for pre-sowing treatment and basic application</p>', '<p>Azot qo&#39;shilgan kompleks fosforli o&#39;g&#39;it. Tarkibi: - Azot (N): 5% - Fosfor (P): 23% - Oltingugurt (S): 4% - Kalsiy (Ca): 12% Xususiyatlari: - Tuproq unumdorligini yaxshilashga va ozuqa moddalarining o&#39;zlashtirilishiga yordam beradi - Fosforning yuqori konsentratsiyasi ildiz tizimining rivojlanishini rag&#39;batlantiradi - Kalsiy tuproq tuzilishini va pH balansini yaxshilaydi Tavsiya etilgan foydalanish: - Fosfor kam bo&#39;lgan tuproqlarda qo&#39;llash uchun ideal - Ekishdan oldingi ishlov berish va asosiy kiritish uchun samarali</p>', '', '', '', 'oltin-mini-amophos', 135000, 120, 1, 0, 'products/images/Mini_Amophos_6B96P74.png', '2024-12-28 12:14:12', '2024-12-28 12:30:32', 3);
INSERT INTO `catalog_product` (`id`, `name`, `name_en`, `name_uz`, `description`, `description_en`, `description_uz`, `specifications`, `specifications_en`, `specifications_uz`, `slug`, `price`, `stock`, `available`, `is_popular`, `image`, `created_at`, `updated_at`, `category_id`) VALUES (11, 'OLTIN CarboPhos Tez 42:5', 'OLTIN CarboPhos Tez 42:5', 'OLTIN CarboPhos Tez 42:5', '<p>Быстродействующее азотно-фосфорное удобрение. Состав: - Азот (N): 42% - Фосфор (P): 5% Особенности: - Быстро восполняет дефицит азота в почве - Идеально подходит для устранения азотного голодания у растений - Эффективно работает на всех типах почв Рекомендуемое использование: - Используется в виде основного удобрения или подкормки - Применяется на стадии активного роста растений</p>', '<p>Fast-acting nitrogen-phosphorus fertilizer. Composition: - Nitrogen (N): 42% - Phosphorus (P): 5% Features: - Quickly replenishes nitrogen deficiency in soil - Perfect for eliminating nitrogen starvation in plants - Works effectively on all soil types Recommended use: - Used as basic fertilizer or top dressing - Applied during active plant growth stage</p>', '<p>Tez ta&#39;sir qiluvchi azot-fosforli o&#39;g&#39;it. Tarkibi: - Azot (N): 42% - Fosfor (P): 5% Xususiyatlari: - Tuproqdagi azot tanqisligini tezda to&#39;ldiradi - O&#39;simliklardagi azot tanqisligini bartaraf etish uchun ideal - Barcha tuproq turlarida samarali ishlaydi Tavsiya etilgan foydalanish: - Asosiy o&#39;g&#39;it yoki oziqlantirish sifatida ishlatiladi - O&#39;simliklarning faol o&#39;sish bosqichida qo&#39;llaniladi</p>', '', '', '', 'oltin-carbophos-tez-42-5', 140000, 110, 1, 0, 'products/images/Carbophos_Tez_rDFhgbR.png', '2024-12-28 12:14:12', '2024-12-28 12:30:26', 3);
INSERT INTO `catalog_product` (`id`, `name`, `name_en`, `name_uz`, `description`, `description_en`, `description_uz`, `specifications`, `specifications_en`, `specifications_uz`, `slug`, `price`, `stock`, `available`, `is_popular`, `image`, `created_at`, `updated_at`, `category_id`) VALUES (12, 'Ammoniated Single Superphosphate (ASSP)', 'Ammoniated Single Superphosphate (ASSP)', 'Ammoniylashtirilgan oddiy superfosfat (ASSP)', '<p>Комплексное фосфорное удобрение с азотом и серой. Состав: - Азот (N): 4% - Фосфор (P): 20% - Сера (S): 12% Особенности: - Обеспечивает длительное фосфорное питание - Содержит серу в доступной для растений форме - Улучшает качество продукции Рекомендуемое использование: - Подходит для всех типов почв - Особенно эффективно для масличных культур</p>', '<p>Complex phosphorus fertilizer with nitrogen and sulfur. Composition: - Nitrogen (N): 4% - Phosphorus (P): 20% - Sulfur (S): 12% Features: - Provides long-term phosphorus nutrition - Contains sulfur in plant-available form - Improves product quality Recommended use: - Suitable for all soil types - Especially effective for oilseed crops</p>', '<p>Azot va oltingugurt qo&#39;shilgan kompleks fosforli o&#39;g&#39;it. Tarkibi: - Azot (N): 4% - Fosfor (P): 20% - Oltingugurt (S): 12% Xususiyatlari: - Uzoq muddatli fosforli oziqlanishni ta&#39;minlaydi - O&#39;simliklar uchun qulay shaklda oltingugurtni o&#39;z ichiga oladi - Mahsulot sifatini yaxshilaydi Tavsiya etilgan foydalanish: - Barcha tuproq turlari uchun mos keladi - Moyli ekinlar uchun ayniqsa samarali</p>', '', '', '', 'ammoniated-single-superphosphate', 128000, 130, 1, 0, 'products/images/ASSP_ieRlRFY.png', '2024-12-28 12:14:12', '2024-12-28 12:30:19', 3);
INSERT INTO `catalog_product` (`id`, `name`, `name_en`, `name_uz`, `description`, `description_en`, `description_uz`, `specifications`, `specifications_en`, `specifications_uz`, `slug`, `price`, `stock`, `available`, `is_popular`, `image`, `created_at`, `updated_at`, `category_id`) VALUES (13, 'OLTIN NPK Supra Blue 12:11:18(14)', 'OLTIN NPK Supra Blue 12:11:18(14)', 'OLTIN NPK Supra Blue 12:11:18(14)', '<p>Водорастворимое комплексное удобрение с серой. Состав: - Азот (N): 12% - Фосфор (P): 11% - Калий (K): 18% - Сера (S): 14% Особенности: - Полностью водорастворимое удобрение - Обеспечивает равномерное питание растений - Высокое содержание калия улучшает качество плодов - Сера способствует синтезу белков и аминокислот Рекомендуемое использование: - Подходит для корневого и листового внесения - Рекомендуется для овощных культур, фруктов и виноградников</p>', '<p>Water-soluble complex fertilizer with sulfur. Composition: - Nitrogen (N): 12% - Phosphorus (P): 11% - Potassium (K): 18% - Sulfur (S): 14% Features: - Fully water-soluble fertilizer - Provides uniform plant nutrition - High potassium content improves fruit quality - Sulfur promotes protein and amino acid synthesis Recommended use: - Suitable for root and foliar application - Recommended for vegetable crops, fruits and vineyards</p>', '<p>Oltingugurtli suvda eruvchan kompleks o&#39;g&#39;it. Tarkibi: - Azot (N): 12% - Fosfor (P): 11% - Kaliy (K): 18% - Oltingugurt (S): 14% Xususiyatlari: - To&#39;liq suvda eruvchan o&#39;g&#39;it - O&#39;simliklarning bir tekis oziqlanishini ta&#39;minlaydi - Kaliyning yuqori miqdori mevalar sifatini yaxshilaydi - Oltingugurt oqsillar va aminokislotalar sinteziga yordam beradi Tavsiya etilgan foydalanish: - Ildizdan va bargdan kiritish uchun mos keladi - Sabzavot ekinlari, mevalar va uzumzorlar uchun tavsiya etiladi</p>', '', '', '', 'oltin-npk-supra-blue-12-11-18-14', 155000, 90, 1, 0, 'products/images/SUPRA_BLUE_PjG5wVc.png', '2024-12-28 12:14:12', '2024-12-28 12:30:12', 4);
INSERT INTO `catalog_product` (`id`, `name`, `name_en`, `name_uz`, `description`, `description_en`, `description_uz`, `specifications`, `specifications_en`, `specifications_uz`, `slug`, `price`, `stock`, `available`, `is_popular`, `image`, `created_at`, `updated_at`, `category_id`) VALUES (14, 'OLTIN NPK Supra Green 18:18:18+TE', 'OLTIN NPK Supra Green 18:18:18+TE', 'OLTIN NPK Supra Green 18:18:18+TE', '<p>Водорастворимое комплексное удобрение с микроэлементами. Состав: - Азот (N): 18% - Фосфор (P): 18% - Калий (K): 18% - Микроэлементы (TE): B, Zn, Cu, Mn, Fe, Mo Особенности: - Универсальное удобрение для всех типов почв - Подходит для использования как в открытом грунте, так и в теплицах - Микроэлементы в хелатной форме для лучшего усвоения Рекомендуемое использование: - Для зерновых, масличных, технических культур - Идеально для листовой подкормки</p>', '<p>Water-soluble complex fertilizer with trace elements. Composition: - Nitrogen (N): 18% - Phosphorus (P): 18% - Potassium (K): 18% - Trace elements (TE): B, Zn, Cu, Mn, Fe, Mo Features: - Universal fertilizer for all soil types - Suitable for use both in open field and greenhouses - Chelated microelements for better absorption Recommended use: - For cereals, oilseeds, industrial crops - Perfect for foliar feeding</p>', '<p>Mikroelementli suvda eruvchan kompleks o&#39;g&#39;it. Tarkibi: - Azot (N): 18% - Fosfor (P): 18% - Kaliy (K): 18% - Mikroelementlar (TE): B, Zn, Cu, Mn, Fe, Mo Xususiyatlari: - Barcha tuproq turlari uchun universal o&#39;g&#39;it - Ochiq maydon va issiqxonalarda foydalanish uchun mos keladi - Yaxshi o&#39;zlashtirilishi uchun xelat shaklidagi mikroelementlar Tavsiya etilgan foydalanish: - Don, moyli, texnik ekinlar uchun - Bargdan oziqlantirish uchun ideal</p>', '', '', '', 'oltin-npk-supra-green-18-18-18-te', 165000, 85, 1, 0, 'products/images/SUPRA_GREEN_wNCvCFN.png', '2024-12-28 12:14:12', '2024-12-28 12:30:05', 4);
INSERT INTO `catalog_product` (`id`, `name`, `name_en`, `name_uz`, `description`, `description_en`, `description_uz`, `specifications`, `specifications_en`, `specifications_uz`, `slug`, `price`, `stock`, `available`, `is_popular`, `image`, `created_at`, `updated_at`, `category_id`) VALUES (15, 'OLTIN NPK Supra Yellow 13:40:13+TE', 'OLTIN NPK Supra Yellow 13:40:13+TE', 'OLTIN NPK Supra Yellow 13:40:13+TE', '<p>Водорастворимое удобрение с высоким содержанием фосфора. Состав: - Азот (N): 13% - Фосфор (P): 40% - Калий (K): 13% - Микроэлементы (TE): B, Zn, Cu, Mn, Fe, Mo Особенности: - Высокое содержание фосфора для развития корневой системы - Оптимально для использования в начальной стадии роста - Микроэлементы в хелатной форме Рекомендуемое использование: - Для всех типов культур, особенно требовательных к фосфору - Эффективно для корневой подкормки</p>', '<p>Water-soluble fertilizer with high phosphorus content. Composition: - Nitrogen (N): 13% - Phosphorus (P): 40% - Potassium (K): 13% - Trace elements (TE): B, Zn, Cu, Mn, Fe, Mo Features: - High phosphorus content for root system development - Optimal for use in early growth stage - Chelated microelements Recommended use: - For all types of crops, especially phosphorus-demanding ones - Effective for root feeding</p>', '<p>Fosfor miqdori yuqori bo&#39;lgan suvda eruvchan o&#39;g&#39;it. Tarkibi: - Azot (N): 13% - Fosfor (P): 40% - Kaliy (K): 13% - Mikroelementlar (TE): B, Zn, Cu, Mn, Fe, Mo Xususiyatlari: - Ildiz tizimini rivojlantirish uchun fosforning yuqori miqdori - O&#39;sishning boshlang&#39;ich bosqichida foydalanish uchun optimal - Xelat shaklidagi mikroelementlar Tavsiya etilgan foydalanish: - Fosforga talabchan bo&#39;lgan barcha turdagi ekinlar uchun - Ildizdan oziqlantirish uchun samarali</p>', '', '', '', 'oltin-npk-supra-yellow-13-40-13-te', 170000, 75, 1, 0, 'products/images/SUPRA_YELLOW_jmSLDCj.png', '2024-12-28 12:14:12', '2024-12-28 12:29:40', 4);
INSERT INTO `catalog_product` (`id`, `name`, `name_en`, `name_uz`, `description`, `description_en`, `description_uz`, `specifications`, `specifications_en`, `specifications_uz`, `slug`, `price`, `stock`, `available`, `is_popular`, `image`, `created_at`, `updated_at`, `category_id`) VALUES (16, 'OLTIN NPK Supra Red 10:10:40+TE', 'OLTIN NPK Supra Red 10:10:40+TE', 'OLTIN NPK Supra Red 10:10:40+TE', '<p>Водорастворимое удобрение с высоким содержанием калия. Состав: - Азот (N): 10% - Фосфор (P): 10% - Калий (K): 40% - Микроэлементы (TE): B, Zn, Cu, Mn, Fe, Mo Особенности: - Высокое содержание калия для улучшения качества плодов - Повышает устойчивость к стрессовым условиям - Улучшает вкусовые качества продукции Рекомендуемое использование: - Для культур, требующих калийного питания - Идеально для применения в период созревания плодов</p>', '<p>Water-soluble fertilizer with high potassium content. Composition: - Nitrogen (N): 10% - Phosphorus (P): 10% - Potassium (K): 40% - Trace elements (TE): B, Zn, Cu, Mn, Fe, Mo Features: - High potassium content for improved fruit quality - Increases resistance to stress conditions - Improves taste qualities of products Recommended use: - For crops requiring potassium nutrition - Perfect for application during fruit ripening period</p>', '<p>Kaliy miqdori yuqori bo&#39;lgan suvda eruvchan o&#39;g&#39;it. Tarkibi: - Azot (N): 10% - Fosfor (P): 10% - Kaliy (K): 40% - Mikroelementlar (TE): B, Zn, Cu, Mn, Fe, Mo Xususiyatlari: - Mevalar sifatini yaxshilash uchun kaliyning yuqori miqdori - Stress sharoitlariga chidamlilikni oshiradi - Mahsulotning ta&#39;m xususiyatlarini yaxshilaydi Tavsiya etilgan foydalanish: - Kaliyga talabchan ekinlar uchun - Mevalarning pishish davrida qo&#39;llash uchun ideal</p>', '', '', '', 'oltin-npk-supra-red-10-10-40-te', 175000, 80, 1, 0, 'products/images/SUPRA_RED_GASuME1.png', '2024-12-28 12:14:12', '2024-12-28 12:29:34', 4);
INSERT INTO `catalog_product` (`id`, `name`, `name_en`, `name_uz`, `description`, `description_en`, `description_uz`, `specifications`, `specifications_en`, `specifications_uz`, `slug`, `price`, `stock`, `available`, `is_popular`, `image`, `created_at`, `updated_at`, `category_id`) VALUES (17, 'OLTIN SOP Sulphate of Potash K:50%', 'OLTIN SOP Sulphate of Potash K:50%', 'OLTIN SOP Kaliy Sulfat K:50%', '<p>Специальное калийное удобрение. Состав: - Калий (K): 50% Особенности: - Не содержит хлор, идеально для культур, чувствительных к соли - Снижает солевой индекс почвы - Улучшает вкус, цвет и устойчивость продукции Рекомендуемое использование: - Идеально для фруктов, цветов, табака и овощей - Применяется для улучшения качества продукции</p>', '<p>Special potassium fertilizer. Composition: - Potassium (K): 50% Features: - Chlorine-free, perfect for salt-sensitive crops - Reduces soil salt index - Improves taste, color and product durability Recommended use: - Perfect for fruits, flowers, tobacco and vegetables - Used to improve product quality</p>', '<p>Maxsus kaliy o&#39;g&#39;iti. Tarkibi: - Kaliy (K): 50% Xususiyatlari: - Xlor yo&#39;q, tuzga sezgir ekinlar uchun ideal - Tuproqning tuz indeksini pasaytiradi - Mahsulotning ta&#39;mi, rangi va chidamliligini yaxshilaydi Tavsiya etilgan foydalanish: - Mevalar, gullar, tamaki va sabzavotlar uchun ideal - Mahsulot sifatini yaxshilash uchun qo&#39;llaniladi</p>', '', '', '', 'oltin-sop-sulphate-of-potash', 180000, 60, 1, 0, 'products/images/SOP_K-50_lW0evyj.png', '2024-12-28 12:14:12', '2024-12-28 12:25:43', 5);
INSERT INTO `catalog_product` (`id`, `name`, `name_en`, `name_uz`, `description`, `description_en`, `description_uz`, `specifications`, `specifications_en`, `specifications_uz`, `slug`, `price`, `stock`, `available`, `is_popular`, `image`, `created_at`, `updated_at`, `category_id`) VALUES (18, 'Ammonium Chloride N:26%', 'Ammonium Chloride N:26%', 'Ammoniy Xlorid N:26%', '<p>Специальное азотное удобрение. Состав: - Азот (N): 26% Особенности: - Эффективен для всех типов почв и культур - Высокое содержание азота для активного роста - Быстрое усвоение растениями Рекомендуемое использование: - Для риса, сахарного тростника, хлопка и овощей - Вносится в почву в виде основного удобрения</p>', '<p>Special nitrogen fertilizer. Composition: - Nitrogen (N): 26% Features: - Effective for all soil types and crops - High nitrogen content for active growth - Quick absorption by plants Recommended use: - For rice, sugarcane, cotton and vegetables - Applied to soil as basic fertilizer</p>', '<p>Maxsus azotli o&#39;g&#39;it. Tarkibi: - Azot (N): 26% Xususiyatlari: - Barcha tuproq turlari va ekinlar uchun samarali - Faol o&#39;sish uchun azotning yuqori miqdori - O&#39;simliklar tomonidan tez o&#39;zlashtiriladi Tavsiya etilgan foydalanish: - Sholi, shakar qamish, paxta va sabzavotlar uchun - Asosiy o&#39;g&#39;it sifatida tuproqqa kiritiladi</p>', '', '', '', 'ammonium-chloride', 145000, 95, 1, 0, 'products/images/AMMONIUM_CHLORIDE_BIaRQP6.png', '2024-12-28 12:14:12', '2024-12-28 12:25:36', 5);


-- Table structure for table `catalog_orderitem`
DROP TABLE IF EXISTS `catalog_orderitem`;
CREATE TABLE `catalog_orderitem` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `price` TEXT NOT NULL,
  `quantity` INT NOT NULL,
  `order_id` TEXT NOT NULL,
  `product_id` TEXT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table `catalog_orderitem`
INSERT INTO `catalog_orderitem` (`id`, `price`, `quantity`, `order_id`, `product_id`) VALUES (1, 116000, 1, 1, 8);
INSERT INTO `catalog_orderitem` (`id`, `price`, `quantity`, `order_id`, `product_id`) VALUES (2, 117000, 1, 1, 9);
INSERT INTO `catalog_orderitem` (`id`, `price`, `quantity`, `order_id`, `product_id`) VALUES (3, 180000, 1, 1, 17);
INSERT INTO `catalog_orderitem` (`id`, `price`, `quantity`, `order_id`, `product_id`) VALUES (4, 145000, 2, 1, 18);
INSERT INTO `catalog_orderitem` (`id`, `price`, `quantity`, `order_id`, `product_id`) VALUES (5, 175000, 6, 2, 16);
INSERT INTO `catalog_orderitem` (`id`, `price`, `quantity`, `order_id`, `product_id`) VALUES (6, 180000, 4, 2, 17);


-- Table structure for table `catalog_cartitem`
DROP TABLE IF EXISTS `catalog_cartitem`;
CREATE TABLE `catalog_cartitem` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `quantity` INT NOT NULL,
  `added_at` DATETIME NOT NULL,
  `cart_id` TEXT NOT NULL,
  `product_id` TEXT NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table `catalog_cartitem`
INSERT INTO `catalog_cartitem` (`id`, `quantity`, `added_at`, `cart_id`, `product_id`) VALUES (8, 1, '2024-12-28 13:23:01', 1, 17);


-- Table structure for table `catalog_article`
DROP TABLE IF EXISTS `catalog_article`;
CREATE TABLE `catalog_article` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(200) NOT NULL,
  `title_en` VARCHAR(200) NOT NULL,
  `title_uz` VARCHAR(200) NOT NULL,
  `slug` VARCHAR(200) NOT NULL,
  `content` TEXT NOT NULL,
  `content_en` TEXT NOT NULL,
  `content_uz` TEXT NOT NULL,
  `image` VARCHAR(100) NOT NULL,
  `published` TEXT NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `author_id` INT NOT NULL,
  `category_id` TEXT NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table `catalog_article`
INSERT INTO `catalog_article` (`id`, `title`, `title_en`, `title_uz`, `slug`, `content`, `content_en`, `content_uz`, `image`, `published`, `created_at`, `updated_at`, `author_id`, `category_id`) VALUES (2, 'Открытие нового склада в Ташкенте', 'New Warehouse Opening in Tashkent', 'Toshkentda yangi ombor ochilishi', 'new-warehouse-opening', '
            Мы рады сообщить об открытии нового современного склада в Ташкенте!
            
            Новый склад оснащен:
            - Современным погрузочно-разгрузочным оборудованием
            - Системой климат-контроля
            - Автоматизированной системой учета
            
            Это позволит нам:
            1. Увеличить скорость обработки заказов
            2. Обеспечить оптимальные условия хранения удобрений
            3. Улучшить логистику в Ташкентской области
            ', '
            We are excited to announce the opening of our new modern warehouse in Tashkent!
            
            The new warehouse is equipped with:
            - Modern loading and unloading equipment
            - Climate control system
            - Automated inventory management system
            
            This will allow us to:
            1. Increase order processing speed
            2. Ensure optimal storage conditions for fertilizers
            3. Improve logistics in the Tashkent region
            ', '
            Toshkentda yangi zamonaviy omborimiz ochilganini mamnuniyat bilan ma''lum qilamiz!
            
            Yangi ombor jihozlangan:
            - Zamonaviy yuklash va tushirish uskunalari
            - Iqlim nazorati tizimi
            - Avtomatlashtirilgan hisobga olish tizimi
            
            Bu bizga imkon beradi:
            1. Buyurtmalarni qayta ishlash tezligini oshirish
            2. O''g''itlarni saqlash uchun optimal sharoitlarni ta''minlash
            3. Toshkent viloyatida logistikani yaxshilash
            ', '', 1, '2024-12-28 12:16:41', '2024-12-28 12:16:41', 1, 7);
INSERT INTO `catalog_article` (`id`, `title`, `title_en`, `title_uz`, `slug`, `content`, `content_en`, `content_uz`, `image`, `published`, `created_at`, `updated_at`, `author_id`, `category_id`) VALUES (3, 'Правильное применение азотных удобрений', 'Proper Application of Nitrogen Fertilizers', 'Azotli o''g''itlardan to''g''ri foydalanish', 'proper-nitrogen-fertilizers', '
            Азотные удобрения являются важнейшим элементом питания растений.
            
            Основные правила применения:
            1. Вносите удобрения в правильные сроки
            2. Соблюдайте рекомендованные дозировки
            3. Учитывайте тип почвы и культуры
            
            Преимущества правильного применения:
            - Повышение урожайности
            - Улучшение качества продукции
            - Экономия средств
            ', '
            Nitrogen fertilizers are an essential plant nutrient.
            
            Basic application rules:
            1. Apply fertilizers at the right time
            2. Follow recommended dosages
            3. Consider soil type and crops
            
            Benefits of proper application:
            - Increased yield
            - Improved product quality
            - Cost savings
            ', '
            Azotli o''g''itlar o''simliklarning eng muhim ozuqa elementi hisoblanadi.
            
            Asosiy qo''llash qoidalari:
            1. O''g''itlarni to''g''ri vaqtda qo''llang
            2. Tavsiya etilgan dozalarga rioya qiling
            3. Tuproq va ekin turini hisobga oling
            
            To''g''ri qo''llashning afzalliklari:
            - Hosildorlikni oshirish
            - Mahsulot sifatini yaxshilash
            - Mablag''larni tejash
            ', '', 1, '2024-12-28 12:16:41', '2024-12-28 12:16:41', 1, 9);
INSERT INTO `catalog_article` (`id`, `title`, `title_en`, `title_uz`, `slug`, `content`, `content_en`, `content_uz`, `image`, `published`, `created_at`, `updated_at`, `author_id`, `category_id`) VALUES (4, 'Тренды в производстве удобрений 2024', 'Fertilizer Production Trends 2024', 'O''g''it ishlab chiqarish tendentsiyalari 2024', 'fertilizer-trends-2024', '
            Обзор основных трендов в производстве удобрений в 2024 году.
            
            Ключевые тенденции:
            1. Экологичное производство
            2. Умные удобрения
            3. Биостимуляторы
            
            Перспективы развития:
            - Внедрение новых технологий
            - Расширение ассортимента
            - Повышение эффективности
            ', '
            Overview of main trends in fertilizer production in 2024.
            
            Key trends:
            1. Eco-friendly production
            2. Smart fertilizers
            3. Biostimulants
            
            Development prospects:
            - Implementation of new technologies
            - Product range expansion
            - Efficiency improvement
            ', '
            2024 yilda o''g''it ishlab chiqarishdagi asosiy tendentsiyalar sharhi.
            
            Asosiy tendentsiyalar:
            1. Ekologik ishlab chiqarish
            2. Aqlli o''g''itlar
            3. Biostimulyatorlar
            
            Rivojlanish istiqbollari:
            - Yangi texnologiyalarni joriy etish
            - Mahsulot turlarini kengaytirish
            - Samaradorlikni oshirish
            ', '', 1, '2024-12-28 12:16:41', '2024-12-28 12:16:41', 1, 8);


SET FOREIGN_KEY_CHECKS=1;
