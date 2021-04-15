### where子句小练习

1. 满足价格大于等于9的所有信息

   ```sql
   select * from order_info_table where price >= 9;
   +------------+-------+--------------+------------+---------------------+---------+
   | order_id   | price | order_status | product_id | created             | user_id |
   +------------+-------+--------------+------------+---------------------+---------+
   | 0000000002 |  9.99 | nopay        |       1002 | 2019-09-26 10:25:26 |       1 |
   | 0000000004 |  9.99 | nopay        |       1002 | 2019-09-24 10:25:26 |       2 |
   | 0000000005 | 19.99 | pay          |       1003 | 2019-09-26 10:25:26 |       2 |
   | 0000000008 |  9.99 | pay          |       1002 | 2019-09-25 10:25:26 |       4 |
   | 0000000009 | 19.99 | pay          |       1003 | 2019-09-26 10:25:26 |       4 |
   | 0000000010 | 29.99 | pay          |       1002 | 2019-09-26 10:25:26 |       6 |
   +------------+-------+--------------+------------+---------------------+---------+
   6 rows in set (0.039 sec)
   ```

2. 查找满足product_id在1002和1003之间的

   ```sql
   select * from order_info_table where product_id between 1002 and 1003;
   +------------+-------+--------------+------------+---------------------+---------+
   | order_id   | price | order_status | product_id | created             | user_id |
   +------------+-------+--------------+------------+---------------------+---------+
   | 0000000002 |  9.99 | nopay        |       1002 | 2019-09-26 10:25:26 |       1 |
   | 0000000004 |  9.99 | nopay        |       1002 | 2019-09-24 10:25:26 |       2 |
   | 0000000005 | 19.99 | pay          |       1003 | 2019-09-26 10:25:26 |       2 |
   | 0000000008 |  9.99 | pay          |       1002 | 2019-09-25 10:25:26 |       4 |
   | 0000000009 | 19.99 | pay          |       1003 | 2019-09-26 10:25:26 |       4 |
   | 0000000010 | 29.99 | pay          |       1002 | 2019-09-26 10:25:26 |       6 |
   +------------+-------+--------------+------------+---------------------+---------+
   6 rows in set (0.039 sec)
   ```

3. 查找user_id在1、3、5这三个数内的信息

   ```sql
   select * from user_info_table where user_id in (1,3,5);
   +---------+-----------+----------+--------------+--------------------+
   | user_id | user_name | password | user_nick    | card_num           |
   +---------+-----------+----------+--------------+--------------------+
   |       1 | zhangsan  | abc123   | zhangsanfeng | 124567894651329785 |
   |       3 | wangwu    | 123aaa   | NULL         | 214567894651324567 |
   |       5 | zhangliu  | 12aaa    | zhangwuji    | 214563356658966567 |
   +---------+-----------+----------+--------------+--------------------+
   3 rows in set (0.037 sec)
   ```

4. 查找订单状态是已支付的信息

   ```sql
   select * from order_info_table where order_status = "pay";
   +------------+-------+--------------+------------+---------------------+---------+
   | order_id   | price | order_status | product_id | created             | user_id |
   +------------+-------+--------------+------------+---------------------+---------+
   | 0000000001 |  4.99 | pay          |       1001 | 2019-09-25 10:25:26 |       1 |
   | 0000000005 | 19.99 | pay          |       1003 | 2019-09-26 10:25:26 |       2 |
   | 0000000006 |  4.99 | pay          |       1001 | 2019-09-25 10:25:26 |       3 |
   | 0000000007 |  4.99 | pay          |       1001 | 2019-09-24 10:25:26 |       4 |
   | 0000000008 |  9.99 | pay          |       1002 | 2019-09-25 10:25:26 |       4 |
   | 0000000009 | 19.99 | pay          |       1003 | 2019-09-26 10:25:26 |       4 |
   | 0000000010 | 29.99 | pay          |       1002 | 2019-09-26 10:25:26 |       6 |
   +------------+-------+--------------+------------+---------------------+---------+
   7 rows in set (0.049 sec)
   ```

5. 查找用户名类似于已li开头的信息

   ```sql
   select * from user_info_table where user_name like "li%";
   +---------+-----------+----------+-----------+--------------------+
   | user_id | user_name | password | user_nick | card_num           |
   +---------+-----------+----------+-----------+--------------------+
   |       2 | lisi      | 122bbb   | limochou  | 124567894651324567 |
   |       4 | liuqi     | 12aaa    | NULL      | 214563356651324567 |
   +---------+-----------+----------+-----------+--------------------+
   2 rows in set (0.041 sec)
   ```

6. 查找用户名中第二个字母是h的信息

   ```sql
   select * from user_info_table where user_name like "_h%";
   +---------+-----------+----------+--------------+--------------------+
   | user_id | user_name | password | user_nick    | card_num           |
   +---------+-----------+----------+--------------+--------------------+
   |       1 | zhangsan  | abc123   | zhangsanfeng | 124567894651329785 |
   |       5 | zhangliu  | 12aaa    | zhangwuji    | 214563356658966567 |
   +---------+-----------+----------+--------------+--------------------+
   2 rows in set (0.041 sec)
   ```

7. 查找用户名中第二个字母不是h的信息

   ```sql
   select * from user_info_table where user_name not like "_h%";
   +---------+-----------+----------+-----------+--------------------+
   | user_id | user_name | password | user_nick | card_num           |
   +---------+-----------+----------+-----------+--------------------+
   |       2 | lisi      | 122bbb   | limochou  | 124567894651324567 |
   |       3 | wangwu    | 123aaa   | NULL      | 214567894651324567 |
   |       4 | liuqi     | 12aaa    | NULL      | 214563356651324567 |
   +---------+-----------+----------+-----------+--------------------+
   3 rows in set (0.038 sec)
   ```

8. 查找用户名中最后一个字母以i结尾的信息

   ```sql
   select * from user_info_table where user_name like "%i";
   +---------+-----------+----------+-----------+--------------------+
   | user_id | user_name | password | user_nick | card_num           |
   +---------+-----------+----------+-----------+--------------------+
   |       2 | lisi      | 122bbb   | limochou  | 124567894651324567 |
   |       4 | liuqi     | 12aaa    | NULL      | 214563356651324567 |
   +---------+-----------+----------+-----------+--------------------+
   2 rows in set (0.039 sec)
   ```

9. 查找价格大于8，并且订单状态是已支付的所有信息

   ```sql
   select * from order_info_table where price > 8 and order_status = "pay";
   +------------+-------+--------------+------------+---------------------+---------+
   | order_id   | price | order_status | product_id | created             | user_id |
   +------------+-------+--------------+------------+---------------------+---------+
   | 0000000005 | 19.99 | pay          |       1003 | 2019-09-26 10:25:26 |       2 |
   | 0000000008 |  9.99 | pay          |       1002 | 2019-09-25 10:25:26 |       4 |
   | 0000000009 | 19.99 | pay          |       1003 | 2019-09-26 10:25:26 |       4 |
   | 0000000010 | 29.99 | pay          |       1002 | 2019-09-26 10:25:26 |       6 |
   +------------+-------+--------------+------------+---------------------+---------+
   4 rows in set (0.037 sec)
   ```

10. 查找用户表中user_nick为null的信息

    ```sql
    select * from user_info_table where user_nick is null;
    +---------+-----------+----------+-----------+--------------------+
    | user_id | user_name | password | user_nick | card_num           |
    +---------+-----------+----------+-----------+--------------------+
    |       3 | wangwu    | 123aaa   | NULL      | 214567894651324567 |
    |       4 | liuqi     | 12aaa    | NULL      | 214563356651324567 |
    +---------+-----------+----------+-----------+--------------------+
    2 rows in set (0.038 sec)
    ```

11. 查找用户表中user_nick为 not null的信息

    ```sql
    select * from user_info_table where user_nick is not null;
    +---------+-----------+----------+--------------+--------------------+
    | user_id | user_name | password | user_nick    | card_num           |
    +---------+-----------+----------+--------------+--------------------+
    |       1 | zhangsan  | abc123   | zhangsanfeng | 124567894651329785 |
    |       2 | lisi      | 122bbb   | limochou     | 124567894651324567 |
    |       5 | zhangliu  | 12aaa    | zhangwuji    | 214563356658966567 |
    +---------+-----------+----------+--------------+--------------------+
    3 rows in set (0.044 sec)
    ```

### 聚合函数练习

1. 查找订单表中最大的价格，查找订单表中最小的价格

   ```sql
   select min(price),max(price) from order_info_table;
   +------------+------------+
   | min(price) | max(price) |
   +------------+------------+
   |       4.99 |      29.99 |
   +------------+------------+
   1 row in set (0.037 sec)
   ```

2. 查找订单表中user_id=2的最小价格

   ```sql
   select min(price) from order_info_table where user_id = 2;
   +------------+
   | min(price) |
   +------------+
   |       4.99 |
   +------------+
   1 row in set (0.036 sec)
   ```

3. 分别列出订单表中user_id=2的最小价格和最大价格

   ```sql
   select min(price),max(price) from order_info_table where user_id = 2;
   +------------+------------+
   | min(price) | max(price) |
   +------------+------------+
   |       4.99 |      19.99 |
   +------------+------------+
   1 row in set (0.037 sec)
   ```

4. 分别列出订单表中user_id=2的最小价格和最大价格，并把最小价格的展示结果的列名改为"min_price"

   ```sql
   select min(price) as min_price,max(price) from order_info_table where user_id = 2;
   +-----------+------------+
   | min_price | max(price) |
   +-----------+------------+
   |      4.99 |      19.99 |
   +-----------+------------+
   1 row in set (0.039 sec)
   ```

5. 求订单表的价格的平均值，求订单表中user_id=2的价格的平均值

   ```sql
   select avg(price) from order_info_table;
   +------------+
   | avg(price) |
   +------------+
   |  11.990000 |
   +------------+
   1 row in set (0.046 sec)
   
   select avg(price) from order_info_table where user_id = 2;
   +------------+
   | avg(price) |
   +------------+
   |  11.656667 |
   +------------+
   1 row in set (0.039 sec)
   ```

6. 分别列出订单表中user_id=2的价格的平均值、最小值、最大值

   ```sql
   select avg(price), min(price), max(price) from order_info_table where user_id = 2;
   +------------+------------+------------+
   | avg(price) | min(price) | max(price) |
   +------------+------------+------------+
   |  11.656667 |       4.99 |      19.99 |
   +------------+------------+------------+
   1 row in set (0.041 sec)
   ```

7. 求订单表中user_id=1的价格的总和

   ```sql
   select sum(price) from order_info_table where user_id = 2;
   +------------+
   | sum(price) |
   +------------+
   |      34.97 |
   +------------+
   1 row in set (0.040 sec)
   ```

8. 求订单表中user_id=1或者user_id=3的价格总和

   ```sql
   select sum(price) from order_info_table where user_id = 1 or user_id = 3;
   +------------+
   | sum(price) |
   +------------+
   |      19.97 |
   +------------+
   1 row in set (0.038 sec)
   ```

### 分组练习

1. 首先筛选状态为已支付的订单，然后按照user_id分组，分组后每一组对支付金额进行求 和，最终展示user_id和对应组求和金额

   ```sql
   select user_id,sum(price) from order_info_table where order_status = "pay" group by user_id;
   +---------+------------+
   | user_id | sum(price) |
   +---------+------------+
   |       1 |       4.99 |
   |       2 |      19.99 |
   |       3 |       4.99 |
   |       4 |      34.97 |
   |       6 |      29.99 |
   +---------+------------+
   5 rows in set (0.042 sec)
   ```

2. 首先筛选状态为支付的订单，然后按照user_id分组，分组后每一组对支付金额进行求和，再过滤求和金额大于10的，最终展示user_id和对应组的求和金额

   ```sql
   select user_id,sum(price) from order_info_table where order_status = "pay" group by user_id having sum(price) > 10 [order by sum(price) desc];
   +---------+------------+
   | user_id | sum(price) |
   +---------+------------+
   |       2 |      19.99 |
   |       4 |      34.97 |
   |       6 |      29.99 |
   +---------+------------+
   3 rows in set (0.047 sec)
   ```

### 数据表连接查询和子查询练习

1. 查询订单表中的价格大于10元的用户的昵称（小提示：用户昵称在用户表中，订单价格在订单表中）

   ```sql
   select a.user_nick from user_info_table a INNER JOIN order_info_table b ON a.user_id = b.user_id where b.price > 10;
   +-----------+
   | user_nick |
   +-----------+
   | limochou  |
   | NULL      |
   +-----------+
   2 rows in set (0.043 sec)
   ```

   ```sql
   select user_nick from user_info_table where user_id in (select user_id from order_info_table where price > 10);
   +-----------+
   | user_nick |
   +-----------+
   | limochou  |
   | NULL      |
   +-----------+
   2 rows in set (0.043 sec)
   ```

2. 查询用户名以l开头的用户买过的所有订单id和对应价格（小提示：订单id和对应价格在订单表中，用户名在用户表中）

   ```sql
   select a.order_id,a.price from order_info_table a INNER JOIN user_info_table b ON a.user_id = b.user_id where user_name like 'l%';
   +------------+-------+
| order_id   | price |
   +------------+-------+
   | 0000000003 |  4.99 |
   | 0000000004 |  9.99 |
| 0000000005 | 19.99 |
   | 0000000007 |  4.99 |
   | 0000000008 |  9.99 |
   | 0000000009 | 19.99 |
   +------------+-------+
   6 rows in set (0.038 sec)
   ```
   
   ```sql
   select order_id,price from order_info_table where user_id in (select user_id from user_info_table where user_name like "l%");
   +------------+-------+
   | order_id   | price |
   +------------+-------+
   | 0000000003 |  4.99 |
   | 0000000004 |  9.99 |
   | 0000000005 | 19.99 |
   | 0000000007 |  4.99 |
   | 0000000008 |  9.99 |
   | 0000000009 | 19.99 |
   +------------+-------+
   6 rows in set (0.066 sec)
   ```
   
   