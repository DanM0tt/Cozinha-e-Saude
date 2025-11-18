CREATE TABLE IF NOT EXISTS usuarios (
    username     VARCHAR(50),
    email        VARCHAR(255) UNIQUE NOT NULL,
    id           INT PRIMARY KEY,
    senha        VARBINARY(64) NOT NULL,
);
