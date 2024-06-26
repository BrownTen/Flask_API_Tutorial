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

INSERT INTO student (name, gender) VALUES ('张三', '男');
INSERT INTO student (name, gender) VALUES ('李四', '女');
