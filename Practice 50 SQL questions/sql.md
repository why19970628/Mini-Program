# 互联网校招SQL笔试经典50题及答案解析
详情：https://zhuanlan.zhihu.com/p/53302593


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

## 12.****

select t1.sid,sname from 
(select sc.sid,count(distinct sc.cid) from  
(select cid from sc where sid='01')t1
left join sc
	on t1.cid=sc.cid
group by sc.sid
having count(distinct sc.cid)=(select count(distinct cid) from sc where sid = '01'))t1
left join student
	on t1.sid=student.sid
where t1.sid!='01';


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

## 22.错误

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

33-36 没有题

## 37.

select cid,sid,score from sc
where score<60
order by cid desc,sid;


## 38

select sc.sid,sname,cid,score from sc
left join student
on student.sid=sc.sid
where cid='01' and score>60;


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


## 41.无


## 42 错误

select sc.sid,sname,cname,score from sc
left join course
on sc.cid=course.cid
left join student
on sc.sid=student.sid
left join teacher
on teacher.tid=course.tid
order by score desc
limit 2;

select * from(select row_number()
over partition by cid order by score desc)rn,
sid,cid,score from course)
where rn<3;



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





























