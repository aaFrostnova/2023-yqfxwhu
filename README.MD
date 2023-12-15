# WHU2023秋舆情分析课程项目

## 任务说明

 + 任务4：美国国会议员
 + 任务描述：爬取美国参议院和众议院议员的社交媒体数据，构建议员社交关系网络。
 + 任务数据：
    - 社交媒体平台：Facebook 或者Twitter
    - 议员数目：全部议员
    - 关系：关注、同现（指的是在同一个推文中被同时@）、内容（在同一个推文内容中共同出现的名字）
    - 目标：网页demo

## 任务要求
1. 完成数据采集，并进行数据信息可视化展示，包括数据内容，数目，采集平台。
2. 完成模型搭建，可以以网页的形式展示分析效果。
3. 完成实验报告撰写，提交数据和完整代码。代码部分需写明安装部署步骤，保证能够正常运行。

## 说明：
1. 因没有符合任务目标的数据，故不提供目标数据，需同学们自行标定

## demo展示
![主页](https://z1.ax1x.com/2023/12/13/pifw18x.png)
![总体关注者网络](https://z1.ax1x.com/2023/12/13/pifw8xK.png)
![个人网络](https://z1.ax1x.com/2023/12/13/pifwtqe.png)

## 1. 安装

1. Python环境中安装Django==3.2：```pip install django==3.2```
2. 切换到项目根目录下，命令行输入:```python manage.py runserver```
3. 在浏览器输入地址127.0.0.1:8000访问页面

## 2. 数据采集

数据采集流程请看[教程](./Scweet/README.md)

## 3. 网络构建

本项目使用[Apache Echart](https://echarts.apache.org/zh/index.html)工具来进行社交关系网络的绘制。Echart是一种使用JavaScript语言在网页画图的工具，参照官网提供的[示例](https://echarts.apache.org/examples/zh/editor.html?c=graph-label-overlap)，我们总体上是使用Echart在前端调用相应的JSON文件进行渲染，因此网络构建的过程实际上是JSON文件的构造过程。

### Echart配置说明

关系图的构造涉及Echart中**option**的配置。最需要关注的是，```option.series[0].data```是节点信息，```option.series[0].links```是各节点之间的连接关系，```option.series[0].categories```是节点的分类信息。其他有关图表的展现形式，可以参考[Echart配置项手册](https://echarts.apache.org/zh/option.html#title)。一个常见的图表模板如下，图表展示位置在HTML页面中```id=='container'```的容器，调用的JSON文件在```/static/data/```目录下，```option```需要根据实际情况配置。

```javascript
<script type="text/javascript">
    var dom = document.getElementById('container');
    var myChart = echarts.init(dom, null, {
      renderer: 'canvas',
      useDirtyRect: false
    });
    var app = {};
    var ROOT_PATH = '/static/data/';
    var option;
    var chartwidth = myChart.getWidth();
    var chartheight = myChart.getHeight();
    myChart.showLoading();
$.getJSON(ROOT_PATH + '{{filename}}', function (graph) {
  myChart.hideLoading();
  option = {
  };
  myChart.setOption(option);
  console.log(option);
});

    if (option && typeof option === 'object') {
      myChart.setOption(option);
    }
    window.addEventListener('resize', myChart.resize);
</script>
```

### 关系图JSON文件生成

根据前面提到的Echart配置说明，一个可能的JSON文件格式如下：
```json
{
    "nodes": [
        {
            "id": "n0",
            "name": "SenKatieBritt",
            "symbolSize": 19.231,
            "x": -266.985,
            "y": 266.442,
            "value": {
                "office": "U.S. Senate Alabama",
                "offfice_url": "www.xxxxx.com",
                "name": "Katie Britt",
                "party": "Republican"
            },
            "category": 0,
        }
    ],
    "links": [
        {
            "soucre":"n0",
            "target":"n56"
        },
    ],
    "categories": [
        {
            "name":"Republican",
        },
        {}
    ]
}
```
在我们的社交关系网络构建中，存在两种网络：```graph-of-one.html```和```graph-overall.html```。下面具体说明这两种网络的数据组织形式。
1. **graph-of-one.html**
   + **nodes**中```id```保持唯一，个人社交网络要求以一个人为中心（假设这个节点为**n0**），所以我们设置**n0**的```x,y```坐标在屏幕中心。
   + 个人社交网络图包括三个子图：关注网络、同现网络和内容网络。使用**category**进行区分。总共有四类，**第0类不表示任何网络而是用于标记n0**；
2. **graph-overall.html**
   + 总体网络包含三个子图：总体关注网络、总体同现网络和总体内容网络。直接使用三个**category**进行区分；

## network_build

+ 关系网络构建需要用到数据采集得到的文件（following.csv/coat.csv/coexist.csv），其中第一列为中心人物，后续列为与之有关系的议员。总体网络生成可直接运行```main.py```生成总体网络的JSON文件；

![piW4jU0.md.png](https://z1.ax1x.com/2023/12/12/piW4jU0.md.png)

+ **data_process.py**：
  1. 根据数据文件构造三个$100\times100$的矩阵```following_mat, coat_mat, coexist_mat```，行列分别表示对应的议员；
  2. 生成```senator_info```字典，键为TwitterID，键值为各种信息的字典；
  3. 生成```analysis_info```字典，用于后续分析个人社交网络的组成情况；
  $ \left\{
  \begin{matrix}
   mat[i,j]=1,~i与j有关系 \\
   mat[i,j]=0,~i与j没有关系 
  \end{matrix}
  \right.
  $

+ **network_dump.py**：
  1. 根据生成的```mats```，进行```network_dump/relation_dump```。前者为总体网络JSON文件生成，后者为个人网络JSON文件生成；

## 4. Django网页框架

Django的MTV框架十分适合本项目的展示形式，我们主要用到templates和views，暂无models构建。更好的一种选择是使用数据库来存取网络信息，限于时间因素并没有实现。
+ **templates**：
  1. 三个页面：graph-of-one.html(个人网络)，graph-overall.html(总体网络)，index.html(导航页面)；
  ```python
  urlpatterns = [
    # 访问127.0.0.1:8000则会显示views.index
    path('', views.index),
    path('index/', views.index),
    # 访问127.0.0.1:8000则会显示views.graph
    path('graphoverall/<int:num>', views.graphoverall),
    path('graphofone/', views.graphofone),
    path('search/', views.search),
  ]
  ```
  2. 通过不同的```num```来访问三个不同的总体网络；
+ **views**：
  1. views主要处理HTML页面中调用的不同JSON文件和一些相关信息展示；
  ```javascript
  $.getJSON(ROOT_PATH + '{{filename}}', function (graph) {}
  ```
  2. 具体的渲染参数可以查看```views.py```中对应的处理函数；
