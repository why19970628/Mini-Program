# ������У��SQL���Ծ���50�⼰�𰸽���


# 1.��������

create database info;

use info;

create table Student(sid varchar(10),sname varchar(10),sage 
datetime,ssex nvarchar(10));

insert into Student values('01' , '����' , '1990-01-01' , '��');

insert into Student values('02' , 'Ǯ��' , '1990-12-21' , '��');

insert into Student values('03' , '���' , '1990-05-20' , '��');

insert into Student values('04' , '����' , '1990-08-06' , '��');

insert into Student values('05' , '��÷' , '1991-12-01' , 'Ů');

insert into Student values('06' , '����' , '1992-03-01' , 'Ů');

insert into Student values('07' , '֣��' , '1989-07-01' , 'Ů');

insert into Student values('08' , '����' , '1990-01-20' , 'Ů');

create table Course(cid varchar(10),cname varchar(10),tid varchar(10));
insert into Course values('01' , '����' , '02');

insert into Course values('02' , '��ѧ' , '01');

insert into Course values('03' , 'Ӣ��' , '03');

create table Teacher(tid varchar(10),tname varchar(10));

insert into Teacher values('01' , '����');

insert into Teacher values('02' , '����');

insert into Teacher values('03' , '����');

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

# 2����ṹԤ��

- ѧ����

Student(SId,Sname,Sage,Ssex)

--SId ѧ�����,Sname ѧ������,Sage ��������,Ssex ѧ���Ա�

- �γ̱�

Course(CId,Cname,TId)

--CId �γ̱��,Cname �γ�����,TId ��ʦ���

- ��ʦ��

Teacher(TId,Tname)

--TId ��ʦ���,Tname ��ʦ����

- �ɼ���

SC(SId,CId,score)

--SId ѧ�����,CId �γ̱��,score ����

# 3.��Ŀ

1����ѯ��01���γ̱ȡ�02���γ̳ɼ��ߵ�����ѧ����ѧ�ţ�

2����ѯƽ���ɼ�����60�ֵ�ͬѧ��ѧ�ź�ƽ���ɼ���

3����ѯ����ͬѧ��ѧ�š�������ѡ�������ܳɼ�

4����ѯ�ա������ʦ�ĸ�����

5����ѯûѧ������������ʦ�ε�ͬѧ��ѧ�š�������

6����ѯѧ����š�01������Ҳѧ����š�02���γ̵�ͬѧ��ѧ�š�������

7����ѯѧ������������ʦ���̵Ŀε�ͬѧ��ѧ�š�������

8����ѯ�γ̱�š�01���ĳɼ��ȿγ̱�š�02���γ̵͵�����ͬѧ��ѧ�š�������
9����ѯ���пγ̳ɼ�С��60�ֵ�ͬѧ��ѧ�š�������

10����ѯû��ѧȫ���пε�ͬѧ��ѧ�š�������

11����ѯ������һ�ſ���ѧ��Ϊ��01����ͬѧ��ѧ��ͬ��ͬѧ��ѧ�ź�������

12����ѯ��"01"�ŵ�ͬѧѧϰ�Ŀγ���ȫ��ͬ������ͬѧ��ѧ�ź�����

13���ѡ�SC�����С���������ʦ�̵Ŀεĳɼ�������Ϊ�˿γ̵�ƽ���ɼ�

14����ѯûѧ��"����"��ʦ���ڵ���һ�ſγ̵�ѧ������

15����ѯ���ż������ϲ�����γ̵�ͬѧ��ѧ�ţ���������ƽ���ɼ�

16������"01"�γ̷���С��60���������������е�ѧ����Ϣ

17����ƽ���ɼ��Ӹߵ�����ʾ����ѧ����ƽ���ɼ�

18����ѯ���Ƴɼ���߷֡���ͷֺ�ƽ���֣���������ʽ��ʾ���γ�ID���γ�name����߷֣���ͷ֣�ƽ���֣�������

19��������ƽ���ɼ��ӵ͵��ߺͼ����ʵİٷ����Ӹߵ���˳��

20����ѯѧ�����ܳɼ�����������

21����ѯ��ͬ��ʦ���̲�ͬ�γ�ƽ���ִӸߵ�����ʾ

22����ѯ���пγ̵ĳɼ���2������3����ѧ����Ϣ���ÿγ̳ɼ�

23��ͳ�Ƹ��Ƴɼ����������������γ̱��,�γ�����,[100-85],[85-70],[70-60],[0-60]����ռ�ٷֱ�

24����ѯѧ��ƽ���ɼ���������

25����ѯ���Ƴɼ�ǰ�����ļ�¼

26����ѯÿ�ſγ̱�ѡ�޵�ѧ����

27����ѯ��ֻѡ����һ�ſγ̵�ȫ��ѧ����ѧ�ź�����

28����ѯ������Ů������

29����ѯ�����к���"��"�ֵ�ѧ����Ϣ

30����ѯͬ��ͬ��ѧ����������ͳ��ͬ������

31����ѯ1990�������ѧ������(ע��Student����Sage�е�������datetime)

32����ѯÿ�ſγ̵�ƽ���ɼ��������ƽ���ɼ��������У�ƽ���ɼ���ͬʱ�����γ̺Ž�������

33����ѯƽ���ɼ����ڵ��� 85 ������ѧ����ѧ�š�������ƽ���ɼ�

34����ѯ�γ�����Ϊ����ѧ�����ҷ������� 60 ��ѧ�������ͷ���

35����ѯ����ѧ���Ŀγ̼��������������ѧ��û�ɼ���ûѡ�ε������

36����ѯ�κ�һ�ſγ̳ɼ��� 70 �����ϵ��������γ����ƺͷ���

37����ѯ������Ŀγ̣������γ̺ŴӴ�С����

38����ѯ�γ̱��Ϊ"01"�ҿγ̳ɼ���60�����ϵ�ѧ����ѧ�ź�������

39����ÿ�ſγ̵�ѧ������

40����ѯѡ�ޡ���������ʦ���ڿγ̵�ѧ���У��ɼ���ߵ�ѧ����������ɼ�

41����ѯ��ͬ�γ̳ɼ���ͬ��ѧ����ѧ����š��γ̱�š�ѧ���ɼ�

42����ѯÿ�Ź��γɼ���õ�ǰ����

43��ͳ��ÿ�ſγ̵�ѧ��ѡ������������5�˵Ŀγ̲�ͳ�ƣ���Ҫ������γ̺ź�ѡ����������ѯ����������������У���������ͬ�����γ̺���������

44����������ѡ�����ſγ̵�ѧ��ѧ��

45����ѯѡ����ȫ���γ̵�ѧ����Ϣ

46����ѯ��ѧ��������

47����ѯ���ܹ����յ�ѧ��

48����ѯ���ܹ����յ�ѧ��

49����ѯ���¹����յ�ѧ��

50����ѯ���¹����յ�ѧ��

���飺https://zhuanlan.zhihu.com/p/53302593


# 4.��

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
where teacher.tname like '��%';


## 5
select sid,sname from student
where student.sid not in
(select sc.sid from teacher
left join course
on teacher.tid=course.tid
left join sc
on course.cid=sc.cid
where teacher.tname='����');


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
where teacher.tname='����'
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

## 12.����

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


## 13.��




## 14.
select sname from student where sid not in
(select sid from sc
left join course
	on sc.cid=course.cid
left join teacher
	on course.tid=teacher.tid
where tname='����');


# 15.
select t1.sid,sname,avg_score from
(select sid,count(if(score<60,cid,null)),avg(score) as avg_score from sc
group by sid
having count(if(score<60,cid,null))>=2)t1
left join student
on student.sid=t1.sid;

## 16.

1.ԭ��
select 
    sid,if(cid='01',score,100)
from sc
where if(cid='01',score,100)<60
order by if(cid='01',score,100) desc

2.�Ľ�
select sname,t1.sid,score_low from
(select sid,if(cid='01',score,null) as score_low
from sc 
where if(cid='01',score,null)<60)t1
left join student
on student.sid=t1.sid
order by t1.score_low desc,sid;

3.������
select sid,sname from student where sid in
(select sid,from sc where score<60 and cid='01')



## 17.

select sname,avg(score) as avg_score from sc
left join student
on student.sid=sc.sid
group by sc.sid,sname
order by avg_score desc;


## 18.
## �����
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

### ��ȷ��
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


## 21. ���ģ���ӽ�ʦ����

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
    ,count(if(score between 85 and 100,sid,null))/count(sid) as '����'
    ,count(if(score between 70 and 85,sid,null))/count(sid) as '����'
    ,count(if(score between 60 and 70,sid,null))/count(sid) as '����'
    ,count(if(score between 0 and 60,sid,null))/count(sid) as '������'
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


## 26.��

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
where sname like '%��%'; 


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



## 33����ѯƽ���ɼ����ڵ��� 85 ������ѧ����ѧ�š�������ƽ���ɼ�
select a.sid,sname,avg(score) from student a
left join sc b
on a.sid=b.sid
group by sid
having avg(score)>85;



34����ѯ�γ�����Ϊ����ѧ�����ҷ������� 60 ��ѧ�������ͷ���

����һ:

select a.sid,sname,score from student a
left join sc b
on a.sid=b.sid
left join course c
on c.cid=b.cid
where cname='��ѧ' and score<60;

������:

select student.sname, sc.score from student, sc, course
where student.sid = sc.sid
and course.cid = sc.cid
and course.cname = "��ѧ"
and sc.score < 60;


35����ѯ����ѧ���Ŀγ̼��������������ѧ��û�ɼ���ûѡ�ε������

select a.sid,sname,cid,score from student a
left join sc b
on a.sid=b.sid;

36����ѯ�κ�һ�ſγ̳ɼ��� 70 �����ϵ��������γ����ƺͷ���

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


## 39 ��ÿ�ſγ̵�ѧ������

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
where tname='����'
order by score desc
limit 1;


## 41.��ѯ��ͬ�γ̳ɼ���ͬ��ѧ����ѧ����š��γ̱�š�ѧ���ɼ�


select distinct a.sid,a.cid,a.score from sc as a
inner join sc as b
on a.sid=b.sid
and a.cid!=b.cid
and a.score=b.score
group by cid,sid;



## 42 ��ѯÿ�Ź��γɼ���õ�ǰ����

����һ:

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

������:

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

select sid,count(cid) as '�γ���' from sc
group by sid
having count(cid)>=2;

## 45 �ο�12��

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





























