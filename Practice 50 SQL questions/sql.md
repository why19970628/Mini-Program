# 互联网校招SQL笔试经典50题及答案解析


# 1.导入数据

create database info;

use info;

create table Student(sid varchar(10),sname varchar(10),sage 
datetime,ssex nvarchar(10));

insert into Student values('01' , '赵雷' , '1990-01-01' , '男');

insert into Student values('02' , '钱电' , '1990-12-21' , '男');

insert into Student values('03' , '孙风' , '1990-05-20' , '男');

insert into Student values('04' , '李云' , '1990-08-06' , '男');

insert into Student values('05' , '周梅' , '1991-12-01' , '女');

insert into Student values('06' , '吴兰' , '1992-03-01' , '女');

insert into Student values('07' , '郑竹' , '1989-07-01' , '女');

insert into Student values('08' , '王菊' , '1990-01-20' , '女');

create table Course(cid varchar(10),cname varchar(10),tid varchar(10));
insert into Course values('01' , '语文' , '02');

insert into Course values('02' , '数学' , '01');

insert into Course values('03' , '英语' , '03');

create table Teacher(tid varchar(10),tname varchar(10));

insert into Teacher values('01' , '张三');

insert into Teacher values('02' , '李四');

insert into Teacher values('03' , '王五');

create table SC(sid varchar(10),cid varchar(10),score decimal(18,1));

insert into SC values('01' , '01' , 80);

insert into SC values('01' , '02' , 90);

insert into SC values('01' , '03' , 99);

insert into SC values('02' , '01' , 70);

insert into SC values('02' , '02' , 60);

insert into SC values('02' , '03' , 80);

insert into SC values('03' , '01' , 80);

insert into SC values('03' , '02' , 80);

insert into SC values('03' , '03' , 80);

insert into SC values('04' , '01' , 50);

insert into SC values('04' , '02' , 30);

insert into SC values('04' , '03' , 20);

insert into SC values('05' , '01' , 76);

insert into SC values('05' , '02' , 87);

insert into SC values('06' , '01' , 31);

insert into SC values('06' , '03' , 34);

insert into SC values('07' , '02' , 89);

insert into SC values('07' , '03' , 98);

# 2、表结构预览

- 学生表

Student(SId,Sname,Sage,Ssex)

--SId 学生编号,Sname 学生姓名,Sage 出生年月,Ssex 学生性别

- 课程表

Course(CId,Cname,TId)

--CId 课程编号,Cname 课程名称,TId 教师编号

- 教师表

Teacher(TId,Tname)

--TId 教师编号,Tname 教师姓名

- 成绩表

SC(SId,CId,score)

--SId 学生编号,CId 课程编号,score 分数

# 3.题目

1、查询“01”课程比“02”课程成绩高的所有学生的学号；

2、查询平均成绩大于60分的同学的学号和平均成绩；

3、查询所有同学的学号、姓名、选课数、总成绩

4、查询姓“李”的老师的个数；

5、查询没学过“张三”老师课的同学的学号、姓名；

6、查询学过编号“01”并且也学过编号“02”课程的同学的学号、姓名；

7、查询学过“张三”老师所教的课的同学的学号、姓名；

8、查询课程编号“01”的成绩比课程编号“02”课程低的所有同学的学号、姓名；
9、查询所有课程成绩小于60分的同学的学号、姓名；

10、查询没有学全所有课的同学的学号、姓名；

11、查询至少有一门课与学号为“01”的同学所学相同的同学的学号和姓名；

12、查询和"01"号的同学学习的课程完全相同的其他同学的学号和姓名

13、把“SC”表中“张三”老师教的课的成绩都更改为此课程的平均成绩

14、查询没学过"张三"老师讲授的任一门课程的学生姓名

15、查询两门及其以上不及格课程的同学的学号，姓名及其平均成绩

16、检索"01"课程分数小于60，按分数降序排列的学生信息

17、按平均成绩从高到低显示所有学生的平均成绩

18、查询各科成绩最高分、最低分和平均分：以如下形式显示：课程ID，课程name，最高分，最低分，平均分，及格率

19、按各科平均成绩从低到高和及格率的百分数从高到低顺序

20、查询学生的总成绩并进行排名

21、查询不同老师所教不同课程平均分从高到低显示

22、查询所有课程的成绩第2名到第3名的学生信息及该课程成绩

23、统计各科成绩各分数段人数：课程编号,课程名称,[100-85],[85-70],[70-60],[0-60]及所占百分比

24、查询学生平均成绩及其名次

25、查询各科成绩前三名的记录

26、查询每门课程被选修的学生数

27、查询出只选修了一门课程的全部学生的学号和姓名

28、查询男生、女生人数

29、查询名字中含有"风"字的学生信息

30、查询同名同性学生名单，并统计同名人数

31、查询1990年出生的学生名单(注：Student表中Sage列的类型是datetime)

32、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列

33、查询平均成绩大于等于 85 的所有学生的学号、姓名和平均成绩

34、查询课程名称为「数学」，且分数低于 60 的学生姓名和分数

35、查询所有学生的课程及分数情况（存在学生没成绩，没选课的情况）

36、查询任何一门课程成绩在 70 分以上的姓名、课程名称和分数

37、查询不及格的课程，并按课程号从大到小排列

38、查询课程编号为"01"且课程成绩在60分以上的学生的学号和姓名；

39、求每门课程的学生人数

40、查询选修“张三”老师所授课程的学生中，成绩最高的学生姓名及其成绩

41、查询不同课程成绩相同的学生的学生编号、课程编号、学生成绩

42、查询每门功课成绩最好的前两名

43、统计每门课程的学生选修人数（超过5人的课程才统计）。要求输出课程号和选修人数，查询结果按人数降序排列，若人数相同，按课程号升序排列

44、检索至少选修两门课程的学生学号

45、查询选修了全部课程的学生信息

46、查询各学生的年龄

47、查询本周过生日的学生

48、查询下周过生日的学生

49、查询本月过生日的学生

50、查询下月过生日的学生

详情：https://zhuanlan.zhihu.com/p/53302593


# 4.答案

## 1. 

select distinct t1.sid as sid,sname
from
(select * from sc where cid='01')t1
left join
(select * from sc where cid='02')t2
on t1.sid=t2.sid
left join student
on t1.sid=student.sid
where t1.score>t2.score;

## 2.
select sid,avg(score) from sc
group by sc.sid 
having avg(score)>60;


select sc.sid,avg(score) as avg_score,sname from sc 
left join student 
on sc.sid=student.sid
group by sc.sid,sname
having avg_score>60; 

## 3.
select student.sid,sname,count(distinct cid) as course_num,sum(score) from student
left join sc
on student.sid=sc.sid
group by student.sid,sname;


## 4.

select count(distinct tid) from teacher
where teacher.tname like '李%';


## 5
select sid,sname from student
where student.sid not in
(select sc.sid from teacher
left join course
on teacher.tid=course.tid
left join sc
on course.cid=sc.cid
where teacher.tname='张三');


## 6.

select t1.sid,sname from
(select sc.sid from sc 
group by sid
having count(if(cid='01',score,null))>0 and
count(if(cid='02',score,null))>0
)t1
left join student
on student.sid=t1.sid;


## 7.

select student.sid,sname from 
(select cid from course
left join teacher
on teacher.tid=course.tid
where teacher.tname='张三'
)course
left join sc
on course.cid=sc.cid
left join student
on student.sid=sc.sid
group by student.sid,sname
;


## 8.

select t1.sid,sname from
(select t1.sid from 
(select * from sc where cid='01')t1
left join 
(select * from sc where cid='02')t2
on t1.sid=t2.sid
where t1.score>t2.score 
)t1
left join student
on t1.sid=student.sid;

## 9.

select t1.sid,sname,low_score_num from
(select sc.sid,count(if(score<60,score,null)) as low_score_num from sc
group by sid
having low_score_num=count(score)
)t1
left join student
on t1.sid=student.sid;

## 10.

select t1.sid,sname from 
(select count(cid),sid from sc 
group by sid
having count(cid)<(select count(distinct cid) from course)
)t1
left join student
on t1.sid=student.sid;

## 11

select distinct sc.sid from 
(select cid from sc where sid='01')t1
left join sc
on t1.cid=sc.cid;

## 12.更改

select t2.sid,sname from 
(select sc.sid,count(distinct sc.cid) from  
(select cid from sc where sid='01')t1
left join sc
	on t1.cid=sc.cid
group by sc.sid
having count(distinct sc.cid)=(select count(distinct cid) from sc where sid = '01'))t2
left join student
	on t2.sid=student.sid
where t2.sid!='01';


## 13.无




## 14.
select sname from student where sid not in
(select sid from sc
left join course
	on sc.cid=course.cid
left join teacher
	on course.tid=teacher.tid
where tname='张三');


# 15.
select t1.sid,sname,avg_score from
(select sid,count(if(score<60,cid,null)),avg(score) as avg_score from sc
group by sid
having count(if(score<60,cid,null))>=2)t1
left join student
on student.sid=t1.sid;

## 16.

1.原答案
select 
    sid,if(cid='01',score,100)
from sc
where if(cid='01',score,100)<60
order by if(cid='01',score,100) desc

2.改进
select sname,t1.sid,score_low from
(select sid,if(cid='01',score,null) as score_low
from sc 
where if(cid='01',score,null)<60)t1
left join student
on student.sid=t1.sid
order by t1.score_low desc,sid;

3.无排序
select sid,sname from student where sid in
(select sid,from sc where score<60 and cid='01')



## 17.

select sname,avg(score) as avg_score from sc
left join student
on student.sid=sc.sid
group by sc.sid,sname
order by avg_score desc;


## 18.
## 错误答案
select
    sc.cid
    ,cname
    ,max(score) as max_score
    ,min(score) as min_score
    ,avg(score) as avg_score
    ,count(if(score>=60,sid,null))/count(sid) as pass_rate
from sc 
left join course
    on sc.cid=course.cid
group by sc.cid

### 正确答案
select sc.cid,cname,max(score) as max_score,
min(score) as min_score,avg(score) as avg_score,
count(if(score>60,sid,null))/count(sid) as pass_rate
from sc
left join course
	on sc.cid=course.cid
group by sc.cid,cname;





# 19.

select cid,avg(score) as avg_score,count(if(score>=60,sid,null))/count(sid) as pass_rate
from sc
group by cid
order by avg_score,pass_rate desc;

# 20.

select sc.sid,sum(score) as sum_score from sc
group by sid
order by sum_score desc;


## 21. 更改：添加教师姓名

select course.tid,avg(score)as avg_score,tname  from course
left join sc
on course.cid=sc.cid
left join teacher
on teacher.tid=course.tid
group by course.tid,tname
order by avg_score desc;

## 22.

select sid,cid,score,rank_num from(
select rank() over(partition by cid order by score desc) as rank_num
,sid,score,cid from sc)t
where rank_num in (2,3);

## 23.

select
    sc.cid
    ,cname
    ,count(if(score between 85 and 100,sid,null))/count(sid) as '优秀'
    ,count(if(score between 70 and 85,sid,null))/count(sid) as '不错'
    ,count(if(score between 60 and 70,sid,null))/count(sid) as '还行'
    ,count(if(score between 0 and 60,sid,null))/count(sid) as '不及格'
from sc
left join course
    on sc.cid=course.cid
group by sc.cid,cname


## 24
select
    sid
    ,avg_score
    ,rank() over (order by avg_score desc) as ranks
from 
    (
        select
            sid
            ,avg(score) as avg_score
        from sc
        group by sid
    )t;


## 25

select
    sid,cid,rank1,score
from 
    (
        select
            cid
            ,sid
	    ,score
            ,rank() over(partition by cid order by score desc) as rank1
        from sc
    )t
where rank1<=3;


## 26.改

select sc.cid,cname,count(sid) from sc
left join course
on sc.cid=course.cid
group by cid,cname;



select cid,count(sid) from sc
group by cid 



## 27.

select sc.sid,sname from sc
left join student
on sc.sid=student.sid
group by sc.sid,sname
having count(cid)=2;

## 28.

select ssex,count(distinct sid) from student
group by ssex;


## 29

select sid,sname from student
where sname like '%风%'; 


## 30

select sname,ssex from student
group by sname,ssex
having count(sid)>=1;


## 31

select sid,sname,sage from student
where year(sage)=1990;


## 32.

select cid,avg(score) as avg_score from sc
group by cid
order by avg_score,cid desc;



## 33、查询平均成绩大于等于 85 的所有学生的学号、姓名和平均成绩
select a.sid,sname,avg(score) from student a
left join sc b
on a.sid=b.sid
group by sid
having avg(score)>85;



34、查询课程名称为「数学」，且分数低于 60 的学生姓名和分数

方法一:

select a.sid,sname,score from student a
left join sc b
on a.sid=b.sid
left join course c
on c.cid=b.cid
where cname='数学' and score<60;

方法二:

select student.sname, sc.score from student, sc, course
where student.sid = sc.sid
and course.cid = sc.cid
and course.cname = "数学"
and sc.score < 60;


35、查询所有学生的课程及分数情况（存在学生没成绩，没选课的情况）

select a.sid,sname,cid,score from student a
left join sc b
on a.sid=b.sid;

36、查询任何一门课程成绩在 70 分以上的姓名、课程名称和分数

select a.sname,a.sid,cname,score from student a
left join sc b on a.sid=b.sid
left join course c on b.cid=c.cid
where b.score>70;


## 37.

select cid,sid,score from sc
where score<60
order by cid desc,sid;


## 38

select sc.sid,sname,cid,score from sc
left join student
on student.sid=sc.sid
where cid='01' and score>60;


## 39 求每门课程的学生人数

select cid,count(distinct sid) as count_sid
from sc
group by sc.cid;




## 40.

select sc.sid,sname,cname,score from sc
left join course
on sc.cid=course.cid
left join student
on sc.sid=student.sid
left join teacher
on teacher.tid=course.tid
where tname='张三'
order by score desc
limit 1;


## 41.查询不同课程成绩相同的学生的学生编号、课程编号、学生成绩


select distinct a.sid,a.cid,a.score from sc as a
inner join sc as b
on a.sid=b.sid
and a.cid!=b.cid
and a.score=b.score
group by cid,sid;



## 42 查询每门功课成绩最好的前两名

方法一:

select
    cid,t.sid,b.sname,rank1
from 
    (
        select
            cid
            ,sid
            ,rank() over(partition by cid order by score desc) as rank1
        from sc
    )t
left join student as b
on t.sid=b.sid
having rank1<=2
order by cid;

方法二:

select a.sid,a.cid,a.score from sc as a 
left join sc as b 
on a.cid = b.cid and a.score<b.score
group by a.cid, a.sid
having count(b.cid)<2
order by a.cid;



## 43.

select  sc.cid,count(sid) as cnt,cname
from  sc
left join course
on course.cid=sc.cid
group by sc.cid,cname
having cnt>=5
order by count(sid) desc,cid;

## 44

select sid,count(cid) as '课程数' from sc
group by sid
having count(cid)>=2;

## 45 参考12题

select sc.sid,count(cid),sname from sc
left join student
on student.sid=sc.sid
group by sc.sid,sname
having count(sc.cid)=(select count(distinct cid) from sc);


## 46

select sid,sname,year(curdate())-year(sage) as sage
from student;


## 47
select sid,sname,sage from student
where  weekofyear(sage)=weekofyear(curdate());

## 48
select sid,sname,sage from student
where  weekofyear(sage)=weekofyear(curdate());

## 48
select sid,sname,sage from student
where weekofyear(sage)=weekofyear(date_add(curdate(),interval 1  week));



## 49

select sid,sname,sage from student
where month(sage)=month(curdate());


## 50 

select sid,sname,sage from student
where month(sage)=month(date_add(curdate(),interval 1 month));





























