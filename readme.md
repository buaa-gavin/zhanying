## 跨域互联


前端端口 8080 启动:`npm run dev`

后端端口 8090    启动:`python manage.py runserver 8090`

## 后端配置

建议使用anaconda管理包和库，目前依赖在`zhanying/backend/requirements.txt`，python版本为3.8

## 前端运行

进入frontend

首先`npm install`

然后`npm run serve`

## 数据库配置

mysql 8.0.25

本地mysql建立zhanying数据库，在django的settings文件中修改：
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'zhanying',
        'USER': 'root',  # 你的user名字
        'PASSWORD': '123456',  # 数据库密码
        'HOST': '127.0.0.1', #host
        'PORT': '3306', #使用的端口
        'OPTIONS': {
            'autocommit': True,
        },
    }
}
```
之后迁移模型

```python
python manage.py makemigrations
python manage.py migrate
```



## 模型

因为模型文件太大，暂不上传。使用时在：

`zhanying/backend/algorithm/efficientnet/effb6.pth`和`zhanying/backend/algorithm/unet/MODEL.pth`

注意，模型名称必须对应，名称不能修改

## 需求分析

获取病人列表

* 病人相关信息 -> `/api/InfoList`

上传检测图片 `/api/upload`

- POST ｛id, 图片)

获取检测结果 

- 检测结果
  - 病人id
  - 保存的图片路径
  - 确诊结果
  - 分割后的图片路径
  - 上传日期

​	->上传病人ID、图片 ->  后端处理跑出检测结果和分割结果，将数据返回给前端 -> 前端响应，跳至详情界面

获取单个病人信息 ` /api/InfoList/<id>`

- 所有病人的字段，比如姓名、性别、出生日。
- 有一个病人的往届检测信息列表
- Person
- Image
- 一对多

---

## 接口

### 病人信息管理

* 路径：`/api/InfoList` 

* 方法

  * GET
    * 获取病人列表信息
  * POST
    * 增加新的病人信息

* 实例:

  * GET

    * 获取字段为

    ```python
    [
        {
            "id": int,
            "name": char,
            "birth": date
            "updated":datetime
        }
    ]
    ```

    ​	示例：

    ```json
    [
        {
            "id": 4,
            "name": "李田所2",
            "birth": "2021-05-26",
            "updated": null
        },
        {
            "id": 3,
            "name": "A",
            "birth": "2021-05-26",
            "updated": null
        },
        {
            "id": 2,
            "name": "野兽先辈",
            "birth": "2021-05-26",
            "updated": null
        },
        {
            "id": 1,
            "name": "李田所",
            "birth": "2021-05-26",
            "updated": "2021-05-27T00:45:24.627924Z"
        }
    ]
    ```

  - PUT

    - 上传必选字段为`name`，其余的`birth`默认为上传日期，`updated`可以为空，`id`自动分配

    示例：

    ```python
    data = {
        "name": "Test上传",
        "birth": "2000-03-21"
    	}
    //POST http://127.0.0.1:8090/api/InfoList/
    ```

### 诊断信息管理

- 路径：`api/diagnose/` , 详细信息为`api/diagnose/1/`

- 方法：

  - POST 上传图片，POST `api/diagnose`，返回信息为：

    ```python
    {
      "id":8,
      "url":"http://127.0.0.1:9000/api/diagnose/8/",
       "content":"http://127.0.0.1:9000/media/images/20210527/Sea1919810114514.jpg",
       "created":"2021-05-27T00:08:19.735430Z",
        "updated":"2021-05-27T02:49:12.830829Z",
       "status":"良性肿瘤",
       "semantic":"http://127.0.0.1:9000/media/images/20210527/Sea1919810114514_out.jpg",
       "person":null
    }
    ```

    有用的是`id`和`url`，`url`

    `content`为可访问的，保存在服务端的图片的地址，可以直接引用

    `smantic`是语义分割的结果

    `status`是分类结果

    `updated`是最好更新时间，datetime

  - PATCH  更新病人信息，当上传图片返回图片相应信息后，直接获取url，然后PATCH url，data数据段为`person`的主键，data格式的示例：

    ```json
    {
        "person":2
    }
    ```

    成功时候返回信息为

    ```python
    {
      "id":8,
      "url":"http://127.0.0.1:9000/api/diagnose/8/",
       "content":"http://127.0.0.1:9000/media/images/20210527/Sea1919810114514.jpg",
       "created":"2021-05-27T00:08:19.735430Z",
        "updated":"2021-05-27T02:49:12.830829Z",
       "status":"良性肿瘤",
       "semantic":"http://127.0.0.1:9000/media/images/20210527/Sea1919810114514_out.jpg",
       "person":2
    }
    ```

    唯一的区别是`person`有了主键的信息。

