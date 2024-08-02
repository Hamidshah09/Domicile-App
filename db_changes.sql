CREATE TABLE `domicile_reports`.`black_list` (
  `black_list_id` INT NOT NULL,
  `cnic` VARCHAR(13) NULL,
  `reason` VARCHAR(100) NULL,
  `clearance_reason` VARCHAR(100) NULL,
  `user_id` INT NULL,
  `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`black_list_id`));
CREATE TABLE `black_list_history` (
  `blk_list_his_id` bigint NOT NULL AUTO_INCREMENT,
  `black_list_id` int DEFAULT NULL,
  `remarks` varchar(100) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`blk_list_his_id`)
);
CREATE TABLE `domicile_reports`.`approvers` (
  `approver_id` INT NOT NULL AUTO_INCREMENT,
  `approver_name` VARCHAR(45) NULL,
  PRIMARY KEY (`approver_id`));