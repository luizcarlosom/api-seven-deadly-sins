CREATE DATABASE IF NOT EXISTS seven_deadly_sins_database;

CREATE TABLE IF NOT EXISTS `seven_deadly_sins_database`.`characters` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    sin VARCHAR(100) NOT NULL,
    sacred_treasure VARCHAR(100),
    description VARCHAR(500) NOT NULL,
    image_base64 LONGBLOB NOT NULL,

    PRIMARY KEY (id)
);

