wsimport: jdk 自带的工具

wsimport -keep url(url为wsdl文件的路径，本地路径或网络路径 )生成客户端代码



[http://www.webxml.com.cn](http://www.webxml.com.cn/)

天气接口调用：<https://blog.csdn.net/w410589502/article/details/51802483>

首先我们将网页打开的wsdl文件保存到本地

修改wsdl文档的部分内容:将 **<s:element ref="s:schema" /><s:any />** 替换成 **<s:any minOccurs="2" maxOccurs="2"/>**

执行wsimport生成代码

将源码加到工程

编写测试请求代码：



```java
package cn.com.webxml;

import java.util.List;

import cn.com.webxml.GetSupportDataSetResponse.GetSupportDataSetResult;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		WeatherWebService impl = new WeatherWebService();
		System.out.println(impl.getServiceName());
		WeatherWebServiceSoap  w =impl.getWeatherWebServiceSoap();

//        //调用WeatherWebServiceSoap提供的getWeather方法获取天气预报情况
//        ArrayOfString response = w.getSupportProvince();	// 省份列表
//        ArrayOfString response = w.getSupportCity("四川"); // 省内各市的数据
//        ArrayOfString response = w.getSupportCity("成都");  // 查不到数据
        ArrayOfString response = w.getWeatherbyCityName("成都"); 
	     
        List<String> responseList = response.getString();
        //遍历天气预报信息
        System.out.println("------------------------");
        for (String string : responseList) {
            System.out.println(string);            
        }
        System.out.println("------------------------");
        GetSupportDataSetResult response2 = w.getSupportDataSet();
        List<Object> list = response2.getAny();
        System.out.println("------------------------");
        for (Object string : list) {
            System.out.println(string);            
        }
        System.out.println("------------------------");       
	}

}

```

