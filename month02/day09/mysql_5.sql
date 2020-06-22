--练习．将　ｂｏｏｋ 表拆分
-- 书籍信息表
-- 出版社信息表
-- 作家信息表
-- 设计表关系并完成E-R模型图，根据模型图 创建这一组表结构

create table 作家(
id int primary key auto_increment,
name varchar(30),
sex char,
remark text
);

create table 出版社(
id int primary key auto_increment,
pname varchar(30),
address varchar(256),
tel char(16)
);

create table 图书(
id int primary key auto_increment,
bname varchar(30),
price float,
aid int,
pid int,
constraint afk foreign key(aid) references 作家(id),
constraint pfk foreign key(pid) references 出版社(id)
);

create table author_publication(
id int primary key auto_increment,
a_id int,
p_id int,
constraint a_fk foreign key(a_id) references 作家(id),
constraint p_fk foreign key(p_id) references 出版社(id)
);