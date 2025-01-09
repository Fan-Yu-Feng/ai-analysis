/*
 Navicat MySQL Data Transfer

 Source Server         : 192.168.15.8-linux主机
 Source Server Type    : MySQL
 Source Server Version : 80036 (8.0.36)
 Source Host           : 192.168.15.8:3306
 Source Schema         : ai_comment

 Target Server Type    : MySQL
 Target Server Version : 80036 (8.0.36)
 File Encoding         : 65001

 Date: 09/01/2025 14:59:31
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for analysis_task_config
-- ----------------------------
DROP TABLE IF EXISTS `analysis_task_config`;
CREATE TABLE `analysis_task_config`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '任务的唯一标识符',
  `prompt_config_id` int NOT NULL COMMENT '评论配置表 id',
  `status` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '任务状态：待处理、处理中、已完成、失败',
  `priority` int NULL DEFAULT 0 COMMENT '任务优先级，数值越大优先级越高',
  `config_detail` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '配置明细',
  `error_message` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '错误信息，如果任务失败则记录错误信息',
  `deleted` tinyint(1) NOT NULL DEFAULT 0 COMMENT '逻辑删除标志，0 表示未删除，1 表示已删除',
  `create_by` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '创建人',
  `update_by` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '修改人',
  `create_time` datetime NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_prompt_config_id`(`prompt_config_id` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '分析任务表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for comment_analytics_info
-- ----------------------------
DROP TABLE IF EXISTS `comment_analytics_info`;
CREATE TABLE `comment_analytics_info`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '评论的唯一标识符',
  `task_id` bigint NULL DEFAULT NULL COMMENT '关联任务 id',
  `comment_id` bigint NULL DEFAULT NULL COMMENT '原始评论数据的 id',
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '评论的内容',
  `sentiment` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '情感倾向：正面、负面、中性',
  `topic` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '主要主题',
  `keywords` json NULL COMMENT '关键词',
  `summary` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '总结��类：对产品的看法、对营销手段的评论、表达向往、表达讽刺、其他',
  `create_time` datetime NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `create_by` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `update_by` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_comment_id`(`comment_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 56953 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for content_analytics_info
-- ----------------------------
DROP TABLE IF EXISTS `content_analytics_info`;
CREATE TABLE `content_analytics_info`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '评论的唯一标识符',
  `task_id` bigint NULL DEFAULT NULL COMMENT '关联任务 id',
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '评论的内容',
  `sentiment` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '情感倾向：正面、负面、中性',
  `topic` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '主要主题',
  `keywords` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '关键词',
  `summary` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '总结��类：对产品的看法、对营销手段的评论、表达向往、表达讽刺、其他',
  `create_time` datetime NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `deleted` tinyint(1) NOT NULL DEFAULT 0 COMMENT '逻辑删除标志，0 表示未删除，1 表示已删除',
  `create_by` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '创建人',
  `update_by` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '修改人',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_task_id`(`task_id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '营销内容分析结果表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for content_creator
-- ----------------------------
DROP TABLE IF EXISTS `content_creator`;
CREATE TABLE `content_creator`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '创作者的唯一标识符',
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '创作者的姓名',
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '创作者的电子邮件地址',
  `bio` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '创作者的简介',
  `profile_picture` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '创作者的头像 URL',
  `platform` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '创作者所属的平台',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `deleted` tinyint(1) NOT NULL DEFAULT 0 COMMENT '逻辑删除标志，0 表示未删除，1 表示已删除',
  `create_by` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '创建人',
  `update_by` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '修改人',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '媒体内容创作者表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for prompt_config
-- ----------------------------
DROP TABLE IF EXISTS `prompt_config`;
CREATE TABLE `prompt_config`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '配置的唯一标识符',
  `sentiment` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '情感倾向：正面、负面、中性',
  `topic` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '主要主题',
  `summary` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '总结类：对产品的看法、对营销手段的评论、表达向往、表达讽刺、其他',
  `ext_info` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '扩展字段，存储其他的 prompt',
  `deleted` tinyint(1) NOT NULL DEFAULT 0 COMMENT '逻辑删除标志，0 表示未删除，1 表示已删除',
  `create_by` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '创建人',
  `update_by` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '修改人',
  `create_time` datetime NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for social_media_comment_info
-- ----------------------------
DROP TABLE IF EXISTS `social_media_comment_info`;
CREATE TABLE `social_media_comment_info`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '评论的唯一标识符',
  `content_id` bigint NOT NULL COMMENT 'social_media_content_info 表 id，关联的营销内容',
  `parent_comment_id` bigint NOT NULL COMMENT '父评论 ID',
  `reply_to_comment_id` bigint NOT NULL COMMENT '回复的评论 ID',
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '评论内容',
  `user_id` bigint NOT NULL COMMENT '用户的唯一标识符',
  `user_username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '用户名',
  `user_profile_pic_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '用户头像 URL',
  `platform` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '评论所在的平台，小红书、tiktok、FB 等',
  `work_link` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '作品链接',
  `child_comment_count` int NULL DEFAULT 0 COMMENT '子评论数量',
  `comment_like_count` int NULL DEFAULT 0 COMMENT '评论点赞数',
  `has_liked_comment` tinyint(1) NULL DEFAULT 0 COMMENT '是否点赞评论',
  `create_time` datetime NULL DEFAULT CURRENT_TIMESTAMP COMMENT '评论创建时间',
  `update_time` datetime NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '评论更新时间',
  PRIMARY KEY (`id`, `content_id`, `parent_comment_id`, `reply_to_comment_id`, `user_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '媒体评论信息表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for social_media_comment_list
-- ----------------------------
DROP TABLE IF EXISTS `social_media_comment_list`;
CREATE TABLE `social_media_comment_list`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `platform` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '平台',
  `platform_account_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '平台账号ID',
  `platform_media_id` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '视频或文章ID',
  `comment_id` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '评论ID',
  `comment_content` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '评论内容',
  `comment_like` int NULL DEFAULT NULL COMMENT '评论内容点赞数',
  `comment_uid` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '评论用户ID',
  `comment_sec_uid` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '评论用户uid',
  `comment_user_nickname` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '评论用户昵称',
  `comment_time` datetime NULL DEFAULT NULL COMMENT '评论时间',
  `deleted` int NULL DEFAULT 0 COMMENT '是否删除',
  `create_by` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '创建者',
  `create_time` datetime NOT NULL,
  `update_by` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `update_time` datetime NULL DEFAULT NULL COMMENT '修改时间',
  `comment_json_extra` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT 'json字符串',
  `reply_comment_total` bigint NULL DEFAULT NULL COMMENT '评论回复数量',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_pk`(`platform` ASC, `platform_account_id` ASC, `platform_media_id` ASC, `comment_id` ASC) USING BTREE,
  INDEX `fk_comment_uid_`(`comment_uid` ASC) USING BTREE,
  INDEX `fk_comment_sec_uid_`(`comment_sec_uid` ASC) USING BTREE,
  INDEX `fk_comment_time_`(`comment_time` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1826810443 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for social_media_content_info
-- ----------------------------
DROP TABLE IF EXISTS `social_media_content_info`;
CREATE TABLE `social_media_content_info`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `platform` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '平台',
  `platform_account_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '平台账号ID',
  `platform_nickname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '平台账号昵称',
  `platform_media_id` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '视频或文章ID',
  `title` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '文章标题',
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '文章内容',
  `comments_count` int NULL DEFAULT NULL COMMENT '评论数量',
  `liked_count` int NULL DEFAULT NULL COMMENT '点赞数量、喜欢数量',
  `collected_count` int NULL DEFAULT NULL COMMENT '收藏数量',
  `link` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '链接地址',
  `pub_time` datetime NULL DEFAULT NULL COMMENT '文章发布时间',
  `pub_update_time` datetime NULL DEFAULT NULL COMMENT '文章更新时间',
  `deleted` int NULL DEFAULT 0 COMMENT '是否删除',
  `create_by` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '创建者',
  `create_time` datetime NOT NULL,
  `update_by` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `update_time` datetime NULL DEFAULT NULL COMMENT '修改时间',
  `ext_info` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT 'json字符串，原始报文',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 18269148 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '社交媒体文章记录表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `hashed_password` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `is_active` tinyint(1) NULL DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `email` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
