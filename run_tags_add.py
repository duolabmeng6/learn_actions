# -*- coding: utf-8 -*-
import os

from github import Github

def 查看系统所有环境变量():
    from icecream import ic
    # 打印系统所有的环境变量
    for item in os.environ:
        name = item
        value = os.environ[item]
        ic(name, value)
# 查看系统所有环境变量()


def main():
    GITHUB_REPOSITORY = os.environ.get('GITHUB_REPOSITORY')
    INPUT_TOKEN = os.environ.get('GITHUB_TOKEN')
    g = Github(INPUT_TOKEN)
    repo = g.get_repo(GITHUB_REPOSITORY)
    print("tags number", repo.get_tags().totalCount)
    if repo.get_tags().totalCount == 0:
        # 没有标签的话 创建标签 0.0.1
        sha = repo.get_commits()[0].sha
        新版本号 = "0.0.1"
        repo.create_git_ref(f"refs/tags/{新版本号}", sha)
        return 新版本号


if __name__ == "__main__":
    main()
    exit(0)