-- Creates the user user_0d_1 with all privileges.
-- Check if user exists
SELECT 1 FROM mysql.user WHERE user = 'user_0d_1' LIMIT 1;
CREATE USER
    IF NOT EXISTS 'user_0d_1'@'localhost'
    IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
   ON *.*
   TO 'user_0d_1'@'localhost';
-- Apply privileges immediately
FLUSH PRIVILEGES;
