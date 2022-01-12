# 说明

由于 [钱迹](http://www.qianjiapp.com/) 目前还未直接支持 MoneyWiz 的数据导入，但提供了模板导入的方式，因此需要将 MoneyWiz 导出的 CSV 数据转换成符合模板样式的字段才能通过手机导入钱迹。

# 如何使用

在你的电脑里需要事先安装 Python 3，可以在 [Python 官网](https://www.python.org/downloads/) 直接下载最新版本。

构建好 Python 环境并将本项目 Clone 至本地后，可以直接使用如下命令安装：

```
python setup.py install
```

安装完成之后直接通过命令行使用：

```
$ qianji-cli --help
Usage: qianji-cli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  moneywiz

```