# API框架
## 作用
根据swagger地址中的tags分别在business,test_cases,data目录下生成项目级别所需的文件

business层级关系
- business:所有业务逻辑
  - project
    - 解析swagger文档中的tags生成的模块py文件
    
test_cases层级关系
- test_cases:测试用例集
  - project
    - 解析swagger文档中的tags生成的test_模块py文件
    
data层级关系
- data:数据集合
  - project_api.xlsx
  - project_settings.py

# 使用
```shell script
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

运行bases目录下的swagger2file.py文件

# 完成功能
- 解析swagger生成基础版的用例
- 根据swagger自动生成项目的总体分层:业务逻辑层,用例校验

# TODO
- 完善日志,解析生成的excel存在模块划分异常
- 运行时进行地址对比
- 使用模板化根据接口地址在case中生成多个基础case
- 整体优化
    

