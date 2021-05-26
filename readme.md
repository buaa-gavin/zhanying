## 跨域互联


前端端口 8080 启动:`npm run dev`

后端端口 8090    启动:`python manage.py runserver 8090`

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
