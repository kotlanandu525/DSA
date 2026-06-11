# Write your MySQL query statement below

select department,employee,salary
from(
    select d.name as department,e.name as Employee,e.salary as salary,
dense_rank() over(partition by d.name order by salary desc) as rk
from employee e join department d on e.departmentId=d.id )
as rank_table where rk<=3