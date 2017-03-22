
# 简介
为了从编辑网页测试用例的繁琐中解放出来，编写具有自动转换功能的脚本。
其中testenv.py中进行总体配置，包括custom_fields，产品需求的`req_spec_title`等字段，测试用例包括:
1. 测试用例名称(以#开头)
2. 摘要(以##开头)
3. 前提条件， 以@@开头，如@@ Precondition: e.g.提交《测试报告》
4. 测试步骤，其中测试步骤与测试期望结果之间采用`&&`作为分割；其中测试步骤可以分为多行，但是测试期望当前与 && 必须在一行才有效，否则会导致测试用例生成错误
5. 产品需求，以@开头，其中主要包括`doc_id：title`, 而`req_spec_title`因为比较统一，当前在`testenv.py`中进行统一设置，
例如：`REQ-YHWD-1-1:提交测试文档`，需要注意的是中间通过":"分隔`doc_id` 和`title`, 而且`REQ-YHWD-1-1`必须已经在当前测试用例集合中存在，否则此requirement全部无效
6. 测试用例之间采用*空白行*进行区分。

#下面举个栗子：
### 如测试用例testcase.txt 内容如下：

```
# 测试用例名字
## 测试用例摘要
测试步骤Step1：do some thing　
输入数据：what's the hehe   &&  期望的结果,当前期望结果只能在一行
测试步骤Step2 ：做一些事情 && step2 excepted result，呵呵
看着办吧  && step3 excepted result
测试步骤Step3：do some thing　
输入数据：what the fuck   
&&  期望的结果,当前期望结果只能在一行
@REQ-YHWD-1-1:提交测试文档，需求可有可无

# 测试用例名字
##  The test case target or summary
@@ Precondition: e.g.提交《测试报告》/《测试用例执行报告》或其他测试报告类文档
测试步骤Step1：现在是可以分行写的
输入数据：what's that?
&&  期望的结果
测试步骤Step2 ：做一些事情 && step2 excepted result
看着办吧  && step3 excepted result


# 测试用例名字，不能重复，否则会自动重命名
## 测试用例摘要
测试步骤Step1：do some thing　输入数据：what the fuck   &&  期望的结果
测试步骤Step2 ：做一些事情 && step2 excepted result
看着办吧  && step3 excepted result
@REQ-YHWD-1-2:提交测试文档
```

### 配置在testenv.py中配置综合属性：

```python
custom_fields['测试用例-检测参数'] = "功能"
EXCUTION_TYPE = ExceutionType.MANUAL
req_spec_title = "用户文档测试"
custom_fields['测试环境需求-测试用例'] = \
'''
测试机:兆芯C1  
硬件配置:
    型号：兆芯C 
    CPU：C-QuadCore C4600@2.0GHz 4核 
    内存：8192MB
    硬盘：200G     
软件配置:
    操作系统：cdos 1.10.0 - 0728 
    中间件：wine1.8.5
'''
```


### 然后运行`python generator.py testcase.txt`
将会生成testcase.txt.xml， xml内容如下：

```xml
<?xml version='1.0' encoding='utf8'?>
<testcases><testcase name="测试用例名字"><summary> 测试用例摘要</summary>
<preconditions>Precondition: e.g.提交《测试报告》/《测试用例执行报告》或其他测试报告类文档</preconditions>
<steps><step><step_number>1</step_number>
<actions>&lt;p&gt;测试步骤Step1：do some thing　
&lt;/p&gt;
&lt;p&gt;输入数据：what the fuck   </actions>
<expectedresults>  期望的结果,当前期望结果只能在一行
&lt;/p&gt;</expectedresults>
<execution_type>1</execution_type>
</step>
<step><step_number>2</step_number>
<actions>测试步骤Step2 ：做一些事情 </actions>
<expectedresults> step2 excepted result，呵呵</expectedresults>
<execution_type>1</execution_type>
</step>
<step><step_number>3</step_number>
<actions>&lt;p&gt;测试步骤Step3：do some thing　
&lt;/p&gt;
&lt;p&gt;输入数据：1 2 3 4 5 5 </actions>
<expectedresults>  期望的结果,当前期望结果只能在一行
&lt;/p&gt;</expectedresults>
<execution_type>1</execution_type>
</step>
</steps>
<custom_fields><custom_field><name>测试用例-检测参数</name>
<value>功能</value>
</custom_field>
<custom_field><name>测试环境需求-测试用例</name>
<value>
测试机:兆芯C1  
硬件配置:
    型号：兆芯C 
    CPU：C-QuadCore C4600@2.0GHz 4核 
    内存：8192MB
    硬盘：200G     
软件配置:
    操作系统：cdos 1.10.0 - 0728 
    中间件：wine1.8.5
</value>
</custom_field>
<custom_field><name>测试用例设计日期</name>
<value>1482192000</value>
</custom_field>
</custom_fields>
<requirements><requirement><req_spec_title>[用户文档测试]</req_spec_title>
<doc_id>REQ-YHWD-1-1</doc_id>
<title>提交测试文档，需求可有可无
</title>
</requirement>
</requirements>
</testcase>
<testcase name="测试用例名字"><summary>  The test case target or summary</summary>
<preconditions>Precondition: e.g.提交《测试报告》/《测试用例执行报告》或其他测试报告类文档</preconditions>
<steps><step><step_number>1</step_number>
<actions>&lt;p&gt;&lt;p&gt;测试步骤Step1：现在是可以分行写的
&lt;/p&gt;
&lt;p&gt;输入数据：what's that?
&lt;/p&gt;&lt;/p&gt;
&lt;p&gt;</actions>
<expectedresults>  期望的结果
&lt;/p&gt;</expectedresults>
<execution_type>1</execution_type>
</step>
<step><step_number>2</step_number>
<actions>测试步骤Step2 ：做一些事情 </actions>
<expectedresults> step2 excepted result</expectedresults>
<execution_type>1</execution_type>
</step>
<step><step_number>3</step_number>
<actions>看着办吧  </actions>
<expectedresults> step3 excepted result</expectedresults>
<execution_type>1</execution_type>
</step>
</steps>
<custom_fields><custom_field><name>测试用例-检测参数</name>
<value>功能</value>
</custom_field>
<custom_field><name>测试环境需求-测试用例</name>
<value>
测试机:兆芯C1  
硬件配置:
    型号：兆芯C 
    CPU：C-QuadCore C4600@2.0GHz 4核 
    内存：8192MB
    硬盘：200G     
软件配置:
    操作系统：cdos 1.10.0 - 0728 
    中间件：wine1.8.5
</value>
</custom_field>
<custom_field><name>测试用例设计日期</name>
<value>1482192000</value>
</custom_field>
</custom_fields>
<requirements />
</testcase>
<testcase name="测试用例名字2"><summary> 测试用例摘要</summary>
<preconditions />
<steps><step><step_number>1</step_number>
<actions>测试步骤Step1：do some thing　输入数据：what the fuck   </actions>
<expectedresults>  期望的结果</expectedresults>
<execution_type>1</execution_type>
</step>
<step><step_number>2</step_number>
<actions>测试步骤Step2 ：做一些事情 </actions>
<expectedresults> step2 excepted result</expectedresults>
<execution_type>1</execution_type>
</step>
<step><step_number>3</step_number>
<actions>看着办吧  </actions>
<expectedresults> step3 excepted result</expectedresults>
<execution_type>1</execution_type>
</step>
</steps>
<custom_fields><custom_field><name>测试用例-检测参数</name>
<value>功能</value>
</custom_field>
<custom_field><name>测试环境需求-测试用例</name>
<value>
测试机:兆芯C1  
硬件配置:
    型号：兆芯C 
    CPU：C-QuadCore C4600@2.0GHz 4核 
    内存：8192MB
    硬盘：200G     
软件配置:
    操作系统：cdos 1.10.0 - 0728 
    中间件：wine1.8.5
</value>
</custom_field>
<custom_field><name>测试用例设计日期</name>
<value>1482192000</value>
</custom_field>
</custom_fields>
<requirements><requirement><req_spec_title>[用户文档测试]</req_spec_title>
<doc_id>REQ-YHWD-1-2</doc_id>
<title>提交测试文档
</title>
</requirement>
</requirements>
</testcase>
</testcases>


```
### 然后把xml导入到TestLink就OK了,注意，是要以测试用例的方式导入，而不是导入测试用例集哦！



**更多内容，有待继续开发：**
1. 测试用例需要的那个东西不知道用不用，现在还没有加
2. 排列组合类型测试用例的自动排列组合。:)
3. 要是能够自动生成测试用例就好了，这应该是一个可以研究的自然语言问题吧
4. 还有测试用例质量评测，当前不知道可以实现的标准