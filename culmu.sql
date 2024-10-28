SELECT  date_id
       ,date_add(date_start_id,pos) AS date_to_day
FROM
(
	SELECT  date_id
	       ,date_sub(date_id,dayofmonth(date_id)-1) AS date_start_id
	FROM t17
) m lateral view posexplode(split(space(datediff(from_unixtime(unix_timestamp(date_id, 'yyyy-MM-dd')), from_unixtime(unix_timestamp(date_start_id, 'yyyy-MM-dd')))), '')) t AS pos, val;

SELECT  a
       ,b
       ,c
       ,SUM(c) over(PARTITION BY a ORDER BY  b) AS d
FROM
(
	SELECT  t1.a
	       ,t1.b
	       ,CASE WHEN t18.b is not null THEN t18.c  ELSE 0 END AS c
	FROM
	(
		SELECT  a
		       ,date_add(s,pos) AS b
		FROM
		(
			SELECT  a
			       ,'2018-01-01' AS s
			       ,'2018-01-07' AS r
			FROM
			(
				SELECT  a
				FROM t18
				GROUP BY  a
			) ta
		) m lateral view posexplode(split(space(datediff(from_unixtime(unix_timestamp(r, 'yyyy-MM-dd')), from_unixtime(unix_timestamp(s, 'yyyy-MM-dd')))), '')) t AS pos, val
	) t1
	LEFT JOIN t18
	ON t1.a = t18.a AND t1.b = t18.b
) ts;

SELECT  date_id
       ,first_value(a) over(PARTITION BY aa ORDER BY  date_id) AS a
       ,first_value(b) over(PARTITION BY bb ORDER BY date_id)  AS b
       ,first_value(c) over(PARTITION BY cc ORDER BY date_id)  AS c
FROM
(
	SELECT  date_id
	       ,a
	       ,b
	       ,c
	       ,COUNT(a) over(order by date_id) AS aa
	       ,COUNT(b) over(order by date_id) AS bb
	       ,COUNT(c) over(order by date_id) AS cc
	FROM t20
)tmp1;

SELECT  tt1.date_id
       ,tt2.user_cnt_act
       ,tt1.user_cnt_act_month
FROM
( -- ④ 按照 t.date_id 分组求出 user_cnt_act_month，得到 tt1 
	SELECT  t.date_id
	       ,COUNT(user_id) AS user_cnt_act_month
	FROM
	( -- ③ 表 a 和表 b 进行笛卡尔积，按照 a.date_id, b.user_id 分组，保证截止到当日的用户唯一， 
 得出表 t。
		SELECT  a.date_id
		       ,b.user_id
		FROM
		( -- ① 按照日期分组，取出 date_id 字段当主表的维度字段 得出表 a 
			SELECT  from_unixtime(unix_timestamp(time_id),'yyyy-MM-dd') AS date_id
			FROM test.temp_tanhaidi_20211213_1
			GROUP BY  from_unixtime(unix_timestamp(time_id),'yyyy-MM-dd')
		) a
		INNER JOIN
		( -- ② 按照 date_id、user_id 分组，保证每天每个用户只有一条记录，得出表 b 
			SELECT  from_unixtime(unix_timestamp(time_id),'yyyy-MM-dd') AS date_id
			       ,user_id
			FROM test.temp_tanhaidi_20211213_1
			GROUP BY  from_unixtime(unix_timestamp(time_id),'yyyy-MM-dd')
			         ,user_id
		) b
		ON 1 = 1
		WHERE a.date_id >= b.date_id
		GROUP BY  a.date_id
		         ,b.user_id
	) t
	GROUP BY  t.date_id
) tt1
LEFT JOIN
( -- ⑥ 按照 date_id 分组求出 user_cnt_act，得到 tt2 
	SELECT  date_id
	       ,COUNT(user_id) AS user_cnt_act
	FROM
	( -- ⑤ 按照日期分组，取出 date_id 字段当主表的维度字段 得出表 a 
		SELECT  from_unixtime(unix_timestamp(time_id),'yyyy-MM-dd') AS date_id
		       ,user_id
		FROM test.temp_tanhaidi_20211213_1
		GROUP BY  from_unixtime(unix_timestamp(time_id),'yyyy-MM-dd')
		         ,user_id
	) a
	GROUP BY  date_id
) tt2
ON tt2.date_id = tt1.date_id




SELECT  a.brand
       ,SUM(a.market_day) matket_day
FROM
(
	SELECT  f.brand
	       ,CASE WHEN f.col_date is null THEN f.enddate - f.startdate +1
	             WHEN f.startdate <= f.col_date THEN f.enddate - f.col_date  
                 ELSE f.enddate - f.startdate + 1 END market_day
	FROM
	(
		SELECT  t.*
             --取同组的上一条记录
		       ,lag(t.enddate,1,null) OVER (PARTITION BY t.brand ORDER BY  t.startdate) col_date
		FROM marketing t
	) f
) a
GROUP BY  a.brand;




sql (
SELECT  Sales.product_id
       ,product_name
       ,'2018' AS 'report_year'
       ,if(period_start < '2019-01-01',(datediff(if(period_end < '2019-01-01',period_end,date('2018-12-31')),if(period_start >= '2018-01-01',period_start,date('2018-01-01')))+1)*average_daily_sales,0) AS total_amount
FROM Sales
JOIN Product
ON Sales.product_id = Product.product_id
HAVING total_amount > 0 ) union(
SELECT  Sales.product_id
       ,product_name
       ,'2019' AS 'report_year'
       ,if( period_start < '2020-01-01',(datediff(if(period_end < '2020-01-01',period_end,date('2019-12-31')),if(period_start >= '2019-01-01',period_start,date('2019-01-01')))+1)*average_daily_sales ,0) AS total_amount
FROM Sales
JOIN Product
ON (Sales.product_id = Product.product_id )
HAVING total_amount > 0 ) union(
SELECT  Sales.product_id
       ,product_name
       ,'2020' AS 'report_year'
       ,(datediff(if(period_end < '2021-01-01',period_end,date('2020-12-31')),if(period_start >= '2020-01-01',period_start,date('2020-01-01')))+1)*average_daily_sales AS total_amount
FROM Sales
JOIN Product
ON (Sales.product_id = Product.product_id)
HAVING total_amount > 0 )
ORDER BY product_id, report_year



--活跃用户，至少联系登录5天及以上
sql
select t3.id,name
from 
(
    select distinct id
    from 
    (
        select id,login_date,lead(login_date,4,null) over(partition by id order by login_date) ld
        from 
        (
            select id,login_date 
            from Logins
            group by id,login_date
        )t1
    )t2
    where datediff(ld,login_date)=4
)t3
left join Accounts a
on t3.id = a.id