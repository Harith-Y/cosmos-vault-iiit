# Installation

### MySQL Install

```
sudo apt install mysql-server
```

### Elmasri test database installation

```
wget https://raw.githubusercontent.com/tolgahanakgun/Elmasri-Database/master/Employee_Database_Script.sql -O company_schema.sql
```

```
sudo mysql
CREATE DATABASE dnacoursetest;
exit;
```

```
sudo mysql dnacoursetest < company_schema.sql
```

## Accessing

```
sudo mysql
```

```
USE dnacoursetest;
SHOW TABLES;
```
