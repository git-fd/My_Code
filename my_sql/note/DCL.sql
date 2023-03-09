-- 数据控制语言：访问权限和安全级别

-- 创建用户
CREATE USER 'fd'@'localhost' IDENTIFIED BY 'passwd';

-- 修改密码
SET PASSWORD FOR 'fd'@'localhost' = '1314';

-- 授权 ALL[select(查询), insert(插入), update(修改), delete(删除), create(创建), drop()]
GRANT ALL ON `mysql`.`user` to 'fd'@'localhost';    -- 将数据库mysql的user表给fd用户添加所有权限
-- 撤销授权
REVOKE ALL ON `mysql`.`user` FROM 'fd'@'localhost';     -- 取消用户fd的数据库mysql的user表所有权限
-- 刷新权限 改表修改权限需要刷新
FLUSH PRIVILEGES;

-- 查看授权
SHOW GRANTS for 'fd'@'localhost';

-- 删除用户
DROP user 'fd'@'localhost';