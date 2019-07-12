

在main 函数的class 上增加注解 @EnableScheduling



然后编写 scheduler 任务类（@Component） 



任务类的方法上加 @Scheduled  注解

 @Scheduled（调度方式相关参数）





默认为单线程调用。

@Scheduled(cron = "*/1 * * * * ?") 

@Scheduled(fixedDelay = 1000)			// 本次执行结束后，与下次开始的时间间隔

 @Scheduled(fixedRate = 1000)				//本次开始执行与下次开始执行的时间间隔



fixedDelay，fixedRate  单位 ms





**@Scheduled(fixedRate)	如何避免任务被阻塞**

注解`@EnableAsync`（类上）和`@Async`（方法上）

