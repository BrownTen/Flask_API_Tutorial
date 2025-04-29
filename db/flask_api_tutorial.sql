DROP DATABASE IF EXISTS flask_api_tutorial;
CREATE DATABASE flask_api_tutorial;

USE flask_api_tutorial;

DROP TABLE IF EXISTS student;
CREATE TABLE student(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(10) NOT NULL,
    gender CHAR NOT NULL,
    birthday TIMESTAMP
);

DROP TABLE IF EXISTS user;
CREATE TABLE user(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(10) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(255) NOT NULL
);

INSERT INTO student (name, gender) VALUES ('张三', '男');
INSERT INTO student (name, gender) VALUES ('李四', '女');

INSERT INTO user (name, password, role) VALUES ('root', 'root', 'admin');
INSERT INTO user (name, password, role) VALUES ('张三', 'zhangsan', 'user');
INSERT INTO user (name, password, role) VALUES ('李四', 'lisi', 'user');
