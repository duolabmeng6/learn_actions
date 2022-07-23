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

def 版本号格式加一(版本号):
    版本号 = 版本号.split('.')
    版本号[-1] = str(int(版本号[-1]) + 1)
    版本号 = '.'.join(版本号)
    return 版本号
def 版本号从大小写排序(tags):
    # 删除非数字的版本号
    tags = [tag for tag in tags if tag.replace('.', '').isdigit()]
    tags_dict = []
    for tag in tags:
        # 获取数值
        tag_value = int("".join(tag.split('.')))
        tags_dict.append({
            "tag": tag,
            'tagint': tag_value
        })
    tags_dict.sort(key=lambda student: student['tagint'])
    tags_dict.reverse()
    # 重新组装
    tags = []
    for tag in tags_dict:
        tags.append(tag['tag'])
    return tags

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

    # 版本号对比
    tags = []
    k = 0
    for tag in repo.get_tags():
        print(tag.name)
        tags.append(tag.name)
        k += 1
        if k == 5:
            break  # 取前5个标签
    print("raw tags", tags)
    # 版本号排序
    tags = 版本号从大小写排序(tags)
    # print("版本号排序:", tags)
    新版本号 = 版本号格式加一(tags[0])
    # print("新版本号:", 新版本号)
    print("new tags", 新版本号)
    sha = repo.get_commits()[0].sha
    print("sha", sha)
    repo.create_git_ref(f"refs/tags/{新版本号}", sha)


if __name__ == "__main__":
    main()
    exit(0)