# coding:utf-8

import pathlib

import click
import pandas as pd

KEYS = ["时间", "分类", "类型", "金额", "账户1", "账户2", "备注", "账单图片"]
NAME_MAPPING = dict(
    账户="账户1",
    转账="账户2",
    描述="备注",
)


@click.group()
def cli():
    ...


@cli.command()
@click.option("-p", "--path", help='The path of MoneyWiz report csv file.', type=pathlib.Path)
def moneywiz(path: pathlib.Path):
    data = pd.read_csv(path, skiprows=1)
    data.loc[:, ["命名", "当前余额"]] = data[["命名", "当前余额"]].ffill()
    data = data.dropna(subset=["账户"])
    data["类型"] = data["金额"].str.replace(",", "").astype(float).map(lambda v: "支出" if v < 0 else "收入")
    data["类型"] = data[["转账", "类型"]].apply(lambda row: "转账" if not pd.isna(row["转账"]) else row["类型"], axis=1)
    data["时间"] = data["日期"].str.cat(data["时间"], sep=" ").pipe(pd.to_datetime)
    data["金额"] = data["金额"].str.replace(",", "").astype(float)

    data = data.rename(columns=NAME_MAPPING)
    data["账单图片"] = None
    data = data[KEYS]
    f = path.parent / "moneywiz_to_qianji.csv"
    data.to_csv(f, index=False, encoding="UTF-8")
    click.echo(f"converted to: {f!s}")


if __name__ == '__main__':
    cli()
