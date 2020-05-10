/*
Navicat MySQL Data Transfer

Source Server         : bjtu_cms
Source Server Version : 50559
Source Host           : localhost:3306
Source Database       : rbac

Target Server Type    : MYSQL
Target Server Version : 50559
File Encoding         : 65001

Date: 2019-08-22 18:16:24
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for permission
-- ----------------------------
DROP TABLE IF EXISTS `permission`;
CREATE TABLE `permission` (
  `pId` varchar(32) NOT NULL,
  `pCode` varchar(20) NOT NULL,
  `pName` varchar(20) NOT NULL,
  `parentId` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`pId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of permission
-- ----------------------------
INSERT INTO `permission` VALUES ('1', '1', '用户管理', '00');
INSERT INTO `permission` VALUES ('2', '02', '角色管理', '00');
INSERT INTO `permission` VALUES ('3', '03', '权限管理', '00');
INSERT INTO `permission` VALUES ('4', '11', '用户查看', '1');
INSERT INTO `permission` VALUES ('5', '05', '角色查看', '02');
INSERT INTO `permission` VALUES ('6', '06', '权限查看', '03');
INSERT INTO `permission` VALUES ('7', '07', '用户编辑', '1');
INSERT INTO `permission` VALUES ('8', '08', '角色编辑', '02');
INSERT INTO `permission` VALUES ('9', '09', '权限编辑', '03');

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `roleId` varchar(32) NOT NULL,
  `roleName` varchar(20) NOT NULL,
  `roleDescribe` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`roleId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of role
-- ----------------------------
INSERT INTO `role` VALUES ('1', '系统管理员', '系统管理');
INSERT INTO `role` VALUES ('2', '设备管理员', '设备管理');
INSERT INTO `role` VALUES ('3', '审核员', '啛啛喳喳');
INSERT INTO `role` VALUES ('4', '教师', 'xxxxxxx');
INSERT INTO `role` VALUES ('5', '学生', null);

-- ----------------------------
-- Table structure for role_permission
-- ----------------------------
DROP TABLE IF EXISTS `role_permission`;
CREATE TABLE `role_permission` (
  `roleId` varchar(32) NOT NULL,
  `pId` varchar(32) NOT NULL,
  PRIMARY KEY (`roleId`,`pId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of role_permission
-- ----------------------------
INSERT INTO `role_permission` VALUES ('1', '7');
INSERT INTO `role_permission` VALUES ('1', '8');
INSERT INTO `role_permission` VALUES ('1', '9');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` varchar(32) NOT NULL,
  `acct` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `ctime` datetime DEFAULT NULL,
  `sts` char(1) DEFAULT NULL,
  `pwd` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'zhangsan', '张三', '2019-07-28 11:31:09', '1', '123456');
INSERT INTO `user` VALUES ('2', 'lisi', '李四', '2019-07-27 15:38:27', '0', '123456');
INSERT INTO `user` VALUES ('3', 'wangwu', 'cvc', '2019-07-28 17:06:42', '0', '123456');
INSERT INTO `user` VALUES ('a4d12f50b1f111e9bd92005056c00008', 'zhaoliu', 'zhailiu', '2019-07-29 19:11:34', '1', '123456');
INSERT INTO `user` VALUES ('feebf628bab311e98070005056c00008', 'aaa', 'aaa', '2019-08-09 22:41:31', '1', '123456');

-- ----------------------------
-- Table structure for user_role
-- ----------------------------
DROP TABLE IF EXISTS `user_role`;
CREATE TABLE `user_role` (
  `accId` varchar(32) NOT NULL,
  `roleId` varchar(32) NOT NULL,
  PRIMARY KEY (`accId`,`roleId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Records of user_role
-- ----------------------------
INSERT INTO `user_role` VALUES ('lisi', '2');
INSERT INTO `user_role` VALUES ('wangwu', '1');
INSERT INTO `user_role` VALUES ('zhangsan', '1');
INSERT INTO `user_role` VALUES ('zhangsan', '2');
