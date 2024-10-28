SELECT  a
       ,round(SUM(diff)/3600,2) AS d
FROM
(
	SELECT  a
	       ,apply_time
	       ,pass_time
	       ,dates
	       ,rn
	       ,ct
	       ,is_work
	       ,CASE WHEN is_work = 1 AND rn = 1 THEN unix_timestamp(concat(dates,' 18:30:00'),'yyyy-MM-dd HH:mm:ss')-unix_timestamp(apply_time,'yyyy-MM-dd HH:mm:ss')
	             WHEN is_work = 0 THEN 0
	             WHEN is_work = 1 AND rn = ct THEN unix_timestamp(pass_time,'yyyy-MM-dd HH:m m:ss')-unix_timestamp(concat(dates,' 09:30:00'),'yyyy-MM-dd HH:mm:ss')
	             WHEN is_work = 1 AND rn != ct THEN 9*3600 END diff
	FROM
	(
		SELECT  a
		       ,apply_time
		       ,pass_time
		       ,time_diff
		       ,day_diff
		       ,rn
		       ,ct
		       ,date_add(start,rn-1) dates
		FROM
		(
			SELECT  a
			       ,apply_time
			       ,pass_time
			       ,time_diff
			       ,day_diff
			       ,strs
			       ,start
			       ,ROW_NUMBER() over(PARTITION BY a)                      AS rn
			       ,COUNT(*) over(PARTITION BY a) AS ct
			FROM
			(
				SELECT  a
				       ,apply_time
				       ,pass_time
				       ,time_diff
				       ,day_diff
				       ,substr(repeat(concat(substr(apply_time,1,10),','),day_diff+1),1,11*(day_diff+1)-1) strs
				FROM
				(
					SELECT  a
					       ,apply_time
					       ,pass_time
					       ,unix_timestamp(pass_time,'yyyy-MM-dd HH:mm:ss')-unix_timestamp(apply_time,'yyyy-MM-dd HH:mm:ss') time_diff
					       ,DATEDIFF(substr(pass_time,1,10),substr(apply_time,1,10)) day_diff
					FROM
					(
						SELECT  a
						       ,MAX(case WHEN b = '申请' THEN c end) apply_time
						       ,MAX(case WHEN b = '通过' THEN c end) pass_time
						FROM t14
						GROUP BY  a
					) tmp1
				) tmp2
			) tmp3 lateral view explode(split(strs, ",")) t AS start
		) tmp4
	) tmp5
	JOIN d_date
	ON tmp5.dates = d_date.date_id
) tmp6
GROUP BY  a;