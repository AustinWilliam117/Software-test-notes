### where子句小练习

1. 满足价格大于等于9的所有信息

   ```sql
   select * from order_info_table where price >= 9;
   ```

2. 查找满足product_id在1002和1003之间的

   ```sql
   select * from order_info_table where product_id between 1002 and 1003;
   ```

3. 查找user_id在1、3、5这三个数内的信息

   ```sql
   select * from user_info_table where user_id in (1,3,5);
   ```

4. 查找订单状态是已支付的信息

   ```sql
   select * from order_info_table where order_status = "pay";
   ```

5. 查找用户名类似于已li开头的信息

   ```sql
   select * from user_info_table where user_name like "li%";
   ```

6. 查找用户名中第二个字母是h的信息

   ```sql
   select * from user_info_table where user_name like "_h%";
   ```

7. 查找用户名中第二个字母不是h的信息

   ```sql
   select * from user_info_table where user_name not like "_h%";
   ```

8. 查找用户名中最后一个字母以i结尾的信息

   ```sql
   select * from user_info_table where user_name like "%i";
   ```

9. 查找价格大于8，并且订单状态是已支付的所有信息

   ```sql
   select * from order_info_table where price > 8 and order_status = "pay";
   ```

10. 查找用户表中user_nick为null的信息

    ```sql
    select * from user_info_table where user_nick is null;
    ```

11. 查找用户表中user_nick为 not null的信息

    ```sql
    select * from user_info_table where user_nick is not null;
    ```

### 聚合函数练习

1. 查找订单表中最大的价格，查找订单表中最小的价格

   ```sql
   select min(price),max(price) from order_info_table;
   ```

2. 查找订单表中user_id=2的最小价格

   ```sql
   select min(price) from order_info_table where user_id = 2;
   ```

3. 分别列出订单表中user_id=2的最小价格和最大价格

   ```sql
   select min(price),max(price) from order_info_table where user_id = 2;
   ```

4. 分别列出订单表中user_id=2的最小价格和最大价格，并把最小价格的展示结果的列名改为"min_price"

   ```sql
   select min(price) as min_price,max(price) from order_info_table where user_id = 2;
   ```

5. 求订单表的价格的平均值，求订单表中user_id=2的价格的平均值

   ```sql
   select avg(price) from order_info_table;
   select avg(price) from order_info_table where user_id = 2;
   ```

6. 分别列出订单表中user_id=2的价格的平均值、最小值、最大值

   ```sql
   select avg(price), min(price), max(price) from order_info_table where user_id = 2;
   ```

7. 求订单表中user_id=1的价格的总和

   ```sql
   select sum(price) from order_info_table where user_id = 2;
   ```

8. 求订单表中user_id=1或者user_id=3的价格总和

   ```sql
   select sum(price) from order_info_table where user_id = 1 and user_id = 3;
   ```

### 分组练习

1. 首先筛选状态为已支付的订单，然后按照user_id分组，分组后每一组对支付金额进行求 和，最终展示user_id和对应组求和金额

   ```sql
   select user_id,price from order_info_table where order_status = "pay" group by user_id;
   ```

2. 首先筛选状态为支付的订单，然后按照user_id分组，分组后每一组对支付金额进行求和，再过滤求和金额大于10的，最终展示user_id和对应组的求和金额

   ```sql
   select user_id,price from order_info_table where order_status = "pay" group by user_id having price > 10 [order by desc price];
   ```

### 数据表连接查询和子查询练习

1. 查询订单表中的价格大于10元的用户的昵称（小提示：用户昵称在用户表中，订单价格在订单表中）

   ```sql
   select a.user_nick from user_info_table a INNER JOIN order_info_table b ON a.user_id = b.user_id where b.price > 10;
   ```

   ```sql
   select user_nick from user_info_table where user_id in (select user_id from order_info_table where price > 10);
   ```

2. 查询用户名以l开头的用户买过的所有订单id和对应价格（小提示：订单id和对应价格在订单表中，用户名在用户表中）

   ```sql
   select a.order_id,a.price from order_info_table a INNER JOIN user_info_table b ON a.user_id = b.user_id where user_name like 'l%';
   ```

   ```sql
   select order_id,price from order_info_table where user_id in (select user_id from user_info_table where user_name like "l%");
   ```

   