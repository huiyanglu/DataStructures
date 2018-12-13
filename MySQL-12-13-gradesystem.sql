create database gradesystem;

use gradesystem;

create table student
(
	sid int PRIMARY KEY AUTO_INCREMENT,
	sname char(20),
    gender char(20) check(gender='female'or gender='male')
);

create table course
(
    cid int PRIMARY KEY AUTO_INCREMENT,
    cname char(20)
);

create table mark
(
	mid int PRIMARY KEY AUTO_INCREMENT,
	sid int(10),
	cid int(10), 
	score int(10),
	FOREIGN KEY(sid) REFERENCES student(sid),
	FOREIGN KEY(cid) REFERENCES course(cid)
) 
AUTO_INCREMENT=1;

insert into student(sname,gender) 
	values
	('Tom','male'),
	('Jack','male'),
	('Rose','female');

insert into course(cname)
	values
	('math'),
	('physics'),
	('chemistry');

insert into mark(sid,cid,score)
	values
	(1,1,80),
	(2,1,85),
	(3,1,90),
	(1,2,60),
	(2,2,90),
	(3,2,75),
	(1,3,95),
	(2,3,75),
	(3,3,85);


# 构建一个简易的成绩管理系统的数据库，来记录几门课程的学生成绩。数据库中有三张表分别用于记录学生信息、课程信息和成绩信息。
# mark 表包含4列：mid(主键)、sid、cid、score ，注意与其他两个表主键之间的关系。
# 建立表时注意 id 自增和键约束
# 每个表插入语句可通过一条语句完成
# source /Users/luhuiyang/SQL3/MySQL-12-13-gradesystem.sql;