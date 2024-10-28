drop TABLE IF EXISTS dim_date;

CREATE TABLE if not exists dim_date( `date` string comment '日期', d_week string comment '年内第几周', weeks string comment '周几', w_start string comment '周开始日', w_end string comment '周结束日', d_month string comment '第几月', m_start string comment '月开始日', m_end string comment '月结束日', d_quarter int comment '第几季', q_start string comment '季开始日', q_end string comment '季结束日', d_year int comment '年份', y_start string comment '年开始日', y_end string comment '年结束日' );
--自然月: 指每月的 1 号到那个月的月底，它是按照阳历来计算的。就是从每月 1 号到月底，不管这个月 有 30 天，31 天，29 天或者 28 天，都算是一个自然月。
INSERT OVERWRITE TABLE dim_date
SELECT  `date`
       ,d_week --年内第几周 
       ,case weekid WHEN 0 THEN '周日' WHEN 1 THEN '周一' WHEN 2 THEN '周二' WHEN 3 THEN '周三' WHEN 4 THEN '周四' WHEN 5 THEN '周五' WHEN 6 THEN '周六' end AS weeks -- 周 
       ,date_add(next_day(`date`,'MO'),-7)                                                                                                     AS w_start --周一 
       ,date_add(next_day(`date`,'MO'),-1)                                                                                                     AS w_end -- 周日_end
-- 月份日期 
       ,concat('第',monthid,'月')                                                                                                                AS d_month
       ,m_start
       ,m_end
-- 季节 
       ,quarterid                                                                                                                              AS d_quart
       ,concat(d_year,'-',substr(concat('0',(quarterid - 1) * 3 + 1),-2),'-01')                                                                AS q_start --季开始日 
       ,date_sub(concat(d_year,'-',substr(concat('0',(quarterid) * 3 + 1),-2),' -01'),1)                                                       AS q_end --季结束日
-- 年 
       ,d_year
       ,y_start
       ,y_end
FROM
(
	SELECT  `date`
	       ,pmod(datediff(`date`,'2012-01-01'),7)                      AS weekid
	--获取周几 
	       ,cast(substr(`date`,6,2) AS int)                            AS monthid
	--获取月份 
	       ,CASE WHEN cast(substr(`date`,6,2)                          AS int) <= 3 THEN 1
	             WHEN cast(substr(`date`,6,2)                          AS int) <= 6 THEN 2
	             WHEN cast(substr(`date`,6,2)                          AS int) <= 9 THEN 3
	             WHEN cast(substr(`date`,6,2) AS int) <= 12 THEN 4 END AS quarterid
	--获取季节 可以直接使用 quarter(`date`) 
	       ,substr(`date`,1,4)                                         AS d_year
	-- 获取年份 
	       ,trunc(`date`,'YYYY')                                       AS y_start
	--年开始日 
	       ,date_sub(trunc(add_months(`date`,12),'YYYY'),1)            AS y_end --年 
 结束日
	       ,date_sub(`date`,dayofmonth(`date`) - 1)                    AS m_start
	--当月第一天 
	       ,last_day(date_sub(`date`,dayofmonth(`date`) - 1)) m_end
	--当月最后一天 
	       ,weekofyear(`date`)                                         AS d_week
	--年内第几周 
	FROM
	(
		-- '2021-04-01'是开始日期, '2022-03-31'是截止日期 
		SELECT  date_add('2021-04-01',t0.pos) AS `date`
		FROM
		(
			SELECT  posexplode( split( repeat('o',DATEDIFF( from_unixtime(unix_timestamp('2022-03-31','yyyy-mm-dd'),'yyyy-mm-dd '),'2021-04-01')),'o' ) )
		) t0
	) t1
) t2